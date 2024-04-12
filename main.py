import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel
from PyQt5.Qt import QSize
from modules.layers import MoveLayout

MAIN_WINDOW_SIZE = QSize(600, 600)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(MAIN_WINDOW_SIZE)

        main_widget = QWidget(self)

        main_layout = QGridLayout()
        main_layout.addWidget(MoveLayout(self), 0, 0)
        main_layout.addWidget(QLabel("asds"), 1, 1)

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    app.exec()