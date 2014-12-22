# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/Escritorio/python/MVC/v/ui_lic_agregar.ui'
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

class Ui_Lic_Agregar(object):
    def setupUi(self, Lic_Agregar):
        Lic_Agregar.setObjectName(_fromUtf8("Lic_Agregar"))
        Lic_Agregar.resize(417, 182)
        Lic_Agregar.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Lic_Agregar)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Lic_Agregar)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leComentario = QtGui.QLineEdit(self.groupBox)
        self.leComentario.setObjectName(_fromUtf8("leComentario"))
        self.gridLayout.addWidget(self.leComentario, 4, 1, 1, 3)
        self.deHasta = QtGui.QDateEdit(self.groupBox)
        self.deHasta.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.deHasta.setObjectName(_fromUtf8("deHasta"))
        self.gridLayout.addWidget(self.deHasta, 1, 3, 1, 1)
        self.lblHasta = QtGui.QLabel(self.groupBox)
        self.lblHasta.setObjectName(_fromUtf8("lblHasta"))
        self.gridLayout.addWidget(self.lblHasta, 1, 2, 1, 1)
        self.lblComentario = QtGui.QLabel(self.groupBox)
        self.lblComentario.setObjectName(_fromUtf8("lblComentario"))
        self.gridLayout.addWidget(self.lblComentario, 4, 0, 1, 1)
        self.deDesde = QtGui.QDateEdit(self.groupBox)
        self.deDesde.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.deDesde.setObjectName(_fromUtf8("deDesde"))
        self.gridLayout.addWidget(self.deDesde, 1, 1, 1, 1)
        self.lblTIpoLicencia = QtGui.QLabel(self.groupBox)
        self.lblTIpoLicencia.setObjectName(_fromUtf8("lblTIpoLicencia"))
        self.gridLayout.addWidget(self.lblTIpoLicencia, 0, 0, 1, 1)
        self.lblDesde = QtGui.QLabel(self.groupBox)
        self.lblDesde.setObjectName(_fromUtf8("lblDesde"))
        self.gridLayout.addWidget(self.lblDesde, 1, 0, 1, 1)
        self.cmbTipoLicencia = QtGui.QComboBox(self.groupBox)
        self.cmbTipoLicencia.setObjectName(_fromUtf8("cmbTipoLicencia"))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.cmbTipoLicencia.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbTipoLicencia, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Lic_Agregar)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Lic_Agregar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Lic_Agregar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Lic_Agregar.reject)
        QtCore.QMetaObject.connectSlotsByName(Lic_Agregar)

    def retranslateUi(self, Lic_Agregar):
        Lic_Agregar.setWindowTitle(QtGui.QApplication.translate("Lic_Agregar", "Agregar licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Lic_Agregar", "Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.deHasta.setDisplayFormat(QtGui.QApplication.translate("Lic_Agregar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHasta.setText(QtGui.QApplication.translate("Lic_Agregar", "Hasta:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblComentario.setText(QtGui.QApplication.translate("Lic_Agregar", "Comentario:", None, QtGui.QApplication.UnicodeUTF8))
        self.deDesde.setDisplayFormat(QtGui.QApplication.translate("Lic_Agregar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTIpoLicencia.setText(QtGui.QApplication.translate("Lic_Agregar", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDesde.setText(QtGui.QApplication.translate("Lic_Agregar", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(0, QtGui.QApplication.translate("Lic_Agregar", "18", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(1, QtGui.QApplication.translate("Lic_Agregar", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(2, QtGui.QApplication.translate("Lic_Agregar", "53", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(3, QtGui.QApplication.translate("Lic_Agregar", "58", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(4, QtGui.QApplication.translate("Lic_Agregar", "Comisión", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(5, QtGui.QApplication.translate("Lic_Agregar", "Enfermedad", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(6, QtGui.QApplication.translate("Lic_Agregar", "Franco", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(7, QtGui.QApplication.translate("Lic_Agregar", "Otro", None, QtGui.QApplication.UnicodeUTF8))

