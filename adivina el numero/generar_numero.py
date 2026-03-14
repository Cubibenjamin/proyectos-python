import random
import math

def generar_numero():
    # 1. Cantidad de operaciones a realizar
    n = random.randint(1, 10) 
    
    # 2. El número "objetivo" que estará en la matriz
    x = random.randint(1, 10)
    
    # 3. Construcción del problema
    problema_texto = ""
    acumulado = 0
    
    for i in range(n):
        # El último paso debe compensar todo lo anterior para llegar exactamente a 'x'
        if i == n - 1:
            necesario = x - acumulado
            if necesario >= 0:
                problema_texto += f" + {necesario}"
            else:
                problema_texto += f" - {abs(necesario)}"
            acumulado += necesario
        
        else:
            # Seleccionamos una operación al azar que garantice un entero
            operacion = random.choice(['pow', 'sqrt', 'log', 'simple'])
            
            if operacion == 'pow':
                base = random.randint(2, 3)
                exp = random.randint(2, 3)
                val = int(math.pow(base, exp))
                problema_texto += f" + math.pow({base}, {exp})"
                acumulado += val
                
            elif operacion == 'sqrt':
                base = random.choice([4, 9, 16, 25, 36]) # Cuadrados perfectos
                val = int(math.sqrt(base))
                problema_texto += f" + math.sqrt({base})"
                acumulado += val
                
            elif operacion == 'log':
                # Usamos log2 para asegurar enteros (base 2)
                exp = random.randint(2, 4)
                argumento = 2**exp
                val = int(math.log2(argumento))
                problema_texto += f" + math.log2({argumento})"
                acumulado += val
                
            else: # Simple entero
                val = random.randint(1, 10)
                problema_texto += f" + {val}"
                acumulado += val

    # Limpiamos el texto (quitar el primer '+' si aparece al inicio)
    if problema_texto.startswith(" + "):
        problema_texto = problema_texto[3:]
    
    return x, problema_texto

# Prueba rápida
resultado, ecuacion = generar_numero()
print(f"Ecuación: {ecuacion}")
print(f"Resultado esperado (x): {resultado}")