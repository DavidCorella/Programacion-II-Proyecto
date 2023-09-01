import traceback
from PyQt6 import QtCore,QtGui,QtWidgets
from Distribuidores.Distribuidores import Ui_Dialog
import SQLBD.SQLQuerys as sql
import os

class DialogoDistribuidores (QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.CmbDistribuidores_Actualizar()
        self.ui.CbxBodegasDist.currentIndexChanged.connect(self.ActualizarTabla)
        self.ActualizarTabla()
        Expr_Regular = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        inputValidator = QtGui.QRegularExpressionValidator(Expr_Regular,self.ui.txtCantidadDist)
        self.ui.txtCantidadDist.setValidator(inputValidator)
        self.CmbPerfiles_Actualizar()
        self.ui.BtnEnviar.clicked.connect(self.Btn_Clicked_Enviar)

    def ActualizarTabla(self):
        resultado = sql.seleccionarTabla(self.ui.CbxBodegasDist.currentText().replace("Bodega",""))
        self.ui.TblProductos.setRowCount(0)
        fila = self.ui.TblProductos.rowCount()
        for i in resultado:
            self.ui.TblProductos.insertRow(fila)
            columna = str(i).replace("(","").replace("'","").replace(")","").split(",")
            for j in range(0,4):
                self.ui.TblProductos.setItem(fila,j,QtWidgets.QTableWidgetItem(columna[j]))
            fila +=1

    def CmbDistribuidores_Actualizar(self):
        self.ui.CbxBodegasDist.clear()
        j = 0
        tablas = sql.obtenerTablas()
        for i in tablas:
            if (tablas[0] != i) and tablas[-1] != i:
                self.ui.CbxBodegasDist.addItem(str(i).replace("('","").replace("',)",""))
                j+=1

    def CmbPerfiles_Actualizar(self):
        self.ui.CmbDistribuirdores.clear()
        j = 0
        tablas = sql.ObtenerDistrubidoresCombobox()
        for i in tablas:
            self.ui.CmbDistribuirdores.addItem(str(i).replace("('","").replace("',)",""))
            j+=1

    def Btn_Clicked_Enviar(self):
        FilaSeleccionada = self.ui.TblProductos.selectedItems()
        if(self.ui.CbxBodegasDist.currentIndex == 0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowTitle("Seleccion?")
            msg.setText("No ha seleccionado ninguna bodega")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        elif (not FilaSeleccionada):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowTitle("Seleccion?")
            msg.setText("No ha seleccionado ningun articulo")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        elif (self.ui.CmbDistribuirdores.currentIndex == -1):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowTitle("Seleccion?")
            msg.setText("No ha seleccionado ningun distribuidor")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setWindowTitle("Desea Continuar?")
            msg.setText("Desea entregar el articulo al distribuidor seleccionado?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            opcion = msg.exec()
            if (opcion == QtWidgets.QMessageBox.StandardButton.Yes):
                Codigo = FilaSeleccionada[0].text()
                Nombre = FilaSeleccionada[1].text()
                Precio = FilaSeleccionada[2].text()
                Bodega = self.ui.CbxBodegasDist.currentText()
                self.EscribirReporte(FilaSeleccionada)
                CantidadEscogida = int(self.ui.txtCantidadDist.text())
                CantidadTabla = int(FilaSeleccionada[3].text())
                if (CantidadEscogida <= CantidadTabla):
                    Resultado = CantidadTabla - CantidadEscogida
                    if (Resultado > 0):
                        sql.ModificarCantidad(Codigo.strip(),Nombre.strip(),Precio.strip(),CantidadTabla,Resultado, Bodega.strip())
                    else: 
                        sql.EliminarArticulo(Codigo.strip(),Nombre.strip(),Precio.strip(),CantidadTabla,Bodega.strip())
                else:
                    msg.setText("La cantidad digitada no puede ser retirada")
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ActualizarTabla()
        

    def EscribirReporte(self, Seleccion):
        Auxiliar = os.listdir(".\\Reportes\\")
        try:
            if Auxiliar != []:
                Ruta = int(Auxiliar[-1].replace("Factura","").replace(".txt",""))+1
                archivo = open(".\\Reportes\\Factura"+str(Ruta)+".txt","w")      
                archivo.write("Distribuidor: "+self.ui.CmbDistribuirdores.currentText()+"\nCodigo: "+Seleccion[0].text()+"\nNombre: "+Seleccion[1].text()+"\nPrecio: "+Seleccion[2].text()+"\nCantidad: "+self.ui.txtCantidadDist.text())            
                archivo.close()
            else:
                archivo = open(".\\Reportes\\Factura1.txt","w")      
                archivo.write("Distribuidor: "+self.ui.CmbDistribuirdores.currentText()+"\nCodigo: "+Seleccion[0].text()+"\nNombre: "+Seleccion[1].text()+"\nPrecio: "+Seleccion[2].text()+"\nCantidad: "+self.ui.txtCantidadDist.text())            
                archivo.close()

        except OSError as oE:
                print(oE.strerror)
        except BaseException:
                print(traceback.format_exc())
    
