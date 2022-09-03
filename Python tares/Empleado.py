#!/usr/bin/python3

class Empleado:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario

    def mostrar_datos(self):
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni} - Salario: {self.salario}\n"
        return texto
