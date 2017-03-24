# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from PIL import Image

def hflip(im):
    L, H = im.size
    pix= im.load()
    cop= im.copy()
    copixH = cop.load()
    for x in range(L//2):
        for y in range(H):
            copixH[x, y] = pix[(L-1-x), y]
    return cop
    
im = Image.open('images.jpeg')
im.show() 
res = hflip(im)
res.show()