import pandas as pd

# Función para calcular el salario
def calcular_salario(empleado):
    salario_base = float(empleado['salario'])
    horas_trabajadas = float(empleado['horas_trabajadas'])
    salario_total = salario_base * horas_trabajadas
    return salario_total

# Leer el CSV y almacenar los datos en un DataFrame de pandas
datos = pd.read_csv('C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/empleados.csv', delimiter=';')

# Calcular los salarios
datos['salario_total'] = datos.apply(calcular_salario, axis=1)

# Guardar los datos actualizados en un nuevo archivo CSV
datos.to_csv('C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/empleados_con_salario2.csv', index=False)
print("CREACION EXITOSA")