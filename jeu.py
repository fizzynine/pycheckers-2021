from data import *
from ihm import *
from tkinter import * 
from time import *
damier = damier() #damier plein

#creer son propre damier pour des tests

#damier = damierVide()
#placer(damier,5,4,4)
#placer(damier,4,3,3)
#placer(damier,4,5,2)

#durée de la partie changeable
hour=0
min=30
sec=0
c = ":"

titre = "Jeu de dame"
f= fenetre(titre)
b= PhotoImage(file='images/b.png')
n= PhotoImage(file='images/n.png')
pb= PhotoImage(file='images/pb.png')
pn= PhotoImage(file='images/pn.png')
ns= PhotoImage(file='images/ns.png')
nst= PhotoImage(file='images/nst.png')
pbr= PhotoImage(file='images/pbr.png')
pnr= PhotoImage(file='images/pnr.png')
texte = genererLesCases(f,damier,pn,pb,n,b,pnr,pbr)
joueur=1
caseClique=None
xCC=0
yCC=0
suggestions=[]
sauts=[]
tour=0
estMultiTour = False;

def click(event):
  coor = f.grid_location(event.x_root - f.winfo_rootx(),event.y_root -f.winfo_rooty())
  x = coor[1]
  y = coor[0]      
  print("x: ",x," y:",y)       
  global caseClique
  global suggestions 
  global sauts
  global xCC
  global yCC
  global tour
  global estMultiTour
  global hour
  global min
  global sec


  if tour==0 and plusDeDeplacementBlancPossible(damier): #Si c'est le tour des blancs et qu'ils ne peuvent plus bouger alors cela devient le tour des noirs
      tour = 1
      print("a0")
  if tour==1 and plusDeDeplacementNoirPossible(damier): #Si c'est le tour des noirs et qu'ils ne peuvent plus bouger alors cela devient le tour des blancs
      tour = 0
      print("a1")

  if (contientPionNoir(damier,x,y) or contientReineNoire(damier,x,y)) and tour==0: 
    print("C'est le tour des blancs !")
    nettoyer(f,damier,suggestions,n)  
    suggestions = []
    print("a2")
    if (not estMultiTour):
      nettoyer(f,damier,sauts,n)
      sauts = []
      print("a3")
    return
  elif (contientPionBlanc(damier,x,y) or contientReineBlanche(damier,x,y)) and tour==1: 
    print("C'est le tour des noirs !")
    nettoyer(f,damier,suggestions,n)  
    suggestions = []
    print("a4")
    if (not estMultiTour):
      nettoyer(f,damier,sauts,n)
      sauts = []
      print("a5")
    return    
  if suggestions==[] and sauts==[]:
    if(damier[x][y]==1):
        print("La case cliqué est vide !")
        print("a6")
    elif (len(deplacements(damier,x,y))==0 and len(deplacementsSauts(damier,x,y))==0):  
        print("Le pion peut pas bouger !")
        print("a7")
    else:

      """
      ddd
      """
      suggestions = deplacements(damier,x,y)
      print(suggestions)
      print("a8")
      for i in range(len(suggestions)):
        suggere(f,damier,suggestions[i][0],suggestions[i][1],ns)
      sauts = deplacementsSauts(damier,x,y)
      for i in range(len(sauts)):
        suggereSaut(f,damier,sauts[i][0],sauts[i][1],nst)
      caseClique = f.grid_slaves(row=x, column=y)[0]
      xCC=x
      yCC=y
  else:
    if not (estUneSuggestion(damier,x,y,suggestions) or estUneSuggestion(damier,x,y,sauts)) and estVide(damier,x,y): #Ici on check si la case cliqué n'est pas une suggestion ni un saut et que c'est une case vide alors c'est une case hors de portée
      print("Case hors de portée !")
      nettoyer(f,damier,suggestions,n)  
      suggestions = []
      if (not estMultiTour):
        nettoyer(f,damier,sauts,n)
        print("a9")
        sauts = []
      return
    elif contientPion(damier,x,y) and not estMultiTour: #Ici on regarde si on clique sur un autre pion (forcément de ta couleur) et si on est pas en train de rejouer car on peut remanger 
        nettoyer(f,damier,suggestions,n)  
        nettoyer(f,damier,sauts,n)
        suggestions = []
        sauts = []
        suggestions = deplacements(damier,x,y)
        print(suggestions)
        print("b0")
        for i in range(len(suggestions)):
          suggere(f,damier,suggestions[i][0],suggestions[i][1],ns)
        sauts = deplacementsSauts(damier,x,y)
        for i in range(len(sauts)):
          suggereSaut(f,damier,sauts[i][0],sauts[i][1],nst)
        caseClique = f.grid_slaves(row=x, column=y)[0]
        xCC=x
        yCC=y     
    else:
      if estUneSuggestion(damier,x,y,suggestions): # Si c'est une suggestion on fais juste un déplacement
        caseDep=f.grid_slaves(row=x, column=y)[0]           
        nettoyer(f,damier,suggestions,n)  
        nettoyer(f,damier,sauts,n)
        deplacerUnPion(f,damier,xCC,yCC,x,y,caseClique,caseDep,n,pn,pb,pnr,pbr)
        suggestions = []
        caseClique=None
        print("b1")
        sauts = []
        PS=pionASoufle(damier,x,y)
        print("PS: ",PS)
        if PS != []:
          """print("SOUFFLE") code pour souffler un pion (ce code ne permet pas que 2 pions puissent être souffler en même temps)
          pion=f.grid_slaves(row=PS[0], column=PS[1])[0]  
          damier[PS[0]][PS[1]] = 1
          pion.configure(image=n)"""
          nettoyer(f,damier,PS,n)
          nettoyerSoufler(damier,PS)
          if tour == 0:
            texte['text'] = "C'est au tour des noirs de jouer ! Un pion blanc a été soufflé !"
            tour = 1
          else:  
            texte['text'] = "C'est au tour des blancs de jouer ! Un pion noir a été soufflé !"
            tour = 0
        else:
          if tour==0:
            tour = 1
            texte['text']="C'est au tour des noirs de jouer !"
            f.update()
            print("b2")
          else:
            tour = 0
            texte['text']="C'est au tour des blancs de jouer !"
            f.update()
            print("b3")  
      elif estUneSuggestion(damier,x,y,sauts): # Si c'est un sauts on mange le pion
        caseDep=f.grid_slaves(row=x, column=y)[0]           
        nettoyer(f,damier,suggestions,n)  
        nettoyer(f,damier,sauts,n)
        sauterUnPion(f,damier,xCC,yCC,x,y,caseClique,caseDep,n,pn,pb,pnr,pbr)
        sauts = deplacementsSauts(damier,x,y) # On recalcule les sauts
        suggestions = []
        print("b4")
        if sauts == []: #Si y'a pas de sauts possible on met fin au tour
          estMultiTour = False 
          caseClique= None
          print("b5")
          if tour==0:
            tour = 1
            texte['text']="C'est au tour des noirs de jouer !"
            f.update()
            print("b6")
          else:
            tour = 0
            texte['text']="C'est au tour des blancs de jouer !"
            f.update()
            print("b7")
        else: # Si un ou plusieurs saut possible on reoffre un tour en faisant en sorte qui puissent uniqument utilisé les sauts sans changer de pion 
          caseClique = caseDep
          estMultiTour = True
          for i in range(len(sauts)):
            suggereSaut(f,damier,sauts[i][0],sauts[i][1],nst)
          xCC = x
          yCC = y    
          print("b8")
  f.update()
  if(plusDeBlanc(damier)):
    hour=0
    min=0
    sec=0
    print('Les noirs ont gagnés')
    texte['text']="Les pions noirs ont gagnés"
    f.update() 
    return 
  if(plusDeNoir(damier)):
    hour=0
    min=0
    sec=0
    print('Les blancs ont gagnés') 
    texte['text']="Les pions blancs ont gagnés"
    f.update()    
    return
  if(plusDeDeplacementPossible(damier)):
    nbBlanc = nombreBlanc(damier)
    nbNoir = nombreNoir(damier)
    if nbBlanc == nbNoir:
      hour=0
      min=0
      sec=0
      print('Egalité')
      texte['text']="Egalité"
      f.update() 
      return
    if nbBlanc < nbNoir:
      hour=0
      min=0
      sec=0
      print('Les noirs ont gagnés')
      texte['text']="Les pions noirs ont gagnés !"
      f.update() 
      return
    if nbBlanc > nbNoir:
      hour=0
      min=0
      sec=0
      print('Les pions blancs ont gagnés')
      texte['text']="les pions blancs ont gagnés"
      f.update() 
      return

f.bind_class('Button','<Button-1>',click)
while hour > -1:
    while min > -1:
        while sec > 0:
            if(hour ==0 and min==0 and sec == 1):
              if(nombreBlanc(damier) < nombreNoir(damier)):
                print('Les noirs ont gagnés')
                texte['text']="Les pions noirs ont gagnés"
                texte.update() 
                break; 
              elif(nombreBlanc(damier) > nombreNoir(damier)):
                print('Les blancs ont gagnés') 
                texte['text']="Les pions blancs ont gagnés"
                texte.update() 
                break;  
              else:
                print('Egalité') 
                texte['text']="Egalité"
                texte.update() 
                break;  
            else:
              sec=sec-1
              sleep(1)
              sec1 = ('%02.f' % sec)  # format
              min1 = ('%02.f' % min)
              hour1 = ('%02.f' % hour)
              sts = texte['text']
              texte['text'] = ('Temps restants: ' + str(hour1) + c + str(min1) + c + str(sec1))
              texte.update()
        min=min-1
        sec=60
    hour=hour-1
    min=59
f.mainloop()    