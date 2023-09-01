from PyQt6 import QtCore,QtGui,QtWidgets
import sys
from Core.VentanaPrincipal import FrmPrincipal

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = FrmPrincipal()
    ventana.show()
    sys.exit(app.exec())