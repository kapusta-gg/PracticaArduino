import pandas as pd
import numpy as np

TEMP1 = [["angle_x", "AcX"], ["angle_y", "AcY"], ["angle_z", "AcZ"]]
COLUMN_NAME = 0
DATA_ID = 1
SPEED_COEF = 4.1
SM_TO_M = 100
SPEED_COEF_2_SEC = SPEED_COEF * (SM_TO_M * 2)


data = pd.read_csv("./data/data.csv", sep=";")
data.drop(data.columns[[-1]], axis=1, inplace=True)
new_data = pd.DataFrame()

#Конвертируем в диапозон +-8g
data["AcX"] = np.round(data["AcX"] / 4096, decimals=4)
data["AcY"] = np.round(data["AcY"] / 4096, decimals=4)
data["AcZ"] = np.round(data["AcZ"] / 4096, decimals=4)

#Получаем углы
data["AcX"] = np.angle(np.arctan(data["AcX"] / np.sqrt(np.power(data["AcY"], 2) + np.power(data["AcZ"], 2))))
data["AcY"] = np.angle(np.arctan(data["AcY"] / np.sqrt(np.power(data["AcX"], 2) + np.power(data["AcZ"], 2))))
data["AcZ"] = np.angle(np.arctan(np.sqrt(np.power(data["AcY"], 2) + np.power(data["AcX"], 2)) / data["AcZ"]))


for id, elem in enumerate(TEMP1):
    new_data.insert(id, elem[COLUMN_NAME], data[elem[DATA_ID]])

#Преобразование данных дальномера см в м
data["Sonar"] = data["Sonar"] / SM_TO_M

#Преобразование скорости в из единиц в  м/сек
data["Speed"] = data["Speed"] / SPEED_COEF_2_SEC

#Получения секунд до столкновения
sec_before_crash = np.round(data["Sonar"] / data["Speed"],2)

new_data.insert(3, "seconds", sec_before_crash)

new_data.to_csv("./result/result.csv")