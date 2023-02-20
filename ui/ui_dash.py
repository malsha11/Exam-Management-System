# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashRpcItn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 600)
        MainWindow.setMinimumSize(QSize(950, 550))
        MainWindow.setStyleSheet(u"QScrollBar {\n"
"\n"
"                   background-color:none;\n"
"                   border:none;\n"
"                   background:none;\n"
"                   border-radius:7;\n"
"width:15px,\n"
"\n"
"                   }\n"
"QScrollBar:handle{\n"
"                   background:rgb(223, 223, 223);\n"
"                   border-radius:7;\n"
"                  }\n"
"")
        self.root = QWidget(MainWindow)
        self.root.setObjectName(u"root")
        self.horizontalLayout = QHBoxLayout(self.root)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.root_front = QFrame(self.root)
        self.root_front.setObjectName(u"root_front")
        self.root_front.setFrameShape(QFrame.StyledPanel)
        self.root_front.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.root_front)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_pan = QFrame(self.root_front)
        self.left_pan.setObjectName(u"left_pan")
        self.left_pan.setMaximumSize(QSize(60, 16777215))
        self.left_pan.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.left_pan.setFrameShape(QFrame.StyledPanel)
        self.left_pan.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_pan)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.left_pan)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.home_btn = QPushButton(self.frame_4)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(50, 50))
        self.home_btn.setMaximumSize(QSize(50, 50))
        self.home_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/Image/style/cat.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"\n"
"border:none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-radius:10px;\n"
"\n"
"border:1px solid;\n"
"\n"
"	border-color: rgb(78, 188, 235);\n"
"}")

        self.verticalLayout_2.addWidget(self.home_btn)

        self.settings_btn = QPushButton(self.frame_4)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(50, 50))
        self.settings_btn.setMaximumSize(QSize(50, 50))
        self.settings_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/Image/style/set.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"\n"
"border:none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"\n"
"	border-color: rgb(78, 188, 235);\n"
"}")

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.about_btn = QPushButton(self.frame_4)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(50, 50))
        self.about_btn.setMaximumSize(QSize(50, 50))
        self.about_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/Image/style/card.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"\n"
"border:none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"\n"
"	border-color: rgb(78, 188, 235);\n"
"}")

        self.verticalLayout_2.addWidget(self.about_btn)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.left_pan)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	image: url(:/Image/style/girl.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"\n"
"border:none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"\n"
"	border-color: rgb(78, 188, 235);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(30, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.exit_btn = QPushButton(self.frame_5)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(50, 50))
        self.exit_btn.setMaximumSize(QSize(50, 50))
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/Image/style/ext.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"\n"
"border:none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"	border-color: rgb(255, 28, 96);\n"
"}")

        self.verticalLayout_3.addWidget(self.exit_btn)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.left_pan)

        self.Center_pan = QFrame(self.root_front)
        self.Center_pan.setObjectName(u"Center_pan")
        self.Center_pan.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.Center_pan.setFrameShape(QFrame.StyledPanel)
        self.Center_pan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Center_pan)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.Center_pan)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.student = QWidget()
        self.student.setObjectName(u"student")
        self.stackedWidget.addWidget(self.student)
        self.teacher = QWidget()
        self.teacher.setObjectName(u"teacher")
        self.horizontalLayout_10 = QHBoxLayout(self.teacher)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.teacher)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 20)
        self.btn_container = QFrame(self.frame_11)
        self.btn_container.setObjectName(u"btn_container")
        self.btn_container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_container.setFrameShape(QFrame.StyledPanel)
        self.btn_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.btn_container)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.btn_container)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 0)
        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 150))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_15)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 150))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_2)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.feed_container = QFrame(self.btn_container)
        self.feed_container.setObjectName(u"feed_container")
        self.feed_container.setMaximumSize(QSize(16777215, 55))
        self.feed_container.setFrameShape(QFrame.StyledPanel)
        self.feed_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.feed_container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 10)
        self.pushButton_3 = QPushButton(self.feed_container)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 72, 152, 255), stop:0.380682 rgba(255, 75, 108, 255), stop:0.625 rgba(255, 75, 108, 255), stop:1 rgba(202, 72, 152, 255));\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout_8.addWidget(self.feed_container)


        self.verticalLayout_7.addWidget(self.btn_container)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 300))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_14)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setAutoFillBackground(False)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 30))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_5)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.label_6)

        self.plainTextEdit = QPlainTextEdit(self.frame_18)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"	color: rgb(115, 115, 115);\n"
