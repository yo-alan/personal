# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/Escritorio/python/MVC/v/ui_error.ui'
#
# Created: Wed Nov  5 20:57:37 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName(_fromUtf8("Error"))
        Error.resize(480, 140)
        Error.setMinimumSize(QtCore.QSize(480, 140))
        Error.setMaximumSize(QtCore.QSize(480, 140))
        Error.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Error)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblMensaje = QtGui.QLabel(Error)
        self.lblMensaje.setText(_fromUtf8(""))
        self.lblMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensaje.setObjectName(_fromUtf8("lblMensaje"))
        self.verticalLayout.addWidget(self.lblMensaje)
        self.buttonBox = QtGui.QDialogButtonBox(Error)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Error)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Error.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Error.reject)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        Error.setWindowTitle(QtGui.QApplication.translate("Error", "ERROR", None, QtGui.QApplication.UnicodeUTF8))

