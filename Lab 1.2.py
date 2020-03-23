import math
from tkinter import *
import numpy as np
from multiprocessing import Process, freeze_support
import time
import math
import random

root = Tk()
root.geometry("1000x720")
canvas = Canvas(root, width=1000, height=720, bg="lightgrey")


class Pyramide:
    def poll(self):
        canvas.create_line(500, 1000, 500, 0, width=1, arrow=LAST)
        canvas.create_line(0, 500, 1000, 500, width=1, arrow=LAST)

    def down(self, a, n):
        for i in range(5):
            for j in range(2):
                if i < 3 and i >= 0:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2, dash=(4, 2), fill=n)
                else:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2, fill=n)

        canvas.create_line(a[0][0], a[0][1], a[5][0], a[5][1], width=2, fill=n)

    def up(self, a, n):
        for i in range(6, 11):
            for j in range(2):
                var = canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2, fill=n)
        canvas.create_line(a[6][0], a[6][1], a[11][0], a[11][1], width=2, fill=n)

    def esle(self, a, n):
        for i in range(6):
            for j in range(2):
                if i < 3 and i > 0:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 6][j], a[i + 6][j + 1], width=2, dash=(4, 2), fill=n)
                else:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 6][j], a[i + 6][j + 1], width=2, fill=n)


class Main():
    canvas.pack()
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    for i in range(5):
        n = random.choice(color)
        m = random.random()
        x0 = random.randint(400, 600)
        y0 = random.randint(400, 700)
        X = Y = 1
        h = np.array([[m, 0, 1],
                      [0, m, 1],
                      [random.random() * 100, random.random() * 100, 1]])
        a = np.array([[x0, y0, 1],
                      [x0 + 90.5, y0 - 89.5, 1],
                      [x0 + 210.5, y0 - 89.5, 1],
                      [x0 + 300.5, y0 + 1.5, 1],
                      [x0 + 210.5, y0 + 90.5, 1],
                      [x0 + 90.5, y0 + 90.5, 1],

                      [x0 + 75.5, y0 - 199.5, 1],
                      [x0 + 125.5, y0 - 244.5, 1],
                      [x0 + 180.5, y0 - 244.5, 1],
                      [x0 + 225.5, y0 - 199.5, 1],
                      [x0 + 180.5, y0 - 154.5, 1],
                      [x0 + 120.5, y0 - 154.5, 1]])
        a = a.dot(h)
        b = Pyramide()
        canvas.create_text(800, 10, fill="darkblue", font="Times 20 italic bold", text="Зрізана піраміда")
        b.poll()
        b.esle(a, n)
        b.up(a, n)
        b.down(a, n)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
    canvas.mainloop()
