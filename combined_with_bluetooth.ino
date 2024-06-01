struct StringParser {
    void reset() {
        from = to = -1;    
    }
    bool update(String& s, char div = ';') {
        if (to == s.length()) return 0;
        from = to + 1;
        to = s.indexOf(div, from);
        if (to < 0) to = s.length();
        str = s.substring(from, to);
        return 1;
    }
    String str;
    int from = -1;
    int to = -1;
};

//Переменные
unsigned long _time;
String data_bl;
String last_str;
StringParser pars; 
//Клавиши
#define BUT_UP 8
#define BUT_DOWN 2
#define BUT_LEFT 4
#define BUT_RIGHT 6



//Левый мотор
#define GPIO_1F 2
#define GPIO_1B 3
//Правый мотор
#define GPIO_2F 4
#define GPIO_2B 5

#include <mobrob3xmotor.h>
#include <IRremote.hpp>
#include <Wire.h> 
#include <mobrob3sonar.h> 

//Переменные датчиков
const int MPU_addr = 0x68; 
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ; 
unsigned long Old_dataTime = 0; 

void setup() {
  Serial.begin(9600);
  motor_setup();
  _time = millis();
  Wire.begin(); 
  Wire.beginTransmission(MPU_addr); 
  Wire.write(0x6B); 
  Wire.write(0);
  Wire.endTransmission(true); 
  Sonar_init(13, 12); 
}

void loop() {
  Wire.beginTransmission(MPU_addr); 
  Wire.write(0x3B); 
  Wire.endTransmission(false); 
  Wire.requestFrom(MPU_addr, 14, true);

  if (readStringUntil(data_bl, '\n')) {
    while (pars.update(data_bl)) {
      if(last_str == ""){
        last_str = pars.str;
        continue;  
      }
      if(last_str == "C"){
        last_str = pars.str;
        start_move(pars.str.toInt());
        continue;  
      }            
      last_str = pars.str;        
    }
    data_bl = "";
    last_str = "";
    pars.reset();
    _time = millis();
  }
 

  if (millis() - Old_dataTime > 2000) {
      gather_data();
  }
    
  if ((millis() - _time) > 2000) {
    motors_power(0, 0);
  }
}

void start_move(int but){
  switch(but){
    case BUT_UP: motors_power(150, 150); break;
    case BUT_DOWN: motors_power(-150, -150); break;
    case BUT_LEFT: motors_power(-150, 150); break;
    case BUT_RIGHT: motors_power(150, -150); break;
    }
}

bool readStringUntil(String& input, char until_c) {
  while (Serial.available()) {
    char c = Serial.read();
    input += c;
    if (c == until_c) {
      return true;
    }
  }
  return false;
}


void gather_data(){
  String data;
  AcX = Wire.read() << 8 | Wire.read(); 
  AcY = Wire.read() << 8 | Wire.read(); 
  AcZ = Wire.read() << 8 | Wire.read(); 
  Tmp = Wire.read() << 8 | Wire.read(); 
  GyX = Wire.read() << 8 | Wire.read(); 
  GyY = Wire.read() << 8 | Wire.read(); 
  GyZ = Wire.read() << 8 | Wire.read(); 
  int16_t dist = Sonar(300); 
  int16_t data_l[] = {dist, AcX, AcY, AcZ, GyX, GyY, GyZ, 150} ;
  for(int16_t elem: data_l){
    data += elem;
    data += ";";
  }
  Serial.println(data); 
  Old_dataTime = millis();
}
