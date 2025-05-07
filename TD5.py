import tkinter as tk
from tkinter import Tk,Canvas,Button

## Exo 1
colour=["yellow","blue","green","red"]
def read_word(canvas, l, h, w,c):
    for i in range(0,len(l)):
        x, y = 20, 20+20*i  # position de départ
        for lettre in l[i]:
            if lettre == "H":
                x2, y2 = x + w, y
            elif lettre == "U":
                x2, y2 = x + w, y - h
            elif lettre == "D":
                x2, y2 = x + w, y + h
            else:
                continue  # ignore tout caractère non reconnu
            canvas.create_line(x, y, x2, y2, width=2, fill=colour[i])
            x, y = x2, y2  # mise à jour de la position


## Exo 2+3+4+5

def conversion(t,n):
    l=["H"]*n
    d={}
    for j in range(0,len(t)):
        d[j]=j
    for i in range (0,len(t)):
        l[d[t[i]]]=l[d[t[i]]]+"DH"
        l[d[t[i]+1]]=l[d[t[i]+1]]+"UH"
        for k in range (0,len(l)):
            if k!=d[t[i]] and k!=d[t[i]+1]:
                l[k]=l[k]+"HH"
        d[t[i]],d[t[i]+1]=d[t[i]+1],d[t[i]]
    return l


# Création de la fenêtre principale
root = tk.Tk()
root.title("Mot dessinable")

# Création du canvas
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.grid(row=1,column=1,columnspan=3)

# Appel de la fonction avec la liste [2, 1, 1, 0, 2] et n=4
read_word(canvas, conversion([2, 1, 1, 0, 2],4), h=20, w=20,c=colour)
Button(root,text="Quit", command=root.destroy).grid(row=2,column=1)

def change_colour(canvas, l, h, w,c):
    for i in range(0,len(c)-1):
        c[i],c[i+1]=colour[i+1],c[i]
        canvas.delete("all")
        read_word(canvas, l, h, w,c)

Button(root, text="change la couleur", command=lambda: change_colour(canvas, conversion([2, 1, 1, 0, 2], 4), h=20, w=20, c=colour)).grid(row=2, column=3)

# Boucle principale Tkinter
root.mainloop()