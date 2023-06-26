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
xg=300
yg=350
catch=0
obr1 = tkinter.PhotoImage(file='obr/pozadie4.png')
canvas.create_image(400,250,image=obr1)
obr2=tkinter.PhotoImage(file='obr/gold1.png')
canvas.create_image(xg,yg,image=obr2,anchor='center',tags='zlato')

def grab():
   global catch
   if xg-35<x<xg+35 and yg-30<y<yg+30:
      catch=1

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
   global degree,pocet,p,catch
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
         canvas.delete('zlato')
         canvas.create_image(x,y,image=obr2,anchor='center',tags='zlato')
         if pocet<=0:
            catch=0
            canvas.delete('zlato')
      canvas.after(5)
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
count()
