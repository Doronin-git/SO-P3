import tkinter as tk

SCALE = 0.2       # коэффициент масштабирования памяти
HEIGHT = 50       # высота прямоугольника

class Visualizer:
    def __init__(self): #setting
        self.root = tk.Tk()
        self.root.title("Memory Visualizer")
        self.canvas = tk.Canvas(self.root, width=450, height=80, bg="white")
        self.canvas.pack()
        self.SCALE = 0.2

    def draw(self, segments): # drawing for every tick
        self.canvas.delete("all")
        x = 10
        for seg in segments:
            w = seg.size * self.SCALE
            color = "lightgreen" if seg.state == "free" else "orange"

            self.canvas.create_rectangle(x, 10, x+w, 60, fill=color)
            self.canvas.create_text(x + w/2, 35, text=seg.state)
            x += w

        self.canvas.update()