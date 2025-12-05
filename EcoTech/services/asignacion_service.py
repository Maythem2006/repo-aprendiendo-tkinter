from db.database import Database

class AsignacionService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def asignar(self, id_empleado, id_proyecto):
        query = """
            INSERT INTO empleado_proyecto (id_empleado, id_proyecto)
            VALUES (:1, :2)
        """
        self.db.ejecutar(query, (id_empleado, id_proyecto))

    def desasignar(self, id_empleado, id_proyecto):
        query = """
            DELETE FROM empleado_proyecto
            WHERE id_empleado=:1 AND id_proyecto=:2
        """
        self.db.ejecutar(query, (id_empleado, id_proyecto))