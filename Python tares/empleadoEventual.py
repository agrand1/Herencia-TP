#!/usr/bin/python3

from Empleado import Empleado

class EmpleadoEventual(Empleado):
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.ventas = ventas
        super().__init__(self, nombre, apellido, dni, salario)
        
    def calcular_comision(self):
        super().calcular_comision(self)
        porcentaje_comision = 0.05
        comision = total_ventas * porcentaje_comision
        return comision

    def mostrar_datos(self):
        texto += f"Ventas: {self.ventas}\n"
        super().mostrar_datos(texto)
        return texto
