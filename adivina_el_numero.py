import random
import math
import msvcrt
import os

# --- CONSTANTES DE COLOR ---
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
CIAN = '\033[96m'
RESET = '\033[0m'

# --- FUNCIÓN 1: GENERACIÓN DEL PROBLEMA ---
def generar_numero():
    n = random.randint(1, 10) 
    x = random.randint(1, 10)
    problema_texto = ""
    acumulado = 0
    
    for i in range(n):
        if i == n - 1:
            necesario = x - acumulado
            problema_texto += f" + {necesario}" if necesario >= 0 else f" - {abs(necesario)}"
            acumulado += necesario
        else:
            operacion = random.choice(['pow', 'sqrt', 'log', 'simple'])
            if operacion == 'pow':
                base, exp = random.randint(2, 3), 2
                val = int(math.pow(base, exp))
                problema_texto += f" + math.pow({base}, {exp})"
                acumulado += val
            elif operacion == 'sqrt':
                base = random.choice([4, 9, 16, 25])
                val = int(math.sqrt(base))
                problema_texto += f" + math.sqrt({base})"
                acumulado += val
            elif operacion == 'log':
                exp = random.randint(2, 4)
                arg = 2**exp
                val = int(math.log2(arg))
                problema_texto += f" + math.log2({arg})"
                acumulado += val
            else:
                val = random.randint(1, 10)
                problema_texto += f" + {val}"
                acumulado += val

    if problema_texto.startswith(" + "):
        problema_texto = problema_texto[3:]
    
    return x, problema_texto

# --- FUNCIÓN 2: CONSTRUCCIÓN DE LA MATRIZ (SIN DUPLICADOS) ---
def construir_escenario(x):
    dimension = random.randint(3, 6)
    total_celdas = dimension * dimension
    
    # Pool extendido para evitar colisiones
    pool_de_numeros = list(range(1, 101)) 
    if x in pool_de_numeros:
        pool_de_numeros.remove(x)
    
    muestreo = random.sample(pool_de_numeros, total_celdas - 1)
    muestreo.append(x)
    random.shuffle(muestreo)
    
    matriz = []
    for i in range(0, total_celdas, dimension):
        matriz.append(muestreo[i : i + dimension])
    
    # Localizar x
    fila_real, col_real = 0, 0
    for f in range(dimension):
        for c in range(dimension):
            if matriz[f][c] == x:
                fila_real, col_real = f, c
    
    return matriz, fila_real, col_real

# --- FUNCIÓN 3: INTERFAZ DE USUARIO ---
def jugar(matriz, x, fila_real, col_real, ecuacion):
    filas = len(matriz)
    cols = len(matriz[0])
    cursor_f, cursor_c = 0, 0 
    
    while True:
        os.system('cls')
        print(f"{CIAN}" + "="*60)
        print(f"{AMARILLO}RESOLVÉ: {RESET}x = {ecuacion}")
        print(f"{CIAN}" + "="*60 + f"{RESET}")
        print("\nUsa las flechas o WASD para moverte. [Enter] para confirmar.\n")

        for f in range(filas):
            linea = "     "
            for c in range(cols):
                valor = matriz[f][c]
                if f == cursor_f and c == cursor_c:
                    linea += f"{AMARILLO}[{valor:2}]{RESET}  " 
                else:
                    linea += f"  {valor:2}   "
            print(linea + "\n")

        key = msvcrt.getch()

        # Movimiento
        if key in (b'\xe0', b'\x00'):
            dir_key = msvcrt.getch()
            if dir_key == b'H': cursor_f = max(0, cursor_f - 1)
            elif dir_key == b'P': cursor_f = min(filas - 1, cursor_f + 1)
            elif dir_key == b'K': cursor_c = max(0, cursor_c - 1)
            elif dir_key == b'M': cursor_c = min(cols - 1, cursor_c + 1)
        elif key.lower() == b'w': cursor_f = max(0, cursor_f - 1)
        elif key.lower() == b's': cursor_f = min(filas - 1, cursor_f + 1)
        elif key.lower() == b'a': cursor_c = max(0, cursor_c - 1)
        elif key.lower() == b'd': cursor_c = min(cols - 1, cursor_c + 1)
        
        # Selección
        elif key == b'\r':
            os.system('cls')
            if cursor_f == fila_real and cursor_c == col_real:
                print(f"\n{VERDE}¡EXCELENTE! El valor de x es {x}.{RESET}")
            else:
                print(f"\n{ROJO}ERROR.{RESET} Elegiste {matriz[cursor_f][cursor_c]}.")
                print(f"La respuesta correcta era {VERDE}{x}{RESET}.")
            break

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    os.system('') # Soporte ANSI
    
    x_obj, ec = generar_numero()
    m, fr, cr = construir_escenario(x_obj)
    
    jugar(m, x_obj, fr, cr, ec)
    
    print("\nPresiona cualquier tecla para cerrar...")
    msvcrt.getch()
    