"                  border: 0px solid;\n"
"	background-color: rgb(248, 248, 248);")

        self.verticalLayout_12.addWidget(self.plainTextEdit)


        self.verticalLayout_11.addWidget(self.frame_18)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 55))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_16)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(67, 233, 123, 255), stop:1 rgba(56, 249, 215, 255));\n"
"\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_4)


        self.verticalLayout_10.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.frame_14)


        self.horizontalLayout_10.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.teacher)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(400, 16777215))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 50))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 72, 152, 255), stop:0.380682 rgba(255, 75, 108, 255), stop:0.625 rgba(255, 75, 108, 255), stop:1 rgba(202, 72, 152, 255));\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.pushButton_9)


        self.verticalLayout_13.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.listWidget_4 = QListWidget(self.frame_20)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setStyleSheet(u"\n"
"QListWidget{\n"
"	color: rgb(115, 115, 115);\n"
"                  border: 0px solid;\n"
"	background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item:hover{\n"
"\n"
"                  color:white;\n"
"                  border:2px solid #3079ed;\n"
"                  border-left:none;\n"
" border-color:rgb(241, 241, 241);\n"
"                  padding-left:5px;\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item{\n"
"	background-color: rgb(240, 240, 240);\n"
"         border:1px solid;\n"
"	border-color: rgb(217, 217, 217);\n"
"border-radius:5px;\n"
"                  padding-top:5px;\n"
"                  padding-bottom:5px;\n"
"\n"
"\n"
"\n"
"                 }\n"
"QListWidget:item:selected{\n"
"                  background:none;\n"
"                  border:none;\n"
"                  color:#4D90FE;\n"
"                  border:1px solid #2C2E33;\n"
"                  border-left:none;\n"
"                  border-right:none;\n"
"                  border-to"
                        "p:none;\n"
"\n"
"                  }\n"
"QListWidget:item:selected:hover{\n"
"                   background:#1D1E24;\n"
"                   border:2px solid white;\n"
"                   border-left:none;\n"
"                   border-top:none;\n"
"                   border-bottom:none;\n"
"                   }\n"
"\n"
"QListWidget::scrollbar{\n"
" background:#1D1E24;\n"
"}")
        self.listWidget_4.setSpacing(5)

        self.horizontalLayout_15.addWidget(self.listWidget_4)


        self.verticalLayout_13.addWidget(self.frame_20)


        self.horizontalLayout_10.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.teacher)
        self.admin = QWidget()
        self.admin.setObjectName(u"admin")
        self.verticalLayout_4 = QVBoxLayout(self.admin)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.admin)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 200))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"\n"
"border:1px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 200))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"\n"
"border:1px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 200))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"\n"
"border:1px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.admin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(270, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.listWidget = QListWidget(self.frame_3)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"\n"
"QListWidget{\n"
"	color: rgb(115, 115, 115);\n"
"                  border: 0px solid;\n"
"	background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item:hover{\n"
"\n"
"                  color:white;\n"
"                  border:2px solid #3079ed;\n"
"                  border-left:none;\n"
" border-color:rgb(241, 241, 241);\n"
"                  padding-left:5px;\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item{\n"
"	background-color: rgb(240, 240, 240);\n"
"         border:1px solid;\n"
"	border-color: rgb(217, 217, 217);\n"
"border-radius:5px;\n"
"                  padding-top:5px;\n"
"                  padding-bottom:5px;\n"
"\n"
"\n"
"\n"
"                 }\n"
"QListWidget:item:selected{\n"
"                  background:none;\n"
"                  border:none;\n"
"                  color:#4D90FE;\n"
"                  border:1px solid #2C2E33;\n"
"                  border-left:none;\n"
"                  border-right:none;\n"
"                  border-to"
                        "p:none;\n"
