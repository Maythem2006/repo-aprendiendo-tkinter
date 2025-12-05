from services.auth_service import AuthService
from services.empleado_service import EmpleadoService
from services.departamento_service import DepartamentoService
from services.proyecto_service import ProyectoService
from services.registro_tiempo_service import RegistroTiempoService
from services.asignacion_service import AsignacionService
from services.usuario_service import UsuarioService

from utils.validators import *
from exceptions.custom_exceptions import *

# ===================================
#           SUBMENÚS
# ===================================

def menu_empleados(emp):
    print("\n=== GESTIÓN DE EMPLEADOS ===")
    print("1. Crear empleado")
    print("2. Listar empleados")
    print("3. Actualizar empleado")
    print("4. Eliminar empleado")
    print("5. Volver")

    opc = input("Seleccione opción: ")

    if opc == "1":
        try:
            nombre = validar_texto(input("Nombre: "))
            direccion = validar_texto(input("Dirección: "))
            telefono = validar_texto(input("Teléfono: "))
            email = validar_email(input("Email: "))
            fecha = input("Fecha inicio (YYYY-MM-DD): ")
            salario = validar_numero(input("Salario: "))
            emp.crear_empleado(nombre, direccion, telefono, email, fecha, salario)
        except Exception as e:
            print("❌ Error:", e)

    elif opc == "2":
        print(emp.listar())

    elif opc == "3":
        try:
            id_emp = int(input("ID del empleado: "))
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            emp.actualizar_empleado(id_emp, nombre, direccion, telefono)
        except Exception as e:
            print("❌ Error:", e)

    elif opc == "4":
        try:
            id_emp = int(input("ID del empleado a eliminar: "))
            emp.eliminar(id_emp)
        except Exception as e:
            print("❌ Error:", e)


def menu_departamentos(dep):
    print("\n=== GESTIÓN DE DEPARTAMENTOS ===")
    print("1. Crear departamento")
    print("2. Listar departamentos")
    print("3. Actualizar departamento")
    print("4. Eliminar departamento")
    print("5. Volver")
    opc = input("Seleccione opción: ")

    if opc == "1":
        nombre = input("Nombre: ")
        id_gerente = input("ID Gerente (opcional): ")
        id_gerente = int(id_gerente) if id_gerente else None
        dep.crear(nombre, id_gerente)

    elif opc == "2":
        print(dep.listar())

    elif opc == "3":
        id_dep = int(input("ID departamento: "))
        nombre = input("Nuevo nombre: ")
        id_gerente = input("Nuevo gerente (enter si no aplica): ")
        id_gerente = int(id_gerente) if id_gerente else None
        dep.actualizar(id_dep, nombre, id_gerente)

    elif opc == "4":
        id_dep = int(input("ID a eliminar: "))
        dep.eliminar(id_dep)


def menu_proyectos(pro):
    print("\n=== GESTIÓN DE PROYECTOS ===")
    print("1. Crear proyecto")
    print("2. Listar proyectos")
    print("3. Actualizar proyecto")
    print("4. Eliminar proyecto")
    print("5. Volver")

    opc = input("Seleccione opción: ")

    if opc == "1":
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha inicio (YYYY-MM-DD): ")
        pro.crear(nombre, descripcion, fecha)

    elif opc == "2":
        print(pro.listar())

    elif opc == "3":
        id_pro = int(input("ID del proyecto: "))
        nombre = input("Nuevo nombre: ")
        descripcion = input("Nueva descripción: ")
        pro.actualizar(id_pro, nombre, descripcion)

    elif opc == "4":
        id_pro = int(input("ID a eliminar: "))
        pro.eliminar(id_pro)


