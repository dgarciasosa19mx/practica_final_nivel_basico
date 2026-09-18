import csv
import os
from empleado import Empleado
from lector_csv import LectorCSV
from procesador import Procesador

# se agregan control de directorio para que el archivo se cree en la carpeta del proyecto
# se agrega el salario base para comparar el cambio
def generar_reporte(lista_empleados, ruta_salida):
    bError : bool = True
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(base_dir, ruta_salida)
        with open(csv_file, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'departamento', 'salario_base', 'salario_final']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for emp in lista_empleados:
                escritor.writerow({
                    'nombre': emp.nombre,
                    'departamento': emp.departamento,
                    'salario_base': emp.salario_base,
                    'salario_final': emp.salario_final
                })
            bError = False
    except FileNotFoundError:
        print(f"No se encontro el archivo {ruta_salida}.")
    except PermissionError:
        print(f"El archivo {ruta_salida} se encuentra abierto y/o en uso. Verifica e intentalo mas tarde.")
    except Exception as e:
        print(f"Un error ha ocurrido: {e} \nNotifica a SISTEMAS e intentalo mas tarde.")
    else:
        bError = False
    finally:
        if bError == False:
            print("Proceso completado. Revisa 'reporte_final.csv' para ver los errores. >.<")

if __name__ == "__main__":
    # se crea archivo CSV para testing
    with open('empleados.csv', 'w', encoding='utf-8') as f:
        f.write("nombre,departamento,antiguedad,meta_cumplida,salario_base\n")
        f.write("Ana,Ventas,6,False,3000\n")      
        f.write("Luis,Soporte,2,True,2500\n")     
        f.write("Carlos,Soporte,1,False,2000\n")  
        f.write("Marta,Ventas,2,False,3000\n")    

    # inicio ejecucion
    empleados = LectorCSV.cargar_empleados('empleados.csv')
    empleados_procesados = Empleado.calcular_bonos(empleados)
    generar_reporte(empleados_procesados, 'reporte_final.csv')
    # se traslado el pront de Proceso completado al metodo generar_reporte()
    # print("Proceso completado. Revisa 'reporte_final.csv' para ver los errores. >.<")
