# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 525)
        self.host = QtWidgets.QLineEdit(Form)
        self.host.setGeometry(QtCore.QRect(100, 30, 113, 21))
        self.host.setObjectName("host")

        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(270, 30, 113, 21))
        self.port.setObjectName("port")

        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(100, 70, 113, 21))
        self.user.setObjectName("user")

        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(270, 70, 113, 21))
        self.passwd.setObjectName("passwd")

        self.db = QtWidgets.QLineEdit(Form)
        self.db.setGeometry(QtCore.QRect(100, 110, 113, 21))
        self.db.setObjectName("db")

        self.charset = QtWidgets.QLineEdit(Form)
        self.charset.setGeometry(QtCore.QRect(270, 110, 113, 21))
        self.charset.setObjectName("charset")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 70, 112, 32))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 561, 351))
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 110, 58, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.label.setText(_translate("Form", "host"))
        self.label_2.setText(_translate("Form", "port"))
        self.label_3.setText(_translate("Form", "user"))
        self.label_4.setText(_translate("Form", "passwd"))
        self.label_5.setText(_translate("Form", "db"))
        self.label_6.setText(_translate("Form", "charset"))
