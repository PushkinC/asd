import math
import sys
import random as rnd
from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pos = (400, 300)
        self.circle = False
        self.pushButton.clicked.connect(self.cl)

    def cl(self):
        self.size = rnd.randint(50, 100)
        self.circle = True
        self.repaint()

    def paintEvent(self, event):
        if self.circle:
            qp = QPainter()
            qp.begin(self)
            self.draw_points(qp)
            qp.end()


    def draw_points(self, qp):
        pen = QtGui.QBrush(QtGui.QColor('yellow'))
        qp.setBrush(pen)
        qp.drawEllipse(self.pos[0] - self.size // 2, self.pos[1] - self.size // 2, self.size, self.size)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())