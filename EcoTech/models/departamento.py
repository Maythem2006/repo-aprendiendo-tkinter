class Departamento:
    def init(self, id_departamento, nombre, id_gerente=None):
        self._id_departamento = id_departamento
        self._nombre = nombre
        self._id_gerente = id_gerente