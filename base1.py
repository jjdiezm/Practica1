# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019

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

urls=["https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario",
      "https://www.marca.com/futbol/primera/equipos.html?intcmp=MENUMIGA&s_kw=equipos-y-jugadores"]
pag_link = urls[1]
# obtenir codi font de la website

pag_resp = requests.get(pag_link)
# raspat html
#pag_content = BeautifulSoup(pag_resp.content, "lxml")
pag_content = BeautifulSoup(pag_resp.text, "lxml")

# Accés al contingut HTML de la pàgina web.

equipos = pag_content.find_all("li",id='nombreEquipo')
#equipos = pag_content.find_all('ul', {'class': ['plantillas-equipos']}) 
EQ== pd.DataFrame(columns=('nom', 'dorsal', 'equip', 'funcio'))
if equipos:
    element=equipos[0].find("h2",class_="cintillo")
    nomEquip=element.text
    element=equipos[0].find_all("dl")
    p1=element[0].find_all("dd")
    entrenador=p1[0].text
    jugadors=p1[1].find_all("li")
    dorsals=jugadors[0].find_all("strong")
    noms=jugadors[0].find_all("span",class_="dorsal-jugador")
    a=dorsals[0].text
    jug1=noms[0].text
    
    EQ.insert(registre)
    
    for e in equipos:
        print(e)

#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# generació de diferents 'user agent'
agents=["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
" Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1"]

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}

 # Implementació de proxys alternatius
 # FONT:  https://www.sslproxies.org/
proxies = ["http://145.253.253.52:8080", "http://34.244.2.233:8123"]
#pag_resp = requests.get(pag_link, proxies=proxies, timeout=5)  

# Honeypots:
# Vigilar : Display:None
# No fer més de 4 nivells de profunditat en links. 

try:
    pag_resp = requests.get(pag_link, timeout=5)
    #pag_resp = requests.get(pag_link, timeout=5, headers=headers)
    if pag_resp.status_code == 200:
        pag_resp = requests.get(pag_link, timeout=5)
    else:
        print(pag_resp.status_code)
         # fer scraping alternatiu
        proxy={'http': proxies[np.random.choice(2,1)]}
        header={'User-Agent': agents[np.random.choice(3,1)]}
        pag_resp = requests.get(pag_link, 
                                proxies=proxy, 
                                headers=header,
                                timeout=5)
        # tornar a provar
except requests.Timeout as e:
    print("Temps d'espera excedit !")
    print(str(e))
