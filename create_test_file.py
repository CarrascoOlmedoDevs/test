def crear_archivo_prueba():
    """
    Crea o sobrescribe el archivo 'agent1_prueba.txt'
    y escribe una línea de texto en él.
    """
    nombre_archivo = 'agent1_prueba.txt'
    contenido = 'Este es un archivo de prueba del Agente 1.'

    try:
        with open(nombre_archivo, 'w') as f:
            f.write(contenido)
        # print(f"Archivo '{nombre_archivo}' creado/sobrescrito exitosamente.")
    except IOError as e:
        # print(f"Error al escribir en el archivo '{nombre_archivo}': {e}")
        pass # Opcional: manejar el error de otra manera si es necesario

if __name__ == "__main__":
    crear_archivo_prueba()