# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Setting.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(11, 11, 781, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 111, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(12, 27, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(12, 53, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 280, 761, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 50, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 50, 87, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 50, 87, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(470, 50, 87, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setGeometry(QtCore.QRect(590, 40, 91, 31))
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "微信号"))
        self.label_2.setText(_translate("MainWindow", "数据缓存路径"))
        self.label_3.setText(_translate("MainWindow", "清空缓存数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "通用配置"))
        self.groupBox.setTitle(_translate("MainWindow", "通用消息订阅"))
        self.checkBox.setText(_translate("MainWindow", "新股开板"))
        self.checkBox_4.setText(_translate("MainWindow", "复牌公告"))
        self.groupBox_2.setTitle(_translate("MainWindow", "个股消息订阅"))
        self.comboBox.setItemText(0, _translate("MainWindow", "公告"))
        self.comboBox.setItemText(1, _translate("MainWindow", "不订阅"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "新闻"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "不订阅"))
        self.lineEdit.setText(_translate("MainWindow", "证券代码"))
        self.toolButton.setText(_translate("MainWindow", "添加订阅"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "微信消息订阅"))

