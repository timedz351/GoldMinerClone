
def final_zapis(ktore_suradnice):
   subor=open('levels.txt','r')

   suradnice=[]
   obrazky=[]
   obr_name=[]
   riadky =subor.readlines()
   sur=riadky[ktore_suradnice].strip().replace('(','').replace(')','').split(',')

   for i in range(len(sur)):
      suradnice.append(int(sur[i]))

   obr=riadky[ktore_suradnice+1].strip().strip("[]").split(',')
   obrazky= [i.replace("'", '').replace(' ','') for i in obr]

   nam=riadky[ktore_suradnice+2].strip().strip("[]").split(',')
   obr_name = [i.replace("'", '').replace(' ','') for i in nam]
   subor.close()
   return suradnice,obrazky,obr_name
