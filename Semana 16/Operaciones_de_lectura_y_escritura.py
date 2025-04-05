# 1. Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("El método write() se usa para escribir en un archivo.\n")
    file.write("Puedo guardar cualquier tipo de texto en un archivo de texto.\n")

# 2. Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    for linea in file:
        print(linea.strip())  # Mostramos cada línea eliminando los saltos de línea

# 3. Cierre de Archivos (Se maneja automáticamente con 'with')
