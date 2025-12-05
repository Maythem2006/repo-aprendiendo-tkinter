from models.persona import Persona

class Empleado(Persona):
    def __init__(self, id_empleado, fecha_inicio, salario, nombre, direccion, telefono, email):
        super().__init__(nombre, direccion, telefono, email)
        self._id_empleado = id_empleado
        self._fecha_inicio = fecha_inicio
        self._salario = salario

    @property
    def id(self):
        return self._id_empleado