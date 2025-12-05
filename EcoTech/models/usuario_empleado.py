from models.usuario import Usuario

class UsuarioEmpleado(Usuario):
    def registrar_horas(self):
        print("Registrando horas…")
    
    def permisos(self):
        return ["registro_tiempo"]