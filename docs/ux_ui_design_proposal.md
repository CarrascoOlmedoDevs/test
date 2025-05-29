import sys

def generate_ux_ui_documentation():
    """
    Genera documentación UX/UI en formato Markdown para un juego de soccer manager.
    """
    doc = "# Documentación UX/UI: Soccer Manager\n\n"
    doc += "Este documento describe las pantallas principales, la información clave y los flujos de navegación básicos para el juego Soccer Manager.\n\n"

    # --- Pantallas Principales ---
    doc += "## Pantallas Principales\n\n"
    doc += "El juego se estructura alrededor de varias pantallas principales accesibles desde un menú de navegación persistente (barra lateral o superior).\n\n"

    screens = {
        "Menú Principal": {
            "description": "Pantalla de inicio y resumen rápido.",
            "key_info": [
                "Noticias recientes del club y la liga",
                "Próximo partido",
                "Estado financiero resumido",
                "Acceso rápido a secciones clave (Plantilla, Tácticas, etc.)"
            ]
        },
        "Plantilla": {
            "description": "Gestión de jugadores del equipo.",
            "key_info": [
                "Lista de jugadores (nombre, posición, edad, valor, estado físico, moral)",
                "Detalle del jugador (estadísticas, historial, contrato)",
                "Opciones de gestión (vender, comprar, entrenar, renovar contrato)"
            ]
        },
        "Tácticas": {
            "description": "Configuración de la formación y estrategia del equipo.",
            "key_info": [
                "Selector de formación (ej. 4-4-2, 4-3-3)",
                "Asignación de jugadores a posiciones",
                "Instrucciones del equipo (presión, estilo de pase, mentalidad)",
                "Instrucciones individuales para jugadores clave"
            ]
        },
        "Calendario": {
            "description": "Visualización de partidos y eventos futuros y pasados.",
            "key_info": [
                "Lista de partidos por mes/temporada",
                "Resultados de partidos pasados",
                "Fechas de eventos clave (transferencias, entrenamientos especiales)"
            ]
        },
        "Finanzas": {
            "description": "Gestión económica del club.",
            "key_info": [
                "Ingresos y gastos detallados (salarios, traspasos, taquilla, patrocinios)",
                "Presupuesto de traspasos y salarios",
                "Balance general",
                "Patrocinios y acuerdos comerciales"
            ]
        },
        "Mercado de Traspasos": {
            "description": "Compra y venta de jugadores.",
            "key_info": [
                "Lista de jugadores disponibles para comprar/vender",
                "Ofertas recibidas por jugadores propios",
                "Realización de ofertas por jugadores de otros clubes",
                "Jugadores libres"
            ]
        },
         "Competiciones": {
            "description": "Información sobre las ligas y copas.",
            "key_info": [
                "Clasificaciones de liga",
                "Calendarios y resultados de competiciones",
                "Estadísticas de jugadores y equipos en competiciones"
            ]
        }
    }

    for screen, details in screens.items():
        doc += f"### {screen}\n\n"
        doc += f"{details['description']}\n\n"
        doc += "Información Clave:\n"
        for item in details['key_info']:
            doc += f"- {item}\n"
        doc += "\n"

    # --- Flujos de Navegación Básicos ---
    doc += "## Flujos de Navegación Básicos\n\n"
    doc += "La navegación principal se realiza a través de un menú persistente (ej. barra lateral) visible en la mayoría de las pantallas.\n\n"
    doc += "Ejemplos de flujos comunes:\n\n"

    flows = [
        "Menú Principal -> Plantilla (para ver el equipo)",
        "Menú Principal -> Tácticas (para ajustar la estrategia)",
        "Menú Principal -> Calendario (para ver el próximo partido)",
        "Plantilla -> Detalle de Jugador (seleccionar un jugador de la lista)",
        "Detalle de Jugador -> Mercado de Traspasos (opción para vender/comprar similar)",
        "Calendario -> Partido Específico (para ver detalles/resultado)",
        "Menú Principal -> Finanzas (para revisar el estado económico)",
        "Menú Principal -> Mercado de Traspasos (para buscar jugadores)",
        "Mercado de Traspasos -> Detalle de Jugador (seleccionar un jugador del mercado)",
        "Menú Principal -> Competiciones (para ver clasificaciones)"
    ]

    for flow in flows:
        doc += f"- {flow}\n"

    doc += "\n\nLa mayoría de las pantallas también tendrán un botón 'Atrás' o una forma de regresar a la pantalla anterior o al Menú Principal."

    return doc

if __name__ == "__main__":
    documentation = generate_ux_ui_documentation()
    print(documentation)