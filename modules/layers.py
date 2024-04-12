from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize

BUTTON_SIZE = QSize(60, 60)
ICON_SIZE = QSize(50, 50)


class MoveLayout(QWidget):
    def __init__(self, *args):
        super().__init__(*args)

        layout = QGridLayout()

        self.up_btn = QPushButton()
        self.up_btn.setFixedSize(BUTTON_SIZE)
        self.up_btn.setIcon(QIcon("data/image/up.png"))
        self.up_btn.setIconSize(ICON_SIZE)

        self.down_btn = QPushButton()
        self.down_btn.setFixedSize(BUTTON_SIZE)
        self.down_btn.setIcon(QIcon("data/image/down.png"))
        self.down_btn.setIconSize(ICON_SIZE)

        self.left_btn = QPushButton()
        self.left_btn.setFixedSize(BUTTON_SIZE)
        self.left_btn.setIcon(QIcon("data/image/left.png"))
        self.left_btn.setIconSize(ICON_SIZE)

        self.right_btn = QPushButton()
        self.right_btn.setFixedSize(BUTTON_SIZE)
        self.right_btn.setIcon(QIcon("data/image/right.png"))
        self.right_btn.setIconSize(ICON_SIZE)

        self.bluetooth_btn = QPushButton()
        self.bluetooth_btn.setFixedSize(BUTTON_SIZE)
        self.bluetooth_btn.setIcon(QIcon("data/image/bluetooth_disconnect.png"))
        self.bluetooth_btn.setIconSize(ICON_SIZE)
        self.bluetooth_btn.clicked.connect(self.connect_bluetooth)

        layout.addWidget(self.up_btn, 0, 1)
        layout.addWidget(self.down_btn, 2, 1)
        layout.addWidget(self.left_btn, 1, 0)
        layout.addWidget(self.right_btn, 1, 2)
        layout.addWidget(self.bluetooth_btn, 1, 1)

        self.setLayout(layout)

    def connect_bluetooth(self):
        self.bluetooth_btn.setIcon(QIcon("data/image/bluetooth_connect.png"))
        self.bluetooth_btn.setIconSize(ICON_SIZE)