Semáforo Inteligente con Recursión

Descripción del Problema

Los semáforos tradicionales operan con ciclos de luces (verde, amarillo, rojo) en intervalos de tiempo definidos. Sin embargo, si la programación del semáforo se implementa usando un bucle infinito (while True) y pausas (time.sleep()), la interfaz gráfica (GUI) se congela y no responde correctamente.

Solución Implementada

Para evitar este problema, el programa utiliza recursión en combinación con Tkinter.after(). Esto permite que la interfaz siga respondiendo mientras el semáforo cambia de estado sin bloquear la ejecución.

Técnica Usada

Se reemplazó while True por una llamada recursiva que cambia el estado del semáforo sin bloquear la UI.

Se utiliza after() para ejecutar cambios de estado en intervalos de tiempo definidos.

Se gestiona la concurrencia con un semafóro (threading.Semaphore) para controlar el acceso a los cambios de luz.

Proyecto Final: Semáforo Inteligente en Tiempo Real

Este proyecto simula un semáforo inteligente que alterna entre dos carriles utilizando programación concurrente, sincronización y manejo de eventos con Python y Tkinter. Forma parte del examen final del curso (Unidades 8-14).

Temas Aplicados

- Programación concurrente con `threading`
- Sincronización con `Semaphore`
- Manejo de eventos con `after()` en Tkinter
- Excepciones y robustez del sistema
- Interfaz gráfica en tiempo real

Requisitos

- Python 3.x
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

Cómo ejecutar

Clona este repositorio o descarga el archivo:

```bash
git clone https://github.com/tu-usuario/semaforo-inteligente.git
cd semaforo-inteligente
python semaforo.py
```
