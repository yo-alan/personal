# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/undercover/personal/v/ui_acerca_de.ui'
#
# Created: Fri Jan 23 09:07:23 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Acerca_de(object):
    def setupUi(self, Acerca_de):
        Acerca_de.setObjectName(_fromUtf8("Acerca_de"))
        Acerca_de.resize(480, 140)
        Acerca_de.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Acerca_de)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblMensaje = QtGui.QLabel(Acerca_de)
        self.lblMensaje.setObjectName(_fromUtf8("lblMensaje"))
        self.verticalLayout.addWidget(self.lblMensaje)
        self.label = QtGui.QLabel(Acerca_de)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Acerca_de)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(Acerca_de)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.buttonBox = QtGui.QDialogButtonBox(Acerca_de)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Acerca_de)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Acerca_de.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Acerca_de.reject)
        QtCore.QMetaObject.connectSlotsByName(Acerca_de)

    def retranslateUi(self, Acerca_de):
        Acerca_de.setWindowTitle(QtGui.QApplication.translate("Acerca_de", "Acerca de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMensaje.setText(QtGui.QApplication.translate("Acerca_de", "Personal es una aplicación creada para la administración de los", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Acerca_de", "empleados de la secretaría de cultura. Cubre los aspectos básicos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Acerca_de", "de los mismos.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Acerca_de", "Autor: marchanalan@hotmail.com", None, QtGui.QApplication.UnicodeUTF8))

