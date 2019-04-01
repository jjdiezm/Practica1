# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019
Descripció:
    Practica nº1 : Tipología i cicle de vida de les dades.
    Implementació pràctica de webscraping en diari esportiu per generar
    un dataset d'analisi sobre el funcionament de la lliga 2018-2019.
    
@author:  Grup pràctiques:  Quim Dalmases / Juanjo Díez
"""

# equipos_marca=["alaves","athletic","atletico","barcelona","betis","celta","eibar","espanyol","getafe","girona","huesca","leganes","levante","rayo","real-madrid","real-sociedad","sevilla","valencia","valladolid","villarreal"]
# "https://www.marca.com/futbol/" & equipos_marca[k] & "/plantilla.html?intcmp=MENUMIGA&s_kw=plantilla-y-datos-del-club"


# Llibreries per implementar Web scraping.
import numpy as np
#from bs4 import BeautifulSoup
import requests
#import re
import pandas as pd
#import pickle
#from skimage import io
import time
import json

# URL's on fer webscraping de les ESTADISTIQUES DELS JUGADORS
url='https://api.unidadeditorial.es/sports/v1/player-total-rank/sport/01/tournament/0101/sort/goals/current/?site=2&mn=100'

agents=["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
" Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1"]

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}
# Implementació de proxys alternatius
# FONT:  https://www.sslproxies.org/
proxies = ["http://145.253.253.52:8080", "http://34.244.2.233:8123"]
#pag_resp = requests.get(pag_link, proxies=proxies, timeout=5)  

# Honeypots: No es necessari per aquesta website
# Vigilar : Display:None
# No fer més de 4 nivells de profunditat en links. 

try:
    # Càlcul del temps de durada del procés de web-scraping.
    time_start = time.time()
    
    # Construcció de la URL d'accés a la pàgina web de cada equip.
    pag_link = url
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
    # Cas status_code==200 - Accés al contingut HTML de la pàgina web.
    # Llegim la resposta en format JSON.
    data=json.loads(pag_resp.text)
    #Guardem totes les files del dataframe final en una llista
    dataframe_list=[]
    # La key 'rank' és la que conté les estadístiques.
    # Bucle per validar quínes estadístiques obtenim de cada jugador
    # d'entre les possibles. Si no hi ha estadística guardem "" o 0.
    for l in data["data"]['rank']:
        # Per saber quínes estadìstiques podem 'raspar', mirem les
        # keys del registre en JSON, que podem tractar com un diccionari
        llista=l.keys()
        # fila es una llista d'estadístiques raspades i amb valors "" o 0,
        # preparada per insertar en el dataframe final.
        fila=[]
        # Per cada estadística mirem si existeix per el jugador actual o és nula.
        # El valor de la variable es afegit a la llista 'fila'.
        vId                         = (l['id'] if 'id' in llista else "")
        fila.append(vId)
        vNom                        = (l['knownName'] if 'knownName' in llista else "")
        fila.append(vNom)
        vNomEquip                   = (l['teamName'] if 'teamName' in llista else "")
        fila.append(vNomEquip)
        vPosicio                    = (l['playerPosition']['name'] if 'playerPosition' in llista else "")
        fila.append(vPosicio)
        vGols                       = (l['goals'] if 'goals' in llista else 0)
        fila.append(vGols)
        vRankingGols                = (l['rankGoals'] if 'rankGoals' in llista else 0)
        fila.append(vRankingGols)
        vPromigGols                 = (l['averageGoals'] if 'averageGoals' in llista else 0)
        fila.append(vPromigGols)
        vPartits                    = (l['games'] if 'games' in llista else 0)
        fila.append(vPartits)
        vTargetes                   = (l['cards'] if 'cards' in llista else 0)
        fila.append(vTargetes)
        vRanking_targetes           = (l['rankCards'] if 'rankCards' in llista else 0)
        fila.append(vRanking_targetes)
        vTargetes_grogues           = (l['yellowCards'] if 'yellowCards' in llista else 0)
        fila.append(vTargetes_grogues)
        vRanking_targetes_vermelles = (l['rankRedCards'] if 'rankRedCards' in llista else 0)
        fila.append(vRanking_targetes_vermelles)
        vAssistencies               = (l['assists'] if 'assists' in llista else 0)
        fila.append(vAssistencies)
        vRanking_assistencies       = (l['rankAssists'] if 'rankAssists' in llista else 0)
        fila.append(vRanking_assistencies)
        vPromig_assistencies        = (l['averageAssists'] if 'averageAssists' in llista else 0)
        fila.append(vPromig_assistencies)
        passes                      = (l['passes'] if 'passes' in llista else 0)
        fila.append(passes)
        passes_bons                 = (l['successPasses'] if 'successPasses' in llista else 0)
        fila.append(passes_bons)
        ranking_passes_bons         = (l['rankSuccessPasses'] if 'rankSuccessPasses' in llista else 0)
        fila.append(ranking_passes_bons)
        promig_passes_bons          = (l['averageSuccessPasses'] if l['averageSuccessPasses'] else 0)
        fila.append(promig_passes_bons)
        ranking_passes              = (l['rankPasses'] if 'rankPasses' in llista else 0)
        fila.append(ranking_passes)
        gols_ok                     = (l['goalsConceded'] if 'goalsConceded' in llista else 0)
        fila.append(gols_ok)
        ranking_gols_ok             = (l['rankGoalsConceded'] if 'rankGoalsConceded' in llista else 0)
        fila.append(ranking_gols_ok)
        promig_gols_ok              = (l['averageGoalsConceded'] if 'averageGoalsConceded' in llista else 0)
        fila.append(promig_gols_ok)
        # Afegim la fila a la llista final que utilitzarem per generar el dataframe final.
        dataframe_list.append(fila)
    # Estructura del dataframe original que raspem.
    #std_jug= pd.DataFrame('id', 'playerId', 'knownName', 'teamName', 'playerPosition', 'goals', 'rankGoals', 
    #                      'averageGoals', 'games', 'cards', 'rankCards', 'yellowCards', 'rankRedCards', 'assists', 'rankAssists', 
    #                      'averageAssists', 'passes', 'successPasses', 'rankSuccessPasses', 'averageSuccessPasses', 'rankPasses', 
    #                      'goalsConceded', 'rankGoalsConceded', 'averageGoalsConceded')
    
    # Generació del dataframe final: Definim totes les estadístiques personalitzades i la llista de valors creada en el bucle anterior.
    std_jug=pd.DataFrame(columns=('jug_id', 'nom', 'nomEquip', 'posicio', 'gols', 'ranking_gols', 'promig_gols', 
                                  'partits', 'targetes', 'ranking_targetes', 'targetes_grogues', 'ranking_targetes_vermelles', 
                                  'assistencies', 'ranking_assistencies', 'promig_assistencies', 'passes', 'passes_bons', 
                                  'ranking_passes_bons', 'promig_passes_bons', 'ranking_passes', 'gols_ok', 'ranking_gols_ok', 
                                  'promig_gols_ok'), data=dataframe_list)
    
    # Notificació de finalització del web scraping i inici de backup a disc.
    print("Webscraping finalitzat...\nInici del backup a disk.")
    # Backup a disk en format CSV.
    std_jug.to_csv("estadistiques_jugadors.csv", decimal="," ,index=False)
    # S'emmagatzemen les dades alfanumeriques en format CSV 
    # Notificació de finalització del procés.
    print("PROCÉS FINALITZAT  en " + str(int(np.round((time.time()-time_start)/60,0))) + " minuts i ", str(int(np.round((time.time()-time_start) % 60,0))) + " segons.")

except requests.Timeout as msgE:
    print("Temps d'espera excedit !")
    print(str(msgE))



