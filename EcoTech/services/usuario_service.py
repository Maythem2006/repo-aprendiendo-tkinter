import bcrypt
from db.database import Database
from exceptions.custom_exceptions import CredencialesInvalidas

class UsuarioService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    # ================================
    # CREATE
    # ================================
    def crear(self, username, password, rol, id_empleado=None):
        try:
            # Encriptar contraseña
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            query = """
                INSERT INTO USUARIO (username, password_hash, rol, id_empleado)
                VALUES (:1, :2, :3, :4)
            """

            self.db.ejecutar(query, (username, password_hash, rol, id_empleado))
            print("✔ Usuario creado correctamente.")

        except Exception as e:
            print("❌ Error al crear usuario:", e)

    # ================================
    # READ (LIST)
    # ================================
    def listar(self):
        try:
            self.db.cursor.execute("""
                SELECT id_usuario, username, rol, id_empleado
                FROM USUARIO
                ORDER BY id_usuario
            """)
            return self.db.cursor.fetchall()

        except Exception as e:
            print("❌ Error al listar usuarios:", e)
            return []

    # ================================
    # UPDATE
    # ================================
    def actualizar(self, id_usuario, nuevo_username=None, nuevo_password=None, nuevo_rol=None, nuevo_id_empleado=None):
        try:
            campos = []
            valores = []

            if nuevo_username:
                campos.append("username = :{}".format(len(valores) + 1))
                valores.append(nuevo_username)

            if nuevo_password:
                password_hash = bcrypt.hashpw(nuevo_password.encode(), bcrypt.gensalt()).decode()
                campos.append("password_hash = :{}".format(len(valores) + 1))
                valores.append(password_hash)

            if nuevo_rol:
                campos.append("rol = :{}".format(len(valores) + 1))
                valores.append(nuevo_rol)

            if nuevo_id_empleado is not None:
                campos.append("id_empleado = :{}".format(len(valores) + 1))
                valores.append(nuevo_id_empleado)

            if not campos:
                print("⚠ No hay nada que actualizar.")
                return

            query = f"UPDATE USUARIO SET {', '.join(campos)} WHERE id_usuario = :{len(valores) + 1}"
            valores.append(id_usuario)

            self.db.ejecutar(query, tuple(valores))
            print("✔ Usuario actualizado correctamente.")

        except Exception as e:
            print("❌ Error al actualizar usuario:", e)

    # ================================
    # DELETE
    # ================================
    def eliminar(self, id_usuario):
        try:
            self.db.ejecutar("DELETE FROM USUARIO WHERE id_usuario = :1", (id_usuario,))
            print("✔ Usuario eliminado correctamente.")

        except Exception as e:
            print("❌ Error al eliminar usuario:", e)