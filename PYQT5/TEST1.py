# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TEST1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(80, 80, 531, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 531, 331))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(100, 130, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(200, 30, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionS = QtWidgets.QAction(MainWindow)
        self.actionS.setObjectName("actionS")
        self.actionX = QtWidgets.QAction(MainWindow)
        self.actionX.setObjectName("actionX")
        self.actionC = QtWidgets.QAction(MainWindow)
        self.actionC.setObjectName("actionC")
        self.actionCV = QtWidgets.QAction(MainWindow)
        self.actionCV.setObjectName("actionCV")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionS_2 = QtWidgets.QAction(MainWindow)
        self.actionS_2.setObjectName("actionS_2")
        self.actionD = QtWidgets.QAction(MainWindow)
        self.actionD.setObjectName("actionD")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.actionS.setText(_translate("MainWindow", "S"))
        self.actionX.setText(_translate("MainWindow", "X"))
        self.actionC.setText(_translate("MainWindow", "C"))
        self.actionCV.setText(_translate("MainWindow", "CV"))
        self.actionA.setText(_translate("MainWindow", "A"))
        self.actionS_2.setText(_translate("MainWindow", "S"))
        self.actionD.setText(_translate("MainWindow", "D"))