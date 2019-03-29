# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019
Descripció:
    Practica nº1 : Tipología i cicle de vida de les dades.
    Implementació pràctica de webscraping en diari esportiu per generar
    un dataset d'analisi sobre el funcionament de la lliga 2018-2019.
    
@author: Quim.
"""

# equipos_marca=["alaves","athletic","atletico","barcelona","betis","celta","eibar","espanyol","getafe","girona","huesca","leganes","levante","rayo","real-madrid","real-sociedad","sevilla","valencia","valladolid","villarreal"]
# "https://www.marca.com/futbol/" & equipos_marca[k] & "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"


# Llibreries per implementar Web scraping.
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# URL's on fer webscraping
urls=["https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario",
      "https://www.marca.com/futbol/primera/equipos.html?intcmp=MENUMIGA&s_kw=equipos-y-jugadores"]

equips_marca=["alaves","athletic","atletico","barcelona","betis","celta","eibar","espanyol","getafe",
               "girona","huesca","leganes","levante","rayo","real-madrid","real-sociedad","sevilla",
               "valencia","valladolid","villarreal"]

EQ= pd.DataFrame(columns=('Nom', 'Equip', 'Funcio', 'Dorsal'))
#for m in range(len(equips_marca)):
for m in range(20):
    url1="https://www.marca.com/futbol/" + equips_marca[m] + "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"
    if m==7:
        a=1
    pag_link = url1
    # obtenir codi font de la website
    
    pag_resp = requests.get(pag_link)
    # raspat html
    #pag_content = BeautifulSoup(pag_resp.content, "lxml")
    pag_content = BeautifulSoup(pag_resp.text, "lxml")
    
    # Accés al contingut HTML de la pàgina web.
    
    equipos = pag_content.find_all("ul",class_='plantilla')
    #equipos = pag_content.find_all('ul', {'class': ['plantillas-equipos']}) 
    
    if equipos:
        element=equipos[0].find_all("li")
        nomEquip=element[0]['id']
        entrenador=element[0].find("p",class_="entrenador").text.replace("Entrenador","").strip()
        EQ=EQ.append({'Nom':entrenador,'Equip': nomEquip, 'Funcio':'Entrenador', 'Dorsal':'0'}, ignore_index=True)
        dorsals=equipos[0].find_all("strong")
        noms_jug=equipos[0].find_all("span", class_="dorsal-jugador")
        pos_jug=equipos[0].find_all("span", class_="posicion")
        
        for k in range(len(noms_jug)):
            EQ=EQ.append({'Nom':noms_jug[k].text.strip(),'Equip': nomEquip.strip(), 'Funcio':pos_jug[k].text.strip(), 'Dorsal':dorsals[k].text.strip()}, ignore_index=True)
    
EQ.to_csv("jugadors.csv")

