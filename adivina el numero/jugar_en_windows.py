import msvcrt
import os
import sys

# Colores ANSI
VERDE = '\033[92m'
ROJO = '\033[91m'
RESET = '\033[0m'
AMARILLO = '\033[93m'

def jugar_en_windows(matriz, x, fila_real, col_real, ecuacion):
    filas = len(matriz)
    cols = len(matriz[0])
    cursor_f, cursor_c = 0, 0 
    
    while True:
        os.system('cls') 
        print("="*50)
        print(f"{AMARILLO}DESAFÍO:{RESET} {ecuacion}")
        print("="*50)
        print("\nUsa las flechas (o WASD) y [Enter] para seleccionar:\n")

        for f in range(filas):
            linea = ""
            for c in range(cols):
                valor = matriz[f][c]
                if f == cursor_f and c == cursor_c:
                    linea += f"  {AMARILLO}[{valor:2}]{RESET}  " 
                else:
                    linea += f"    {valor:2}    "
            print(linea + "\n")

        # Captura de tecla
        key = msvcrt.getch()

        # 1. Detección de flechas (prefijos b'\xe0' o b'\x00')
        if key in (b'\xe0', b'\x00'):
            direccion = msvcrt.getch()
            if direccion == b'H': cursor_f = max(0, cursor_f - 1)    # Arriba
            elif direccion == b'P': cursor_f = min(filas - 1, cursor_f + 1) # Abajo
            elif direccion == b'K': cursor_c = max(0, cursor_c - 1)    # Izquierda
            elif direccion == b'M': cursor_c = min(cols - 1, cursor_c + 1) # Derecha
        
        # 2. Detección de WASD (respaldo para terminales de VS Code)
        elif key.lower() == b'w': cursor_f = max(0, cursor_f - 1)
        elif key.lower() == b's': cursor_f = min(filas - 1, cursor_f + 1)
        elif key.lower() == b'a': cursor_c = max(0, cursor_c - 1)
        elif key.lower() == b'd': cursor_c = min(cols - 1, cursor_c + 1)
        
        # 3. Enter
        elif key == b'\r':
            os.system('cls')
            if cursor_f == fila_real and cursor_c == col_real:
                print(f"\n{VERDE}¡CORRECTO! El número era {x}.{RESET}")
            else:
                print(f"\n{ROJO}INCORRECTO. Elegiste {matriz[cursor_f][cursor_c]}, pero el secreto era {x}.{RESET}")
            break

if __name__ == "__main__":
    os.system('') # Activa soporte ANSI en Windows
    matriz_p = [[10, 20], [30, 40]]
    jugar_en_windows(matriz_p, 40, 1, 1, "20 + 20")
    print("\nPresiona cualquier tecla para salir...")
    msvcrt.getch()