def afficher(M):
  "Affiche une matrice en respectant les alignements par colonnes (biblio.py)"
  w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
  for i in range(len(M)):
      for j in range(len(M[0])):
          print("%*s" %(w[j],str(M[i][j])), end= ' ')
      print()

def damierVide():
  "Retourne une matrice de 10x10 remplit de zéro et un"
  M=[]
  for x in range(10):
      L=[]
      for y in range(10):
          if (x%2==0 and y%2!=0)  or (x%2!=0 and y%2==0):
             L.append(1)
          else:
             L.append(0)   
      M.append(L)
  return M

def damier():
  """creation du damier avec tous les pions de ranges"""
  m = damierVide()
  number = 1
  for x in range(10):
      if x < 4:
          number = 3 
      elif x > 3 and x < 6:
          number = 1
      else:
          number = 2 
      for y in range(10):
          if (x%2==0 and y%2!=0)  or (x%2!=0 and y%2==0):
              m[x][y] = number
  return m

def damierInverse(damier):
  m = damierVide
  for x in range(10):
      for y in range(10):
          m[x][y] = damier[9-x][9-y]
  return m

def placer(m,x,y,value):
  m[x][y] = value

def estVide(m,x,y):
  if(x >= 0 and y >= 0):
    return m[x][y] == 1
  return False
  
def contientPion(m,x,y):
  return m[x][y] == 2 or m[x][y] == 3 or m[x][y] == 4 or m[x][y] == 5
  
def contientPionNoir(m,x,y):
  return m[x][y] == 2 
    
def contientPionBlanc(m,x,y):
  return m[x][y] == 3 

def contientReineNoire(m,x,y):
  return m[x][y] == 4 
    
def contientReineBlanche(m,x,y):
  return m[x][y] == 5 

def contientBlanc(m,x,y):
  return contientPionBlanc(m,x,y) or contientReineBlanche(m,x,y)

def contientNoir(m,x,y):
  return contientPionNoir(m,x,y) or contientReineNoire(m,x,y)

def estUnPionAdverse(m,x1,y1,x2,y2):
  return (contientNoir(m,x1,y1) and contientBlanc(m,x2,y2)) or (contientBlanc(m,x1,y1) and contientNoir(m,x2,y2))

def deplacements(m,x,y):
  """liste des deplacements momentanement possible pour un pion"""
  L=[]
  if contientPionBlanc(m,x,y):
    if (not x+1>9 and not y-1<0) and estVide(m,x+1,y-1):
      L.append([x+1,y-1])
    if (not x+1>9 and not y+1>9) and estVide(m,x+1,y+1): 
      L.append([x+1,y+1])  
  elif contientPionNoir(m,x,y):
    if (not x-1<0 and not y+1>9) and estVide(m,x-1,y+1):
      L.append([x-1,y+1])
    if (not x-1<0 and not y-1<0) and estVide(m,x-1,y-1): 
      L.append([x-1,y-1]) 
  elif contientReineNoire(m,x,y) or contientReineBlanche(m,x,y):
    d1 = True
    d2 = True
    d3 = True
    d4 = True
    for i in range(1,10):
      if (not x-i<0 and not y+i>9) and estVide(m,x-i,y+i) and d1:
        L.append([x-i,y+i])
      else:
        d1 = False
      if (not x+i>9 and not y+i>9) and estVide(m,x+i,y+i) and d2: 
        L.append([x+i,y+i])
      else:
        d2 = False
      if (not x+i>9 and not y-i<0) and estVide(m,x+i,y-i) and d3:
        L.append([x+i,y-i])
      else:
        d3 = False
      if (not x-i<0 and not y-i<0) and estVide(m,x-i,y-i) and d4: 
        L.append([x-i,y-i])
      else:
        d4 = False
  return L

def pionEntre(xCC,yCC,x, y):
  #incrémentation
  increX = 0
  incretY = 0
  
  if x < xCC and y < yCC:
    increX = 1
    increY = 1  
  elif x < xCC and y > yCC:
    increX = 1
    increY =-1    
  elif x > xCC and y < yCC: 
    increX = -1
    increY = 1 
  else:
    increX = -1
    increY = -1 
  return [x+increX,y+increY]

