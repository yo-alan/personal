# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_eliminar.ui'
#
# Created: Mon Jan 19 20:16:08 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        Eliminar.setObjectName(_fromUtf8("Eliminar"))
        Eliminar.resize(480, 140)
        Eliminar.setMinimumSize(QtCore.QSize(480, 140))
        Eliminar.setMaximumSize(QtCore.QSize(480, 140))
        Eliminar.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Eliminar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblMensaje = QtGui.QLabel(Eliminar)
        self.lblMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensaje.setObjectName(_fromUtf8("lblMensaje"))
        self.verticalLayout.addWidget(self.lblMensaje)
        self.buttonBox = QtGui.QDialogButtonBox(Eliminar)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Eliminar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Eliminar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Eliminar.reject)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(QtGui.QApplication.translate("Eliminar", "Eliminar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMensaje.setText(QtGui.QApplication.translate("Eliminar", "¿Está seguro de querer eliminar este empleado?", None, QtGui.QApplication.UnicodeUTF8))

