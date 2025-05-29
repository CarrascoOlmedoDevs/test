import os

# Define the content for the Markdown file

introduction = """
Este documento resume la investigación realizada para identificar fuentes de datos nutricionales adecuadas para el proyecto 'calories'. El objetivo es encontrar fuentes fiables, accesibles y con buena cobertura para obtener información detallada sobre la composición nutricional de diversos alimentos y productos.
"""

data_sources = [
    {
        'name': 'Open Food Facts',
        'description': 'Base de datos colaborativa sobre productos alimenticios con información nutricional.',
        'type': 'Base de datos, Pública',
        'cost': 'Gratis',
        'format': 'JSON, CSV',
        'coverage': 'Productos alimenticios de todo el mundo, incluyendo escaneo de códigos de barras.',
        'pros': [
            'Gran cantidad de datos aportados por la comunidad.',
            'API pública y fácil de usar.',
            'Cobertura internacional.',
            'Datos abiertos y gratuitos.'
        ],
        'cons': [
            'Calidad de datos variable debido a la entrada manual.',
            'Puede faltar información detallada para algunos productos.',
            'La estructura de datos puede ser inconsistente.'
        ],
        'links': [
            'https://world.openfoodfacts.org/',
            'https://wiki.openfoodfacts.org/API'
        ]
    },
    {
        'name': 'USDA FoodData Central',
        'description': 'Base de datos completa del Departamento de Agricultura de EE. UU. con información nutricional detallada.',
        'type': 'Base de datos, Pública',
        'cost': 'Gratis',
        'format': 'JSON, CSV, XML',
        'coverage': 'Alimentos básicos, productos de marca, datos de investigación y suplementos, principalmente de EE. UU.',
        'pros': [
            'Datos muy fiables y científicamente validados.',
            'Información nutricional detallada (hasta 150 nutrientes).',
            'Varias categorías de datos (SR Legacy, Foundation, FNDDS, Branded Foods, Survey).',
            'API disponible.'
        ],
        'cons': [
            'Principalmente enfocado en productos de EE. UU.',
            'La estructura de la base de datos puede ser compleja de entender inicialmente.',
            'Menos cobertura de productos de marca internacionales.'
        ],
        'links': [
            'https://fdc.nal.usda.gov/',
            'https://fdc.nal.usda.gov/api-guide.html'
        ]
    },
    {
        'name': 'Edamam Nutrition Analysis API',
        'description': 'API que permite analizar el contenido nutricional de recetas e ingredientes.',
        'type': 'API, Privada (con plan gratuito)',
        'cost': 'Plan gratuito limitado, suscripción de pago para mayor uso.',
        'format': 'JSON',
        'coverage': 'Ingredientes y recetas de todo el mundo.',
        'pros': [
            'Ideal para analizar recetas y texto libre de ingredientes.',
            'API bien documentada y fácil de integrar.',
            'Datos de alta calidad para ingredientes comunes.'
        ],
        'cons': [
            'El plan gratuito es muy limitado en número de peticiones.',
            'El costo de la suscripción puede ser elevado para proyectos grandes.',
            'Menos enfocado en productos específicos con código de barras.'
        ],
        'links': [
            'https://developer.edamam.com/nutrition-details-api',
            'https://developer.edamam.com/pricing'
        ]
    }
]

conclusion = """
Considerando los requisitos del proyecto 'calories', que probablemente necesite identificar productos específicos (quizás por código de barras) y tener una amplia cobertura internacional, **Open Food Facts** parece ser la fuente más adecuada como punto de partida. Su naturaleza colaborativa y su enfoque en productos de marca con códigos de barras la hacen ideal para una aplicación orientada al consumidor.

Aunque la calidad de los datos puede variar, la gran cantidad de productos disponibles y la API gratuita compensan esta limitación inicial.

Para obtener datos nutricionales más detallados y fiables sobre ingredientes básicos y alimentos genéricos, **USDA FoodData Central** es una excelente fuente complementaria, especialmente si el proyecto tiene un enfoque significativo en alimentos consumidos en EE. UU.

**Edamam** es muy útil para el análisis de recetas o texto libre de ingredientes, pero su modelo de costos basado en suscripción puede ser una barrera para un proyecto con un presupuesto limitado o un gran número de usuarios.

Por lo tanto, la recomendación inicial es integrar **Open Food Facts** como fuente principal de datos de productos y considerar **USDA FoodData Central** para datos de ingredientes básicos o como fuente secundaria si se necesita mayor fiabilidad científica en ciertos casos.
"""

# Build the Markdown content

markdown_content = "# Resumen de Investigación: Fuentes de Datos Nutricionales\n\n"

markdown_content += "## Introducción\n"
markdown_content += introduction.strip() + "\n\n"

markdown_content += "## Fuentes de Datos Identificadas\n\n"

for source in data_sources:
    markdown_content += f"### {source['name']}\n"
    markdown_content += f"- **Descripción:** {source['description']}\n"
    markdown_content += f"- **Tipo:** {source['type']}\n"
    markdown_content += f"- **Costo:** {source['cost']}\n"
    markdown_content += f"- **Formato de Datos:** {source['format']}\n"
    markdown_content += f"- **Cobertura:** {source['coverage']}\n"

    markdown_content += "- **Pros:**\n"
    if source['pros']:
        for pro in source['pros']:
            markdown_content += f"    - {pro}\n"
    else:
        markdown_content += "    - N/A\n"

    markdown_content += "- **Contras:**\n"
    if source['cons']:
        for con in source['cons']:
            markdown_content += f"    - {con}\n"
    else:
        markdown_content += "    - N/A\n"

    markdown_content += "- **Enlaces Relevantes:**\n"
    if source['links']:
        for link in source['links']:
            markdown_content += f"    - <{link}>\n" # Markdown auto-links URLs in angle brackets
    else:
        markdown_content += "    - N/A\n"
    markdown_content += "\n" # Add a blank line between sources

markdown_content += "## Conclusiones y Recomendaciones\n"
markdown_content += conclusion.strip() + "\n"

# Write the content to the Markdown file

file_name = "research_summary.md"

try:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    # print(f"Archivo '{file_name}' creado exitosamente.") # Removed print as per instructions
except IOError as e:
    # print(f"Error al escribir el archivo '{file_name}': {e}") # Removed print as per instructions
    pass # Handle error silently as per instructions (no output)