def deplacementsSauts(m,x,y):
  """liste des sauts momentanement possible pour un pion"""
  L=[]
  if(contientPionBlanc(m,x,y) or contientPionNoir(m,x,y)):
    if (not x+2>9 and not y+2>9) and (not x+1==10 and not y+1==10) and estUnPionAdverse(m,x,y,x+1,y+1) and estVide(m,x+2,y+2):
      L.append([x+2,y+2])
    if (not x+2>9 and not y-2<0) and (not x+1==10 and not y-1==-1) and estUnPionAdverse(m,x,y,x+1,y-1) and estVide(m,x+2,y-2): 
      L.append([x+2,y-2])
    if (not x-2<0 and not y+2>9) and (not x-1==-1 and not y+1==10) and estUnPionAdverse(m,x,y,x-1,y+1) and estVide(m,x-2,y+2): 
      L.append([x-2,y+2])
    if (not x-2<0 and not y-2<0) and (not x-1==-1 and not y-1==-1) and estUnPionAdverse(m,x,y,x-1,y-1) and estVide(m,x-2,y-2): 
      L.append([x-2,y-2])
  elif(contientReineBlanche(m,x,y) or contientReineNoire(m,x,y)):
    d1 = True
    d2 = True
    d3 = True
    d4 = True
    for i in range(8):
      if (not x+i+2>9 and not y+i+2>9) and (not x+i+1>9 and not y+i+1>9) and estUnPionAdverse(m,x,y,x+i+1,y+i+1) and estVide(m,x+i+2,y+i+2) and d1:
        if not estVide(m,x+i,y+i) and i != 0:
          d1 = False
        else:
          L.append([x+i+2,y+i+2])
          d1 = False 
      if (not x+i+2>9 and not y-i-2<0) and (not x+i+1>9 and not y-i-1<0) and estUnPionAdverse(m,x,y,x+i+1,y-i-1) and estVide(m,x+i+2,y-i-2) and d2:
        if not estVide(m,x+i,y-i) and i != 0: 
          d2 = False
        else: 
          L.append([x+i+2,y-i-2])
          d2 = False
      if (not x-i-2<0 and not y+i+2>9) and (not x-i-1<0 and not y+i+1>9) and estUnPionAdverse(m,x,y,x-i-1,y+i+1) and estVide(m,x-i-2,y+i+2) and d3:
        if not estVide(m,x-i,y+i) and i != 0:
          d3 = False
        else:
          L.append([x-i-2,y+i+2])
          d3 = False
      if (not x-i-2<0 and not y-i-2<0) and (not x-i-1<0 and not y-i-1<0) and estUnPionAdverse(m,x,y,x-i-1,y-i-1) and estVide(m,x-i-2,y-i-2) and d4:
        if not estVide(m,x-i,y-i) and i != 0:
          d4 = False
        else:
          L.append([x-i-2,y-i-2])
          d4 = False
  return L

def estUneSuggestion(m,x,y,suggestion):
  for i in range(len(suggestion)):
    if x == suggestion[i][0] and y == suggestion[i][1]:
      return True
  return False

def plusDeBlanc(m):
  for x in range(10):
    for y in range(10):
      if contientBlanc(m,x,y):
        return False
  return True

def plusDeNoir(m):
  for x in range(10):
    for y in range(10):
      if contientNoir(m,x,y):
        return False
  return True

def plusDeDeplacementPossible(m):
  for x in range(10):
    for y in range(10):
      if contientPion(m,x,y):
        if deplacements(m,x,y) != [] or deplacementsSauts(m,x,y) !=[]:
          return False
  return True

def plusDeDeplacementNoirPossible(m):
  for x in range(10):
    for y in range(10):
      if contientNoir(m,x,y):
        if deplacements(m,x,y) != [] or deplacementsSauts(m,x,y) !=[]:
          return False
  return True

def plusDeDeplacementBlancPossible(m):
  for x in range(10):
    for y in range(10):
      if contientBlanc(m,x,y):
        if deplacements(m,x,y) != [] or deplacementsSauts(m,x,y) !=[]:
          return False
  return True


def nombreBlanc(m):
  res= 0
  for x in range(10):
    for y in range(10):
      if contientBlanc(m,x,y):
        res +=1
  return res

def nombreNoir(m):
  res= 0
  for x in range(10):
    for y in range(10):
      if contientBlanc(m,x,y):
        res +=1
  return res

def pionASoufle(m,x,y):
  L = []
  if(contientBlanc(m,x,y)): 
    for x1 in range(10):
      for y1 in range(10):  
        if contientBlanc(m,x1,y1) and (x1!=x or y1!=y):
          if deplacementsSauts(m,x1,y1) !=[]:
            L.append([x1,y1])
  else:
    for x1 in range(10):
      for y1 in range(10):
        if contientNoir(m,x1,y1) and (x1!=x or y1!=y):
          if deplacementsSauts(m,x1,y1) !=[]:
            L.append([x1,y1])
  return L

def nettoyerSoufler(damier,PS):
  for i in range(len(PS)):
    damier[PS[i][0]][PS[i][1]] = 1
         

    