# -*- coding: utf-8 -*-


from PyQt5.QtCore import pyqtSlot
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import sys

from ui_login import *

class Main_UI(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.show_text)

    def show_text(self):
         print(self.ui.user.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main_UI()
    main.show()
    app.exec_()







