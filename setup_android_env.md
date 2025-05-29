import os

def create_setup_android_env_markdown():
    """
    Creates a markdown file with instructions to set up an Android development environment.
    """
    markdown_content = """# Configuración del Entorno de Desarrollo Android

Este documento describe los pasos necesarios para configurar un entorno de desarrollo Android utilizando Android Studio, incluyendo la instalación del SDK y la verificación de dependencias.

## 1. Instalar Android Studio

Android Studio es el IDE oficial para el desarrollo de Android. Incluye todo lo necesario para empezar.

1.  **Descargar Android Studio:**
    Dirígete al sitio oficial de Android Developer y descarga la última versión de Android Studio para tu sistema operativo (Windows, macOS, Linux).
    [Descargar Android Studio](https://developer.android.com/studio)

2.  **Ejecutar el instalador:**
    Sigue las instrucciones del instalador. Se recomienda aceptar las configuraciones por defecto a menos que tengas una razón específica para cambiarlas. Asegúrate de que la opción para instalar el Android SDK esté seleccionada.

## 2. Configurar el Android SDK

El Android SDK (Software Development Kit) contiene las herramientas, plataformas y APIs necesarias para desarrollar aplicaciones Android.

1.  **Abrir el SDK Manager:**
    Una vez instalado Android Studio, ábrelo. En la pantalla de bienvenida o desde el menú `File > Settings` (Windows/Linux) o `Android Studio > Preferences` (macOS), busca y abre el **SDK Manager**.

2.  **Pestaña "SDK Platforms":**
    -   Selecciona la(s) versión(es) de Android (API level) para la(s) cual(es) deseas desarrollar. Generalmente, es bueno tener la última versión estable y quizás un par de versiones anteriores para asegurar compatibilidad.
    -   Haz clic en "Apply" para descargar e instalar las plataformas seleccionadas.

3.  **Pestaña "SDK Tools":**
    -   Asegúrate de que las siguientes herramientas estén instaladas (o selecciónalas para instalar):
        -   `Android SDK Build-Tools` (Generalmente se instala una versión compatible automáticamente)
        -   `Android SDK Platform-Tools`
        -   `Android SDK Command-line Tools (latest)`
        -   `CMake` y `NDK (Side by side)` si planeas desarrollar con código nativo (C/C++).
        -   `Android Emulator` (Si deseas usar emuladores virtuales).
        -   `Intel HAXM` (para aceleración de emulador en procesadores Intel en Windows/macOS) o `KVM` (en Linux).
    -   Haz clic en "Apply" para descargar e instalar las herramientas seleccionadas.

4.  **Configurar variables de entorno (Opcional pero recomendado):**
    Añade la ruta al directorio `platform-tools` del SDK a la variable de entorno `PATH` de tu sistema. Esto te permitirá usar herramientas como `adb` (Android Debug Bridge) desde cualquier terminal.
    -   La ubicación por defecto del SDK suele ser `C:\\Users\\YourUsername\\AppData\\Local\\Android\\sdk` en Windows, `~/Library/Android/sdk` en macOS, o `~/Android/sdk` en Linux.
    -   La ruta a añadir sería `<sdk_path>/platform-tools`.

    Verifica ejecutando `adb --version` en una nueva terminal.

## 3. Verificar Dependencias (Gradle)

Gradle es el sistema de construcción utilizado por Android Studio. Viene incluido con Android Studio y no suele requerir una instalación separada para proyectos estándar.

1.  **Verificar la instalación de Gradle:**
    Cuando creas o abres un proyecto Android en Android Studio, este descargará automáticamente la versión de Gradle necesaria para el proyecto si no está ya en caché.
    No necesitas instalar Gradle globalmente a menos que tengas un caso de uso específico (por ejemplo, construir desde la línea de comandos sin Android Studio).

2.  **Verificar la versión de Gradle en un proyecto:**
    En un proyecto Android, puedes encontrar la configuración de Gradle en el archivo `gradle/wrapper/gradle-wrapper.properties`. Este archivo especifica la versión de Gradle que debe usar el proyecto.

3.  **Construir un proyecto de ejemplo:**
    La mejor manera de verificar que todo funciona es crear un nuevo proyecto básico en Android Studio y intentar construirlo y ejecutarlo en un emulador o dispositivo conectado. Si la construcción se completa sin errores, Gradle y el SDK están configurados correctamente para ese proyecto.

## Enlaces Útiles

*   [Documentación oficial de Android Developer](https://developer.android.com/)
*   [Guía de instalación de Android Studio](https://developer.android.com/studio/install)
*   [Configurar el SDK de Android](https://developer.android.com/studio/intro/update#sdk-manager)
*   [Guía de usuario de Gradle (para Android)](https://developer.android.com/build/gradle-build-system)

"""

    file_path = 'setup_android_env.md'

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Archivo '{file_path}' creado exitosamente.")
    except IOError as e:
        print(f"Error al escribir en el archivo '{file_path}': {e}")

if __name__ == "__main__":
    create_setup_android_env_markdown()