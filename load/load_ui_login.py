#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.usuariodao import UsuarioDao


#2.- Cargar archivo .ui
class Load_ui_login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_login.ui", self)
        self.resize(1200, 800)
        self.show()

        self.usuariodao = UsuarioDao()

#4.- Conectar botones a funciones
        self.boton_login.clicked.connect(self.iniciar_sesion)
        self.boton_registro.clicked.connect(self.registrar_usuario)
        self.login_password.returnPressed.connect(self.iniciar_sesion)

#5.- Operaciones con el modelo de datos 
    def iniciar_sesion(self):
        # Obtener datos de los campos
        nombre = self.login_user.text()
        contraseña = self.login_password.text()
        
        # Validar que no estén vacíos
        if not nombre or not contraseña:
            QtWidgets.QMessageBox.warning(self, "Error", "Complete todos los campos")
            return
        
        # Validar usuario y contraseña
        exito, id_usuario = self.usuariodao.confirmarContraseña(nombre, contraseña)
        
        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", f"Bienvenido {nombre}")
            self.accept() 
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
            self.login_password.clear()
            self.login_password.setFocus()
    
    def registrar_usuario(self):
        # Obtener datos de los campos
        nombre = self.login_user.text()
        contraseña = self.login_password.text()
        
        # Validar que no estén vacíos
        if not nombre or not contraseña:
            QtWidgets.QMessageBox.warning(self, "Error", "Complete todos los campos")
            return
        
        # Registrar usuario
        exito = self.usuariodao.registrarUsuario(nombre, contraseña)
        
        if exito:
            QtWidgets.QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente")
            self.login_user.clear()
            self.login_password.clear()
            self.login_user.setFocus()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "El usuario ya existe")