import math
from tkinter import *
import numpy as np
from multiprocessing import Process, freeze_support
import time
import math

root = Tk()
canvas = Canvas(root, width=1000, height=1000, bg="lightgrey")


class Pyramide:
    def Drawline(self, x1, y1, x2, y2):
        h, w = 500, 500
        canvas.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            # fill=self.fg_color,
            # dash=(20, 40)
        )

    def poll(self, a):
        canvas.create_line(500, 1000, 500, 0, width=1, arrow=LAST)
        canvas.create_line(0, 500, 1000, 500, width=1, arrow=LAST)

    def down(self, a):
        i = 0
        for j in range(2):
            self.Drawline(a[i][j], a[i + 1][j], a[i][j + 1], a[i + 1][j + 1])
        self.Drawline(a[0][2], a[1][2], a[0][0], a[1][0])

    def up(self, a):
        i = 0
        for j in range(3, 5):
            self.Drawline(a[i][j], a[i + 1][j], a[i][j + 1], a[i + 1][j + 1])
        self.Drawline(a[0][5], a[1][5], a[0][3], a[1][3])

    def esle(self, a):
        i = 0
        for j in range(3):
            self.Drawline(a[i][j], a[i + 1][j], a[i][j + 3], a[i + 1][j + 3])

    def MoveForward(self, a, m):
        b = np.array([[1, 0, 0],
                      [0, math.cos(m * 0.01), -math.sin(m * 0.01)],
                      [0, math.sin(m * 0.01), math.cos(m * 0.01)]])
        # b = np.array([[0.5, 0, 0],
        #               [0, 0.5, 0],
        #               [0, 0, 0]])
        a = b.dot(a)
        # self.poll(a)
        self.down(a)
        self.up(a)
        self.esle(a)

    def Move(self, k, a):
        for i in range(1, k):
            canvas.delete("all")
            # X += X
            # Y += Y
            canvas.create_text(800, 10, fill="darkblue", font="Times 20 italic bold", text="Зрізана піраміда, обертання по Х")
            self.MoveForward(a, i)
            root.update_idletasks()
            root.update()
        canvas.mainloop()


class Main():
    canvas.pack()
    b = Pyramide()
    x0 = 500
    y0 = 500
    z0 = 1
    a = np.array([[0, 0, 400, 100, 100, 500],
                  [0, 400, 100, 100, 500, 200],
                  [100, 0, 200, 500, 400, 600]])
    b.Move(3600, a)
