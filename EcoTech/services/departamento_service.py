from db.database import Database
import oracledb

class DepartamentoService:
    def __init__(self):
        self.db = Database()
        self.db.conectar()

    def crear(self, nombre, id_gerente=None):
        try:
            query = """
                INSERT INTO DEPARTAMENTO (nombre, id_gerente)
                VALUES (:1, :2)
            """
            self.db.ejecutar(query, (nombre, id_gerente))
            print("✔ Departamento creado correctamente.")
        except Exception as e:
            print("❌Error al crear departamento:", e)

    def listar(self):
        try:
            self.db.cursor.execute("SELECT * FROM DEPARTAMENTO")
            return self.db.cursor.fetchall()
        except Exception as e:
            print("❌Error al listar departamentos:", e)

    def actualizar(self, id_dep, nombre, id_gerente):
        try:
            query = """
                UPDATE DEPARTAMENTO
                SET nombre=:1, id_gerente=:2
                WHERE id_departamento=:3
            """
            self.db.ejecutar(query, (nombre, id_gerente, id_dep))
            print("✔ Departamento actualizado.")
        except Exception as e:
            print("❌Error al actualizar departamento:", e)

    def eliminar(self, id_dep):
        try:
            self.db.ejecutar(
                "DELETE FROM DEPARTAMENTO WHERE id_departamento=:1",
                (id_dep,)
            )
            print("✔ Departamento eliminado.")
        except Exception as e:
            print("❌Error al eliminar:", e)