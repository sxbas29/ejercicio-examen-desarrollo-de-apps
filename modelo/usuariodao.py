from modelo.usuario import Usuario
from modelo.conexionbd import ConexionBD

class UsuarioDao:
    def __init__(self):
        self.bd = ConexionBD()
        self.usuario = Usuario()

    def registrarUsuario(self, nombre, contraseña):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_registrar_usuario] @nombre=?, @contraseña=?'
        param = (nombre, contraseña)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()
        
        return True  

    def confirmarContraseña(self, nombre, contraseña):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_validar_contraseña] @nombre=?, @contraseña=?'
        param = (nombre, contraseña)
        cursor.execute(sp, param)
        resultado = cursor.fetchone()
        self.bd.cerrarConexionBD()
            
        if resultado[0] == 1:
            return True, resultado[1]  
        else:
            return False, None