import tkinter
canvas = tkinter.Canvas(width=610, height=150)
canvas.pack()
obrazky = []
def nacitaj(nazov, typ, pocet, obrazky):
   for i in range(1, pocet+1):
   obrazok = tkinter.PhotoImage(file=nazov + str(i) + '.'+typ)
   obrazky.append(obrazok)
def nakresli(x,y,obrazky):
   for obrazok in obrazky:
      canvas.create_image(x, y, image=obrazok, anchor='nw')
      x += 100
      nacitaj('obrazky/kocka_', 'png', 6, obrazky)
nakresli(10, 30, obrazky)
