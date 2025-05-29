import os

def generate_user_flow_markdown():
    """
    Generates the user flow markdown document for the 'calories' app scanning feature.
    """
    markdown_content = """# Flujo de Usuario Principal - Aplicación 'Calories' (Escaneo de Alimentos)

Este documento describe el flujo principal que un usuario seguiría al utilizar la función de escaneo de alimentos en la aplicación 'Calories'.

## 1. Inicio del Proceso de Escaneo

El usuario inicia la función de escaneo para identificar un alimento.

*   **Paso 1.1:** El usuario abre la aplicación 'Calories'.
*   **Paso 1.2:** En la pantalla principal o en una sección dedicada, el usuario localiza y toca el botón o icono que inicia el proceso de escaneo (ej. un icono de cámara o un botón con la etiqueta "Escanear Alimento").
*   **Paso 1.3:** La aplicación solicita acceso a la cámara del dispositivo (si es la primera vez o si los permisos fueron revocados). El usuario concede el permiso.
*   **Paso 1.4:** La interfaz de la cámara se activa, mostrando una vista previa en tiempo real. El usuario apunta la cámara hacia el alimento o su empaque.

## 2. Visualización del Resultado del Escaneo

Una vez que la aplicación identifica el alimento, muestra los resultados relevantes al usuario.

*   **Paso 2.1:** La aplicación procesa la imagen o el código escaneado.
*   **Paso 2.2:** Tras una breve espera (indicada quizás por un spinner o mensaje de "Procesando..."), la aplicación presenta una pantalla de resultados.
*   **Paso 2.3:** Esta pantalla muestra claramente:
    *   La identificación del alimento (ej. "Manzana Roja", "Barra de Proteína sabor Chocolate").
    *   Valores nutricionales clave para una porción estándar o la cantidad escaneada (si es posible), como:
        *   Calorías
        *   Proteínas
        *   Carbohidratos (posiblemente desglosados en azúcares y fibra)
        *   Grasas (posiblemente desglosadas en saturadas/insaturadas)
    *   Otros datos relevantes como tamaño de la porción, vitaminas, minerales, etc. (dependiendo de la base de datos).

## 3. Interacción con el Resultado

El usuario puede interactuar con los resultados mostrados.

*   **Paso 3.1:** El usuario revisa la información nutricional presentada en la pantalla de resultados.
*   **Paso 3.2:** Dependiendo de la funcionalidad adicional:
    *   Puede haber opciones para ajustar la cantidad consumida para recalcular los valores.
    *   Puede haber un botón para añadir este alimento a un registro diario de consumo.
    *   Puede haber un enlace o botón para ver detalles nutricionales más completos.
*   **Paso 3.3:** El usuario puede cerrar la pantalla de resultados o navegar a otra sección de la aplicación (ej. al registro diario, a la pantalla principal).
"""

    file_name = "user_flow.md"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Archivo '{file_name}' generado exitosamente.")
    except IOError as e:
        print(f"Error al escribir el archivo '{file_name}': {e}")

if __name__ == "__main__":
    generate_user_flow_markdown()