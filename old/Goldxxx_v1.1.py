import tkinter, math
from random import *
canvas=tkinter.Canvas(width=800,height=500)
canvas.pack()
degree=-10
sx = 400
sy = 100
r = 50
p=50
stop=0
pos=0
sirka=4
interval=50
pocet=0
speed=5
catch=0
pokus=0
bg = tkinter.PhotoImage(file='obr/pozadie4.png')
canvas.create_image(400,250,image=bg)
obr1=tkinter.PhotoImage(file='obr/gold1.png')
obr2=tkinter.PhotoImage(file='obr/gold2.png')
ore_x=[]
ore_y=[]
def level1():
   global ore_x,ore_y,ore_name
   ore_x=[265,335,465,535]
   ore_y=[320,380,320,380]
   ore_name=['zlato','zlato2']
   canvas.create_image(300,350,image=obr1,anchor='center',tags='zlato')
   canvas.create_image(500,350,image=obr2,anchor='center',tags='zlato2')
   canvas.create_rectangle(465,320,535,380)

which_ore=0
def grab():
   u=0
   q=0
   global catch, pokus
   while q !=2:
      for u in range(0,2,2):
         print(q)
         if ore_x[u]<x<ore_x[u] and ore_y[u]<y<ore_y[u]:
            pokus=2
            which_ore=ore_name[int(pokus/2)]
            catch=1
            u+=2
         else:
            q+=1
         
def pull_up():
   global pokus,catch
   if pokus==0:
      canvas.delete(ore_name[which_ore])
      canvas.create_image(x,y,image=obr1,anchor='center',tags='zlato')
   if pokus==2:
      canvas.delete(ore_name[which_ore])
      canvas.create_image(x,y,image=obr2,anchor='center',tags='zlato2')
   if pocet<=0:
      ore_x[pokus],ore_x[pokus+1],ore_y[pokus],ore_y[pokus+1]=1000,1000,1000,1000
      catch=0
      pokus=0
      canvas.delete(ore_name[which_ore])
   
def hook_down():
   global r,x,y,pocet,p,speed
   while 0<x<800 and 0<y<500:
      degree_rad = math.radians(degree)
      x = sx + math.cos(degree_rad) * p
      y = sy - math.sin(degree_rad) * p
      canvas.create_line(sx,sy,x,y,width=sirka,tags='rope',fill='#DAC9B6')
      p+= 2
      pocet+=1
      grab()
      if catch ==1:
         pull_up()
         break
##      canvas.after(1)
      canvas.update()
   hook_up()

def shoot():
   global stop
   if stop==0:
      stop=1
      hook_down()
   else:
      stop=0
      if pos==-1:
         back()
      if pos==1:
         forth()
def hook_up():
   global degree,pocet,p,catch,x,y
   degree +=180
   while pocet >0:
      pocet-=1
      degree_rad = math.radians(degree)
      x = sx - math.cos(degree_rad) * p
      y = sy + math.sin(degree_rad) * p
      canvas.delete('rope')
      canvas.create_line(sx,sy,x,y,width=sirka,tags='rope',fill='#DAC9B6')
      p-=2
      if catch==1:
         pull_up()
      print(x,y)
      canvas.after(1)
      canvas.update()
   degree-=180
   shoot()
   
def shot():
   global stop,pos
   if stop==1:
      shoot()

def back():
   global degree,stop,pos,x,y
   if stop ==0:
      if degree != -170:
         pos=-1
         degree -=5
         degree_rad = math.radians(degree)
         x = sx + math.cos(degree_rad) * r
         y = sy - math.sin(degree_rad) * r
         canvas.delete('rope')
         canvas.create_line(sx, sy, x, y,width=sirka,tags='rope',fill='#DAC9B6')
##         canvas.create_oval(x-10,y-10,x+10,y+10,width=sirka)
         shot()
         canvas.after(interval,back)
         
      else:
         count()
   
def forth():
   global degree,stop,pos,x,y
   if stop==0:
      if degree != -10:
         pos=1
         degree +=5
         degree_rad = math.radians(degree)
         x = sx + math.cos(degree_rad) * r
         y = sy - math.sin(degree_rad) * r
         canvas.delete('rope')
         canvas.create_line(sx, sy, x, y,width=sirka,tags='rope',fill='#DAC9B6')
##         canvas.create_oval(x-10,y-10,x+10,y+10,width=sirka)
         shot()
         canvas.after(interval,forth)
         
         
      else:
         count()
   
def count():
   if degree==-10:
      back()
   if degree==-170:
      forth()
def shoot_key(event):
   shoot()

canvas.bind_all('<space>',shoot_key)
level1()
count()

