import os

def generate_step_counting_report():
    """
    Generates a Markdown report summarizing Android step counting methods.

    Returns:
        str: The Markdown formatted report.
    """
    report_title = "# Informe sobre Métodos de Conteo de Pasos en Android\n\n"
    introduction = "Este informe resume los hallazgos de la investigación sobre diferentes métodos para contar pasos en dispositivos Android, comparando sus características y ofreciendo una recomendación.\n\n"

    methods_data = {
        "Acelerómetro Nativo (Manual Implementation)": {
            "description": "Implementación manual de un algoritmo de detección de pasos utilizando datos crudos del sensor acelerómetro del dispositivo.",
            "pros": [
                "Control total sobre el algoritmo.",
                "No requiere dependencias externas (fuera de los sensores del sistema)."
            ],
            "cons": [
                "Alta complejidad de implementación (requiere desarrollar o integrar un algoritmo robusto).",
                "Precisión variable, depende mucho de la calidad del algoritmo y la calibración.",
                "Consumo de energía potencialmente alto si no se maneja correctamente (uso constante del sensor).",
                "Sensible a falsos positivos (movimientos no relacionados con caminar)."
            ],
            "complexity": "Alta",
            "energy": "Potencialmente Alta",
            "precision": "Variable (depende del algoritmo)",
            "permissions": "android.permission.ACTIVITY_RECOGNITION (para versiones recientes de Android, aunque a veces se puede evitar si solo se usa el sensor sin intención de reconocer actividad)."
        },
        "Google Fit API - History API": {
            "description": "Utiliza datos agregados de actividad física (incluido el conteo de pasos) que Google Fit ya ha recolectado en el dispositivo.",
            "pros": [
                "Muy eficiente energéticamente (Google Fit maneja la recolección en segundo plano).",
                "Relativamente sencilla de implementar para obtener datos históricos.",
                "Precisión generalmente buena, ya que se basa en la infraestructura optimizada de Google Fit.",
                "Acceso a datos históricos (pasos contados previamente por Google Fit)."
            ],
            "cons": [
                "Dependencia de la aplicación Google Fit instalada y configurada en el dispositivo.",
                "Los datos pueden no estar disponibles en tiempo real (hay un pequeño retraso en la agregación).",
                "Requiere autenticación con la cuenta de Google del usuario.",
                "Puede haber discrepancias si el usuario usa múltiples dispositivos o si Google Fit no está activo."
            ],
            "complexity": "Media",
            "energy": "Baja (delega a Google Fit)",
            "precision": "Buena (gestionada por Google Fit)",
            "permissions": "Com.google.android.gms.permission.ACTIVITY_RECOGNITION (obtenido a través de la integración con Google Fit), requiere consentimiento del usuario para acceder a los datos de actividad física."
        },
        "Google Fit API - Recording API": {
            "description": "Permite a la aplicación registrar la intención de recibir datos de actividad física (como pasos) de Google Fit de forma continua en segundo plano.",
            "pros": [
                "Eficiente energéticamente (Google Fit gestiona la recolección).",
                "Permite a la aplicación recibir actualizaciones continuas de pasos sin mantener el sensor activo directamente.",
                "Menos susceptible a ser 'matada' por el sistema operativo que un servicio propio usando sensores directos."
            ],
            "cons": [
                "Dependencia de Google Fit.",
                "Requiere autenticación.",
                "Los datos se entregan a Google Fit primero y luego a tu aplicación, no es tiempo real estricto.",
                "Requiere que la aplicación se registre para tipos de datos específicos."
            ],
            "complexity": "Media",
            "energy": "Baja (delega a Google Fit)",
            "precision": "Buena (gestionada por Google Fit)",
            "permissions": "Com.google.android.gms.permission.ACTIVITY_RECOGNITION, consentimiento del usuario."
        },
        "Google Fit API - Sensors API": {
            "description": "Permite a la aplicación acceder a los datos de los sensores de actividad física (incluido el sensor de conteo de pasos hardware si está disponible) a través de Google Fit.",
            "pros": [
                "Acceso a datos casi en tiempo real del sensor de pasos (si existe hardware dedicado).",
                "Utiliza el sensor de conteo de pasos del hardware (TYPE_STEP_COUNTER) que es muy eficiente energéticamente.",
                "Google Fit maneja parte de la complejidad de interactuar con los sensores del sistema."
            ],
            "cons": [
                "Dependencia de Google Fit.",
                "Requiere autenticación.",
                "La disponibilidad del sensor de conteo de pasos hardware varía entre dispositivos.",
                "Requiere manejar el flujo de datos del sensor directamente (aunque facilitado por Google Fit)."
            ],
            "complexity": "Media a Baja (si el sensor hardware está disponible)",
            "energy": "Muy Baja (si usa TYPE_STEP_COUNTER hardware)",
            "precision": "Alta (si usa TYPE_STEP_COUNTER hardware)",
            "permissions": "Com.google.android.gms.permission.ACTIVITY_RECOGNITION, consentimiento del usuario."
        }
    }

    report_content = report_title + introduction

    report_content += "## Métodos Investigados\n\n"

    for method, details in methods_data.items():
        report_content += f"### {method}\n\n"
        report_content += f"**Descripción:** {details['description']}\n\n"
        report_content += "**Pros:**\n"
        for pro in details["pros"]:
            report_content += f"- {pro}\n"
        report_content += "\n"
        report_content += "**Contras:**\n"
        for con in details["cons"]:
            report_content += f"- {con}\n"
        report_content += "\n"
        report_content += f"**Complejidad de Implementación:** {details['complexity']}\n"
        report_content += f"**Eficiencia Energética:** {details['energy']}\n"
        report_content += f"**Precisión:** {details['precision']}\n"
        report_content += f"**Permisos Necesarios:** {details['permissions']}\n\n"
        report_content += "---\n\n" # Separator

    report_content += "## Comparación\n\n"
    report_content += "| Característica          | Acelerómetro Nativo | Google Fit - History | Google Fit - Recording | Google Fit - Sensors |\n"
    report_content += "|-------------------------|---------------------|----------------------|------------------------|----------------------|\n"
    for characteristic in ["Complejidad de Implementación", "Eficiencia Energética", "Precisión", "Permisos Necesarios"]:
         report_content += f"| {characteristic} | {methods_data['Acelerómetro Nativo (Manual Implementation)'][characteristic.split(' ')[0].lower() if characteristic != 'Permisos Necesarios' else 'permissions']} | {methods_data['Google Fit API - History API'][characteristic.split(' ')[0].lower() if characteristic != 'Permisos Necesarios' else 'permissions']} | {methods_data['Google Fit API - Recording API'][characteristic.split(' ')[0].lower() if characteristic != 'Permisos Necesarios' else 'permissions']} | {methods_data['Google Fit API - Sensors API'][characteristic.split(' ')[0].lower() if characteristic != 'Permisos Necesarios' else 'permissions']} |\n"

    report_content += "\n"

    report_content += "## Recomendación\n\n"
    report_content += "Para la mayoría de las aplicaciones de conteo de pasos en Android, el enfoque **Google Fit API** es generalmente el más recomendado, específicamente utilizando una combinación de **Sensors API** y **History API**.\n\n"
    report_content += "**Justificación:**\n"
    report_content += "- **Eficiencia Energética:** Utilizar la infraestructura de Google Fit, especialmente el acceso al sensor de conteo de pasos hardware (TYPE_STEP_COUNTER) a través de la Sensors API, es significativamente más eficiente en términos de batería que procesar datos crudos del acelerómetro manualmente.\n"
    report_content += "- **Precisión:** Google Fit utiliza algoritmos optimizados y puede acceder a sensores de hardware dedicados, lo que generalmente resulta en un conteo de pasos más preciso y menos propenso a falsos positivos que una implementación manual simple.\n"
    report_content += "- **Complejidad de Implementación:** Aunque requiere integrar la API de Google Fit y manejar la autenticación, es menos complejo que desarrollar y mantener un algoritmo de detección de pasos robusto desde cero.\n"
    report_content += "- **Datos Históricos:** La History API permite acceder fácilmente a los pasos contados por Google Fit incluso cuando la aplicación no estaba activa, proporcionando una experiencia de usuario más completa.\n\n"
    report_content += "La **Sensors API** es ideal para obtener actualizaciones en tiempo real (o casi real) cuando la aplicación está en primer plano o necesita monitoreo activo. La **History API** es crucial para mostrar resúmenes diarios, semanales, etc., y para recuperar datos si la aplicación se cerró.\n\n"
    report_content += "La implementación manual del acelerómetro solo se consideraría en casos muy específicos donde la dependencia de Google Fit es inaceptable o se requiere un control extremadamente granular sobre el procesamiento del sensor, asumiendo la inversión significativa en desarrollo y pruebas necesarias para lograr precisión y eficiencia aceptables.\n\n"

    return report_content

if __name__ == "__main__":
    report_markdown = generate_step_counting_report()

    # Specify the output file name
    output_filename = "informe_conteo_pasos_android.md"

    # Save the report to a Markdown file
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(report_markdown)
        print(f"Informe generado exitosamente en '{output_filename}'")
    except IOError as e:
        print(f"Error al escribir el archivo '{output_filename}': {e}")