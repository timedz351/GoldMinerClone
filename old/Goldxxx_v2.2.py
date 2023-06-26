###     Velkosti obrazkov
###      gold1= 60x60px
###      gold2=30x30px
###      stone1=48x48px
import tkinter, math, time
from random import *
from time import sleep
level=1
timer=60

canvas=tkinter.Canvas(width=800,height=500)
canvas.pack()
bg = tkinter.PhotoImage(file='obr/pozadie5.png')
bg_end = tkinter.PhotoImage(file='obr/pozadie.png')
bg_intro = tkinter.PhotoImage(file='obr/bg_intro.png')
player=tkinter.PhotoImage(file='obr/player.png')
def dalsi_level():
   global level
   canvas.create_text(405,255,font=('8514oem',60,'bold'),fill='#2d2d2d',text='GOOD JOB!',tags='gmover')
   canvas.create_text(400,250,font=('8514oem',60,'bold'),fill='#999999',text='GOOD JOB!',tags='gmover')
   button_pokracuj.pack()
   button_pokracuj.place(x=350,y=300)
   level+=1

def end():
   global koniec,stop,button_koniec,level,uvod
   koniec=1
   stop=1
   sleep(0.5)
   canvas.delete('all')
   canvas.create_image(400,250,image=bg_end,tags='gmover')
   if goal > skore:
      button_koniec=tkinter.Button(text='TRY AGAIN',command=intro,font=('8514oem',20,'bold'),highlightcolor='yellow')
      canvas.create_text(405,255,font=('8514oem',60,'bold'),fill='#2d2d2d',text='GAME OVER',tags='gmover')
      canvas.create_text(400,250,font=('8514oem',60,'bold'),fill='#999999',text='GAME OVER',tags='gmover')
      button_koniec.pack()
      button_koniec.place(x=350,y=300)
      level=1
      uvod=1
   else:
      dalsi_level()

def casomer():
   global cas,start_sek,odpocet,koniec,stop
   now=time.time()
   cas=now-base_time
   if koniec==0:
      if cas > start_sek +1:
         start_sek= int(cas)
         odpocet=timer-int(cas)
         canvas.delete('cas')
         canvas.create_text(230,62,text='Čas:'+str(odpocet),tags='cas',font=('8514oem',0,'bold'))
   if odpocet==0:
      end()
def vypocet_sur():
   global ore_sur
   ntica=()
   for i in range(0,len(suradnice),2):
      if obrazky[int(i//2)]=='gold1':
         sirka=30
         ntica=(suradnice[i]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
         ore_sur.append(ntica)
      if obrazky[i//2]=='gold2':
         sirka=15
         ntica=(suradnice[i]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
         ore_sur.append(ntica)
      if obrazky[i//2]=='stone1':
            sirka=20
            ntica=(suradnice[i]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
            ore_sur.append(ntica)
         
def generuj_level(level):
   global obrazky_file,obrazky,ore_sur,ore_name,goal,suradnice
   ore_sur=[]
   if level==1:
      obrazky=['gold1','gold1','gold1','gold2','gold2','gold2','gold2',
                     'stone1','stone1','stone1']
      ore_name=['zlato1','zlato2','zlato3','zlato4','zlato5','zlato6',
                        'zlato7','stone1','stone2','stone3']
      suradnice=(200,420,400,465,600,440,305,390,470,410,110,370,720,370,240,330,400,340,540,310)
      goal=150
   if level==2:
      obrazky=['gold2','gold2','gold2','stone1','stone1','stone1','stone1','stone1','stone1']
      ore_name=['zlato1','zlato2','zlato3','stone1','stone2','stone3','stone4','stone5','stone5']
      suradnice=(90,380,400,390,710,380,140,350,400,350,660,350,190,320,400,310,610,320)
      goal=800
   vypocet_sur()
   for i in range(len(obrazky)):
      obrazok=tkinter.PhotoImage(file='obr/'+obrazky[i]+'.png')
      obrazky_file.append(obrazok)
   
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
   if koniec==0:
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
         if degree != -170 and koniec==0:
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
         if degree != -10 and koniec==0:
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
def tlacidla():
   global button_pokracuj,button_koniec
   
   button_pokracuj=tkinter.Button(text='NEXT LEVEL',command=start,font=('8514oem',20,'bold'))
   button_koniec=tkinter.Button(text='TRY AGAIN',command=intro,font=('8514oem',20,'bold'))
def start():
   global base_time,cas, start_sek,i,skore,obrazky_file,odpocet,koniec,degree,stop,pos,pocet,catch,sx,sy,r,p,sirka,rope_step,interval,level
   button_koniec.destroy()
   button_pokracuj.destroy()
   tlacidla()
   base_time=time.time()
   canvas.create_image(400,250,image=bg)
   canvas.create_image(490,54,image=player)
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
   odpocet=60
   start_sek=0
   ###menitelne
   sx = 400
   sy = 100
   r = 50
   p=60
   sirka=4
   rope_step=4 ##iba cisla, kt. vsetky sucty su parne
   interval=2
   generuj_level(level)
   level_kresli()
   scoreboard()
   count()

uvod =1
slide=1
canvas.create_image(400,-230,image=bg_intro,anchor='n',tags='bgintro')
def intro():
   global slide,uvod
   slide=1
   canvas.create_image(400,-230,image=bg_intro,anchor='n',tags='bgintro')
   button_koniec.destroy()
   button_pokracuj.destroy()
def intro_animacia():
   global slide,uvod
   for i in range(71):
         canvas.delete('bgintro')
         canvas.create_image(400,-230+slide,image=bg_intro,anchor='n',tags='bgintro')
         slide-=5
         canvas.after(10)
         canvas.update()
   uvod=0
   start()
def klik(s):
   global uvod
   mx= s.x
   my= s.y
   if uvod==1 and 120 <= mx <= 220 and 150 <= my <= 270:
      uvod=0
      intro_animacia()
      
canvas.bind_all('<space>',shoot_key)
canvas.bind('<Button-1>',klik)
button_pokracuj=tkinter.Button(text='NEXT LEVEL',command=start,font=('8514oem',20,'bold'))
button_koniec=tkinter.Button(text='TRY AGAIN',command=intro,font=('8514oem',20,'bold'))

