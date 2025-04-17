import tkinter as tk
import random
import threading
from threading import Semaphore

class SemaforoApp:
    """
    Clase principal que representa una aplicación de semáforo inteligente con GUI.
    Utiliza tkinter para la interfaz gráfica, programación concurrente con threading,
    y sincronización con semáforos (Semaphore) para alternar el control de luces
    de dos carriles en función del número de vehículos.
    """
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica, los semáforos visuales, el estado inicial
        del sistema, y lanza los procesos periódicos de actualización.
        """
        self.root = root
        self.root.title("Proyecto Semáforo con Recursión")

        # Crear un lienzo donde se dibujarán los semáforos
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        # Crear las luces del carril 1
        self.red_light_1 = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.yellow_light_1 = self.canvas.create_oval(50, 160, 150, 260, fill="gray")
        self.green_light_1 = self.canvas.create_oval(50, 270, 150, 370, fill="gray")

        # Crear las luces del carril 2
        self.red_light_2 = self.canvas.create_oval(250, 50, 350, 150, fill="gray")
        self.yellow_light_2 = self.canvas.create_oval(250, 160, 350, 260, fill="gray")
        self.green_light_2 = self.canvas.create_oval(250, 270, 350, 370, fill="gray")

        # Estado inicial del semáforo
        self.current_state = "lane_1_green"
        self.vehicles_lane_1 = 0
        self.vehicles_lane_2 = 0

        # Semáforo de sincronización para evitar condiciones de carrera
        self.semaphore = Semaphore(1)

        # Iniciar procesos periódicos
        self.update_vehicle_count()
        self.update_semaphore_state()

    def update_vehicle_count(self):
        """
        Actualiza aleatoriamente el número de vehículos en cada carril cada 5 segundos.
        Se maneja con una excepción en caso de error para mantener la ejecución continua.
        """
        try:
            self.vehicles_lane_1 = random.randint(0, 10)
            self.vehicles_lane_2 = random.randint(0, 10)
            print(f"Vehículos en carril 1: {self.vehicles_lane_1}, Vehículos en carril 2: {self.vehicles_lane_2}")
            self.root.after(5000, self.update_vehicle_count)  # Llama a sí mismo cada 5s
        except Exception as e:
            print(f"Error al actualizar la cantidad de vehículos: {e}")
            self.root.after(5000, self.update_vehicle_count)

    def update_semaphore_state(self):
        """
        Controla el estado del semáforo para ambos carriles de forma alternada.
        Utiliza un semáforo (Semaphore) para evitar colisiones al cambiar de estado.
        """
        try:
            self.semaphore.acquire()  # Bloqueo para evitar condiciones de carrera
            try:
                if self.current_state == "lane_1_green":
                    self.set_lights("lane_1", "green")
                    self.set_lights("lane_2", "red")
                    self.root.after(3000, self.next_state)  # Espera 3s

                elif self.current_state == "lane_1_yellow":
                    self.set_lights("lane_1", "yellow")
                    self.root.after(2000, self.next_state)  # Espera 2s

                elif self.current_state == "lane_2_green":
                    self.set_lights("lane_2", "green")
                    self.set_lights("lane_1", "red")
                    self.root.after(3000, self.next_state)

                elif self.current_state == "lane_2_yellow":
                    self.set_lights("lane_2", "yellow")
                    self.root.after(2000, self.next_state)
            finally:
                self.semaphore.release()
        except Exception as e:
            print(f"Error al actualizar el estado del semáforo: {e}")

    def next_state(self):
        """
        Define la lógica de transición entre los diferentes estados del semáforo.
        Llama nuevamente a la función de actualización para continuar el ciclo.
        """
        try:
            if self.current_state == "lane_1_green":
                self.current_state = "lane_1_yellow"
            elif self.current_state == "lane_1_yellow":
                self.current_state = "lane_2_green"
            elif self.current_state == "lane_2_green":
                self.current_state = "lane_2_yellow"
            elif self.current_state == "lane_2_yellow":
                self.current_state = "lane_1_green"

            self.update_semaphore_state()
        except Exception as e:
            print(f"Error al cambiar de estado: {e}")

    def set_lights(self, lane, color):
        """
        Cambia el color de las luces del semáforo en el carril indicado.

        Parámetros:
        - lane (str): 'lane_1' o 'lane_2'
        - color (str): 'red', 'yellow' o 'green'
        """
        try:
            if lane == "lane_1":
                self.canvas.itemconfig(self.red_light_1, fill="red" if color == "red" else "gray")
                self.canvas.itemconfig(self.yellow_light_1, fill="yellow" if color == "yellow" else "gray")
                self.canvas.itemconfig(self.green_light_1, fill="green" if color == "green" else "gray")
            elif lane == "lane_2":
                self.canvas.itemconfig(self.red_light_2, fill="red" if color == "red" else "gray")
                self.canvas.itemconfig(self.yellow_light_2, fill="yellow" if color == "yellow" else "gray")
                self.canvas.itemconfig(self.green_light_2, fill="green" if color == "green" else "gray")
        except Exception as e:
            print(f"Error al configurar las luces: {e}")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoApp(root)
    root.mainloop()

