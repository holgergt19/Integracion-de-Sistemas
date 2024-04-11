import pandas as pd

# Leer el archivo CSV
datos = pd.read_csv('C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/empleados.csv')

# Imprimir los nombres de las columnas
print("Nombres de las columnas:")
print(datos.columns)