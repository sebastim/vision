# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:53:21 2017

@author: Mervin Sebastian
"""
import  Tkinter as tk 
from PIL import Image, ImageTk 
from math import *

points = []
last = None
distTab = []
dist = 0
global perfect
#perfect represente la valeur de la perfection et marge represente la marge d'erreur autorisée

marge = 0.5


#calcul requis
def beautyTest(largeur, pupils):
    
    perfect=0
    c= (largeur*46)/100

    if (abs(pupils-c)<marge) :
        print("perfect a pris +25%")
        perfect = 25
    else :
        print ("Vous n'avez pas les proportions requises, passez a la deuxieme etape.. sorry ") 
    print "Votre score de perfection actuel est de ",perfect, "%"
    print ("saisir la distance entre le centre de votre oeil et la queue de votre sourcil puis la hauteur de votre visage:")


#Sert a faire la frame global

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
#Sert a faire un bouton pour quitter

    def createWidgets(self):

        self.QUIT = tk.Button(self, text="QUIT", fg="black",
                                            command=root.destroy)
        self.QUIT.pack()





#nous faisons saisir a l'utilisateur les mesures de son visage

#Sert a calculer la distance entre deux points

def distance(xa, ya, xb, yb):
    
    m = (xb-xa)**2
    n = (yb-ya)**2
    d = sqrt(m+n)
    #distTab.append(d)
    dist=d 
    print "La distance entre A et B est :",dist,"\n"
    for d in range(3):
        break
    return dist

#Sert a obtenir les coordonnees en cliquant sur un point

def pointeur(event):
    #chaine.configure(text="Clique detecte en x="+str(event.x)+\
    #                    ", Y =" + str(event.y))
    chaine.configure(text="(%r, %r)" % (event.x, event.y))
    
    global points
    global last
    global distTab
    Px = str(event.x)
    Py = str(event.y)
    if  (Px, Py) == last:
        return
    last =(Px, Py)
    points.append((Px, Py))
    print (points) 
    if len(points) < 2:
        return
    xa=int(points[0][0])
    ya=int(points[0][1])
    xb=int(points[1][0])
    yb=int(points[1][1])

    distTab.append(distance(xa, ya, xb, yb))
    print (distTab) 
   
    if len(distTab) == 2:
       
        beautyTest(*distTab)
   
    points = []        

root = tk.Tk()

cadre = tk.Frame(root, width =500, height =300, bg="light blue")
cadre.bind("<Button-1>", pointeur)
cadre.pack()


chaine = tk.Label(root)
#chaine.bind("<Motion>", pointeur)
chaine.pack()
print ("saisir la largeur de votre visage puis la distance entre vos 2 pupilles ")
#root.bind("<Double-Button-1>", pointeur)
app = Application(master=root)
app.mainloop()
