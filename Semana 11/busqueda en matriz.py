# Definir la matriz 3x3 con números
matriz = [
    [3, 5, 7],
    [8, 2, 6],
    [4, 9, 1]
]

# Pedir al usuario el número que quiere buscar
num_buscado = int(input("Ingrese el número que desea buscar: "))

# Variable para saber si encontramos el número
encontrado = False

# Recorrer la matriz
for i in range(len(matriz)):  # Recorre las filas
    for j in range(len(matriz[i])):  # Recorre las columnas
        if matriz[i][j] == num_buscado:
            print(f"El número {num_buscado} se encuentra en la posición ({i}, {j})")
            encontrado = True

# Si no se encontró el número
if not encontrado:
    print(f"El número {num_buscado} no está en la matriz.")
