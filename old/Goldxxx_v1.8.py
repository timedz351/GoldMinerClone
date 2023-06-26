###     Velkosti obrazkov
###      gold1= 60x60px
###      gold2=30x30px
###      stone1=48x48px
import tkinter, math, time
from random import *
from threading import Timer

canvas=tkinter.Canvas(width=800,height=500)
canvas.pack()
bg = tkinter.PhotoImage(file='obr/pozadie5.png')
canvas.create_image(400,250,image=bg)

def end():
   global koniec,stop
   koniec=1
   stop=1
   canvas.delete('all')
   canvas.create_image(400,250,image=bg)
   
   if goal > skore:
      canvas.create_text(400,250,font=('8514oem',60,'bold'),text='GAME OVER',tags='gmover')
def casomer():
   global cas,start_sek,odpocet,koniec,stop
   now=time.time()
   cas=now-base_time
   if koniec==0:
      if cas > start_sek +1:
         start_sek= int(cas)
         odpocet=10-int(cas)
         canvas.delete('cas')
         canvas.create_text(230,62,text='Čas:'+str(odpocet),tags='cas',font=('8514oem',0,'bold'))
   if odpocet==0:
      end()
   
def generuj_level():
   global obrazky_file,obrazky,ore_sur,ore_name,goal
   obrazky=['gold1','gold1','gold1','gold2','gold2','gold2','gold2',
                  'stone1','stone1','stone1']
   ore_name=['zlato1','zlato2','zlato3','zlato4','zlato5','zlato6',
                     'zlato7','stone1','stone2','stone3']
   ore_sur=[(165,235,390,450),(365,435,435,495),(565,635,410,470),(290,320,375,405),(455,485,395,425),(95,125,355,385),(705,735,355,385),
                  (220,260,306,354),(380,420,316,364),(520,560,286,334)]
   for i in range(len(obrazky)):
      obrazok=tkinter.PhotoImage(file='obr/'+obrazky[i]+'.png')
      obrazky_file.append(obrazok)
   goal=2000
   

def level_kresli():
   global i
   canvas.create_text(730,57,text='Goal: '+str(goal),font=('8514oem',0,'bold'))
   for obr in obrazky_file:
      ox=(ore_sur[i][0]+ore_sur[i][1])/2
      oz=(ore_sur[i][2]+ore_sur[i][3])/2
      canvas.create_image(ox,oz,image=obr,anchor='center',tags=ore_name[i])
      i+=1

def grab():
   global catch,index_ore,which_ore,obrazok
   index_ore=0
   for u in range(0,(len(ore_sur))):
      if ore_sur[u][0]<x<ore_sur[u][1] and ore_sur[u][2]<y<ore_sur[u][3]:
         index_ore=u
         catch=1
         which_ore=ore_name[u]
         obrazok=tkinter.PhotoImage(file='obr/'+obrazky[index_ore]+'.png')
def pull_up():
   global catch, ore_sur
   canvas.delete(which_ore)
   canvas.create_image(x,y,image=obrazok,anchor='center',tags=which_ore)
   if pocet<=0:
      ore_sur[index_ore]=0,0,0,0
      catch=0
      canvas.delete(which_ore)
      
def pull_speed():
   global ore_speed,typ
   if empty ==1:
      ore_speed=1
   elif obrazky[index_ore]=='gold1':
      ore_speed=35
      typ='gold_big'
   elif obrazky[index_ore]=='gold2':
      ore_speed=10
      typ='gold_small'
   elif obrazky[index_ore]=='stone1':
      ore_speed=50
      typ='stone'   

def scoreboard():
   canvas.delete('scoreboard_tag')
   canvas.create_text(592,57,text=str(skore),tags='scoreboard_tag',fill='white',
                                  font=('8514oem',0,'bold'))
def points_ore():
   global skore
   if empty==1:
      points=0
   else:
      if typ=='gold_big':
         points=500
      if typ=='gold_small':
         points=250
      if typ=='stone':
         points=50
      size_text=5
      
      for cas in range(80):
         casomer()
         canvas.delete('points')
         canvas.create_text(400,90,text=points,tags='points',fill='white',font=('8514oem',size_text,'bold'))
         size_text+=1
         canvas.update()
         canvas.after(5)
      canvas.delete('points')
      skore+=points
      scoreboard()
   

def hook_down():
   global r,x,y,pocet,p,empty
   while 0<x<800 and 0<y<500 and koniec==0:
      casomer()
      degree_rad = math.radians(degree)
      x = sx + math.cos(degree_rad) * p
      y = sy - math.sin(degree_rad) * p
      canvas.create_line(sx,sy,x,y,width=sirka,tags='rope',fill='#DAC9B6')
      p+= 2
      pocet+=1
      grab()
      if catch ==1:
         empty=0
         pull_up()
         break
      else:
         empty=1
      canvas.after(1)
      canvas.update()
   hook_up()

def shoot():
   global stop
   if koniec==0:
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
   while pocet >0 and koniec==0:
      if koniec==0:
         casomer()
         pocet-=1
         degree_rad = math.radians(degree)
         x = sx - math.cos(degree_rad) * p
         y = sy + math.sin(degree_rad) * p
         canvas.delete('rope')
         canvas.create_line(sx,sy,x,y,width=sirka,tags='rope',fill='#DAC9B6')
         p-=2
         if catch==1:
            pull_up()
         pull_speed()
         canvas.after(ore_speed)
         canvas.update()
      else:
         casomer()
   
   points_ore()
   degree-=180
   shoot()
   
def shot():
   global stop,pos
   if stop==1:
      shoot()

def back():
   global degree,stop,pos,x,y
   if koniec==0:
      
      if stop ==0:
         if degree != -170:
            casomer()
            pos=-1
            degree -=rope_step
            degree_rad = math.radians(degree)
            x = sx + math.cos(degree_rad) * r
            y = sy - math.sin(degree_rad) * r
            canvas.delete('rope')
            canvas.create_line(sx, sy, x, y,width=sirka,tags='rope',fill='#DAC9B6')
            shot()
            canvas.after(interval,back)
         else:
            count()
      else:
         casomer()
   
def forth():
   global degree,stop,pos,x,y
   if koniec==0:
      
      if stop==0:
         if degree != -10:
            casomer()
            pos=1
            degree +=rope_step
            degree_rad = math.radians(degree)
            x = sx + math.cos(degree_rad) * r
            y = sy - math.sin(degree_rad) * r
            canvas.delete('rope')
            canvas.create_line(sx, sy, x, y,width=sirka,tags='rope',fill='#DAC9B6')
            shot()
            canvas.after(interval,forth)
         else:
            count()
      else:
         casomer()
   
def count():
   
   casomer()
   if degree==-10:
      back()
   if degree==-170:
      forth()
def shoot_key(event):
   if stop ==0:
      shoot()
def start():
   global base_time,cas, start_sek,i,skore,obrazky_file,odpocet,koniec,degree,stop,pos,pocet,catch,sx,sy,r,p,sirka,rope_step,interval
   base_time=time.time()
   canvas.delete('gmover')
   i=0
   degree=-10
   stop=0
   pos=0
   pocet=0
   catch=0
   obrazky_file=[]
   skore=0
   cas=0
   koniec=0
   odpocet=10
   start_sek=0
   ###menitelne
   sx = 400
   sy = 100
   r = 50
   p=60
   sirka=4
   rope_step=4 ##iba cisla, kt. vsetky sucty su parne
   interval=2
   generuj_level()
   level_kresli()
   scoreboard()
   count()
canvas.bind_all('<space>',shoot_key)
start()
##casomer()
##
##
