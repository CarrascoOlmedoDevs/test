# Define content data
title = "Informe de Investigación: Métodos de Conteo de Pasos en Android"
introduction = """
Este informe resume la investigación realizada sobre las diversas tecnologías y sensores disponibles en la plataforma Android para el conteo de pasos. El objetivo es evaluar las opciones, identificar sus fortalezas y debilidades, y proporcionar una recomendación fundamentada para la implementación en el proyecto 'pasos'.
"""

methods_data = [
    {
        "name": "Acelerómetro Puro",
        "description": "Análisis directo de los datos del sensor de aceleración (TYPE_ACCELEROMETER) para detectar patrones que corresponden a pasos.",
        "pros": [
            "Disponible en prácticamente todos los dispositivos Android.",
            "No requiere permisos especiales (más allá de los sensores básicos).",
            "Puede funcionar completamente offline."
        ],
        "cons": [
            "Requiere algoritmos complejos de procesamiento de señal.",
            "Muy sensible a la posición y movimiento del teléfono (en el bolsillo, mano, etc.).",
            "Precisión muy variable y difícil de garantizar.",
            "Alto consumo de batería si no se implementa con cuidado (requiere el sensor activo constantemente)."
        ]
    },
    {
        "name": "Sensor de Conteo de Pasos (TYPE_STEP_COUNTER)",
        "description": "Sensor de hardware (o software fusionado) que proporciona el número total de pasos detectados desde la última vez que el dispositivo se reinició o el sensor se activó.",
        "pros": [
            "Hardware-acelerado, muy eficiente en consumo de energía.",
            "Diseñado específicamente para el conteo de pasos, generalmente más preciso que el acelerómetro puro.",
            "Maneja mejor las variaciones en la posición del teléfono.",
            "Proporciona un conteo acumulativo, simplificando la lógica de la aplicación (se mide la diferencia)."
        ],
        "cons": [
            "Requiere API Nivel 19 (KitKat) o superior.",
            "La disponibilidad depende del hardware específico del dispositivo.",
            "El conteo es acumulativo, lo que requiere manejar el estado (guardar el valor inicial/anterior)."
        ]
    },
    {
        "name": "Sensor Detector de Pasos (TYPE_STEP_DETECTOR)",
        "description": "Sensor de hardware (o software fusionado) que dispara un evento cada vez que se detecta un paso.",
        "pros": [
            "Hardware-acelerado, muy eficiente en consumo de energía.",
            "Basado en eventos, simplifica la lógica de detección.",
            "Bajo consumo de batería."
        ],
        "cons": [
            "Requiere API Nivel 19 (KitKat) o superior.",
            "La disponibilidad depende del hardware específico del dispositivo.",
            "Puede ser menos preciso para contar pasos que el TYPE_STEP_COUNTER en algunos escenarios, ya que solo reporta la detección de un evento, no mantiene un conteo continuo."
        ]
    },
    {
        "name": "Google Fit API (History API)",
        "description": "Utiliza los servicios de Google Play para acceder a datos de actividad física agregados, incluyendo pasos, que pueden provenir de múltiples fuentes (sensores del teléfono, wearables, otras apps).",
        "pros": [
            "Potencialmente la fuente más precisa al fusionar datos.",
            "Maneja la complejidad de la detección y agregación.",
            "Permite acceder a datos históricos y sincronizar entre dispositivos.",
            "Se integra con el ecosistema de Google Fit del usuario."
        ],
        "cons": [
            "Requiere Google Play Services instalado en el dispositivo.",
            "Requiere que el usuario tenga una cuenta de Google y otorgue permisos.",
            "Puede requerir conexión a internet para sincronizar datos.",
            "Introduce una dependencia externa (Google Play Services)."
        ]
    }
]

comparison = """
En comparación, los sensores dedicados (TYPE_STEP_COUNTER y TYPE_STEP_DETECTOR) ofrecen un buen equilibrio entre precisión, eficiencia energética y complejidad de implementación en comparación con el análisis del acelerómetro puro. La Google Fit API proporciona la mayor precisión potencial y funcionalidades adicionales (historial, fusión de datos), pero introduce dependencias externas y requisitos de usuario. El acelerómetro puro es la opción de menor denominador común pero con serias limitaciones en precisión y eficiencia.
"""

recommendation = """
Basado en la investigación, la recomendación principal para el proyecto 'pasos' es utilizar el **Sensor de Conteo de Pasos (TYPE_STEP_COUNTER)**.

**Justificación:**
*   **Precisión y Fiabilidad:** Es un sensor diseñado específicamente para este propósito, ofreciendo una precisión significativamente mayor que el acelerómetro puro y manejando mejor las variaciones de uso del dispositivo.
*   **Eficiencia Energética:** Está optimizado a nivel de hardware, resultando en un consumo de batería muy bajo en comparación con el procesamiento constante del acelerómetro.
*   **Simplicidad de Implementación:** Aunque requiere manejar el estado acumulativo, es mucho más sencillo que implementar algoritmos complejos de detección de pasos desde cero.
*   **Disponibilidad:** Aunque requiere API 19+, la mayoría de los dispositivos Android modernos lo soportan, cubriendo una amplia base de usuarios.

Para dispositivos muy antiguos que no soporten TYPE_STEP_COUNTER, se podría considerar TYPE_STEP_DETECTOR como alternativa (aunque menos ideal para un conteo continuo preciso) o, como último recurso, un algoritmo básico basado en acelerómetro, aunque se debe ser consciente de sus limitaciones. La Google Fit API podría considerarse como una opción complementaria para características avanzadas como historial detallado o sincronización, pero no como la fuente principal si se busca minimizar dependencias externas y requisitos de usuario.

Por lo tanto, TYPE_STEP_COUNTER es la opción más robusta y eficiente para la funcionalidad principal de conteo de pasos.
"""

# Function to generate Markdown string
def generate_step_counting_research_markdown(title, introduction, methods, comparison, recommendation):
    markdown_content = f"# {title}\n\n"
    markdown_content += f"{introduction}\n\n"

    markdown_content += "## Métodos Evaluados\n\n"
    for method in methods:
        markdown_content += f"### {method['name']}\n\n"
        markdown_content += f"{method['description']}\n\n"
        markdown_content += "**Ventajas:**\n"
        for pro in method['pros']:
            markdown_content += f"- {pro}\n"
        markdown_content += "\n"
        markdown_content += "**Desventajas:**\n"
        for con in method['cons']:
            markdown_content += f"- {con}\n"
        markdown_content += "\n"

    markdown_content += "## Comparación\n\n"
    markdown_content += f"{comparison}\n\n"

    markdown_content += "## Recomendación\n\n"
    markdown_content += f"{recommendation}\n"

    return markdown_content

# Main execution block
if __name__ == "__main__":
    markdown_output = generate_step_counting_research_markdown(
        title,
        introduction,
        methods_data,
        comparison,
        recommendation
    )

    file_name = "step_counting_research.md"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(markdown_output)
    except IOError:
        # Handle error silently as per requirement
        pass