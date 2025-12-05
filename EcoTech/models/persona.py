from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, direccion, telefono, email):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email