# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:26:21 2019

@author: qdeda
"""

#with open('fotos.pickle', 'wb') as fitxer:
#    pickle.dump(Fotos, fitxer, protocol=pickle.HIGHEST_PROTOCOL)


#with open('fotos.pickle', 'wb') as f:
#    f.write(response)


import pickle
from skimage import io
import matplotlib.pyplot as plt


with open('fotos.pickle', 'rb') as fitxer:
    c = pickle.load(fitxer)

tam=len(c.keys())

def jugadors_equips(l):
    for e in l:
        num=1
        for k in c.keys():
            if e in k:
                plt.imshow(c[k])
                plt.title(k.replace("_","\n"),fontsize=18)
                plt.show()
                num+=1
        print("Plantilla "+ str(num) + " jugadors.")
    return

jugadors_equips(['Betis','Eibar'])