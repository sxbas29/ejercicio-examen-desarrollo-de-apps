from modelo.empleado import Empleado
from modelo.conexionbd import ConexionBD

class EmpleadoDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.empleado = Empleado()
        
    def listarEmpleados(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_listar_empleados]'
        cursor.execute(sp)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas
    
    def insertarEmpleado(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_insertar_empleado]@clave_empleado=?, @nombre_empleado=?, @numero_telefono=?, @ciudad_empleado=?'
        param = (self.empleado.clave, self.empleado.nombre, self.empleado.telefono, self.empleado.ciudad)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()
    
    def actualizarEmpleado(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_actualizar_empleado] @clave_empleado=?,@nombre_empleado=?,@numero_telefono=?,@ciudad_empleado=?'
        param = (self.empleado.clave,self.empleado.nombre,self.empleado.telefono,self.empleado.ciudad)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

    def eliminarEmpleado(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_eliminar_empleado] @clave=?'
        cursor.execute(sp, self.empleado.clave)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

        
    def buscarEmpleado(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_buscar_empleado] @clave=?'
        param = [self.empleado.clave]
        cursor.execute(sp, param) 
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas 
