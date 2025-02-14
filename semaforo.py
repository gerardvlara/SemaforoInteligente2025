import tkinter as tk
import random

class SemaforoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semáforo Inteligente en Tiempo Real")

     
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()


        self.red_light_1 = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.yellow_light_1 = self.canvas.create_oval(50, 160, 150, 260, fill="gray")
        self.green_light_1 = self.canvas.create_oval(50, 270, 150, 370, fill="gray")

        self.red_light_2 = self.canvas.create_oval(250, 50, 350, 150, fill="gray")
        self.yellow_light_2 = self.canvas.create_oval(250, 160, 350, 260, fill="gray")
        self.green_light_2 = self.canvas.create_oval(250, 270, 350, 370, fill="gray")

        self.current_light = {"lane_1": "red", "lane_2": "red"}
        self.vehicles_lane_1 = 0
        self.vehicles_lane_2 = 0


        self.update_vehicle_count()
        self.update_lights()

    def update_vehicle_count(self):
    
        self.vehicles_lane_1 = random.randint(0, 10)  
        self.vehicles_lane_2 = random.randint(0, 10)  
        print(f"Vehículos en carril 1: {self.vehicles_lane_1}, Vehículos en carril 2: {self.vehicles_lane_2}")


        self.root.after(5000, self.update_vehicle_count)

    def update_lights(self):

        if self.vehicles_lane_1 >= self.vehicles_lane_2:
            self.set_lights("lane_1", "green")
            self.set_lights("lane_2", "red")
        else:
            self.set_lights("lane_2", "green")
            self.set_lights("lane_1", "red")

        self.root.after(5000, self.update_lights)

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