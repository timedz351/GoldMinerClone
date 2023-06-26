import tkinter, math
canvas = tkinter.Canvas(height=500, width=500, bg='white')
canvas.pack()
uhol = 0
sx = 200
sy = 200
r = 100
def hak():
   global uhol
   while uhol  180:
      uhol -= 1
      uhol_rad = math.radians(uhol)
      x = sx + math.cos(uhol_rad) * r
      y = sy - math.sin(uhol_rad) * r
      canvas.delete('all')
      canvas.create_line(x, y, sx, sy)
      
##   while uhol != 0:
##         uhol += 1
##         uhol_rad = math.radians(uhol)
##         x = sx + math.cos(uhol_rad) * r
##         y = sy - math.sin(uhol_rad) * r
##         canvas.delete('all')
##         canvas.create_line(x, y, sx, sy)
##         canvas.after(100, rucicka)
      

hak()
