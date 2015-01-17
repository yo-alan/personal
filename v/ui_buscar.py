# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_buscar.ui'
#
# Created: Sat Jan 17 15:29:33 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Buscar(object):
    def setupUi(self, Buscar):
        Buscar.setObjectName(_fromUtf8("Buscar"))
        Buscar.resize(480, 360)
        Buscar.setMinimumSize(QtCore.QSize(480, 360))
        Buscar.setMaximumSize(QtCore.QSize(480, 360))
        Buscar.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Buscar)
        self.buttonBox.setGeometry(QtCore.QRect(160, 320, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Buscar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Buscar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Buscar.reject)
        QtCore.QMetaObject.connectSlotsByName(Buscar)

    def retranslateUi(self, Buscar):
        Buscar.setWindowTitle(QtGui.QApplication.translate("Buscar", "Buscar empleado", None, QtGui.QApplication.UnicodeUTF8))

