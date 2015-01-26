# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/undercover/personal/v/ui_error.ui'
#
# Created: Mon Jan 26 10:56:39 2015
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
        Error.setModal(True)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        Error.setWindowTitle(QtGui.QApplication.translate("Error", "ERROR", None, QtGui.QApplication.UnicodeUTF8))

