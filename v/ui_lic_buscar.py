# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_lic_buscar.ui'
#
# Created: Sun Dec 28 15:47:41 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Lic_Buscar(object):
    def setupUi(self, Lic_Buscar):
        Lic_Buscar.setObjectName(_fromUtf8("Lic_Buscar"))
        Lic_Buscar.resize(480, 360)
        Lic_Buscar.setMinimumSize(QtCore.QSize(480, 360))
        Lic_Buscar.setMaximumSize(QtCore.QSize(480, 360))
        Lic_Buscar.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Lic_Buscar)
        self.buttonBox.setGeometry(QtCore.QRect(160, 320, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Lic_Buscar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Lic_Buscar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Lic_Buscar.reject)
        QtCore.QMetaObject.connectSlotsByName(Lic_Buscar)

    def retranslateUi(self, Lic_Buscar):
        Lic_Buscar.setWindowTitle(QtGui.QApplication.translate("Lic_Buscar", "Buscar licencia", None, QtGui.QApplication.UnicodeUTF8))

