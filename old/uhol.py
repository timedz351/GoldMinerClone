import tkinter, math
canvas = tkinter.Canvas(height=500, width=500, bg='white')
canvas.pack()
sx = 300
sy = 300
r = 100
##for uhol in range(0, 181, 2):
##   uhol_rad = math.radians(uhol)
##   x = sx + math.cos(uhol_rad) * r
##   y = sy - math.sin(uhol_rad) * r
##   canvas.create_line(sx, sy, x, y)
##   canvas.after(10)
##   canvas.update()
for uhol in range(0,181, -2):
   uhol_rad = math.radians(uhol)
   x = sx - math.cos(uhol_rad) * r
   y = sy + math.sin(uhol_rad) * r
   canvas.create_line(sx, sy, x, y)
   canvas.after(10)
   canvas.update()
