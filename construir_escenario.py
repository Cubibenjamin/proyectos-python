import random

def construir_escenario(x):
    # 1. Dimensión aleatoria (n x n)
    dimension = random.randint(3, 7)
    total_celdas = dimension * dimension
    
    # 2. Generar números ÚNICOS
    # Creamos un rango amplio (del 1 al 100) para asegurar que haya suficientes números
    # random.sample garantiza que no se repitan
    pool_de_numeros = list(range(1, 101)) 
    
    # Nos aseguramos de quitar 'x' del pool para que no aparezca dos veces
    if x in pool_de_numeros:
        pool_de_numeros.remove(x)
    
    # Tomamos los números necesarios para llenar la matriz (menos uno, que es 'x')
    muestreo = random.sample(pool_de_numeros, total_celdas - 1)
    
    # 3. Insertar 'x' en una posición aleatoria y mezclar
    muestreo.append(x)
    random.shuffle(muestreo) # Mezclamos para que 'x' no esté siempre al final
    
    # 4. Convertir la lista plana en una matriz cuadrada
    matriz = []
    for i in range(0, total_celdas, dimension):
        matriz.append(muestreo[i : i + dimension])
    
    # 5. Encontrar la posición de x para retornar las coordenadas
    for f in range(dimension):
        for c in range(dimension):
            if matriz[f][c] == x:
                fila_real, col_real = f, c
    
    return matriz, fila_real, col_real

# --- PRUEBA EN VS CODE ---
if __name__ == "__main__":
    x_secreto = 7
    m, f, c = construir_escenario(x_secreto)
    print(f"Matriz de {len(m)}x{len(m)} sin repeticiones:")
    print(f"Escondido en: Fila {f}, Columna {c}\n")
    for fila in m:
        print(fila)