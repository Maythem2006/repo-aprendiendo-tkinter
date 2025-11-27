/*

-- Nombre:
-- Atributos: TIPO DE DATOS (SQL) (CONSTRAINT)
-- EMPLEADO
-- ADMINISTRACION
-- TRABAJO_REALIZADO
-- PROYECTOS
-- USER_APP
-- INFORME
*/

CREATE TABLE EMPLEADO (
    id_empleado      VARCHAR2(20) PRIMARY KEY,
    nombre           VARCHAR2(64),
    direccion        VARCHAR2(128),
    telefono         VARCHAR2(20),
    email            VARCHAR2(64),
    fecha_inicio     DATE,
    salario          FLOAT
);

CREATE TABLE TRABAJO_REALIZADO (
    id_TR       INTEGER PRIMARY KEY,
    fecha       DATE,
    horas       INTEGER
);

CREATE TABLE PROYECTOS (
    id_proyect      INTEGER PRIMARY KEY,
    nombre          VARCHAR2(64),
    descripcion     VARCHAR2(256),
    fecha_inicio    DATE
);

CREATE TABLE ADMINISTRACION (
    id_admin        INTEGER PRIMARY KEY,
    nombre          VARCHAR2(64),
    id_empleado     VARCHAR2(20) NOT NULL UNIQUE,
    FOREIGN KEY (id_empleado) REFERENCES EMPLEADO(id_empleado)
);

CREATE TABLE USER_APP (
    id_user         INTEGER PRIMARY KEY,
    user_name       VARCHAR2(64) UNIQUE,
    user_password   VARCHAR2(64)
);

CREATE TABLE INFORME (
    id_informe      INTEGER PRIMARY KEY,
    id_user         INTEGER NOT NULL,  
    FOREIGN KEY (id_user) REFERENCES USER_APP(id_user)
);

CREATE TABLE PROYECTO_EMPLEADO (
    id_proyect      INTEGER NOT NULL,
    id_empleado     VARCHAR2(20) NOT NULL,
    PRIMARY KEY (id_proyect, id_empleado),
    FOREIGN KEY (id_proyect) REFERENCES PROYECTOS(id_proyect),
    FOREIGN KEY (id_empleado) REFERENCES EMPLEADO(id_empleado)
);

CREATE TABLE INFORME_PROYECTO (
    id_informe      INTEGER NOT NULL,
    id_proyect      INTEGER NOT NULL,
    PRIMARY KEY (id_informe, id_proyect),
    FOREIGN KEY (id_informe) REFERENCES INFORME(id_informe),
    FOREIGN KEY (id_proyect) REFERENCES PROYECTOS(id_proyect)
);