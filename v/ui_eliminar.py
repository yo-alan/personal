# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_eliminar.ui'
#
# Created: Sat Jan 31 18:27:20 2015
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
        Eliminar.setModal(True)

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(QtGui.QApplication.translate("Eliminar", "Eliminar empleado", None, QtGui.QApplication.UnicodeUTF8))

