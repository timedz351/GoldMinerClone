###     Velkosti obrazkov
###      gold1= 60x60px
###      gold2=30x30px
###      stone1=48x48px
ore_sur=[]
ntica=()
obrazky=['gold2','gold2','gold2']
suradnice=(90,380,400,390,710,380)
for i in range(0,len(suradnice),2):
   if obrazky[int(i//2)]=='gold1':
      sirka=30
      ntica=(suradnice[i//2]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
      ore_sur.append(ntica)
   if obrazky[i//2]=='gold2':
      sirka=15
      ntica=(suradnice[i]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
      ore_sur.append(ntica)
    if obrazky[i//2]=='stone1':
      sirka=20
      ntica=(suradnice[i]-sirka,suradnice[i]+sirka,suradnice[i+1]-sirka,suradnice[i+1]+sirka)
      ore_sur.append(ntica)
