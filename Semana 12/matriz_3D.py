# Definimos la matriz tridimensional de temperaturas
temperaturas = [
    [  # Cuenca (Ciudad 1)
        [15, 18],  # Lunes (Semana 1, Semana 2)
        [20, 22],  # Martes
        [25, 28],  # Miércoles
        [24, 27],  # Jueves
        [21, 23],  # Viernes
        [19, 21],  # Sábado
        [16, 20]   # Domingo
    ],
    [  # Quevedo (Ciudad 2)
        [17, 19],  # Lunes
        [21, 24],  # Martes
        [26, 29],  # Miércoles
        [28, 30],  # Jueves
        [23, 25],  # Viernes
        [22, 24],  # Sábado
        [18, 22]   # Domingo
    ],
    [  # Ambato (Ciudad 3)
        [14, 16],  # Lunes
        [18, 20],  # Martes
        [22, 24],  # Miércoles
        [25, 27],  # Jueves
        [19, 21],  # Viernes
        [16, 18],  # Sábado
        [15, 17]   # Domingo
    ]
]

# Nombres de las ciudades
ciudades = ["Cuenca", "Quevedo", "Ambato"]
semanas = 2  # Dos semanas

# Bucle anidado para calcular el promedio de temperaturas
for i, ciudad in enumerate(ciudades):  # Iteramos sobre las ciudades
    for semana in range(semanas):  # Iteramos sobre las semanas
        suma = 0
        for dia in range(7):  # Iteramos sobre los días de la semana
            suma += temperaturas[i][dia][semana]  # Sumamos temperaturas
        promedio = suma / 7  # Calculamos el promedio
        print(f"Promedio de temperatura en {ciudad} durante la Semana {semana + 1}: {promedio:.2f}°C")
