import os

def generate_documentation(filename="documentation.md"):
    """
    Genera un archivo de documentación en formato Markdown para el proyecto 'calories'.
    """
    documentation_content = """# Proyecto Calories - Alcance Inicial y Requisitos

Este documento define el alcance inicial y los requisitos para la primera versión del proyecto 'calories'.

## 1. Funcionalidades Mínimas Viables (MVP)

El MVP del proyecto 'calories' se centrará en las siguientes características esenciales:

*   **Escaneo de Productos:** Permitir al usuario escanear un producto utilizando un método soportado.
*   **Visualización de Datos Nutricionales:** Mostrar la información nutricional clave del producto escaneado.
*   **Base de Datos Local (Inicial):** Almacenar una base de datos limitada de productos y su información nutricional para las pruebas iniciales. (Nota: Una versión futura podría integrar APIs externas).

## 2. Tipos de Escaneo Soportados (MVP)

Para el MVP, el proyecto soportará el siguiente tipo de escaneo:

*   **Escaneo de Códigos de Barras (Barcode):** Utilizar la cámara del dispositivo (o un escáner simulado) para leer códigos de barras estándar (como EAN-13, UPC-A).

## 3. Datos Nutricionales Clave

Para cada producto escaneado, el MVP deberá mostrar la siguiente información nutricional clave:

*   **Calorías:** Energía total por porción o por 100g/ml.
*   **Grasas Totales:** Cantidad total de grasas.
*   **Grasas Saturadas:** Cantidad de grasas saturadas.
*   **Carbohidratos Totales:** Cantidad total de carbohidratos.
*   **Azúcares:** Cantidad de azúcares simples.
*   **Proteínas:** Cantidad de proteínas.
*   **Sal (o Sodio):** Cantidad de sal o sodio.
*   **Tamaño de la Porción:** Información sobre el tamaño de la porción utilizada para los valores nutricionales.

"""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(documentation_content)
        print(f"Archivo de documentación '{filename}' generado exitosamente.")
    except IOError as e:
        print(f"Error al escribir el archivo {filename}: {e}")

if __name__ == "__main__":
    generate_documentation()