from PyQt6 import QtCore,QtGui,QtWidgets
import SQLBD.SQLQuerys as BD
from Articulos.frmRegistrarArticulo import Ui_DlgRegistrarArticulo

class DialogoRegistro (QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_DlgRegistrarArticulo()
        self.ui.setupUi(self)
        self.ui.BtnResgistrar.clicked.connect(self.Btn_Clicked_Registro)
        Expr_Regular = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        inputValidator = QtGui.QRegularExpressionValidator(Expr_Regular,self.ui.txtCodigo)
        inputValidator2 = QtGui.QRegularExpressionValidator(Expr_Regular,self.ui.txtPrecio)
        inputValidator3 = QtGui.QRegularExpressionValidator(Expr_Regular,self.ui.txtCantidad)
        self.ui.txtCodigo.setValidator(inputValidator)
        self.ui.txtPrecio.setValidator(inputValidator2)
        self.ui.txtCantidad.setValidator(inputValidator3)

    def Btn_Clicked_Registro (self):
        Codigo = self.ui.txtCodigo.text()
        Nombre = self.ui.txtNombre.text()
        Precio = self.ui.txtPrecio.text()
        Cantidad = self.ui.txtCantidad.text()   
        if(Codigo != "" and Nombre != "" and Precio != "" and Cantidad != ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setWindowTitle("Desea Continuar?")
            msg.setText("Desea registrar el articulo?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            opcion = msg.exec()
            if(opcion == QtWidgets.QMessageBox.StandardButton.Yes):

                BD.registrarArticulo(Codigo,Nombre,Precio,Cantidad)
                self.ui.txtCodigo.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtPrecio.setText("")
                self.ui.txtCantidad.setText("")
        
        