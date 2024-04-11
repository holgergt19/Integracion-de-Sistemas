import shutil

# Ruta de origen y destino de los archivos
ruta_origen = 'C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/empleados_con_salario2.csv'
ruta_destino = 'C:/Users/corpa/Desktop/Semestre 9/Integracion/Taller1/SistemaNomina'
#Tiempo especificado: 12:00 horas
# Copiar el archivo de origen al destino
shutil.copy(ruta_origen, ruta_destino)
