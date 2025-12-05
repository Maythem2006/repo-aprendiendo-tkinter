from models.usuario import Usuario

class UsuarioAdmin(Usuario):
    def generar_informes(self):
        print("Generando informes...")
    
    def permisos(self):
        return ["empleados", "departamentos", "proyectos", "registro_tiempo", "asignacion", "usuarios"]