def menu_registros(reg):
    print("\n=== REGISTRO DE TIEMPO ===")
    print("1. Crear registro")
    print("2. Listar registros")
    print("3. Eliminar registro")
    print("4. Volver")

    opc = input("Seleccione opción: ")

    if opc == "1":
        fecha = input("Fecha (YYYY-MM-DD): ")
        horas = validar_numero(input("Horas trabajadas: "))
        desc = input("Descripción: ")
        id_emp = int(input("ID empleado: "))
        id_pro = int(input("ID proyecto: "))
        reg.crear(fecha, horas, desc, id_emp, id_pro)

    elif opc == "2":
        print(reg.listar())

    elif opc == "3":
        id_tiempo = int(input("ID registro a eliminar: "))
        reg.eliminar(id_tiempo)


def menu_asignacion(asi):
    print("\n=== ASIGNAR EMPLEADO A PROYECTO ===")
    print("1. Asignar")
    print("2. Desasignar")
    print("3. Volver")

    opc = input("Seleccione: ")

    if opc == "1":
        emp = int(input("ID empleado: "))
        pro = int(input("ID proyecto: "))
        asi.asignar(emp, pro)

    elif opc == "2":
        emp = int(input("ID empleado: "))
        pro = int(input("ID proyecto: "))
        asi.desasignar(emp, pro)


def menu_usuarios(us):
    print("\n=== GESTIÓN DE USUARIOS ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Volver")

    opc = input("Seleccione opción: ")

    if opc == "1":
        username = input("Username: ")
        password = input("Password: ")
        rol = input("Rol (ADMIN/EMPLEADO): ")
        id_emp = input("ID empleado (opcional): ")
        id_emp = int(id_emp) if id_emp else None
        us.crear(username, password, rol, id_emp)

    elif opc == "2":
        print(us.listar())

    elif opc == "3":
        id_u = int(input("ID usuario: "))
        username = input("Nuevo username (enter si no cambia): ")
        password = input("Nuevo password (enter si no cambia): ")
        rol = input("Nuevo rol (enter si no cambia): ")
        id_emp = input("Nuevo empleado (enter si no cambia): ")
        id_emp = int(id_emp) if id_emp else None

        us.actualizar(id_u,
                      username or None,
                      password or None,
                      rol or None,
                      id_emp)

    elif opc == "4":
        id_u = int(input("ID a eliminar: "))
        us.eliminar(id_u)


# ===================================
#              MAIN
# ===================================

def main():

    # ---------- LOGIN -------------
    auth = AuthService()

    print("\n===== LOGIN SISTEMA ECOTECH =====")

    USUARIO = None
    while USUARIO is None:
        try:
            username = input("Usuario: ")
            password = input("Contraseña: ")
            USUARIO = auth.login(username, password)
        except Exception as e:
            print("❌", e)

    print(f"\n✔ Bienvenido {USUARIO._username} ({USUARIO.rol})")
    permisos = USUARIO.permisos()

    # ---------- SERVICIOS ----------
    emp = EmpleadoService()
    dep = DepartamentoService()
    pro = ProyectoService()
    reg = RegistroTiempoService()
    asi = AsignacionService()
    us = UsuarioService()

    # ------------ MENÚ ------------
    while True:

        print("\n=========== MENU PRINCIPAL ===========")
        print("1. Gestión de empleados")
        print("2. Gestión de departamentos")
        print("3. Gestión de proyectos")
        print("4. Registro de tiempo")
        print("5. Asignación empleado–proyecto")
        print("6. Gestión de usuarios")
        print("7. Salir")

        opc = input("Seleccione opción: ")

        # CONTROL DE PERMISOS
        if opc != "7" and USUARIO.rol != "ADMIN" and opc != "4":
            print("❌ No tienes permisos para esta opción.")
            continue

        if opc == "1":
            menu_empleados(emp)

        elif opc == "2":
            menu_departamentos(dep)

        elif opc == "3":
            menu_proyectos(pro)

        elif opc == "4":
            menu_registros(reg)

        elif opc == "5":
            menu_asignacion(asi)

        elif opc == "6":
            menu_usuarios(us)

        elif opc == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()