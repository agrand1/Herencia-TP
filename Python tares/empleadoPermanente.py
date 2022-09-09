#!/usr/bin/python3

from Empleado import Empleado

class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.antiguedad = antiguedad
        super().__init__(self, nombre, apellido, dni, salario)
        
    def mostrar_datos(self):
        texto += f"Antigüedad: {self.antiguedad}\n"
        super().mostrar_datos(texto)
        return texto
