from PyQt6 import QtCore,QtGui,QtWidgets
import SQLBD.SQLQuerys as BD
from Articulos.IngresoArticulos import Ui_IngresoaBodega
import SQLBD.SQLQuerys as sql

class VentanaIngresoBodega (QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_IngresoaBodega()
        self.ui.setupUi(self)
        self.ActualizarTabla()
        self.CmbIngresoaBodega_Actualizar()
        self.ui.BtnIngresarArticulos.clicked.connect(self.GuardarenBodega)


    def ActualizarTabla(self):
        resultado = sql.SeleccionarTablaArticulos()
        self.ui.TblArticulosNoRegistrados.setRowCount(0)
        fila = self.ui.TblArticulosNoRegistrados.rowCount()
        for i in resultado:
            self.ui.TblArticulosNoRegistrados.insertRow(fila)
            columna = str(i).replace("(","").replace("'","").replace(")","").split(",")
            for j in range(0,4):
                self.ui.TblArticulosNoRegistrados.setItem(fila,j,QtWidgets.QTableWidgetItem(columna[j]))
            fila +=1

    def CmbIngresoaBodega_Actualizar(self):
        self.ui.CmbBodegas.clear()
        j = 0
        tablas = sql.obtenerTablas()
        for i in tablas:
            if (tablas[0] != i and tablas[-1]!=i):
                self.ui.CmbBodegas.addItem(str(i).replace("('","").replace("',)",""))
                j+=1

    def GuardarenBodega(self): 
        Seleccion = self.ui.TblArticulosNoRegistrados.selectedItems()
        if(self.ui.CmbBodegas.currentIndex == 0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowTitle("Seleccion?")
            msg.setText("No ha seleccionado ninguna bodega")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        elif (not Seleccion):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowTitle("Seleccion?")
            msg.setText("No ha seleccionado ningun articulo")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setWindowTitle("Desea Continuar?")
            msg.setText("Desea registrar el articulo en la bodega seleccionada?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            opcion = msg.exec()
            if (opcion == QtWidgets.QMessageBox.StandardButton.Yes):
                BD.GuardarArticuloBodega(self.ui.CmbBodegas.currentText().replace("Bodega",""),Seleccion[0].text().strip(),Seleccion[1].text().strip(),Seleccion[2].text().strip(),Seleccion[3].text().strip())
                self.ActualizarTabla()
                
