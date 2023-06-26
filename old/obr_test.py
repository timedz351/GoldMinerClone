import tkinter, math
from random import *
canvas=tkinter.Canvas(width=800,height=500)
canvas.pack()

obr1 = tkinter.PhotoImage(file='obr/figurka.png')
canvas.create_image(400,300,image=obr1)
