Semáforo Inteligente con Recursión

Descripción del Problema

Los semáforos tradicionales operan con ciclos de luces (verde, amarillo, rojo) en intervalos de tiempo definidos. Sin embargo, si la programación del semáforo se implementa usando un bucle infinito (while True) y pausas (time.sleep()), la interfaz gráfica (GUI) se congela y no responde correctamente.

Solución Implementada

Para evitar este problema, el programa utiliza recursión en combinación con Tkinter.after(). Esto permite que la interfaz siga respondiendo mientras el semáforo cambia de estado sin bloquear la ejecución.

Técnica Usada

Se reemplazó while True por una llamada recursiva que cambia el estado del semáforo sin bloquear la UI.

Se utiliza after() para ejecutar cambios de estado en intervalos de tiempo definidos.

Se gestiona la concurrencia con un semafóro (threading.Semaphore) para controlar el acceso a los cambios de luz.

