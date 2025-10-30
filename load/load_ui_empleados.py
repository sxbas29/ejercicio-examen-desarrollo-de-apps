#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.empleadodao import EmpleadoDAO


#2.- Cargar archivo .ui
class Load_ui_empleados(QtWidgets.QMainWindow):
    def __init__(self, ventana_menu=None):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_empleados.ui", self)

        font = QtGui.QFont()
        font.setPointSize(10)
        for widget in self.findChildren(QtWidgets.QWidget):
            if widget.font().pointSize() <= 0:
                widget.setFont(font)

        self.resize(1200, 800)
        self.show()


        self.ventana_menu = ventana_menu
        self.empleadodao = EmpleadoDAO()

#3.- Configurar contenedores#

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
       
        self.boton_salir.clicked.connect(self.regresar_menu)

        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        #menu lateral
        self.boton_menu.clicked.connect(self.mover_menu)
        #Fijar ancho columnas
        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

#4.- Conectar botones a funciones
        #Botones para cambiar de página
        self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

        #Botones para guardar, buscar, actualizar, eliminar y limpiar
        self.accion_guardar.clicked.connect(self.guardar_empleado)
        self.accion_actualizar.clicked.connect(self.actualizar_empleado)
        self.accion_eliminar.clicked.connect(self.eliminar_empleado)
        self.accion_limpiar.clicked.connect(self.limpiar_empleado)
        self.buscar_actualizar.clicked.connect(self.buscar_empleado_actualizar)
        self.buscar_eliminar.clicked.connect(self.buscar_empleado_eliminar)
        self.buscar_buscar.clicked.connect(self.buscar_empleado_buscar)
        self.boton_refresh.clicked.connect(self.actualizar_tabla)

    def regresar_menu(self):
        if self.ventana_menu:
            self.ventana_menu.show()
            self.close()
        else:
            from load.load_ui_menu import Load_ui_menu
            self.ventana_menu_nueva = Load_ui_menu()
            self.ventana_menu_nueva.show()
            self.close()

#5.- Operaciones con el modelo de datos 
    def actualizar_tabla(self):
        empleados = self.empleadodao.listarEmpleados()
        self.tabla_consulta.clearContents()
        self.tabla_consulta.setRowCount(len(empleados))
        self.tabla_consulta.setColumnCount(4)
        self.tabla_consulta.setHorizontalHeaderLabels(['Clave', 'Nombre', 'Teléfono', 'Ciudad'])
        
        for fila, empleado in enumerate(empleados):
            self.tabla_consulta.setItem(fila, 0, QTableWidgetItem(str(empleado[0])))
            self.tabla_consulta.setItem(fila, 1, QTableWidgetItem(str(empleado[1])))
            self.tabla_consulta.setItem(fila, 2, QTableWidgetItem(str(empleado[2])))
            self.tabla_consulta.setItem(fila, 3, QTableWidgetItem(str(empleado[3])))

        self.tabla_consulta.resizeColumnsToContents()

    def buscar_empleado_actualizar(self):
        self.empleadodao.empleado.clave = self.clave_actualizar.text()
        datos = self.empleadodao.buscarEmpleado()
    
        if len(datos) > 0:
            self.nombre_actualizar.setText(str(datos[0][1]))
            self.telefono_actualizar.setText(str(datos[0][2]))
            self.ciudad_actualizar.setText(str(datos[0][3]))
    
    def buscar_empleado_eliminar(self):
        self.empleadodao.empleado.clave = self.clave_eliminar.text()
        datos = self.empleadodao.buscarEmpleado()
    
        if len(datos) > 0:
            self.nombre_eliminar.setText(str(datos[0][1]))
            self.telefono_eliminar.setText(str(datos[0][2]))
            self.ciudad_eliminar.setText(str(datos[0][3]))
    
    def buscar_empleado_buscar(self):
        self.empleadodao.empleado.clave = self.clave_buscar.text()
        datos = self.empleadodao.buscarEmpleado()
    
        if len(datos) > 0:
            self.nombre_buscar.setText(str(datos[0][1]))
            self.telefono_buscar.setText(str(datos[0][2]))
            self.ciudad_buscar.setText(str(datos[0][3]))
    
    def guardar_empleado(self):
        self.empleadodao.empleado.clave = self.clave_agregar.text()
        self.empleadodao.empleado.nombre = self.nombre_agregar.text()
        self.empleadodao.empleado.telefono = self.telefono_agregar.text()
        self.empleadodao.empleado.ciudad = self.ciudad_agregar.text()

        self.empleadodao.insertarEmpleado()

    def limpiar_empleado(self):
        self.clave_buscar.clear()
        self.nombre_buscar.clear()
        self.telefono_buscar.clear()
        self.ciudad_buscar.clear()

    def actualizar_empleado(self):
        self.empleadodao.empleado.clave = self.clave_actualizar.text()
        self.empleadodao.empleado.nombre = self.nombre_actualizar.text()
        self.empleadodao.empleado.telefono = self.telefono_actualizar.text()
        self.empleadodao.empleado.ciudad = self.ciudad_actualizar.text()

        self.empleadodao.actualizarEmpleado()

    def eliminar_empleado(self):
        self.empleadodao.empleado.clave = self.clave_eliminar.text()
        self.empleadodao.eliminarEmpleado()

# 6.- mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

#7.- Mover menú
    def mover_menu(self):
        if True:			
            width = self.frame_lateral.width()
            widthb = self.boton_menu.width()
            normal = 0
            if width==0:
                extender = 200
                self.boton_menu.setText("Menú")
            else:
                extender = normal
                self.boton_menu.setText("")
                
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            
            self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
        
            self.animacionb.setStartValue(width)
            self.animacionb.setEndValue(extender)
            self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacionb.start()