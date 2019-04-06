# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019
Descripció:
    Pràctica nº1 : Tipología i cicle de vida de les dades.
    Implementació pràctica de web-scraping en diari esportiu per generar
    un dataset d'analisi sobre el funcionament de la lliga 2018-2019.
    
@author: Quim Dalmases / Juanjo Díez
"""

import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
from skimage import io
import time
# import re

# URL's to web-scraping
urls = ["https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario",
        "https://www.marca.com/futbol/primera/equipos.html?intcmp=MENUMIGA&s_kw=equipos-y-jugadores"]

equips_marca = ["alaves", "athletic", "atletico", "barcelona", "betis", "celta", "eibar", "espanyol", "getafe",
                "girona", "huesca", "leganes", "levante", "rayo", "real-madrid", "real-sociedad", "sevilla",
                "valencia", "valladolid", "villarreal"]

agents = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
          "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1"]

# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                          ' Chrome/49.0.2623.63 Safari/537.36'}

# Alternatives proxies FONT:  https://www.sslproxies.org/
proxies = ["http://145.253.253.52:8080", "http://34.244.2.233:8123"]
# pag_resp = requests.get(pag_link, proxies=proxies, timeout=5)

# Honeypots care:
# Take care of : Display:None
# Do not deep more than 4 levels on links

try:
    # Data frame definition
    EQ = pd.DataFrame(columns=('idDB', 'Nom', 'Equip', 'Funcio', 'Dorsal'))
    # Photos dictionary to store players pictures
    pictures_dict = dict()
    # To control the execution time of our web-scraping process
    time_start = time.time()
    # Teams extraction loop
    for m in range(len(equips_marca)):
        # URL build for each team
        pag_link = "https://www.marca.com/futbol/{}".format(equips_marca[m])
        pag_link += "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"
        # Get HTML from pag_link, using time_out = 1 sec on each request.
        pag_resp = requests.get(pag_link, timeout=1)
        # If the server is blocked [status_code!=200], we proceed with an alternate request
        # by changing user-agent and IP using a proxy
        if pag_resp.status_code != 200:
            print(pag_resp.status_code)
            proxy = {'http': proxies[int(np.random.choice(2, 1))]}
            header = {'User-Agent': agents[int(np.random.choice(3, 1))]}
            # We wait 5 sec to retry
            pag_resp = requests.get(pag_link, proxies=proxy, headers=header, timeout=5)
        # Access to the HTML got using BeautifulSoup
        pag_content = BeautifulSoup(pag_resp.text, "lxml")
        # Browse HTML marks tree: We choose team, coach and players.
        # We got a list of teams -> <ul></u>
        teams = pag_content.find_all("ul", class_='plantilla')
        if teams:
            # Get the array at begin of response list
            element = teams[0].find_all("li")
            # Get the team name
            team_name = element[0]['id']
            # Get the coach name by extracting name and surname.
            coach = element[0].find("p", class_="entrenador").text.replace("Entrenador", "").strip()
            # The coach has no number thus we assign 0
            EQ = EQ.append({'Nom': coach, 'Equip': team_name, 'Funcio': 'Entrenador', 'Dorsal': '0'},
                           ignore_index=True)
            # Get the players
            # Numbers, name and surname, position at field and picture
            # Due to optimize we process them at the same time.
            dorsals = teams[0].find_all("strong")
            noms_jug = teams[0].find_all("span", class_="dorsal-jugador")
            pos_jug = teams[0].find_all("span", class_="posicion")
            dirFoto = teams[0].find_all("img")

            print("Raspat dels jugadors de : " + team_name)
            # Loop to store on the data_frame
            for k in range(len(noms_jug)):
                idDB = dirFoto[k]['src'].strip().split("/")[-1]
                idDB = idDB.split(".")[0]
                try:
                    idDB = int(idDB)
                except ValueError:
                    # Coach and some players has no idDB
                    idDB = ""
                EQ = EQ.append({'idDB': idDB,
                                'Nom': noms_jug[k].text.strip(),
                                'Equip': team_name.strip(),
                                'Funcio': pos_jug[k].text.strip(),
                                'Dorsal': dorsals[k].text.strip()},
                               ignore_index=True)
                # Get player picture.
                picture = io.imread(dirFoto[k]['src'].strip())
                picture_title = team_name.strip() + "_" + dorsals[k].text + "_" + noms_jug[k].text.replace(" ", "_")
                pictures_dict.update({picture_title: picture})
    print("Web-scraping finalitzat...\n Inici del backup a disk.")
    EQ.to_csv("jugadors.csv")
    # We store the alphanumeric data as CSV and the pictures on a binary pickle file
    with open('fotos.pickle', 'wb') as pickle_file:
        pickle.dump(pictures_dict, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    print("PROCÉS FINALITZAT  en " + str(int(np.round((time.time()-time_start)/60, 0))) +
          " minuts i " + str(int(np.round((time.time()-time_start) % 60, 0))) + " segons.")

except requests.Timeout as msgE:
    print("Temps d'espera excedit !")
    print(str(msgE))
