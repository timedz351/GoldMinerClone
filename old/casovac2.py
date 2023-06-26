import time
from time import sleep
base=time.time()
cas=0
while cas<10:
   now=time.time()
   cas= now - base
   print(int(cas))
   

   
