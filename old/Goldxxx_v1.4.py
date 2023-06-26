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
catch=0

bg = tkinter.PhotoImage(file='obr/pozadie4.png')
canvas.create_image(400,250,image=bg)
##obr1=tkinter.PhotoImage(file='obr/gold1.png')
##obr2=tkinter.PhotoImage(file='obr/gold2.png')
##obr3=tkinter.PhotoImage(file='obr/stone1.png')

##ore_sur=[(265,335,320,380),(485,515,335,365),(376,424,226,274)]
####   ore_sur_y=[(320,380),(335,365)]
##ore_name=['zlato','zlato2','stone1']
##obrazky=['gold1','gold2','stone1']

##for i in range(len(ore_sur)):
##   obrazok=tkinter.PhotoImage(file='obr/'+obrazky[i]+'.png')
##   ox=int(ore_sur[i][0]+ore_sur[i][1])/2
##   oz=int(ore_sur[i][2]+ore_sur[i][3])/2
##   canvas.create_image(ox,oz,image=obrazok,anchor='center',tags=ore_name[i])
##   canvas.after(1000)
##   canvas.update()
i=0
def level1():
   global ore_sur,ore_name,obrazky,i
   
   ore_sur=[(265,335,320,380),(485,515,335,365),(376,424,226,274)]
   ore_name=['zlato','zlato2','stone1']
   obrazky=['gold1','gold2','stone1']
   obrazok=tkinter.PhotoImage(file='obr/'+obrazky[i]+'.png')
   ox=(ore_sur[i][0]+ore_sur[i][1])/2
   oz=(ore_sur[i][2]+ore_sur[i][3])/2
   canvas.create_image(ox,oz,image=obrazok,anchor='center',tags=ore_name[i])
   i+=1
##   canvas.create_image(300,350,image=obr1,anchor='center',tags='zlato')
##   canvas.create_image(500,350,image=obr2,anchor='center',tags='zlato2')
##   canvas.create_image(400,250,image=obr3,anchor='center',tags='stone1')                  
##   canvas.create_rectangle(465,320,535,380)

which_ore=0
index_ore=None
def grab():
   global catch,index_ore,which_ore,obrazok
   
   for u in range(0,(len(ore_sur))):

      if ore_sur[u][0]<x<ore_sur[u][1] and ore_sur[u][2]<y<ore_sur[u][3]:
         index_ore=u
         catch=1
         which_ore=ore_name[u]
         obrazok=tkinter.PhotoImage(file='obr/'+obrazky[index_ore]+'.png')
def pull_up():
   global catch, ore_sur
##   if index_ore==0:
##      canvas.delete(which_ore)
##      canvas.create_image(x,y,image=obr1,anchor='center',tags='zlato')
##   if index_ore==1:
##      canvas.delete(which_ore)
##      canvas.create_image(x,y,image=obr2,anchor='center',tags='zlato2')
   canvas.delete(which_ore)
   canvas.create_image(x,y,image=obrazok,anchor='center',tags=which_ore)
   if pocet<=0:
      ore_sur[index_ore]=0,0,0,0
      catch=0
      canvas.delete(which_ore)
   
def hook_down():
   global r,x,y,pocet,p
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
      canvas.after(1)
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
      canvas.after(2)
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
   if stop ==0:
      shoot()
      
      
   

canvas.bind_all('<space>',shoot_key)

level1()
count()

