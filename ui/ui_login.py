# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginTFzxkp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(500, 550)
        login.setMinimumSize(QSize(500, 550))
        login.setStyleSheet(u"")
        self.root = QWidget(login)
        self.root.setObjectName(u"root")
        self.verticalLayout = QVBoxLayout(self.root)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 150, 0, 0)
        self.lbl_frm = QFrame(self.root)
        self.lbl_frm.setObjectName(u"lbl_frm")
        self.lbl_frm.setMaximumSize(QSize(16777215, 50))
        self.lbl_frm.setFrameShape(QFrame.StyledPanel)
        self.lbl_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lbl_frm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lg_lbl = QLabel(self.lbl_frm)
        self.lg_lbl.setObjectName(u"lg_lbl")
        self.lg_lbl.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setFamily(u"Adobe Fan Heiti Std B")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lg_lbl.setFont(font)
        self.lg_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lg_lbl)


        self.verticalLayout.addWidget(self.lbl_frm)

        self.lin_frm = QFrame(self.root)
        self.lin_frm.setObjectName(u"lin_frm")
        self.lin_frm.setMaximumSize(QSize(16777215, 93))
        self.lin_frm.setFrameShape(QFrame.StyledPanel)
        self.lin_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lin_frm)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user = QLineEdit(self.lin_frm)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(300, 35))
        self.user.setMaximumSize(QSize(300, 16777215))
        self.user.setStyleSheet(u"QLineEdit{\n"
"\n"
"}")
        self.user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.user)

        self.pwd = QLineEdit(self.lin_frm)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setMinimumSize(QSize(300, 35))
        self.pwd.setMaximumSize(QSize(300, 16777215))
        self.pwd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.pwd)


        self.verticalLayout.addWidget(self.lin_frm, 0, Qt.AlignHCenter)

        self.btn_frm = QFrame(self.root)
        self.btn_frm.setObjectName(u"btn_frm")
        self.btn_frm.setMaximumSize(QSize(16777215, 100))
        self.btn_frm.setFrameShape(QFrame.StyledPanel)
        self.btn_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btn_frm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_btn = QPushButton(self.btn_frm)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 50))
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.login_btn)

        self.sign_btn = QPushButton(self.btn_frm)
        self.sign_btn.setObjectName(u"sign_btn")
        self.sign_btn.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.sign_btn)


        self.verticalLayout.addWidget(self.btn_frm)

        self.frame_2 = QFrame(self.root)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.root)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_btn = QPushButton(self.frame)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignRight)

        login.setCentralWidget(self.root)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.lg_lbl.setText(QCoreApplication.translate("login", u"Login", None))
        self.user.setPlaceholderText(QCoreApplication.translate("login", u"Enter your user name", None))
        self.pwd.setPlaceholderText(QCoreApplication.translate("login", u"Enter your password", None))
        self.login_btn.setText(QCoreApplication.translate("login", u"Login", None))
        self.sign_btn.setText(QCoreApplication.translate("login", u"SignUP", None))
        self.exit_btn.setText(QCoreApplication.translate("login", u"Exit", None))
    # retranslateUi

