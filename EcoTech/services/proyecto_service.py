from db.database import Database

class ProyectoService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def crear(self, nombre, descripcion, fecha_inicio):
        query = """
            INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
            VALUES (:1, :2, :3)
        """
        self.db.ejecutar(query, (nombre, descripcion, fecha_inicio))

    def listar(self):
        self.db.cursor.execute("SELECT * FROM proyecto")
        return self.db.cursor.fetchall()

    def actualizar(self, id_proy, nombre, descripcion):
        query = """
            UPDATE proyecto
            SET nombre=:1, descripcion=:2
            WHERE id_proyecto=:3
        """
        self.db.ejecutar(query, (nombre, descripcion, id_proy))

    def eliminar(self, id_proy):
        self.db.ejecutar("DELETE FROM proyecto WHERE id_proyecto=:1", (id_proy,))