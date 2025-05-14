
import tkinter as tk
from tkinter import Tk, Canvas, Button
import random

class App:
    def __init__(self, Data):
        self.__Data = Data
        c = ["yellow", "blue", "green", "red"]
        self.__c = c
        root = tk.Tk()
        self.max_fils = 4
        self.max_croisements = 10
        self.__root = root
        self.__root.title("Mot dessinable")
        canvas = tk.Canvas(root, width=400, height=200, bg="white")
        self.__canvas = canvas
        canvas.grid(row=1, column=1, columnspan=3)
        Button(root, text="Quit", command=root.destroy).grid(row=2, column=1)
        Button(root, text="change la couleur", command=lambda: self.change_colour()).grid(row=2, column=3)
        Button(root, text="Tirer un entrelacs", command=self.random_entrelacs).grid(row=2, column=2)

    def read_word(self):
        for i in range(len(self.__Data.conversion())):
            x, y = 20, 20 + 20 * i  # position de départ
            for lettre in self.__Data.conversion()[i]:
                if lettre == "H":
                    x2, y2 = x + 20, y
                elif lettre == "U":
                    x2, y2 = x + 20, y - 20
                elif lettre == "D":
                    x2, y2 = x + 20, y + 20
                else:
                    continue
                line_id = self.__canvas.create_line(x, y, x2, y2, width=2, fill=self.__c[i])
                self.__canvas.tag_bind(line_id, '<Button-1>', lambda e, idx=i: self.simplifier_reidemeister(idx))
                x, y = x2, y2

    def redraw(self):
        self.__canvas.delete("all")
        self.read_word()

    def run_forever(self):
        self.__root.mainloop()

    def change_colour(self):
        for i in range(len(self.__c) - 1):
            self.__c[i], self.__c[i + 1] = self.__c[i + 1], self.__c[i]
        self.redraw()

    def random_entrelacs(self):
        t = [random.randint(0, self.max_fils - 2) for _ in range(self.max_croisements)]
        self.__Data = Data(t, self.max_fils)
        self.redraw()

    def simplifier_reidemeister(self, index):
        t = self.__Data.get_croisements()
        if index >= len(t):
            print("Indice hors limites")
            return

        fil = t[index]
        n = len(t)

        for j in range(index + 1, n):
            if t[j] == fil:
                autres = [k for k in range(index + 1, j) if t[k] == fil]
                if len(autres) == 0:
                    print(f"Simplification entre {index} et {j}")
                    new_t = t[:index] + t[index + 1:j] + t[j + 1:]
                    self.__Data = Data(new_t, self.__Data.get_nb_fils())
                    self.redraw()
                    return
                else:
                    print(f"Un autre croisement entre les mêmes fils se trouve entre {index} et {j}")
                    return

        print("Pas de mouvement de Reidemeister possible depuis cet indice")


class Data:
    def __init__(self, tcroisement, n):
        self.__t = tcroisement
        self.__n = n

    def conversion(self):
        l = ["H"] * self.__n
        d = {}
        for j in range(len(self.__t)):
            d[j] = j
        for i in range(len(self.__t)):
            l[d[self.__t[i]]] += "DH"
            l[d[self.__t[i] + 1]] += "UH"
            for k in range(len(l)):
                if k != d[self.__t[i]] and k != d[self.__t[i] + 1]:
                    l[k] += "HH"
            d[self.__t[i]], d[self.__t[i] + 1] = d[self.__t[i] + 1], d[self.__t[i]]
        return l

    def get_croisements(self):
        return self.__t

    def set_croisements(self, new_t):
        self.__t = new_t

    def get_nb_fils(self):
        return self.__n


if __name__ == "__main__":
    Data_instance = Data([2, 1, 1, 0, 2], 4)
    app = App(Data_instance)
    app.read_word()
    app.run_forever()
