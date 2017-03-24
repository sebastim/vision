# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#perfect represente la valeur de la perfection et marge represente la marge d'erreur autorisée
perfect=0
marge = 0.5


#nous faisons saisir a l'utilisateur les mesures de son visage
print ("saisir la distance entre vos 2 pupilles :")
a= float(input())
print ("saisir la largeur de votre visage")
largeur=float(input())


#calcul requis
c= (largeur*46)/100

#calcul de la perfection
if (abs(a-c)<marge) :
    print("perfect a pris +25%")
    perfect = 25
else :
    print ("Vous n'avez pas les proportions requises, passez a la deuxieme etape.. sorry ") 

print ("Votre score de perfection actuel est de ",perfect, "%")


#nous faisons saisir a l'utilisateur les mesures de son visage
print ("saisir la distance entre le centre de votre oeil et la queue de votre sourcil puis la hauteur de votre visage:")
os= float(input())
print ("saisir la hauteur de votre visage")
hauteur=float(input())

#calcul requis
d=(hauteur/10)

#calcul de la perfection
if (abs(os-d)<marge) :
    print("perfect a pris +25%")
    perfect = perfect+25
else :
    print ("Vous n'avez pas les proportions requises, passez a la troisieme etape.. sorry" )
    
print ("Votre score de perfection actuel est de ",perfect, "%")

#nous faisons saisir a l'utilisateur les mesures de son visage
print ("saisir la distance entre votre menton et le bas de votre bouche:")
menton= float(input())

#calcul requis
f=(hauteur/5)


#calcul de la perfection
if (abs(menton-f)<marge) :
    print("perfect a pris +25%")
    perfect = perfect +25
else :
    print ("Vous n'avez pas les proportions requises, passez a la derniere etape.. sorry ")
    
print ("Votre score de perfection actuel est de ",perfect, "%")


#nous faisons saisir a l'utilisateur les mesures de son visage
print ("saisir la largeur de votre bouche :")
bouche= float(input())
print ("saisir la largeur de votre visage mesuré a la heuteur de la bouche")
largeurbouche=float(input())

#calcul requis
e=(largeurbouche/2)

#calcul de la perfection
if (abs(bouche-e)<marge) :
    print("perfect a pris +25%")
    perfect = perfect +25
else :
    print ("Vous n'avez pas les proportions requises.. sorry ")
    
print ("Votre score de perfection actuel est de ",perfect, "%")
