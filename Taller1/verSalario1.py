import pandas as pd
import numpy as np

# Función para calcular el salario
def calcular_salario(empleado):
    salario_base = float(empleado['salario'])
    horas_trabajadas = float(empleado['horas_trabajadas'])
    salario_total = salario_base * horas_trabajadas
    return salario_total

# Leer el CSV y almacenar los datos en una lista de diccionarios
datos = pd.read_csv('C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/empleados.csv', delimiter=';').to_dict('records')

# Filtrar los registros con campos vacíos
datos = [empleado for empleado in datos if not any(pd.isna(value) for value in empleado.values())]

# Mostrar los datos por la terminal
print("Datos de los empleados:")
for empleado in datos:
    print(empleado)

# Procesar los datos para calcular los salarios
salarios = []
for empleado in datos:
    salario = calcular_salario(empleado)
    salarios.append(salario)

print("\nSalarios:")
for i, salario in enumerate(salarios):
    print(f"Empleado {i+1}: {salario}")
