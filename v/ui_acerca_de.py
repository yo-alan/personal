# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/undercover/personal/v/ui_acerca_de.ui'
#
# Created: Fri Jan 23 13:09:52 2015
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
        Acerca_de.resize(450, 241)
        Acerca_de.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Acerca_de)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(Acerca_de)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.lblMensaje = QtGui.QLabel(Acerca_de)
        self.lblMensaje.setLineWidth(3)
        self.lblMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensaje.setObjectName(_fromUtf8("lblMensaje"))
        self.verticalLayout.addWidget(self.lblMensaje)
        self.label_6 = QtGui.QLabel(Acerca_de)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_3 = QtGui.QLabel(Acerca_de)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_7 = QtGui.QLabel(Acerca_de)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtGui.QLabel(Acerca_de)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.buttonBox = QtGui.QDialogButtonBox(Acerca_de)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Acerca_de)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Acerca_de.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Acerca_de.reject)
        QtCore.QMetaObject.connectSlotsByName(Acerca_de)

    def retranslateUi(self, Acerca_de):
        Acerca_de.setWindowTitle(QtGui.QApplication.translate("Acerca_de", "Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Acerca_de", "Acerca de...", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMensaje.setText(QtGui.QApplication.translate("Acerca_de", "<html><head/><body><p>Personal es una aplicación creada para la administración de los</p><p>empleados de la Secretaría de Cultura de la Provincia del Chubut.</p><p>Cubriendo los aspectos básicos de los mismos y sus licencias.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Acerca_de", "Autor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Acerca_de", "Marchán, Alan. Copyright (c) 2015.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Acerca_de", "E-Mail:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Acerca_de", "marchanalan@hotmail.com", None, QtGui.QApplication.UnicodeUTF8))

