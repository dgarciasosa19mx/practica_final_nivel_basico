class Empleado:
    def __init__(self, nombre, departamento, antiguedad, meta_cumplida, salario_base):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = int(antiguedad)
        self.meta_cumplida = meta_cumplida == "True"
        self.salario_base = float(salario_base)
        self.salario_final = float(salario_base)
    
    def calcular_neto(lista_empleados):
        for emp in lista_empleados:
            # se cambio de ubicacion la variable tiene_derecho_a_bono, se coloca dentro del 
            # bucle for para que iteractue en el ciclo y se reinicie a False cada que cambie 
            # de empleado
            tiene_derecho_a_bono = False 
            if (emp.departamento == "Ventas" and emp.antiguedad > 5) or emp.meta_cumplida:
                tiene_derecho_a_bono = True
                
            if tiene_derecho_a_bono:
                emp.salario_final = emp.salario_base + 500
            else:
                emp.salario_final = emp.salario_base
        return lista_empleados
