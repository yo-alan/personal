# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/undercover/personal/v/ui_lic_eliminar.ui'
#
# Created: Wed Jan 14 13:58:59 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Lic_Eliminar(object):
    def setupUi(self, Lic_Eliminar):
        Lic_Eliminar.setObjectName(_fromUtf8("Lic_Eliminar"))
        Lic_Eliminar.resize(480, 140)
        Lic_Eliminar.setMinimumSize(QtCore.QSize(480, 140))
        Lic_Eliminar.setMaximumSize(QtCore.QSize(480, 140))
        Lic_Eliminar.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Lic_Eliminar)
        self.buttonBox.setGeometry(QtCore.QRect(160, 100, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lblMensaje = QtGui.QLabel(Lic_Eliminar)
        self.lblMensaje.setGeometry(QtCore.QRect(0, 0, 480, 100))
        self.lblMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensaje.setObjectName(_fromUtf8("lblMensaje"))

        self.retranslateUi(Lic_Eliminar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Lic_Eliminar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Lic_Eliminar.reject)
        QtCore.QMetaObject.connectSlotsByName(Lic_Eliminar)

    def retranslateUi(self, Lic_Eliminar):
        Lic_Eliminar.setWindowTitle(QtGui.QApplication.translate("Lic_Eliminar", "Eliminar licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMensaje.setText(QtGui.QApplication.translate("Lic_Eliminar", "¿Está seguro de querer eliminar esta licencia?", None, QtGui.QApplication.UnicodeUTF8))

