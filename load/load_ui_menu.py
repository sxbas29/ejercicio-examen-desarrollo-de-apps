#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.usuariodao import UsuarioDao


#2.- Cargar archivo .ui
class Load_ui_menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_menu.ui", self)
        font = QtGui.QFont()
        font.setPointSize(10)
        for widget in self.findChildren(QtWidgets.QWidget):
            if widget.font().pointSize() <= 0:
                widget.setFont(font)
        self.resize(1200, 800)
        self.show()

        self.usuariodao = UsuarioDao()

#4.- Conectar botones a funciones
        self.menu_productos.clicked.connect(self.productos)
        self.menu_empleados.clicked.connect(self.empleados)
        self.menu_logout.clicked.connect(self.cerrar_sesion)

    def productos (self):
        from load.load_ui_productos import Load_ui_productos
        
        self.hide()
        
        self.ventana_productos = Load_ui_productos(ventana_menu=self)
        self.ventana_productos.show()

    def empleados (self):
        from load.load_ui_empleados import Load_ui_empleados
        
        self.hide()
        
        self.ventana_empleados = Load_ui_empleados(ventana_menu=self)
        self.ventana_empleados.show()

    def cerrar_sesion(self):
        self.close()
        QtWidgets.QApplication.quit()