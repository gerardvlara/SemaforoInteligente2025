import tkinter as tk
import random
import threading
from threading import Semaphore

class SemaforoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Semáforo con Recursión")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        
        self.red_light_1 = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.yellow_light_1 = self.canvas.create_oval(50, 160, 150, 260, fill="gray")
        self.green_light_1 = self.canvas.create_oval(50, 270, 150, 370, fill="gray")

        self.red_light_2 = self.canvas.create_oval(250, 50, 350, 150, fill="gray")
        self.yellow_light_2 = self.canvas.create_oval(250, 160, 350, 260, fill="gray")
        self.green_light_2 = self.canvas.create_oval(250, 270, 350, 370, fill="gray")

        self.current_state = "lane_1_green"
        self.vehicles_lane_1 = 0
        self.vehicles_lane_2 = 0

        self.semaphore = Semaphore(1)

        self.update_vehicle_count()
        self.update_semaphore_state()

    def update_vehicle_count(self):
        
        self.vehicles_lane_1 = random.randint(0, 10)
        self.vehicles_lane_2 = random.randint(0, 10)
        print(f"Vehículos en carril 1: {self.vehicles_lane_1}, Vehículos en carril 2: {self.vehicles_lane_2}")
        self.root.after(5000, self.update_vehicle_count)  # Se ejecuta cada 5 segundos

    def update_semaphore_state(self):
        # Método recursivo que controla el semáforo
        self.semaphore.acquire()
        try:
            if self.current_state == "lane_1_green":
                self.set_lights("lane_1", "green")
                self.set_lights("lane_2", "red")
                self.root.after(3000, self.next_state)
            elif self.current_state == "lane_1_yellow":
                self.set_lights("lane_1", "yellow")
                self.root.after(2000, self.next_state)
            elif self.current_state == "lane_2_green":
                self.set_lights("lane_2", "green")
                self.set_lights("lane_1", "red")
                self.root.after(3000, self.next_state)
            elif self.current_state == "lane_2_yellow":
                self.set_lights("lane_2", "yellow")
                self.root.after(2000, self.next_state)
        finally:
            self.semaphore.release()

    def next_state(self):
        
        if self.current_state == "lane_1_green":
            self.current_state = "lane_1_yellow"
        elif self.current_state == "lane_1_yellow":
            self.current_state = "lane_2_green"
        elif self.current_state == "lane_2_green":
            self.current_state = "lane_2_yellow"
        elif self.current_state == "lane_2_yellow":
            self.current_state = "lane_1_green"
        
        self.update_semaphore_state()

    def set_lights(self, lane, color):
        
        if lane == "lane_1":
            self.canvas.itemconfig(self.red_light_1, fill="red" if color == "red" else "gray")
            self.canvas.itemconfig(self.yellow_light_1, fill="yellow" if color == "yellow" else "gray")
            self.canvas.itemconfig(self.green_light_1, fill="green" if color == "green" else "gray")
        elif lane == "lane_2":
            self.canvas.itemconfig(self.red_light_2, fill="red" if color == "red" else "gray")
            self.canvas.itemconfig(self.yellow_light_2, fill="yellow" if color == "yellow" else "gray")
            self.canvas.itemconfig(self.green_light_2, fill="green" if color == "green" else "gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoApp(root)
    root.mainloop()
