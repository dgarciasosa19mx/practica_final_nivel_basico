# se importo modulo CSV para el manejo de archivos CSV y la clase Empleado para el manejo de los mismos.
import os
import csv
from empleado import Empleado

# se crea la clase para manejar la persistencia de datos en disco (Capa de Datos).
class LectorCSV:

    def cargar_empleados(ruta_archivo):
        # agregado para manejo de directorio
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_csv = os.path.join(base_dir, ruta_archivo)
        
        empleados = []
        if not os.path.exists(ruta_archivo):
            return []
        try:
            #with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            with open(file_csv, mode='r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    emp = Empleado(
                        fila['nombre'], 
                        fila['departamento'], 
                        fila['antiguedad'], 
                        fila['meta_cumplida'], 
                        fila['salario_base']
                    )
                    empleados.append(emp)
            return empleados
        except (IOError, FileNotFoundError):
            print(f"⚠️ Error al leer el archivo JSON {file_csv}. Se iniciará una lista vacía.")
            return []
