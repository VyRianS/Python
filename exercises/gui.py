#!/usr/bin/python3.6

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__() # Calls the __init__ method of its super class QMainWindow?
        self.title = 'PyQt5 first window'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI() # Constructor
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        # Create button object
        button = QPushButton('Qt button', self)
        button.setToolTip('Eg button.')
        button.move(100,380)

        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('clicked!')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

