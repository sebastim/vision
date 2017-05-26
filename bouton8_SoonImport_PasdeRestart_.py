# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:08:59 2017

@author: sebastim
"""

import  Tkinter as tk              
from PIL import Image, ImageFont, ImageDraw, ImageTk 
from math import *
from Tkinter import *
import Image, ImageTk
import Tkinter, tkFileDialog

"VARIABLES"

points = []
last = None
distTab = []
distTab1 = []
distTab2 = []
distTab3 = []
distTab4 = []
dist = 0
perfect = 0 #perfect represente le pourcentage de perfection

"FONCTIONS"

dicimg = {}


def chargerImage(): 
    im=Image.open("vis.jpg") 
    photo = ImageTk.PhotoImage(im) 
    dicimg['img1'] = photo
    item = cadre.create_image(125, 110, image = photo)

def Open_file(label):
    "Function to open a file"
    image = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    image = Image.open(image)
    photo = ImageTk.PhotoImage(image)
    label.configure(image = photo)
    label.image = photo


def beautyTest(largeur, pupilles): #largeur du visage et distance entre les 2 pupilles
    global perfect
    c = (largeur*46)/100
    if pupilles==c:
        perfect = perfect + 25
        #print"Perfect a pris +100%"
    if pupilles < c:
        perfect = perfect + (pupilles/c*25)
        #print"Perfect a pris +",round(perfect,2)*4, "%"
    else:
        perfect = perfect + c/pupilles*25
        #print"Perfect a pris+",round(perfect,2)*4, "%"
        
    print "Passez a la deuxieme etape"
    print "Votre score de perfection actuel est de ",round(perfect,2), "%/25%", "%","\n","\n"
    print "**Saisir la distance entre le centre de votre oeil et la queue de votre sourcil puis la hauteur de votre visage:","\n"

def beautyEyes(eyes,hauteur):  # distance entre le centre de l'oeil et la queue du sourcil puis hauteur du visage
    global perfect
    d=(hauteur/10)
    
    if eyes==d:
        perfect = perfect + 25
        #print"Perfect a pris +100%"
    elif eyes<d:
        perfect = perfect + eyes/d*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"
    else:
        perfect = perfect + d/eyes*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"
        
    print "Passez a la troisieme etape"
    print "Votre score de perfection actuel est de ",round(perfect,2), "%/50%", "%","\n","\n"
    print "***Saisir la distance entre votre menton et le bas de votre bouche, puis la hauteur de votre visage:","\n"
    
def beautyChin(chin,hauteur):  #distance entre menton et bas de la bouche puis hauteur du visage
    global perfect
    e=(hauteur/5)
    if chin==e:
        perfect = perfect + 25
        #print"Perfect a pris +100%"
    elif chin<e:
        perfect = perfect + chin/e*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"
    else :
        perfect = perfect + e/chin*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"   
    
    print "Passez a la quatrieme etape"
    print "Votre score de perfection actuel est de ",round(perfect,2), "%/75%", "%","\n","\n"
    print "****Saisir la largeur de votre bouche, puis saisir la largeur de votre visage mesuree à la hauteur de la bouche:","\n"
         
def beautyMouth(mouth,largeurbouche):  # largeur de la bouche puis largeur du visage mesurée a la heuteur de la bouche
    global perfect
    f=(largeurbouche/2)    
    if mouth==f:
        perfect = perfect + 25
        #print"Perfect a pris +100%"
    elif mouth<f:
        perfect = perfect + mouth/f*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"
    else:
        perfect = perfect + f/mouth*25
        #print"Perfect a pris +",round(perfect,2)*4, "%"
    print "*****Votre score de FINAL de perfection est de ",round(perfect,2),"%/100%","\n","\n"

    if perfect<50:
        print"*****Bonne chance pour te trouver un compagnon !", "\n"
    elif 50<perfect<80:
        print"*****Tu geres pas mal !", "\n"
    else:
        print"*****Il est temps que tu ailles à Hollywood, tu es une star !", "\n"    

class Application(tk.Frame):  #Creation d'une frame global
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):  #Bouton pour quitter

        self.QUIT = tk.Button(self, relief=RAISED, cursor="pirate", text="QUIT", fg="black", command=root.destroy)
        self.QUIT.pack()

def boutonSimple():
        global perfect
        print(round(perfect,2), "%")
        
def distance(xa, ya, xb, yb):  #Calcul de la distance entre deux points
    m = (xb-xa)**2
    n = (yb-ya)**2
    d = sqrt(m+n)
    dist= round(d, 3) 
    print "\n", "Tableau des distances:"
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
    global distTab1
    global distTab2
    global perfect
    Px = str(event.x)
    Py = str(event.y)

    if  (Px, Py) == last:
        return
    last = (Px, Py)
    points.append((Px, Py))
    
    if len(points)//2: 
        print ("Tableau des couples de coordonnés:")
        print (points)
        
    if len(points)%2:
        return
    xa=int(points[-2][0]) 
    ya=int(points[-2][1])
    xb=int(points[-1][0])
    yb=int(points[-1][1])
    
    distTab.append(distance(xa, ya, xb, yb))    #Ajout des distances dans distTab
    print distTab,"\n" 
    cadre.create_line(xa, ya, xb, yb)   #Creation des traits a chaque couple de points donnes  
     
        
    if len(distTab) == 2:
        distTab1.append(distTab[0])
        distTab1.append(distTab[1])
        beautyTest(*distTab1)
#    
#    if len(points) == 4: 
#        print ("Tableau des couples de coordonnés:")
#        print (points) 
#        
    if len(distTab) == 4:
        distTab2.append(distTab[2])
        distTab2.append(distTab[3])
        beautyEyes(*distTab2)
#                
#    if len(points) == 6: 
#        print ("Tableau des couples de coordonnés:")
#        print (points)   
#        
    if len(distTab) == 6:
        distTab3.append(distTab[4])
        distTab3.append(distTab[5])
        beautyChin(*distTab3)
#
#    if len(points) == 8: 
#        print ("Tableau des couples de coordonnés:")
#        print (points) 
#        
    if len(distTab) == 8:
        distTab4.append(distTab[6])
        distTab4.append(distTab[7])
        beautyMouth(*distTab4)
           

root = tk.Tk() #Fenetre principale

#integration de l'ouverture d'image
root.title("picture viewer")

cadre = tk.Canvas(root, relief=RAISED, cursor="tcross") # width =500, height =300, bg="light blue")
cadre.bind("<Button-1>", pointeur)
cadre.bind("<Motion>", pointeurz)
cadre.pack()

But=tk.Button(root, text='Open', relief=RAISED, cursor="star", command=lambda :Open_file(cadre))
But.pack(side=Tkinter.LEFT)

bouton = tk.Button(root, relief=RAISED, cursor="heart", text='Taux de perfection', command = boutonSimple)
bouton.pack()

chaine = tk.Label(root)
chaine.pack()

coor = tk.Label(root)
coor.pack()

b = tk.Button(root, text='Import', command = chargerImage)
b.pack()

print ("*Saisir la largeur de votre visage puis la distance entre vos 2 pupilles\n")
app = Application(master=root)
app.mainloop()
