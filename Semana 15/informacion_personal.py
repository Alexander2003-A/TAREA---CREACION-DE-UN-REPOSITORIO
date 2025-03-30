# 1. Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# 2. Acceder y modificar valores
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos la ciudad a otra

# 3. Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio

# 4. Eliminar la clave "edad"
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
