import math
from tkinter import *
import numpy as np
from multiprocessing import Process, freeze_support
import time
import math

root = Tk()
root.geometry("1000x720")
canvas = Canvas(root, width=1000, height=720, bg="lightgrey")


class Pyramide:
    def poll(self):
        canvas.create_line(500, 1000, 500, 0, width=1, arrow=LAST)
        canvas.create_line(0, 500, 1000, 500, width=1, arrow=LAST)

    def down(self, a):
        for i in range(5):
            for j in range(2):
                if i < 3 and i >= 0:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2, dash=(4, 2))
                else:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2)

        canvas.create_line(a[0][0], a[0][1], a[5][0], a[5][1], width=2)

    def up(self, a):
        for i in range(6, 11):
            for j in range(2):
                var = canvas.create_line(a[i][j], a[i][j + 1], a[i + 1][j], a[i + 1][j + 1], width=2)
        canvas.create_line(a[6][0], a[6][1], a[11][0], a[11][1], width=2)

    def esle(self, a):
        for i in range(6):
            for j in range(2):
                if i < 3 and i > 0:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 6][j], a[i + 6][j + 1], width=2, dash=(4, 2))
                else:
                    canvas.create_line(a[i][j], a[i][j + 1], a[i + 6][j], a[i + 6][j + 1], width=2)


class Main():
    canvas.pack()
    m = 1
    x0 = 500
    y0 = 500
    X = Y = 1
    canvas.create_text(800, 10, fill="darkblue", font="Times 20 italic bold", text="Зрізана піраміда")
    h = np.array([[m, 0, 1],
                  [0, m, 1],
                  [X, Y, 1]])
    a = np.array([[x0, y0, 1],
                  [590.5, 410.5, 1],
                  [710.5, 410.5, 1],
                  [800.5, 500.5, 1],
                  [710.5, 590.5, 1],
                  [590.5, 590.5, 1],

                  [575.5, 300.5, 1],
                  [625.5, 255.5, 1],
                  [680.5, 255.5, 1],
                  [725.5, 300.5, 1],
                  [680.5, 345.5, 1],
                  [620.5, 345.5, 1]])
    a = a.dot(h)
    b = Pyramide()
    b.poll()
    b.esle(a)
    b.up(a)
    b.down(a)
    canvas.mainloop()
