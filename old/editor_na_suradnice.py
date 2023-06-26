###     Velkosti obrazkov
###      gold1= 60x60px
###      gold2=30x30px
###      stone1=48x48px
import tkinter
import suradnice_open

canvas_edit=tkinter.Canvas(width=800,height=500)
canvas_edit.pack()
bg = tkinter.PhotoImage(file='obr/pozadie5.png') 
canvas_edit.create_image(400,250,image=bg)
canvas_edit.create_line(0,180,800,180,width=5,fill='white')
suradnice=()
obrazky=[]
obr_name=[]
typ=[]
nazov=[]
level=1
number=1
vyber=0
canvas_edit.create_text(400,160,text='Level:'+str(level),fill='white',font='Arial 20 bold',tags='lvl')
canvas_edit.create_text(400,130,text='Mas vybrate:'+str(nazov),fill='white',font='Arial 20 bold',tags='vyb')
subor=open('levels.txt','w')
subor.close()

def next_level():
   global suradnice,obrazky,obr_name,typ,nazov,vyber,level
   canvas_edit.delete('vyb')
   level+=1
   suradnice=()
   obrazky=[]
   obr_name=[]
   typ=[]
   nazov=[]
   canvas_edit.delete('vyb','lvl','ores')
   vyber=0
   canvas_edit.create_text(400,130,text='Mas vybrate:'+str(nazov),fill='white',font='Arial 20 bold',tags='vyb')
   canvas_edit.create_text(400,160,text='Level:'+str(level),fill='white',font='Arial 20 bold',tags='lvl')

def klik(s):
   global suradnice,number,obrazky,obr_name,nazov
   mx= s.x
   my= s.y
   if vyber==1 and my>180:
      
      
      suradnice += (mx,)+(my,)
      obrazky.append(typ)
      
      if typ=='gold1':
          nazov="gold"+str(number)
          canvas_edit.create_oval(mx-30,my-30,mx+30,my+30,outline='yellow',width=5,tags='ores')
      if typ=='gold2':
          nazov="gold"+str(number)
          canvas_edit.create_oval(mx-15,my-15,mx+15,my+15,outline='yellow',width=5,tags='ores')
      if typ=='stone1':
          nazov="stone"+str(number)
          canvas_edit.create_oval(mx-24,my-24,mx+24,my+24,outline='gray',width=5,tags='ores')
      obr_name.append(nazov)      
      number+=1

   
def gold_big():
   global typ,nazov,vyber
   vyber=1
   canvas_edit.delete('vyb')
   nazov='Big gold'
   canvas_edit.create_text(400,130,text='Mas vybrate:'+str(nazov),fill='white',font='Arial 20 bold',tags='vyb')
   typ='gold1'
   
def gold_small():
   global typ,nazov,vyber
   vyber=1
   canvas_edit.delete('vyb')
   nazov='Small gold'
   canvas_edit.create_text(400,130,text='Mas vybrate:'+str(nazov),fill='white',font='Arial 20 bold',tags='vyb')
   typ='gold2'
   
def stone():
   global typ,nazov,vyber
   vyber=1
   nazov='Stone'
   canvas_edit.delete('vyb')
   canvas_edit.create_text(400,130,text='Mas vybrate:'+str(nazov),fill='white',font='Arial 20 bold',tags='vyb')
   typ='stone1'

def zapis():
      subor=open('levels.txt','a')
      subor.write(str(suradnice)+'\n')
      subor.write(str(obrazky)+'\n')
      subor.write(str(obr_name)+'\n')

def koniec():
   global done
   subor.close()
   print(suradnice)
   print(obrazky)
   print(obr_name)
   b1.destroy()
   b2.destroy()
   b3.destroy()
   b4.destroy()
   b5.destroy()
   b0.destroy()
   canvas_edit.destroy()
   suradnice_open.final_zapis(0)
   import hra2
   
   
canvas_edit.bind('<Button-1>',klik)
button_frame = tkinter.Frame()
button_frame.pack()
b1=tkinter.Button(button_frame,text='Big gold',command=gold_big)
b2=tkinter.Button(button_frame,text='Small gold',command=gold_small)
b3=tkinter.Button(button_frame,text='Stone',command=stone)
b4=tkinter.Button(button_frame,text='Write to file',command=zapis)
b0=tkinter.Button(button_frame,text='Write next level', command= next_level)
b5=tkinter.Button(button_frame,text='End',command=koniec)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b0.grid(row=0,column=4)
b5.grid(row=0, column=5)


