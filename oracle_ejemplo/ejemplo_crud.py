from datetime import datetime
import oracledb 
import os 
from dotenv import load_dotenv 
load_dotenv() 
 
username = os.getenv("ORACLE_USER") 
dsn = os.getenv("ORACLE_DSN") 
password = os.getenv("ORACLE_PASSWORD") 

def get_connection():
    return oracledb.connect(user=username, password= password, dsn= dsn)


def create_schema():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n{query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")

tables = [
    (
        "CREATE TABLE EMPLEADO ("
        "id_empleado      VARCHAR2(20) PRIMARY KEY,"
        "nombre           VARCHAR2(64),"
        "direccion        VARCHAR2(128),"
        "telefono         VARCHAR2(20),"
        "email            VARCHAR2(64),"
        "fecha_inicio     DATE,"
        "salario          FLOAT"
        ")"
    ),
    (
        "CREATE TABLE TRABAJO_REALIZADO ("
        "id_TR       INTEGER PRIMARY KEY,"
        "fecha       DATE,"
        "horas       INTEGER"
        ")"         
    ),
    (
        "CREATE TABLE PROYECTOS ("
        "id_proyect      INTEGER PRIMARY KEY,"
        "nombre          VARCHAR2(64),"
        "descripcion     VARCHAR2(256),"
        "fecha_inicio    DATE"
        ")"
    ),
    (
        "CREATE TABLE ADMINISTRACION ("
        "id_admin        INTEGER PRIMARY KEY,"
        "nombre          VARCHAR2(64),"
        "id_empleado     VARCHAR2(20) NOT NULL UNIQUE,"
        "FOREIGN KEY (id_empleado) REFERENCES EMPLEADO(id_empleado)"
        ")"   
    ),
    (
        "CREATE TABLE USER_APP ("
        "id_user         INTEGER PRIMARY KEY,"
        "user_name       VARCHAR2(64) UNIQUE,"
        "user_password   VARCHAR2(64)"
        ")"
    ),
    (
        "CREATE TABLE INFORME ("
        "id_informe      INTEGER PRIMARY KEY,"
        "id_user         INTEGER NOT NULL,"  
        "FOREIGN KEY (id_user) REFERENCES USER_APP(id_user)"
        ")"
    ),
    (
        "CREATE TABLE PROYECTO_EMPLEADO ("
        "id_proyect      INTEGER NOT NULL,"
        "id_empleado     VARCHAR2(20) NOT NULL,"
        "PRIMARY KEY (id_proyect, id_empleado),"
        "FOREIGN KEY (id_proyect) REFERENCES PROYECTOS(id_proyect),"
        "FOREIGN KEY (id_empleado) REFERENCES EMPLEADO(id_empleado)"
        ")"
    ),
    (
        "CREATE TABLE INFORME_PROYECTO ("
        "id_informe      INTEGER NOT NULL,"
        "id_proyect      INTEGER NOT NULL,"
        "PRIMARY KEY (id_informe, id_proyect),"
        "FOREIGN KEY (id_informe) REFERENCES INFORME(id_informe),"
        "FOREIGN KEY (id_proyect) REFERENCES PROYECTOS(id_proyect)"
        ")"
    )
]

for query in tables:
    create_schema(query)

    # CREATE - Inserción de datos
    def create_empeleado(
            id_empleado: int,
            nombre: str,     
            direccion: str,
            telefono: str,   
            email: str,
            fecha_inicio: str,
            salario: float         
    ):
        sql = (
            "INSERT INTO EMPLEADO (id_empleado, nombre, direccion, telefono, email, fecha_inicio, salario) "
            "VALUES (:id_empleado, :nombre, :direccion, :telefono, :email, TO_DATE(:fecha_inicio, 'YYYY-MM-DD'), :salario)"
        )

        parametros = {
            "id_empleado": id_empleado,
            "nombre": nombre,     
            "direccion": direccion,
            "telefono": telefono,   
            "email": email,
            "fecha_inicio": datetime.strptime(fecha_inicio, '%Y-%m-%d'),
            "salario": salario
        }

        try:
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    print("Tabla 'personas' creada.")
        except oracledb.DatabaseError as error:
            print(f"No se pudo crear la tabla: {error}")

    def create_trabajo_realizado(
            id_TR,
            fecha,
            horas
    ):
        sql = (
            "INSERT INTO TRABAJO_REALIZADO (id_TR, fecha, horas) "
            "VALUES (:id_TR,:fecha,:horas)"
        )

        parametros = {
            "id_TR": id_TR,
            "fecha": datetime.strptime(fecha, '%Y-%m-%d'),
            "horas": int(horas)
        }
