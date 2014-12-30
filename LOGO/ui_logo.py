# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_logo.ui'
#
# Created: Tue Dec 30 18:33:47 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Logo(object):
    def setupUi(self, Logo):
        Logo.setObjectName(_fromUtf8("Logo"))
        Logo.resize(320, 240)
        self.centralwidget = QtGui.QWidget(Logo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 96, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Logo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Logo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Logo.setMenuBar(self.menubar)

        self.retranslateUi(Logo)
        QtCore.QMetaObject.connectSlotsByName(Logo)

    def retranslateUi(self, Logo):
        Logo.setWindowTitle(QtGui.QApplication.translate("Logo", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Logo", "CARGANDO...", None, QtGui.QApplication.UnicodeUTF8))

