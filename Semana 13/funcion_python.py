# Definir la función para calcular temperaturas promedio
def calcular_temperatura_promedio(temperaturas, ciudades):
    """
    Calcula el promedio de temperatura por ciudad y semana.

    Parámetros:
    - temperaturas (list): Lista tridimensional con temperaturas por ciudad, día y semana.
    - ciudades (list): Lista con los nombres de las ciudades.

    Retorna:
    - dict: Diccionario con los promedios de temperatura por ciudad y semana.
    """
    semanas = len(temperaturas[0][0])  # Número de semanas
    promedios_ciudades = {}  # Diccionario para almacenar los promedios

    # Iterar sobre cada ciudad
    for i, ciudad in enumerate(ciudades):
        promedios_ciudades[ciudad] = []  # Lista de promedios por semana

        # Iterar sobre cada semana
        for semana in range(semanas):
            suma = 0

            # Iterar sobre los días de la semana
            for dia in range(7):
                suma += temperaturas[i][dia][semana]  # Sumar temperaturas

            # Calcular el promedio y agregarlo al diccionario
            promedio = suma / 7
            promedios_ciudades[ciudad].append(promedio)

    return promedios_ciudades  # Retornar resultados


# Datos de temperatura de la tarea anterior
temperaturas = [
    [  # Cuenca
        [15, 18], [20, 22], [25, 28], [24, 27], [21, 23], [19, 21], [16, 20]
    ],
    [  # Quevedo
        [17, 19], [21, 24], [26, 29], [28, 30], [23, 25], [22, 24], [18, 22]
    ],
    [  # Ambato
        [14, 16], [18, 20], [22, 24], [25, 27], [19, 21], [16, 18], [15, 17]
    ]
]
ciudades = ["Cuenca", "Quevedo", "Ambato"]

# Llamamos a la función y mostramos los resultados
resultados = calcular_temperatura_promedio(temperaturas, ciudades)
for ciudad, promedios in resultados.items():
    for i, promedio in enumerate(promedios):
        print(f"Promedio de temperatura en {ciudad} durante la Semana {i + 1}: {promedio:.2f}°C")
