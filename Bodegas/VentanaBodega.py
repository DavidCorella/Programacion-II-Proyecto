from PyQt6 import QtCore, QtWidgets, QtGui
from Bodegas.uiFrmAdministrarBodegas import Ui_frmAdministrarBodegas
import SQLBD.SQLQuerys as sql
import mariadb
import Core.VentanaPrincipal as pp

class DialogBodega(QtWidgets.QDialog):
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_frmAdministrarBodegas()
        self.ui.setupUi(self)
        self.ui.btnCrear.clicked.connect(self.btnCrear_Clicked_CrearBodega)
        self.ui.btnEliminarBod.clicked.connect(self.btnEliminar_Clicked_EliminarBodega)
        self.actualizarCmbBodega()
        
    def btnCrear_Clicked_CrearBodega(self):
        bodegas=[]
        tablas = sql.obtenerTablas()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setWindowTitle("Desea Continuar?")
        msg.setText("Desea crear la bodega?")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        opcion = msg.exec()
        if(opcion == QtWidgets.QMessageBox.StandardButton.Yes):
            print(tablas[-1])
            if(str(tablas[1]).replace("('","").replace("',)","")=="Distribuidores"):
                sql.crearBodega(1)
            else:
                for i in tablas:
                    if(i != tablas[0] and i != tablas[-1]):
                        bodegas.append(int(str(i).replace("('Bodega","").replace("',)","")))
                j = 1
                for i in range(1,int(bodegas[-1])+1):
                    if(bodegas[0]!=1):
                        sql.crearBodega(1)
                        break
                    if(i==bodegas[-1]):
                        sql.crearBodega(i+1)
                        break
                    if(int(i)+1 != bodegas[j]):
                        sql.crearBodega(j+1)
                        break
                    j+=1

        self.actualizarCmbBodega()
        
    def btnEliminar_Clicked_EliminarBodega(self):
        if(self.ui.cmbBodegas.currentIndex()!=-1):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setWindowTitle("Desea Continuar?")
            msg.setText("Desea eliminar la Bodega")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            opcion = msg.exec()
            if(opcion == QtWidgets.QMessageBox.StandardButton.Yes): 
                sql.eliminarBodega(self.ui.cmbBodegas.itemText(self.ui.cmbBodegas.currentIndex()).replace("Bodega",""))
                self.actualizarCmbBodega()
        
    def actualizarCmbBodega(self):
        self.ui.cmbBodegas.clear()
        j = 0
        tablas = sql.obtenerTablas()
        for i in tablas:
            if(tablas[0]!=i and tablas[-1] != i):
                self.ui.cmbBodegas.addItem(str(i).replace("('","").replace("',)",""))
                j+=1
    
    def closeEvent( self,a0: QtGui.QCloseEvent) -> None:
        self.destroy()
        
        
        