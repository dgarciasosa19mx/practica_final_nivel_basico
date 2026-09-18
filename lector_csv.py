# se importo modulo CSV para el manejo de archivos CSV y la clase Empleado para el manejo de los mismos.
import os
import csv
from empleado import Empleado

# se crea la clase para manejar la persistencia de datos en disco (Capa de Datos).
class LectorCSV:

    def __init__(self, ruta_archivo="empleados.json"):
        # agregado para manejo de directorio
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ruta_archivo = os.path.join(base_dir, ruta_archivo)

    def cargar_empleados(self):
        empleados = []
        if not os.path.exists(self.ruta_archivo):
            return []
        try:
            #with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            with open(self.ruta_archivo, mode='r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    emp = Empleado(
                        fila['nombre'], 
                        fila['departamento'], 
                        fila['antiguedad'], 
                        fila['meta_cumplida'], 
                        fila['salario_base']
                    )
                    # si el salario y la antiguedad son validos, se procede a agregarlos a 
                    #  la lista de empleados para el calculo del salario neto
                    if self.validar_datos(fila['antiguedad'],fila['salario_base']):
                        empleados.append(emp)
                # finaliza el for
            #finaliza el while
            return empleados
        except (IOError, FileNotFoundError):
            print(f"⚠️ Error al leer el archivo JSON {self.ruta_archivo}. Se iniciará una lista vacía.")
            return []

    def validar_datos(self,antiguedad, salario_base):
        if self._pedir_float_positivo(antiguedad) and self._pedir_int(salario_base):
            return True
        else:
            return False

    def _pedir_float_positivo(self, valor):
        while True:
            try:
                valor = float(valor)
                if valor < 0:
                    #print("La percepcion debe ser mayor o igual a 0.")
                    return False
                else:
                    return True
            except ValueError:
                #print("Entrada inválida. Archivo corrupto.")
                return False

    def _pedir_int(self, valor):
        try:
            if int(valor) < 0:
                #print("La antiguedad no puede ser menor a 0.")
                return False
            else:
                return True
        except ValueError:
            return False
    