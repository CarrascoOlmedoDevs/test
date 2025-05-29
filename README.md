import os

readme_content = """# calories

crear apk para escanear comida y devolver valores energéticos

## Instalación

(Detalles de instalación se añadirán aquí más tarde)

## Uso

(Instrucciones de uso se añadirán aquí más tarde)
"""

file_path = "README.md"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    # print(f"Archivo '{file_path}' generado exitosamente.") # Removed print as per instructions
except IOError as e:
    # print(f"Error al escribir el archivo '{file_path}': {e}") # Removed print as per instructions
    pass # Keep silent as per instructions