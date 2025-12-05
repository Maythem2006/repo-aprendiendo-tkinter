from models.persona import Persona

class Empleado(Persona):
    def init(self, id_empleado, fecha_inicio, salario, nombre, direccion, telefono, email):
        super().init(nombre, direccion, telefono, email)
        self._id_empleado = id_empleado
        self._fecha_inicio = fecha_inicio
        self._salario = salario

    @property
    def id(self):
        return self._id_empleado