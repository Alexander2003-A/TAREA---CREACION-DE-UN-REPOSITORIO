# Definir la matriz 3x3 con números
matriz = [
    [3, 5, 7],
    [8, 2, 6],
    [4, 9, 1]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario qué fila desea ordenar
fila_ordenar = int(input("Ingrese el número de la fila que desea ordenar (0, 1 o 2): "))

# Verificar que el número de fila sea válido
if 0 <= fila_ordenar < len(matriz):
    # Ordenar la fila seleccionada
    matriz[fila_ordenar].sort()

    # Mostrar la matriz después de ordenar
    print("\nMatriz después de ordenar la fila:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila no válido. Debe ser 0, 1 o 2.")
