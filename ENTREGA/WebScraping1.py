# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019
Descripció:
    Practica nº1 : Tipología i cicle de vida de les dades.
    Implementació pràctica de webscraping en diari esportiu per generar
    un dataset d'analisi sobre el funcionament de la lliga 2018-2019.
    
@author: Grup pràctiques:  Quim Dalmases / Juanjo Díez
"""

# equipos_marca=["alaves","athletic","atletico","barcelona","betis","celta","eibar","espanyol","getafe","girona","huesca","leganes","levante","rayo","real-madrid","real-sociedad","sevilla","valencia","valladolid","villarreal"]
# "https://www.marca.com/futbol/" & equipos_marca[k] & "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"


# Llibreries per implementar Web scraping.
import numpy as np
from bs4 import BeautifulSoup
import requests
#import re
import pandas as pd
import pickle
from skimage import io
import time

# URL's on fer webscraping
urls=["https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario",
      "https://www.marca.com/futbol/primera/equipos.html?intcmp=MENUMIGA&s_kw=equipos-y-jugadores"]

equips_marca=["alaves","athletic","atletico","barcelona","betis","celta","eibar","espanyol","getafe",
               "girona","huesca","leganes","levante","rayo","real-madrid","real-sociedad","sevilla",
               "valencia","valladolid","villarreal"]

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
    # Definim l'estructura del dataframe.
    EQ= pd.DataFrame(columns=('idDB','Nom', 'Equip', 'Funcio', 'Dorsal'))
    # Diccinari que guarda les fotografies dels jugadors.
    Fotos=dict()
    # Càlcul del temps de durada del procés de web-scraping.
    time_start = time.time()
    # Bucle d'extracció per cada equip de 1ª divisió.
    for m in range(len(equips_marca)):
        # Construcció de la URL d'accés a la pàgina web de cada equip.
        pag_link = "https://www.marca.com/futbol/" + equips_marca[m] + "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"
        # obtenir codi font HTML de la website: time_out de 1 segon en cada petició.
        pag_resp = requests.get(pag_link, timeout=1)
        # Si el access al servidor està bloquejat [status_code!=200],executem una petició alternativa
        # Diferent user-agent i diferenta IP usant un proxy seleccionats aleatoriament.
        if pag_resp.status_code != 200:
            print(pag_resp.status_code)
            # fer scraping alternatiu
            # proxy i capçalera diferents. 
            proxy={'http': proxies[int(np.random.choice(2,1))]}
            header={'User-Agent': agents[int(np.random.choice(3,1))]}
            # Es torna a provar la petició, ara amb un temps d'espera de 5 segons.
            pag_resp = requests.get(pag_link, proxies=proxy, headers=header, timeout=5)
        # Accés al contingut HTML de la pàgina web.
        pag_content = BeautifulSoup(pag_resp.text, "lxml")
        # Navegació per l'arbre de marques HTML: Seleccionarem equip, entrenador i jugadors.
        # Selecció dels equips d'una llista d'equips. -> <ul></u>
        equipos = pag_content.find_all("ul",class_='plantilla')
        if equipos:
            # Obtenim l'array situat en la posició 0 de la resposta.
            element=equipos[0].find_all("li")
            # Obtenim el nom de l'equip.
            nomEquip=element[0]['id']
            # Obtenim el nom de l'entrenador, fent extraccció només del nom i cognoms.
            entrenador=element[0].find("p",class_="entrenador").text.replace("Entrenador","").strip()
            # L'entrenador es un cas especial, ja que no té dorsal com els jugadors. Per defecte té dorsal 0.
            EQ=EQ.append({'Nom':entrenador,'Equip': nomEquip, 'Funcio':'Entrenador', 'Dorsal':'0'}, ignore_index=True)
            # Extracció de les dades dels jugadors de l'equip.
            # Obtenim dorsals, nom i cognom, la posició en el camp i la seva fotografia
            # Per optimitzar l'extraccció o fem en paral·lel per tots els jugadors alhora.
            dorsals=equipos[0].find_all("strong")
            noms_jug=equipos[0].find_all("span", class_="dorsal-jugador")
            pos_jug=equipos[0].find_all("span", class_="posicion")
            dirFoto=equipos[0].find_all("img")
            
            # Notificació a l'usuari de quin equip s'està processant.
            print("Raspat dels jugadors de : " + nomEquip)
            # Bucle per emmagatzemar les dades en el dataframe.
            for k in range(len(noms_jug)):
                idDB=dirFoto[k]['src'].strip().split("/")[-1]
                idDB=idDB.split(".")[0]
                try:
                    idDB = int(idDB)
                except ValueError:
                    idDB=""
                EQ=EQ.append({'idDB':idDB, 'Nom':noms_jug[k].text.strip(),'Equip': nomEquip.strip(), 'Funcio':pos_jug[k].text.strip(), 'Dorsal':dorsals[k].text.strip()}, ignore_index=True)
                # Descarrega de les imatges de cada jugador.
                imatge = io.imread(dirFoto[k]['src'].strip())
                Fotos.update({nomEquip.strip() + "_" + dorsals[k].text + "_" + noms_jug[k].text.replace(" ","_") :imatge})
    # Notificació de finalització del web scraping i inici de backup a disc.
    print("Webscraping finalitzat...\nInici del backup a disk.")
    # Backup a disk en format CSV.
    EQ.to_csv("jugadors.csv")
    # S'emmagatzemen les dades alfanumeriques en format CSV i les imatges apart en un fitxer binari format pickle.
    with open('fotos.pickle', 'wb') as fitxer:
        pickle.dump(Fotos, fitxer, protocol=pickle.HIGHEST_PROTOCOL)
    # Notificació de finalització del procés.
    print("PROCÉS FINALITZAT  en " + str(int(np.round((time.time()-time_start)/60,0))) + " minuts i ", str(int(np.round((time.time()-time_start) % 60,0))) + " segons.")

except requests.Timeout as msgE:
    print("Temps d'espera excedit !")
    print(str(msgE))



