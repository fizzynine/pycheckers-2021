from tkinter import *

def x_y_Interne(x1,y1,x2,y2,ratio):
    r2 = 0.5*(x2-x1)
    r1 = r2*ratio
    x = x1+(r2-r1)
    y = y1+(r2-r1)
    x_ = x2-(r2-r1)
    y_ = y2-(r2-r1)
    return [[x,y],[x_,y_]]

def creerPionBlanc(cnv,x,y,l):
    cnv.create_rectangle(x,y,x+l,y+l, fill='#AB8E52',outline="#AB8E52")         
    L = x_y_Interne(x,y,x+l,y+l,0.75)
    L1 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.70) #détail 1
    L2 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.60) #détail 2
    L3 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.40) #détail 3
    L4 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.35) #détail 4
    cnv.create_oval(L[0][0],L[0][1],L[1][0],L[1][1], fill="#C5B498",outline="#948460")
    cnv.create_oval(L1[0][0],L1[0][1],L1[1][0],L1[1][1], outline="#948460")
    cnv.create_oval(L2[0][0],L2[0][1],L2[1][0],L2[1][1], outline="#948460")
    cnv.create_oval(L3[0][0],L3[0][1],L3[1][0],L3[1][1], outline="#948460")
    cnv.create_oval(L4[0][0],L4[0][1],L4[1][0],L4[1][1], outline="#948460")
def creerPionNoir(cnv,x,y,l):
    cnv.create_rectangle(x,y,x+l,y+l, fill='#AB8E52',outline="#AB8E52")            
    L = x_y_Interne(x,y,x+l,y+l,0.75)
    L1 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.70) #détail 1
    L2 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.60) #détail 2
    L3 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.40) #détail 3
    L4 = x_y_Interne(L[0][0],L[0][1],L[1][0],L[1][1],0.35) #détail 4
    cnv.create_oval(L[0][0],L[0][1],L[1][0],L[1][1], fill="#3D3741",outline="#140E18")
    cnv.create_oval(L1[0][0],L1[0][1],L1[1][0],L1[1][1], outline="#140E18")
    cnv.create_oval(L2[0][0],L2[0][1],L2[1][0],L2[1][1], outline="#140E18")
    cnv.create_oval(L3[0][0],L3[0][1],L3[1][0],L3[1][1], outline="#140E18")
    cnv.create_oval(L4[0][0],L4[0][1],L4[1][0],L4[1][1], outline="#140E18")


w = Tk() 
w.geometry("500x400")
bg = PhotoImage(file = "dame.png")
c =Canvas(w, width = 500, height = 400)
c.pack()
c.create_image( 0, 0, image = bg, anchor = "nw")
police = "Purisa"
taille = 19
noir = "#AB8E52"
blanc = "#D8D5AF"
c.create_text(250, 100, font=(police, 35), text= "JEU DE DAME",fill=noir)  
b1 = Button(w,text   = "Local 1 VS 1  ",width=15,fg=noir,bg=blanc,font=(police,taille))
b2 = Button(w, text = "Local 1 VS IA ",width=15,fg=noir,bg=blanc,font=(police,taille))
b3 = Button(w, text = "ONLINE 1 VS 1 ",width=15,fg=noir,bg=blanc,font=(police,taille))
b1c = c.create_window( 150, 200, anchor = "nw",window = b1)
b2c = c.create_window( 100, 250, anchor = "nw",window = b2)
b3c = c.create_window( 150, 300, anchor = "nw",window = b3)
creerPionBlanc(c,100,200,50)
creerPionNoir(c,335,250,50)
creerPionBlanc(c,100,300,50)
w.mainloop()












"""

def ajouterTexte(f,texte):
    l = Label(f, text=texte, fg="#303030")
    l.pack()   
    return l 

def ajouterLeBouton(f,texte,couleurFond):
    b = Button(f, text=texte,height = 3, width = 25,highlightthickness=0,background=couleurFond)
    b.pack()
    return b

style = Style()
style.configure('TButton',borderwidth = '0')
f = Tk()
f.geometry("400x400")
bg = PhotoImage(file = "dame.png")
police = "Helvetica"
tailleTexte = 10
noir = "#AB8E52"
blanc = "#D8D5AF"
c = Canvas(f, width = 400, height = 400)
c.pack(fill = "both", expand = True)
c.create_image( 0, 0, image = bg, anchor = "nw")
b1 = ajouterLeBouton(f,"     Multijoueur local          ",noir)
b2 = ajouterLeBouton(f,"Multijoueur local (Humain vs IA)",noir)
b3 = ajouterLeBouton(f,"     Multijoueur en ligne       ",noir)
bc1 = c.create_window( 100, 10,anchor = "nw",window = b1)
bc2 = c.create_window( 100, 40,anchor = "nw",window = b2)
bc3 = c.create_window( 100, 70,anchor = "nw",window = b3)
f.wm_attributes('-alpha', 0.8, '-transparentcolor', '', '-disabled', 0, '-fullscreen', 0, '-toolwindow', 0, '-topmost', 0)

f.mainloop()

def lancerMenu(longueur,largeur):
    police = "Helvetica"
    tailleTexte = 10
    noir = "#AB8E52"
    blanc = "#D8D5AF"
    root = Tk()
    dame = PhotoImage(file = "dame.png")
    # Adjust size 
    root.geometry("400x400")
  
    # Add image file
    dame = PhotoImage(file = "dame.png")
  
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
  
    canvas1.pack(fill = "both", expand = True)

    canvas1.create_image( 0, 0, image = dame, anchor = "nw")
    
f = Frame(w,width=int(longueur/1.5), height=int(largeur/3),bd = 50,background="black")
    w.wm_attributes('-alpha', 0.9, '-transparentcolor', 'black', '-disabled', 0, '-fullscreen', 0, '-toolwindow', 0, '-topmost', 0)
    
    f.pack(expand=YES)
    ajouterTexte(f,"JEU DE DAME","arial",25)
    ajouterLeBouton(f,"     Multijoueur local          ",noir,blanc,police,tailleTexte)
    ajouterLeBouton(f,"Multijoueur local (Humain vs IA)",noir,blanc,police,tailleTexte)
    ajouterLeBouton(f,"     Multijoueur en ligne       ",noir,blanc,police,tailleTexte)

    return root

w = lancerMenu(500,500,dame)
w.mainloop()

s1 = Label(text="Les blancs ont gagnés !",foreground="white")
s1.pack()
s2 = Label(text="Les noirs ont gagnés !",foreground="white")
s3 = Label(text="Égalité",foreground="white")"""







