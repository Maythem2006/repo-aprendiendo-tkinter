import oracledb
import os
from dotenv import load_dotenv

# Cargar .env desde la carpeta DB
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

class Database:
    def __init__(self):  
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = oracledb.connect(
                user=os.getenv("ORACLE_USER"),
                password=os.getenv("ORACLE_PASSWORD"),
                dsn=os.getenv("ORACLE_DSN")    
            )
            self.cursor = self.conn.cursor()
            print("✅Conexión establecida con Oracle.")
        except oracledb.DatabaseError as e:
            print("❌Error al conectar a Oracle:", e)

    def ejecutar(self, query, params=None):
        try:
            if self.cursor is None:
                raise Exception("Cursor no inicializado. ¿Llamaste a conectar()?")

            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            self.conn.commit()
        except Exception as e:
            print("❌Error al ejecutar consulta:", e)

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()