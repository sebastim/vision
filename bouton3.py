# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:08:59 2017

@author: sebastim
"""

import  tkinter as tk 
from PIL import Image, ImageTk 
from math import *

"VARIABLES"

points = []
last = None
distTab = []
distTab2 = []
distTab3 = []
distTab4 = []
dist = 0
global perfect #perfect represente le pourcentage de perfection

marge = 0.5 #marge represente la marge d'erreur autorisee

"FONCTIONS"

def beautyTest(largeur, pupils): #(description a ajouter)
    perfect=0
    c= (largeur*46)/100

    if (abs(pupils-c)<marge) :
        print("perfect a pris +25%")
        perfect = 25
    else :
        print ("Vous n'avez pas les proportions requises, passez a la deuxieme etape.. sorry") 
        print ("Votre score de perfection actuel est de ",perfect, "%","\n","\n")
        print ("**Saisir la distance entre le centre de votre oeil et la queue de votre sourcil puis la hauteur de votre visage:","\n")

def beautyEyes(eyes,hauteur):  #(description a ajouter)
    perfect=0
    d=(hauteur/10)
    
    if (abs(eyes-d)<marge) :
        print("perfect a pris +25%")
        perfect = perfect + 25
    else :
        print ("Vous n'avez pas les proportions requises, passez a la troisieme etape.. sorry") 
        print ("Votre score de perfection actuel est de ",perfect, "%","\n","\n")
        print ("***Saisir la distance entre votre menton et le bas de votre bouche, puis la hauteur de votre visage:","\n")
        
def beautyChin(chin,hauteur):  #(description a ajouter)
    perfect=0
    e=(hauteur/5)
    
    if (abs(chin-e)<marge) :
        print("perfect a pris +25%")
        perfect = perfect + 25
    else :
        print ("Vous n'avez pas les proportions requises, passez a la quatrieme etape.. sorry") 
        print ("Votre score de perfection actuel est de ",perfect, "%","\n","\n")
        print ("****Saisir la largeur de votre bouche, puis saisir la largeur de votre visage mesurée à la hauteur de la bouche:","\n")
             
def beautyMouth(mouth,largeurbouche):  #(description a ajouter)
    f=(largeurbouche/2)
    perfect=0
    
    if (abs(mouth-f)<marge):
        print("perfect a pris +25%","\n")
        perfect = perfect + 25 
    else :
        print ("Vous n'avez pas les proportions requises... sorry")
        print ("Votre score de perfection actuel est de ",perfect, "%","\n","\n")
    if perfect == 0:
        print("*****RIP !!! T'es trop moche, sale asymetrique va :P", "\n")

class Application(tk.Frame):  #Creation d'une frame global
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):  #Bouton pour quitter

        self.QUIT = tk.Button(self, text="QUIT", fg="black", command=root.destroy)
        self.QUIT.pack()

"Non fonctionnel encore"
def boutonSimple():
        perfect = 0
        print(perfect, "%")
        
def distance(xa, ya, xb, yb):  #Calcul de la distance entre deux points
    m = (xb-xa)**2
    n = (yb-ya)**2
    d = sqrt(m+n)
    dist= round(d, 3) 
    print ("\n", "Tableau des distances:")
    for d in range(3):
        break
    return dist

def pointeurz(event):  #Affiche les coordonnees en passant dessus

    coor.configure(text="(%r, %r)" % (event.x, event.y))
    
def pointeur(event):  #Recupere les coordonnees d'un point en cliquant dessus

    chaine.configure(text="(%r, %r)" % (event.x, event.y))
    coor.configure(text="(%r, %r)" % (event.x, event.y))
    
    global points
    global last
    global distTab
    global distTab2
    global perfect
    Px = str(event.x)
    Py = str(event.y)
    
    if  (Px, Py) == last:
        return
    last =(Px, Py)
    points.append((Px, Py))
    print ("Tableau des couples de coordonnés:")
    print (points) 
    if len(points) < 2:
        return
    xa=int(points[0][0])
    ya=int(points[0][1])
    xb=int(points[1][0])
    yb=int(points[1][1])

    distTab.append(distance(xa, ya, xb, yb))
    print (distTab,"\n") 
   
    if len(distTab) == 2:
        beautyTest(*distTab)
    
    if len(distTab) == 4:
        distTab2.append(distTab[2])
        distTab2.append(distTab[3])
        beautyEyes(*distTab2)
        
    if len(distTab) == 6:
        distTab3.append(distTab[4])
        distTab3.append(distTab[5])
        beautyChin(*distTab3)
        
    if len(distTab) == 8:
        distTab4.append(distTab[6])
        distTab4.append(distTab[7])
        beautyMouth(*distTab4)
           

root = tk.Tk() #Fenetre principale

cadre = tk.Frame(root, width =500, height =300, bg="red")
cadre.bind("<Button-1>", pointeur)
cadre.bind("<Motion>", pointeurz)
cadre.pack()

bouton = tk.Button(root, text='Taux de perfection', command = boutonSimple)
bouton.pack()

chaine = tk.Label(root)
chaine.pack()

coor = tk.Label(root)
coor.pack()

print ("*Saisir la largeur de votre visage puis la distance entre vos 2 pupilles","\n")
app = Application(master=root)
app.mainloop()
