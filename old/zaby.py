import tkinter
from random import *
canvas = tkinter.Canvas(width=610, height=270, bg='white')
canvas.pack()
sirka_zaby = 60
zaby = list(range(10))

print(zaby)
for i in range(len(zaby)):
   ktory = randrange(10)
   zaby[i], zaby[ktory] = zaby[ktory], zaby[i]
print(zaby)

def kresli_zabu(x, y, cislo):
      canvas.create_line(x, y+55, x+55, y+55, width=3, fill='green')
      if cislo != 0:
         canvas.create_oval(x, y, x+50, y+50, fill='lightgreen')
         canvas.create_oval(x+7, y+28, x+43, y+38, fill='red')
         canvas.create_oval(x+7, y, x+22, y+15, fill='white')
         canvas.create_oval(x+28, y, x+43, y+15, fill='white')
         canvas.create_oval(x+11, y+7, x+19, y+15, fill='black')
         canvas.create_oval(x+31, y+7, x+39, y+15, fill='black')
         canvas.create_oval(x+35, y-20, x+60, y, fill='white')
         canvas.create_text(x+48, y-10, text=cislo)

def kresli():
   
   canvas.delete('all')
   for i in range(len(zaby)):
      kresli_zabu(i*sirka_zaby+10, 100, zaby[i])
kresli()

presun=0
def klik(sur):
   global presun
  
   index = (sur.x - 10)//sirka_zaby
   prazdne = zaby.index(0)

   vzdialenost = abs(index-prazdne)
   if vzdialenost < 3 and 0 <= index <= 9:
      zaby[index], zaby[prazdne] = zaby[prazdne], zaby[index]
      kresli()
      if not index==prazdne:
         presun+=1
         canvas.create_text(305,50,text='Pocet presunov:'+str(presun))
         
      else:
         canvas.create_text(305,50,text='Pocet presunov:'+str(presun))
   if vyherna_pozicia():
      gratulacia()
canvas.bind('<Button-1>', klik)
def vyherna_pozicia():
   for i in range(len(zaby)-1):
      if i != zaby[i]-1:
         return False
   return True
def gratulacia():
   canvas.create_text(300, 200, text='Vyhral si!', font='Arial 50',
   fill='green')
tsada=[]
def trening():
   global tsada, zaby
   tsada=entry.get().split(' ')
   for i in range(len(tsada)):
      tsada[i]=int(tsada[i])
   zaby[:]=tsada[:]
   print(zaby)
   kresli()
canvas.create_text(305,50,text='Pocet presunov:'+str(presun))
      
button=tkinter.Button(text='trenovacia sada',command=trening)
button.pack()
label=tkinter.Label(text='Zadaj poradie zab 0-9 oddelene medzerou= "x y z..." 0=medzera')
label.pack()
entry=tkinter.Entry()
entry.pack()
