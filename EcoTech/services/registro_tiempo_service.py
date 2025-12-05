from db.database import Database

class RegistroTiempoService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def crear(self, fecha, horas, descripcion, id_empleado, id_proyecto):
        query = """
            INSERT INTO REGISTRO_TIEMPO
            (fecha, horas, descripcion, id_empleado, id_proyecto)
            VALUES (:1, :2, :3, :4, :5)
        """
        self.db.ejecutar(query, (fecha, horas, descripcion, id_empleado, id_proyecto))

    def listar(self):
        self.db.cursor.execute("SELECT * FROM REGISTRO_TIEMPO")
        return self.db.cursor.fetchall()

    def eliminar(self, id_tiempo):
        self.db.ejecutar("DELETE FROM REGISTRO_TIEMPO WHERE id_tiempo=:1", (id_tiempo,))