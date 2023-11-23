import sys
import random
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QMetaObject, QRect, QCoreApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(150, 10, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QRect(10, 50, 380, 240))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQT Example"))
        self.pushButton.setText(_translate("MainWindow", "Draw Circles"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        width = self.graphicsView.width()
        height = self.graphicsView.height()
        scene = QtWidgets.QGraphicsScene()
        n = random.randint(1, 10)
        for i in range(n):
            d = random.randint(10, 100)
            x = random.randint(0, width - d)
            y = random.randint(0, height - d)
            colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "cyan", "magenta", "brown"]
            color = random.choice(colors)
            circle = QtWidgets.QGraphicsEllipseItem(x, y, d, d)
            circle.setBrush(QtGui.QColor(color))
            scene.addItem(circle)
        self.graphicsView.setScene(scene)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())


#############COPYRIGHT-AND-USAGE#############
#  Written by Lev, Sokolov on 23Nov 2023    #
#          Owned by Aboba Inc.              #
#          Free to use and edit             #
#############################################