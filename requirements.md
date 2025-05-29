import os

markdown_content = """# Requisitos de la Aplicación: Contador de Pasos Simple

Este documento describe los requisitos iniciales para una aplicación simple de conteo de pasos para Android.

## 1. Funcionalidades Clave

*   **Conteo de Pasos:** Implementar un algoritmo para el conteo preciso de pasos utilizando los sensores de movimiento del dispositivo (principalmente acelerómetro; giroscopio podría usarse para refinamiento si es necesario).
*   **Visualización en Tiempo Real:** Mostrar el conteo actual de pasos en la interfaz de usuario principal, actualizándose en tiempo real a medida que el usuario camina.
*   **Historial Diario:** Registrar el conteo total de pasos al final de cada día y permitir al usuario visualizar un historial de sus pasos diarios (ej. los últimos 7 o 30 días).
*   **Meta Diaria:** Permitir al usuario establecer una meta de pasos diaria y mostrar visualmente el progreso hacia esa meta.
*   **Interfaz de Usuario:** Diseñar una interfaz de usuario limpia, intuitiva y fácil de navegar, enfocada en la funcionalidad principal de conteo de pasos.

## 2. Público Objetivo

*   Usuarios de dispositivos Android que buscan una herramienta básica y fiable para rastrear su actividad física diaria a través del conteo de pasos.
*   Personas que prefieren una aplicación gratuita, sin anuncios intrusivos (si es posible en futuras iteraciones) y sin funcionalidades complejas como redes sociales, planes de entrenamiento personalizados o gamificación avanzada.

## 3. Limitaciones Técnicas Iniciales

*   **Dependencia de Sensores:** La precisión del conteo de pasos dependerá directamente de la disponibilidad, calidad y calibración de los sensores de movimiento en el dispositivo del usuario.
*   **Consumo de Batería:** La implementación debe optimizarse para minimizar el consumo de batería, ya que el seguimiento de pasos requiere el uso continuo de sensores.
*   **Compatibilidad:** La versión inicial se centrará en la compatibilidad con versiones recientes de Android (ej. Android 8.0 Oreo o superior), aunque se buscará la mayor compatibilidad posible sin comprometer la estabilidad o el consumo de batería.
*   **Sin Integración Externa:** En esta fase inicial, no se incluirá integración con servicios externos como Google Fit, plataformas de salud de fabricantes de dispositivos, ni APIs de terceros.
*   **Variabilidad del Conteo:** El conteo de pasos puede variar ligeramente entre dispositivos y dependiendo de cómo el usuario lleve el teléfono (bolsillo, mano, bolso). La aplicación debe manejar estas variaciones lo mejor posible, pero se reconoce que la precisión perfecta es un desafío.
"""

file_path = "requirements.md"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    # print(f"Documento '{file_path}' creado exitosamente.") # Optional: for confirmation
except IOError as e:
    print(f"Error al escribir el archivo {file_path}: {e}")