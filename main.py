import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from requests import get


class SlideShow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.url = "https://static-maps.yandex.ru/1.x/"
        self.params = (
            {"ll": "56.782558,54.419429", "z": "17", "l": "sat"},
            {"ll": "-49.089295,-21.805418", "z": "17", "l": "sat"},
            {"ll": "-3.472239,40.499424", "z": "17", "l": "sat"},
        )

        self.pics = []
        self.index = 0
        self.get_pics()
        self.image.setPixmap(self.pics[self.index])

        self.next.clicked.connect(self.next_pic)
        self.prev.clicked.connect(self.prev_pic)

    def next_pic(self):
        self.index += 1
        self.index %= 3
        self.image.setPixmap(self.pics[self.index])

    def prev_pic(self):
        self.index -= 1
        self.index %= 3
        self.image.setPixmap(self.pics[self.index])

    def get_pics(self):
        for param in self.params:
            qp = QPixmap()
            qp.loadFromData(get(self.url, params=param).content)
            self.pics.append(qp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    s = SlideShow()
    s.show()
    sys.exit(app.exec())
