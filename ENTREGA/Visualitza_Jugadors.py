# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:26:21 2019

@author: Grup pràctiques:  Quim Dalmases / Juanjo Díez
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
        num=0
        for k in c.keys():
            if e in k:
                num+=1
                plt.imshow(c[k])
                plt.title(k.replace("_","\n"),fontsize=18)
                plt.show()
                
        print("Plantilla "+ str(num) + " jugadors.")
    return


# llista total d'equips
llista_equips=['Alavés','Athletic','Atlético','Barça','Betis','Celta','Eibar','Espanyol',
               'Getafe','Girona','Huesca','Leganés','Levante','Rayo','Real Madrid','Real Sociedad',
               'Sevilla FC','Valencia','Valladolid','Villarreal']

# Exemple d'aplicació de la funció.
jugadors_equips(['Valencia','Valladolid','Villarreal'])