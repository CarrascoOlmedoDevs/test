def generate_android_step_counter_architecture_markdown():
    """
    Genera un documento Markdown que describe la arquitectura propuesta
    para una aplicación de conteo de pasos en Android.
    """
    markdown_content = """
# Arquitectura de Aplicación Android: Contador de Pasos

Este documento describe la arquitectura propuesta para una aplicación de conteo de pasos en Android, enfocándose en la gestión de sensores, ejecución en segundo plano, almacenamiento de datos y comunicación entre componentes.

## 1. Gestión de Sensores

La aplicación utilizará el sistema de sensores de Android para detectar y contar los pasos del usuario.

-   **Acceso al Sensor:** Se accederá a los sensores de pasos a través de la clase `SensorManager`. Los sensores clave son:
    -   `TYPE_STEP_COUNTER`: Proporciona el número total de pasos desde que el dispositivo se reinició por última vez. Es persistente a través de reinicios del sensor, pero no del dispositivo. Es ideal para obtener un conteo acumulado.
    -   `TYPE_STEP_DETECTOR`: Dispara un evento cada vez que se detecta un paso. Es útil para detectar pasos individuales en tiempo real, pero no proporciona un conteo acumulado.
    -   Se priorizará el uso de `TYPE_STEP_COUNTER` para el conteo diario, registrando el valor inicial al comienzo del día y calculando la diferencia con el valor actual. `TYPE_STEP_DETECTOR` podría usarse como fallback o para funcionalidades adicionales (ej. retroalimentación háptica por paso).
-   **SensorManager y SensorEventListener:** Se obtendrá una instancia de `SensorManager` y se registrará un `SensorEventListener` para escuchar los eventos del sensor (`onSensorChanged`).
-   **Permisos:** Se requerirá el permiso `com.google.android.gms.permission.ACTIVITY_RECOGNITION` (o `android.permission.ACTIVITY_RECOGNITION` en Android 10+). Este permiso debe ser solicitado al usuario en tiempo de ejecución si la versión de Android lo requiere.
-   **Compatibilidad:** Se verificará la disponibilidad de los sensores `TYPE_STEP_COUNTER` o `TYPE_STEP_DETECTOR` en el dispositivo utilizando `SensorManager.getDefaultSensor()`. Si ninguno está disponible, la aplicación informará al usuario o deshabilitará la funcionalidad de conteo de pasos. Se considerarán posibles diferencias en la precisión y el comportamiento entre fabricantes de dispositivos.

## 2. Servicio en Segundo Plano

El conteo de pasos debe continuar incluso si la aplicación principal no está visible. Esto requiere un servicio que se ejecute de forma continua.

-   **Implementación:** Se creará un `Service` que se iniciará al arrancar la aplicación o al iniciar el conteo.
-   **Foreground Service:** Para garantizar que el servicio no sea terminado por el sistema operativo debido a restricciones de batería o memoria, se implementará como un `Foreground Service`. Esto requiere:
    -   Llamar a `startForeground()` dentro del servicio.
    -   Proporcionar una `Notification` persistente que informe al usuario que el servicio está en ejecución (ej. mostrando el conteo de pasos actual o un mensaje informativo).
    -   Declarar el permiso `android.permission.FOREGROUND_SERVICE` en el `AndroidManifest.xml`.
    -   En Android 12+, se requerirá un `foregroundServiceType` apropiado (ej. `health`).
-   **Registro del Listener:** El `SensorEventListener` se registrará dentro del servicio, no en una actividad.
-   **Manejo de Reinicios:** El servicio debe ser capaz de reiniciarse automáticamente si el dispositivo se reinicia. Esto se puede lograr utilizando un `BroadcastReceiver` que escuche la acción `ACTION_BOOT_COMPLETED` y reinicie el servicio.

## 3. Almacenamiento de Datos

Se necesita una estrategia para almacenar el conteo de pasos diario y, opcionalmente, un historial.

-   **Conteo Diario Actual:** El conteo de pasos para el día actual puede almacenarse de forma eficiente en `SharedPreferences`. Se guardaría el valor del `TYPE_STEP_COUNTER` al inicio del día (o la última vez que se registró un paso ese día) y se calcularía la diferencia con el valor actual para obtener los pasos del día. `SharedPreferences` es adecuado para datos clave-valor simples y persistentes.
-   **Historial Diario:** Para almacenar un historial de conteos diarios (fecha y pasos), se utilizará una base de datos local. **Room Database** es la solución recomendada por Android, ya que es una capa de abstracción sobre SQLite que simplifica la creación y gestión de bases de datos.
    -   Se definirá una entidad `DailySteps` con campos como `date` (clave primaria) y `steps`.
    -   Se creará un `DAO` (Data Access Object) para realizar operaciones de inserción, consulta y actualización.
    -   Se implementará la lógica para guardar el conteo diario al final del día (ej. usando `AlarmManager` para programar una tarea nocturna) o al detectar el cambio de día.
-   **Persistencia del Sensor:** El valor de `TYPE_STEP_COUNTER` es persistente a través de reinicios del sensor, pero no del dispositivo. Al reiniciar el dispositivo, el sensor `TYPE_STEP_COUNTER` se reseteará a 0. La aplicación debe manejar esto:
    -   Al iniciar el servicio (especialmente después de un reinicio del dispositivo), se debe obtener el valor actual del `TYPE_STEP_COUNTER` y almacenarlo (ej. en `SharedPreferences`) como el "valor base" para el día actual. Los pasos del día se calcularán como `current_value - base_value`.
    -   Si el dispositivo se reinicia a mitad del día, el nuevo valor base será 0, y el conteo continuará desde 0. La aplicación podría intentar estimar los pasos perdidos si fuera necesario (lo cual es complejo y a menudo no se hace) o simplemente aceptar la pérdida de datos para ese día. La estrategia más común es simplemente resetear el conteo diario al valor base del sensor después del reinicio.

## 4. Comunicación entre Componentes

Se establecerán mecanismos para que el servicio, la UI y el almacenamiento interactúen.

-   **Servicio a UI:**
    -   **Broadcasts Locales:** El servicio puede enviar `LocalBroadcast`s con el conteo de pasos actualizado periódicamente o cada vez que cambie significativamente. La actividad principal (UI) puede registrar un `BroadcastReceiver` para escuchar estos eventos y actualizar la interfaz.
    -   **Bound Service:** La actividad podría "enlazar" (`bind`) al servicio para llamar directamente a métodos públicos del servicio (ej. `getStepsToday()`). Esto es útil cuando la UI está activa, pero `Broadcasts` son mejores para actualizaciones cuando la UI no está en primer plano pero podría volverse activa en cualquier momento.
    -   **ViewModel y LiveData:** En una arquitectura MVVM, el servicio podría actualizar un repositorio, que a su vez actualiza un `LiveData` observado por el `ViewModel` de la actividad. Esta es una forma limpia y moderna de gestionar el flujo de datos.
-   **UI a Servicio:**
    -   La actividad principal puede iniciar (`startService()`) o detener (`stopService()`) el servicio.
    -   Puede enviar comandos al servicio a través de `Intents` (ej. `intent.putExtra("command", "reset_steps")`).
-   **Servicio/UI a Almacenamiento:**
    -   El servicio (para el conteo diario persistente y el guardado nocturno) y potencialmente la UI (para consultar el historial) accederán a la base de datos Room a través del `DAO`.
    -   Se recomienda el uso de un `Repository` como capa intermedia entre el `ViewModel`/Servicio y el `DAO` para abstraer la fuente de datos.
    -   Las operaciones de base de datos deben realizarse fuera del hilo principal (ej. usando Coroutines, RxJava o `AsyncTask` - aunque obsoleto).

Esta arquitectura proporciona una base robusta para una aplicación de conteo de pasos que opera de manera confiable en segundo plano y gestiona los datos de manera persistente.
"""
    print(markdown_content)

if __name__ == "__main__":
    generate_android_step_counter_architecture_markdown()