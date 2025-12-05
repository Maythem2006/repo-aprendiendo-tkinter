from db.database import Database
from models.empleado import Empleado
import oracledb

class EmpleadoService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def crear(self, empleado: Empleado):
        try:
            query = """
            INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio, salario)
            VALUES (:1, :2, :3, :4, :5, :6)
            """
            self.db.ejecutar(query, (
                empleado._nombre,
                empleado._direccion,
                empleado._telefono,
                empleado._email,
                empleado._fecha_inicio,
                empleado._salario
            ))
            print("Empleado creado con éxito.")
        except Exception as e:
            print("Error al crear empleado:", e)

    def listar(self):
        try:
            self.db.cursor.execute("SELECT * FROM empleado")
            return self.db.cursor.fetchall()
        except Exception as e:
            print("Error al listar empleados:", e)
            return []

    def actualizar(self, empleado: Empleado):
        try:
            query = """
            UPDATE empleado SET nombre=:1, direccion=:2, telefono=:3
            WHERE id_empleado=:4
            """
            self.db.ejecutar(query, (
                empleado._nombre,
                empleado._direccion,
                empleado._telefono,
                empleado._id_empleado
            ))
            print("Empleado actualizado.")
        except Exception as e:
            print("Error al actualizar:", e)

    def eliminar(self, id_empleado):
        try:
            self.db.ejecutar("DELETE FROM empleado WHERE id_empleado=:1", (id_empleado,))
            print("Empleado eliminado.")
        except Exception as e:
            print("Error al eliminar:", e)