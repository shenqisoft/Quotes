# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Register.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(319, 289)
        Form.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.QToolButton_Close = QtWidgets.QToolButton(self.frame)
        self.QToolButton_Close.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.QToolButton_Close.setFont(font)
        self.QToolButton_Close.setMouseTracking(False)
        self.QToolButton_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.QToolButton_Close.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.QToolButton_Close.setAcceptDrops(False)
        self.QToolButton_Close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QToolButton_Close.setAutoFillBackground(False)
        self.QToolButton_Close.setStyleSheet("")
        self.QToolButton_Close.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.QToolButton_Close.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QToolButton_Close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/closePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Close.setIcon(icon)
        self.QToolButton_Close.setAutoRepeat(False)
        self.QToolButton_Close.setAutoExclusive(False)
        self.QToolButton_Close.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.QToolButton_Close.setAutoRaise(True)
        self.QToolButton_Close.setObjectName("QToolButton_Close")
        self.horizontalLayout_7.addWidget(self.QToolButton_Close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.QLineEdit_usr = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_usr.setObjectName("QLineEdit_usr")
        self.horizontalLayout.addWidget(self.QLineEdit_usr)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.QLineEdit_pwd = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_pwd.setObjectName("QLineEdit_pwd")
        self.horizontalLayout_2.addWidget(self.QLineEdit_pwd)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.QLineEdit_rpwd = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_rpwd.setObjectName("QLineEdit_rpwd")
        self.horizontalLayout_3.addWidget(self.QLineEdit_rpwd)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.QLineEdit_phone = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_phone.setObjectName("QLineEdit_phone")
        self.horizontalLayout_4.addWidget(self.QLineEdit_phone)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.QLineEdit_qq = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_qq.setStyleSheet("background-image:url(:/icons/bgxx.jpg);")
        self.QLineEdit_qq.setObjectName("QLineEdit_qq")
        self.horizontalLayout_5.addWidget(self.QLineEdit_qq)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.QPustButton_Register = QtWidgets.QPushButton(self.frame)
        self.QPustButton_Register.setMaximumSize(QtCore.QSize(100, 16777215))
        self.QPustButton_Register.setObjectName("QPustButton_Register")
        self.horizontalLayout_6.addWidget(self.QPustButton_Register)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Form)
        self.QToolButton_Close.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "用 户 名:"))
        self.label_6.setText(_translate("Form", "*必填   "))
        self.label_2.setText(_translate("Form", " 密  码 :"))
        self.label_7.setText(_translate("Form", "*必填   "))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.label_8.setText(_translate("Form", "*必填   "))
        self.label_4.setText(_translate("Form", "电话号码:"))
        self.label_9.setText(_translate("Form", "*选填   "))
        self.label_5.setText(_translate("Form", "腾 讯 QQ:"))
        self.label_10.setText(_translate("Form", "*选填   "))
        self.QPustButton_Register.setText(_translate("Form", "注  册"))

import UI_Resource_rc
