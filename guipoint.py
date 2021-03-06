# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiPoint.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelfx = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelfx.setFont(font)
        self.labelfx.setObjectName("labelfx")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelfx)
        self.doubleSpinBoxFx = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxFx.setMinimumSize(QtCore.QSize(60, 40))
        self.doubleSpinBoxFx.setMinimum(-4000000.0)
        self.doubleSpinBoxFx.setMaximum(4000000.0)
        self.doubleSpinBoxFx.setSingleStep(0.1)
        self.doubleSpinBoxFx.setObjectName("doubleSpinBoxFx")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxFx)
        self.labelfy = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelfy.setFont(font)
        self.labelfy.setObjectName("labelfy")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelfy)
        self.doubleSpinBoxFy = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxFy.setMinimumSize(QtCore.QSize(60, 40))
        self.doubleSpinBoxFy.setMinimum(-4000000.0)
        self.doubleSpinBoxFy.setMaximum(4000000.0)
        self.doubleSpinBoxFy.setSingleStep(0.1)
        self.doubleSpinBoxFy.setObjectName("doubleSpinBoxFy")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxFy)
        self.labelfz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelfz.setFont(font)
        self.labelfz.setObjectName("labelfz")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelfz)
        self.doubleSpinBoxFz = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxFz.setMinimumSize(QtCore.QSize(60, 40))
        self.doubleSpinBoxFz.setMinimum(-4000000.0)
        self.doubleSpinBoxFz.setMaximum(4000000.0)
        self.doubleSpinBoxFz.setSingleStep(0.1)
        self.doubleSpinBoxFz.setObjectName("doubleSpinBoxFz")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxFz)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBoxTime = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxTime.setMinimumSize(QtCore.QSize(60, 40))
        self.spinBoxTime.setMaximum(1000)
        self.spinBoxTime.setObjectName("spinBoxTime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxTime)
        self.verticalLayout.addLayout(self.formLayout)
        self.labelKoor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelKoor.setFont(font)
        self.labelKoor.setText("")
        self.labelKoor.setObjectName("labelKoor")
        self.verticalLayout.addWidget(self.labelKoor)
        self.labelSpeed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSpeed.setFont(font)
        self.labelSpeed.setText("")
        self.labelSpeed.setObjectName("labelSpeed")
        self.verticalLayout.addWidget(self.labelSpeed)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Point"))
        self.labelfx.setText(_translate("MainWindow", "Fx, Н"))
        self.labelfy.setText(_translate("MainWindow", "Fy, H"))
        self.labelfz.setText(_translate("MainWindow", "Fz, H"))
        self.label_4.setText(_translate("MainWindow", "Time, c"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
