import tkinter as tk
from tkinter import Tk, Canvas, Button
import numpy as np
from random import random

class graph:
    def __init__(self):
        root=tk.Tk()
        self.__root=root
        self.__graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
        self.__canvas = tk.Canvas(root, width=1000, height=600, bg="white")
        self.__canvas.grid(row=1, column=1)
        self.__pos = np.array([(np.random.randint(50,950), np.random.randint(50,550))
            for i in range(len(self.__graph))])
        self.__vit = np.array([((random()-0.5)*10, (random()-0.5)*10)
            for i in range(len(self.__graph))])
        self.__root.bind("<Key>", self.on_key_press)



    def run_forever(self):
        self.__root.mainloop()

    def draw(self):
        self.__canvas.delete("all")
        for i in range(len(self.__graph)):
            for j in self.__graph[i]:  # sucs de i a j
                self.__canvas.create_line(self.__pos[i][0], self.__pos[i][1], self.__pos[j][0], self.__pos[j][1])
        for (x, y) in self.__pos:
            self.__canvas.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")

    def on_key_press(self, event):
        if event.char == 'f':
            self.update_positions()
            self.draw()

    def update_positions(self):
        k = 0.01  # constante de raideur
        l0 = 50   # longueur idéale du ressort
        dt = 0.25    # durée d’un pas de temps
        forces = np.zeros_like(self.__pos, dtype=float) #initialise la liste des forces associé à chaque sommet
        for i, voisins in enumerate(self.__graph):
            for j in voisins:
                if i == j:
                    continue
                delta = self.__pos[j] - self.__pos[i]
                #écart des positions "l" entre les deux sommets pour calculer la force f=k*(l-l0)
                dist = np.linalg.norm(delta) #calcule la distance en faisant la norme de l'écart des positions
                if dist == 0:
                    continue
                direction = delta / dist #écart des positions sur la norme
                force = k * (dist - l0) * direction #f=k*(l-l0)
                forces[i] += force #on rajoute la nouvelle force
        for i, voisins in enumerate(self.__graph):
            delta_centre=self.__pos[i]-np.array([500,300])
            dist_centre=np.linalg.norm(delta_centre)
            direction_centre=delta_centre/dist_centre
            forces[i]=forces[i]-dist_centre*direction_centre/(2*np.pi)-k*self.__vit[i]
        for i in range(0,len(self.__graph)):
            for j in range(0,len(self.__graph)):
                if i==j:
                    continue
                delta = self.__pos[j] - self.__pos[i]
                dist = np.linalg.norm(delta)
                direction=delta/dist
                force[i]=force[i]+direction*5/(4*np.pi*dist**2)
        self.__vit += forces * dt #on met à jour la vitesse
        self.__pos = self.__pos + self.__vit * dt #on met à jour la position


if __name__ == "__main__":
    graph=graph()
    graph.draw()
    graph.run_forever()