# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alan/dev/personal/v/ui_editar.ui'
#
# Created: Mon Jan 19 20:16:07 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Editar(object):
    def setupUi(self, Editar):
        Editar.setObjectName(_fromUtf8("Editar"))
        Editar.resize(540, 312)
        Editar.setMinimumSize(QtCore.QSize(540, 312))
        Editar.setMaximumSize(QtCore.QSize(540, 312))
        Editar.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Editar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Editar)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lblNombre = QtGui.QLabel(self.groupBox)
        self.lblNombre.setObjectName(_fromUtf8("lblNombre"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblNombre)
        self.leNombre = QtGui.QLineEdit(self.groupBox)
        self.leNombre.setObjectName(_fromUtf8("leNombre"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.leNombre)
        self.lblApellido = QtGui.QLabel(self.groupBox)
        self.lblApellido.setObjectName(_fromUtf8("lblApellido"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblApellido)
        self.leApellido = QtGui.QLineEdit(self.groupBox)
        self.leApellido.setObjectName(_fromUtf8("leApellido"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.leApellido)
        self.lblFechaNacimiento = QtGui.QLabel(self.groupBox)
        self.lblFechaNacimiento.setObjectName(_fromUtf8("lblFechaNacimiento"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblFechaNacimiento)
        self.deFechaNacimiento = QtGui.QDateEdit(self.groupBox)
        self.deFechaNacimiento.setObjectName(_fromUtf8("deFechaNacimiento"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.deFechaNacimiento)
        self.lblGenero = QtGui.QLabel(self.groupBox)
        self.lblGenero.setObjectName(_fromUtf8("lblGenero"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblGenero)
        self.cmbGenero = QtGui.QComboBox(self.groupBox)
        self.cmbGenero.setObjectName(_fromUtf8("cmbGenero"))
        self.cmbGenero.addItem(_fromUtf8(""))
        self.cmbGenero.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmbGenero)
        self.lblCuil = QtGui.QLabel(self.groupBox)
        self.lblCuil.setObjectName(_fromUtf8("lblCuil"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblCuil)
        self.leCuil = QtGui.QLineEdit(self.groupBox)
        self.leCuil.setMaxLength(13)
        self.leCuil.setObjectName(_fromUtf8("leCuil"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.leCuil)
        self.lblTelefono = QtGui.QLabel(self.groupBox)
        self.lblTelefono.setObjectName(_fromUtf8("lblTelefono"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.lblTelefono)
        self.leTelefono = QtGui.QLineEdit(self.groupBox)
        self.leTelefono.setObjectName(_fromUtf8("leTelefono"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.leTelefono)
        self.lblDomicilio = QtGui.QLabel(self.groupBox)
        self.lblDomicilio.setObjectName(_fromUtf8("lblDomicilio"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.lblDomicilio)
        self.leDomicilio = QtGui.QLineEdit(self.groupBox)
        self.leDomicilio.setObjectName(_fromUtf8("leDomicilio"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.leDomicilio)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Editar)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblNroLegajo = QtGui.QLabel(self.groupBox_2)
        self.lblNroLegajo.setObjectName(_fromUtf8("lblNroLegajo"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblNroLegajo)
        self.sbNroLegajo = QtGui.QSpinBox(self.groupBox_2)
        self.sbNroLegajo.setMinimum(1)
        self.sbNroLegajo.setMaximum(1000)
        self.sbNroLegajo.setObjectName(_fromUtf8("sbNroLegajo"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbNroLegajo)
        self.lblFechaIngreso = QtGui.QLabel(self.groupBox_2)
        self.lblFechaIngreso.setObjectName(_fromUtf8("lblFechaIngreso"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblFechaIngreso)
        self.deFechaIngreso = QtGui.QDateEdit(self.groupBox_2)
        self.deFechaIngreso.setObjectName(_fromUtf8("deFechaIngreso"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.deFechaIngreso)
        self.lblRevista = QtGui.QLabel(self.groupBox_2)
        self.lblRevista.setObjectName(_fromUtf8("lblRevista"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblRevista)
        self.cmbRevista = QtGui.QComboBox(self.groupBox_2)
        self.cmbRevista.setObjectName(_fromUtf8("cmbRevista"))
        self.cmbRevista.addItem(_fromUtf8(""))
        self.cmbRevista.addItem(_fromUtf8(""))
        self.cmbRevista.addItem(_fromUtf8(""))
        self.cmbRevista.addItem(_fromUtf8(""))
        self.cmbRevista.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmbRevista)
        self.lblCargo = QtGui.QLabel(self.groupBox_2)
        self.lblCargo.setObjectName(_fromUtf8("lblCargo"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblCargo)
        self.cmbCargo = QtGui.QComboBox(self.groupBox_2)
        self.cmbCargo.setObjectName(_fromUtf8("cmbCargo"))
        self.cmbCargo.addItem(_fromUtf8(""))
        self.cmbCargo.addItem(_fromUtf8(""))
        self.cmbCargo.addItem(_fromUtf8(""))
        self.cmbCargo.addItem(_fromUtf8(""))
        self.cmbCargo.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.cmbCargo)
        self.lblNivel = QtGui.QLabel(self.groupBox_2)
        self.lblNivel.setObjectName(_fromUtf8("lblNivel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.lblNivel)
        self.leNivel = QtGui.QLineEdit(self.groupBox_2)
        self.leNivel.setObjectName(_fromUtf8("leNivel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.leNivel)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Editar)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Editar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Editar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Editar.reject)
        QtCore.QMetaObject.connectSlotsByName(Editar)

    def retranslateUi(self, Editar):
        Editar.setWindowTitle(QtGui.QApplication.translate("Editar", "Editar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Editar", "Datos personales", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setText(QtGui.QApplication.translate("Editar", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblApellido.setText(QtGui.QApplication.translate("Editar", "Apellido:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaNacimiento.setText(QtGui.QApplication.translate("Editar", "F. Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.deFechaNacimiento.setDisplayFormat(QtGui.QApplication.translate("Editar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGenero.setText(QtGui.QApplication.translate("Editar", "Género:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGenero.setItemText(0, QtGui.QApplication.translate("Editar", "Femenino", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGenero.setItemText(1, QtGui.QApplication.translate("Editar", "Masculino", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCuil.setText(QtGui.QApplication.translate("Editar", "Cuil:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setText(QtGui.QApplication.translate("Editar", "Teléfono:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDomicilio.setText(QtGui.QApplication.translate("Editar", "Domicilio:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Editar", "Datos laborales", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNroLegajo.setText(QtGui.QApplication.translate("Editar", "Nro. Legajo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaIngreso.setText(QtGui.QApplication.translate("Editar", "Ingreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.deFechaIngreso.setDisplayFormat(QtGui.QApplication.translate("Editar", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRevista.setText(QtGui.QApplication.translate("Editar", "Sit. de Revista:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRevista.setItemText(0, QtGui.QApplication.translate("Editar", "Comisión", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRevista.setItemText(1, QtGui.QApplication.translate("Editar", "Pasantía", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRevista.setItemText(2, QtGui.QApplication.translate("Editar", "Permanente", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRevista.setItemText(3, QtGui.QApplication.translate("Editar", "Temporaria", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRevista.setItemText(4, QtGui.QApplication.translate("Editar", "Transitoria", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCargo.setText(QtGui.QApplication.translate("Editar", "Cargo:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCargo.setItemText(0, QtGui.QApplication.translate("Editar", "Administrativo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCargo.setItemText(1, QtGui.QApplication.translate("Editar", "Jerárquico", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCargo.setItemText(2, QtGui.QApplication.translate("Editar", "Obrero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCargo.setItemText(3, QtGui.QApplication.translate("Editar", "Profesional", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCargo.setItemText(4, QtGui.QApplication.translate("Editar", "Servicio", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNivel.setText(QtGui.QApplication.translate("Editar", "Nivel:", None, QtGui.QApplication.UnicodeUTF8))

