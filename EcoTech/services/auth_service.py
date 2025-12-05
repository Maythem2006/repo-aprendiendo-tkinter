from db.database import Database
from models.usuario_admin import UsuarioAdmin
from models.usuario_empleado import UsuarioEmpleado
from models.usuario import Usuario
from exceptions.custom_exceptions import CredencialesInvalidas

class AuthService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def login(self, username, password):
        # obtener usuario desde la BD
        query = """
            SELECT id_usuario, username, password_hash, rol, id_empleado
            FROM USUARIO
            WHERE username = :1
        """

        try:
            self.db.cursor.execute(query, (username,))
            row = self.db.cursor.fetchone()

            if not row:
                raise CredencialesInvalidas("Usuario no existe.")

            id_usuario, username_db, password_hash, rol, id_empleado = row

            # POLIMORFISMO SEGÚN ROL
            if rol == "ADMIN":
                usuario = UsuarioAdmin(id_usuario, username_db, password_hash, rol)
            else:
                usuario = UsuarioEmpleado(id_usuario, username_db, password_hash, rol)

            # validar contraseña
            if usuario.autenticar(password):
                return usuario
            else:
                raise CredencialesInvalidas("Contraseña incorrecta.")
        except CredencialesInvalidas:
            raise
        except Exception as e:
            raise CredencialesInvalidas("Error al autenticar usuario.")