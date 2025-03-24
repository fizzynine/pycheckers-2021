from tkinter import *
from data import *
from tkinter import ttk


def fenetre(titre):
  w= Tk()
  w.title(titre)
  w.geometry("520x550")
  w.resizable(0,0)
  return w

def genererLesCases(fenetre,damier,pn,pb,n,b,pnr,pbr):
  longueurParCase = 50
  l = None
  for x in range(len(damier)):
      for y in range(len(damier)):
          if contientPionNoir(damier,x,y):
              Button(fenetre,image=pn,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0,).grid(row=x, column=y)
          elif contientPionBlanc(damier,x,y):
              Button(fenetre,image=pb,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0).grid(row=x, column=y)
          elif contientReineNoire(damier,x,y):
              Button(fenetre,image=pnr,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0,).grid(row=x, column=y)
          elif contientReineBlanche(damier,x,y):
              Button(fenetre,image=pbr,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0).grid(row=x, column=y)    
          elif estVide(damier,x,y):
              Button(fenetre,image=n,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0).grid(row=x, column=y)
          else:
              Label(fenetre,image=b,borderwidth=0,height=longueurParCase,width=longueurParCase,highlightthickness=0).grid(row=x, column=y)   
              l = Label(fenetre,height=2)
              l.grid(row=10,columnspan=10)             
  fenetre.update()
  return l
    
def suggere(fenetre,damier,x,y,ns):
  case = fenetre.grid_slaves(row=x, column=y)[0]
  case.configure(image=ns)         
def suggereSaut(fenetre,damier,x,y,nst):
  case = fenetre.grid_slaves(row=x, column=y)[0]
  case.configure(image=nst)    
def nettoyer(fenetre,damier,suggestions,n):
  for i in range(len(suggestions)):
    case = fenetre.grid_slaves(row=suggestions[i][0], column=suggestions[i][1])[0]
    case.configure(image=n)   
        

        
def deplacerUnPion(fenetre,damier,xCC,yCC,x,y,caseDep,caseSug,n,pn,pb,pnr,pbr):
  print()
  print("(",xCC,",",yCC,") -> (",x,",",y,")")
  print()
  if contientPionNoir(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      caseDep.configure(image=n)
      if x == 0:
        damier[x][y] = 4
        caseSug.configure(image=pnr)
      else:
        damier[x][y] = c
        caseSug.configure(image=pn)
  elif contientReineNoire(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      caseSug.configure(image=pnr)
  elif contientReineBlanche(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      caseSug.configure(image=pbr)         
  else:
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      caseDep.configure(image=n)
      if x == 9:
        damier[x][y] = 5
        caseSug.configure(image=pbr)
      else:
        damier[x][y] = c
        caseSug.configure(image=pb)
  fenetre.update()       

def sauterUnPion(fenetre,damier,xCC,yCC,x,y,caseDep,caseSug,n,pn,pb,pnr,pbr):
  coor = pionEntre(xCC,yCC,x,y)
  x1 = coor[0]
  y1 = coor[1]
  print()   
  print("(",xCC,",",yCC,") *(",x1,",",y1,")* (",x,",",y,")") 
  print() 
  pionABouffer=fenetre.grid_slaves(row=x1, column=y1)[0]
  print("Pion: ",pionABouffer)
  if contientPionNoir(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x1][y1] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      pionABouffer.configure(image=n)
      caseSug.configure(image=pn)
      ########### Résolution du bug "Un pion qui mange un pion adverse,
      # si le pion qui mange tombe sur la dernière/première rangé, il devient pas une dame"
      if x == 0:
        damier[x][y] = 4
        caseSug.configure(image=pnr)
      else:
        damier[x][y] = c
        caseSug.configure(image=pn)
      ###########"  
  elif contientReineNoire(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x1][y1] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      pionABouffer.configure(image=n)
      caseSug.configure(image=pnr)
  elif contientReineBlanche(damier,xCC,yCC):
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x1][y1] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      pionABouffer.configure(image=n)
      caseSug.configure(image=pbr) 
  else:
      c=damier[xCC][yCC]
      damier[xCC][yCC] = 1
      damier[x1][y1] = 1
      damier[x][y] = c
      caseDep.configure(image=n)
      pionABouffer.configure(image=n)
      caseSug.configure(image=pb)
      ############### Résolution du bug "Un pion qui mange un pion adverse,
      # si le pion qui mange tombe sur la dernière/première rangé en fonction, il devient pas une dame"
      if x == 9:
        damier[x][y] = 5
        caseSug.configure(image=pbr)
      else:
        damier[x][y] = c
        caseSug.configure(image=pb)
      ##############
  afficher(damier)
  fenetre.update() # """ 