"\n"
"                  }\n"
"QListWidget:item:selected:hover{\n"
"                   background:#1D1E24;\n"
"                   border:2px solid white;\n"
"                   border-left:none;\n"
"                   border-top:none;\n"
"                   border-bottom:none;\n"
"                   }\n"
"\n"
"QListWidget::scrollbar{\n"
" background:#1D1E24;\n"
"}")
        self.listWidget.setSpacing(5)

        self.verticalLayout_5.addWidget(self.listWidget)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(270, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.listWidget_3 = QListWidget(self.frame_7)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setStyleSheet(u"\n"
"QListWidget{\n"
"	color: rgb(115, 115, 115);\n"
"                  border: 0px solid;\n"
"	background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item:hover{\n"
"\n"
"                  color:white;\n"
"                  border:2px solid #3079ed;\n"
"                  border-left:none;\n"
" border-color:rgb(241, 241, 241);\n"
"                  padding-left:5px;\n"
"\n"
"                  }\n"
"\n"
"QListWidget:item{\n"
"	background-color: rgb(240, 240, 240);\n"
"         border:1px solid;\n"
"	border-color: rgb(217, 217, 217);\n"
"border-radius:5px;\n"
"                  padding-top:5px;\n"
"                  padding-bottom:5px;\n"
"\n"
"\n"
"\n"
"                 }\n"
"QListWidget:item:selected{\n"
"                  background:none;\n"
"                  border:none;\n"
"                  color:#4D90FE;\n"
"                  border:1px solid #2C2E33;\n"
"                  border-left:none;\n"
"                  border-right:none;\n"
"                  border-to"
                        "p:none;\n"
"\n"
"                  }\n"
"QListWidget:item:selected:hover{\n"
"                   background:#1D1E24;\n"
"                   border:2px solid white;\n"
"                   border-left:none;\n"
"                   border-top:none;\n"
"                   border-bottom:none;\n"
"                   }\n"
"\n"
"QListWidget::scrollbar{\n"
" background:#1D1E24;\n"
"}")
        self.listWidget_3.setSpacing(5)

        self.verticalLayout_6.addWidget(self.listWidget_3)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.calendarWidget = QCalendarWidget(self.frame_8)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.calendarWidget)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.admin)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.Center_pan)


        self.horizontalLayout.addWidget(self.root_front)

        MainWindow.setCentralWidget(self.root)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Home</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText("")
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText("")
#if QT_CONFIG(tooltip)
        self.about_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>About</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.about_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>profile</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Get me Out</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exit_btn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload Papers", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Student Details", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Send Feedback", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reacent Mails", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"By:John", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"dfcerregvrtgrtgrtgtrg", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mail Box", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Results", None))

        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_4.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget_4.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget_4.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget_4.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_4.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_4.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_4.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled)

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Teachers Details", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Student Details", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"FeedBack", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Availible Teachers:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"20", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.listWidget.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"efefer", None));
        ___qlistwidgetitem8 = self.listWidget.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget.item(3)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget.item(4)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem12 = self.listWidget.item(5)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem13 = self.listWidget.item(6)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem14 = self.listWidget.item(7)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem15 = self.listWidget.item(8)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Availible Students:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"20", None))

        __sortingEnabled2 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem16 = self.listWidget_3.item(0)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem17 = self.listWidget_3.item(1)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem18 = self.listWidget_3.item(2)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem19 = self.listWidget_3.item(3)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem20 = self.listWidget_3.item(4)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem21 = self.listWidget_3.item(5)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem22 = self.listWidget_3.item(6)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled2)

    # retranslateUi

