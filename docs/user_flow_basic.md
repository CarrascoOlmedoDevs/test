import os

def generate_user_flow_markdown(filename="user_flow.md"):
    """
    Genera un archivo Markdown que describe el flujo de usuario básico
    para la aplicación 'calories'.
    """
    markdown_content = """# Flujo de Usuario Básico: Aplicación 'Calories'

Este documento describe el flujo de usuario principal para escanear y obtener información nutricional de alimentos utilizando la aplicación 'Calories'.

## 1. Iniciar el Escaneo de un Alimento

El usuario abre la aplicación 'Calories'. La pantalla principal presenta una opción clara para iniciar el escaneo de un alimento.

1.  El usuario pulsa el botón o icono "Escanear Alimento".
2.  La aplicación activa la cámara del dispositivo y muestra una interfaz de escaneo.
3.  El usuario apunta la cámara hacia el alimento o su envase (si aplica).

## 2. Mostrar el Resultado del Escaneo

Una vez que la aplicación identifica el alimento, presenta un resumen de la información nutricional clave.

1.  La aplicación procesa la imagen o el código escaneado.
2.  Si la identificación es exitosa, la aplicación muestra una nueva pantalla o superpone la información sobre la vista de la cámara.
3.  Se muestra el nombre identificado del alimento.
4.  Se presentan los valores energéticos principales, típicamente:
    *   Calorías (kcal)
    *   Grasas (g)
    *   Carbohidratos (g)
    *   Proteínas (g)
    *   (Opcional) Fibra (g)
    *   (Opcional) Azúcares (g)
    Estos valores pueden mostrarse por porción o por 100g/ml.

## 3. Acceder a Datos Energéticos Detallados

Si hay información nutricional más completa disponible para el alimento identificado, el usuario tiene la opción de verla.

1.  En la pantalla de resultados del escaneo (Paso 2), hay un botón o enlace etiquetado como "Ver Detalles Nutricionales" o similar.
2.  El usuario pulsa este botón.
3.  La aplicación navega a una nueva pantalla que muestra un desglose más completo de la información nutricional, que puede incluir:
    *   Vitaminas
    *   Minerales
    *   Ácidos grasos específicos (saturadas, insaturadas)
    *   Colesterol
    *   Sodio
    *   Información sobre alérgenos
    *   Lista de ingredientes
    *   Información por diferentes tamaños de porción
4.  El usuario puede regresar a la pantalla anterior o a la pantalla principal de la aplicación desde esta vista detallada.

Este flujo permite al usuario obtener rápidamente la información nutricional esencial de un alimento escaneado y acceder a detalles adicionales si es necesario.
"""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        # print(f"Archivo '{filename}' generado exitosamente.") # Optional: for confirmation
    except IOError as e:
        # print(f"Error al escribir en el archivo '{filename}': {e}") # Optional: for error handling
        pass # Silent failure as per implicit requirement of no output outside markdown/code

if __name__ == "__main__":
    generate_user_flow_markdown()