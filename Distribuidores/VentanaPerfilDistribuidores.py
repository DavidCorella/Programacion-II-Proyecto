from PyQt6 import QtCore,QtGui,QtWidgets
from Distribuidores.AsignarDistribuidores import Ui_DialogDistribuidores
import SQLBD.SQLQuerys as sql

class PerfilesDistribuidor (QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_DialogDistribuidores()
        self.ui.setupUi(self)
        self.ActualizarTabla()
        self.ui.BtnAnadir.clicked.connect(self.BtnAnadir_clicked_Distr)

    def ActualizarTabla(self):
        resultado = sql.ObtenerDistrubidores()
        self.ui.TblPerfiles.setRowCount(0)
        fila = self.ui.TblPerfiles.rowCount()
        for i in resultado:
            self.ui.TblPerfiles.insertRow(fila)
            columna = str(i).replace("(","").replace("'","").replace(")","").split(",")
            for j in range(0,2):
                self.ui.TblPerfiles.setItem(fila,j,QtWidgets.QTableWidgetItem(columna[j]))
            fila +=1
    
    def BtnAnadir_clicked_Distr(self):
        Codigo = self.ui.txtCodigoDistribuidores.text()
        Nombre = self.ui.txtNombreDistribuidores.text()
        if(Codigo != "" and Nombre != ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setWindowTitle("Desea Continuar?")
            msg.setText("Desea registrar al distribuidor?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            opcion = msg.exec()
            if(opcion == QtWidgets.QMessageBox.StandardButton.Yes):
                print(Codigo,Nombre)
                sql.RegistrarDistribuidor(Codigo,Nombre)
                self.ui.txtCodigoDistribuidores.setText("")
                self.ui.txtNombreDistribuidores.setText("")
                self.ActualizarTabla()