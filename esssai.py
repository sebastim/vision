
# SERT AFFICHER UNE IMAGE PAS FINI

#! /usr/bin/env python 
# -*- coding: Latin-1 -*- 

#from Tkinter import Tk
#from PIL import Image
#from tkFileDialog import askopenfilename

#def hflip(im):
#    L, H = im.size
#    pix= im.load()
#    cop= im.copy()
#    copixH = cop.load()
#    for x in range(L//2):
#        for y in range(H):
#            copixH[x, y] = pix[(L-1-x), y]
#    return cop
#    im.show()
#    res = hflip(im)
#    res.show()
#
#
#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename()
##return open(filename, 'r')# show an "Open" dialog box and return the path to the selected file
#file = Image.open(filename)
#hflip(file)



#" COMMENT CREER UN BOUTON "

#from Tkinter import *
#
#def Pressed():                          #function
#        print 'buttons are cool'
#        button['bg'] = 'blue'
#        button['fg'] = 'white'
#
#root = Tk()                             #main window
#root.geometry('300x410+150+70')
#button = Button(root, text = 'Press', command = Pressed)
#button.pack(pady=130, padx = 20)
#Pressed()
#root.mainloop()


#!/usr/bin/python

#!/usr/bin/python


#"TEST "  
#if __name__ == "__main__":
#    a = multiply( 9 , 3)
#    answer = adder(4, a)
#
#    print (answer)

#!/usr/bin/python
from Tkinter import *                 
from PIL import Image, ImageFont, ImageDraw, ImageTk 
 
fen=Tk()
 
dicimg = {}
def chargerImage(): 
    im=Image.open("vis.jpg") 
    photo = ImageTk.PhotoImage(im) 
    dicimg['img1'] = photo
    item = cadre.create_image(125, 110, image = photo)

def pointeur(event):  #Recupere les coordonnees d'un point en cliquant dessus

    chaine.configure(text="(%r, %r)" % (event.x, event.y))
    coor.configure(text="(%r, %r)" % (event.x, event.y))
    
    global points    
    Px = str(event.x)
    Py = str(event.y)
    
    if  (Px, Py) == last:
        return
    last =(Px, Py)
    points.append((Px, Py))
    print cpc
    print (points) 
    if len(points) < 2:
        return
    xa=int(points[0][0])
    ya=int(points[0][1])
    xb=int(points[1][0])
    yb=int(points[1][1])
 

cadre = Canvas(fen, width =500, height =300, bg="light blue")
cadre.bind("<Button-1>", pointeur)
cadre.pack()

b=Button(fen,text="ON",command=chargerImage)
b.pack()
fen.mainloop()


#from tkinter import *
#
#def Check():
#    input = ent.get()
#
#    if input == 'pass' or input == 'hi' :
#        print ('COrrect password')
#    elif input == 'passe':
#        print ('Close but not it')
#    else:
#        print ('wrong wrong wrong')
#
#    ent.delete(0,END)
#    ent.focus()
#
#root = Tk()
#
#ent = Entry(root, bg = 'g')
#button = Button(root, text = 'Press', command = Check)
#
#ent.pack(anchor = W)
#button.pack(anchor = E)
#
#ent.focus()
#
#root.mainloop()