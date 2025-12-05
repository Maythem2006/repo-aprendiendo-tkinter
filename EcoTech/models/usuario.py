import bcrypt

class Usuario:
    def __init__(self, id_usuario, username, password_hash, rol):
        self._id_usuario = id_usuario
        self._username = username
        self._password_hash = password_hash
        self.rol = rol

    def autenticar(self, password):
        # password_hash viene de la BD como bytes o string
        if isinstance(self._password_hash, str):
            self._password_hash = self._password_hash.encode()
        return bcrypt.checkpw(password.encode(), self._password_hash)