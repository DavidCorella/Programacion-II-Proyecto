# Form implementation generated from reading ui file 'Distribuidores.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 450)
        self.LblDistribuidores = QtWidgets.QLabel(parent=Dialog)
        self.LblDistribuidores.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblDistribuidores.setFont(font)
        self.LblDistribuidores.setObjectName("LblDistribuidores")
        self.CbxBodegasDist = QtWidgets.QComboBox(parent=Dialog)
        self.CbxBodegasDist.setGeometry(QtCore.QRect(20, 80, 101, 22))
        self.CbxBodegasDist.setObjectName("CbxBodegasDist")
        self.LblBodega = QtWidgets.QLabel(parent=Dialog)
        self.LblBodega.setGeometry(QtCore.QRect(20, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblBodega.setFont(font)
        self.LblBodega.setObjectName("LblBodega")
        self.txtCantidadDist = QtWidgets.QLineEdit(parent=Dialog)
        self.txtCantidadDist.setGeometry(QtCore.QRect(20, 400, 113, 20))
        self.txtCantidadDist.setObjectName("txtCantidadDist")
        self.LblCantidad = QtWidgets.QLabel(parent=Dialog)
        self.LblCantidad.setGeometry(QtCore.QRect(20, 370, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblCantidad.setFont(font)
        self.LblCantidad.setObjectName("LblCantidad")
        self.BtnEnviar = QtWidgets.QPushButton(parent=Dialog)
        self.BtnEnviar.setGeometry(QtCore.QRect(270, 380, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnEnviar.setFont(font)
        self.BtnEnviar.setObjectName("BtnEnviar")
        self.TblProductos = QtWidgets.QTableWidget(parent=Dialog)
        self.TblProductos.setGeometry(QtCore.QRect(20, 121, 411, 241))
        self.TblProductos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TblProductos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.TblProductos.setObjectName("TblProductos")
        self.TblProductos.setColumnCount(4)
        self.TblProductos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TblProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblProductos.setHorizontalHeaderItem(3, item)
        self.CmbDistribuirdores = QtWidgets.QComboBox(parent=Dialog)
        self.CmbDistribuirdores.setGeometry(QtCore.QRect(300, 80, 121, 22))
        self.CmbDistribuirdores.setObjectName("CmbDistribuirdores")
        self.LblDistribuidoresperfil = QtWidgets.QLabel(parent=Dialog)
        self.LblDistribuidoresperfil.setGeometry(QtCore.QRect(300, 60, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblDistribuidoresperfil.setFont(font)
        self.LblDistribuidoresperfil.setObjectName("LblDistribuidoresperfil")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LblDistribuidores.setText(_translate("Dialog", "Distribuidores"))
        self.LblBodega.setText(_translate("Dialog", "Bodega"))
        self.LblCantidad.setText(_translate("Dialog", "Cantidad"))
        self.BtnEnviar.setText(_translate("Dialog", "Enviar y generar reporte"))
        item = self.TblProductos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Codigo"))
        item = self.TblProductos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.TblProductos.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Precio"))
        item = self.TblProductos.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Cantidad"))
        self.LblDistribuidoresperfil.setText(_translate("Dialog", "Distribuidores"))
