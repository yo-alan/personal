# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_lic_editar.ui'
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

class Ui_Lic_Editar(object):
    def setupUi(self, Lic_Editar):
        Lic_Editar.setObjectName(_fromUtf8("Lic_Editar"))
        Lic_Editar.resize(417, 182)
        Lic_Editar.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Lic_Editar)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Lic_Editar)
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
        self.buttonBox = QtGui.QDialogButtonBox(Lic_Editar)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Lic_Editar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Lic_Editar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Lic_Editar.reject)
        QtCore.QMetaObject.connectSlotsByName(Lic_Editar)

    def retranslateUi(self, Lic_Editar):
        Lic_Editar.setWindowTitle(QtGui.QApplication.translate("Lic_Editar", "Editar licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Lic_Editar", "Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.deHasta.setDisplayFormat(QtGui.QApplication.translate("Lic_Editar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHasta.setText(QtGui.QApplication.translate("Lic_Editar", "Hasta:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblComentario.setText(QtGui.QApplication.translate("Lic_Editar", "Comentario:", None, QtGui.QApplication.UnicodeUTF8))
        self.deDesde.setDisplayFormat(QtGui.QApplication.translate("Lic_Editar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTIpoLicencia.setText(QtGui.QApplication.translate("Lic_Editar", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDesde.setText(QtGui.QApplication.translate("Lic_Editar", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(0, QtGui.QApplication.translate("Lic_Editar", "18", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(1, QtGui.QApplication.translate("Lic_Editar", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(2, QtGui.QApplication.translate("Lic_Editar", "53", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(3, QtGui.QApplication.translate("Lic_Editar", "58", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(4, QtGui.QApplication.translate("Lic_Editar", "Comisión", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(5, QtGui.QApplication.translate("Lic_Editar", "Enfermedad", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(6, QtGui.QApplication.translate("Lic_Editar", "Franco", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoLicencia.setItemText(7, QtGui.QApplication.translate("Lic_Editar", "Otro", None, QtGui.QApplication.UnicodeUTF8))

