from modelo.producto import Producto
from modelo.conexionbd import ConexionBD

class ProductoDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.producto = Producto()
        
    def listarProductos(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_listar_productos]'
        cursor.execute(sp)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas 
    
    def buscarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_buscar_producto] @clave=?'
        param = [self.producto.clave]
        cursor.execute(sp, param) 
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas 

    def insertarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_insertar_producto]@clave=?,@descripcion=?,@existencia=?,@precio=?'
        param = (self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_actualizar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?'
        param = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_eliminar_producto] @clave=?'
        cursor.execute(sp, self.producto.clave)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()
