from PyQt6 import QtCore,QtGui,QtWidgets
from Core.uiFrmPrincipal import Ui_frmPrincipal
from Bodegas.VentanaBodega import DialogBodega
from Articulos.VentanaRegistro import DialogoRegistro
from Distribuidores.VentanaDistribuidores import DialogoDistribuidores
from Distribuidores.VentanaPerfilDistribuidores import PerfilesDistribuidor
from Articulos.VentanaIngresoaBodega import VentanaIngresoBodega
import SQLBD.SQLQuerys as sql

class FrmPrincipal(QtWidgets.QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_frmPrincipal()
        self.ventanaDialogBodega = DialogBodega()
        self.ui.setupUi(self)
        self.cmbBodegas_Actualizar()
        self.ui.btnRegistarArticulo.clicked.connect(self.RegistroArticulo)
        self.ui.btnCrearBodega.clicked.connect(self.btnCrearBodega_Clicked_AbrirDialog)
        self.ui.btnMostrar.clicked.connect(self.btnMostrar_Clicked_VerDatos)
        self.ventanaDialogBodega.ui.btnCrear.clicked.connect(self.cmbBodegas_Actualizar)
        self.ventanaDialogBodega.ui.btnEliminarBod.clicked.connect(self.cmbBodegas_Actualizar)
        self.ui.btnDistribuidores.clicked.connect(self.Distribuidores)
        self.ui.BtnAdmDistribuidores.clicked.connect(self.PerfilesDistribuidores)
        self.ui.btnGuardarArticulo.clicked.connect(self.IngresodeArticulo)
        
    def btnCrearBodega_Clicked_AbrirDialog(self):
        self.ventanaDialogBodega.show()
        
    def btnMostrar_Clicked_VerDatos(self):
        resultado = sql.seleccionarTabla(self.ui.cmbBodega.currentText().replace("Bodega",""))
        self.ui.tblDatos.setRowCount(0)
        fila = self.ui.tblDatos.rowCount()
        for i in resultado:
            self.ui.tblDatos.insertRow(fila)
            columna = str(i).replace("(","").replace("'","").replace(")","").split(",")
            for j in range(0,4):
                self.ui.tblDatos.setItem(fila,j,QtWidgets.QTableWidgetItem(columna[j]))
            fila +=1
    
    def cmbBodegas_Actualizar(self):
        self.ui.cmbBodega.clear()
        j = 0
        tablas = sql.obtenerTablas()
        for i in tablas:
            if(tablas[0]!=i and tablas[-1] != i):
                self.ui.cmbBodega.addItem(str(i).replace("('","").replace("',)",""))
                j+=1

    def RegistroArticulo(self):
        self.VentanaRegistro = DialogoRegistro()
        self.VentanaRegistro.show()

    def Distribuidores(self):
        self.VentanaDistribuidores = DialogoDistribuidores()
        self.VentanaDistribuidores.show()

    def IngresodeArticulo(self):
        self.VentanaIngresos = VentanaIngresoBodega()
        self.VentanaIngresos.show()

    def PerfilesDistribuidores(self):
        self.VentanaPerfiles = PerfilesDistribuidor()
        self.VentanaPerfiles.show()