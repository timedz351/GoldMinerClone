import tkinter, math
from random import *
canvas=tkinter.Canvas(width=800,height=500)
canvas.pack()

def cas():
   for i in range(60,0,-1):
      canvas.delete('time')
      canvas.create_text(200,180,text='Čas:'+str(i),fill='black',tags='time')
      print('sekunda')
      canvas.after(1000)
      canvas.update()
cas()
