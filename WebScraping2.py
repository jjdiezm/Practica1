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
import requests
import pandas as pd
import time
import json

# URL with JSON to web-scraping players statistics
url = "https://api.unidadeditorial.es/sports/v1/player-total-rank/sport"
url += "/01/tournament/0101/sort/goals/current/?site=2&mn=100"

agents = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
          "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1"]

# header_text = 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
# header_text += 'Chrome/49.0.2623.63 Safari/537.36'
# headers = {'User-Agent': header_text}
# Alternatives proxies FONT:  https://www.sslproxies.org/
proxies = ["http://145.253.253.52:8080", "http://34.244.2.233:8123"]
# pag_resp = requests.get(pag_link, proxies=proxies, timeout=5)
# Honeypots: We only process JSON so not needed

try:
    # To control the execution time of our web-scraping process
    time_start = time.time()
    # Same URL for all the teams
    pag_link = url
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
    # Read JSON response with this structure.
    # {
    #     "status": "success",
    #     "data": {
    #         "classificationHead": {
    #              ...
    #             }
    #         },
    #         "rank": [
    #             {
    #                 "id": "01_0101_2018_19054",
    #                 "playerId": "19054",
    #                 "knownName": "Messi",
    #                 "teamName": "Barcelona",
    #                 "playerPosition": {
    #                     "id": "4",
    #                     "name": "delantero",
    #                     "alternateNames": {
    #                         "ptBR": "atacante",
    #                         "esES": "delantero",
    #                         "enEN": "forward"
    #                     }
    #                 },
    #                 "goals": 32,
    #                 "rankGoals": 1,
    #                 "averageGoals": 1.14,
    #                 "games": 28,
    #                 "cards": 3,
    #                 "rankCards": 193,
    #                 "yellowCards": 3,
    #                 "rankRedCards": 183,
    #                 "assists": 12,
    #                 "rankAssists": 1,
    #                 "averageAssists": 0.43,
    #                 "passes": 1559,
    #                 "successPasses": 1276,
    #                 "rankSuccessPasses": 16,
    #                 "averageSuccessPasses": 81.85,
    #                 "rankPasses": 14,
    #                 "goalsConceded": 22,
    #                 "rankGoalsConceded": 158,
    #                 "averageGoalsConceded": 0.79
    #             },
    #             ...
    #          ]
    #     }
    # }
    data = json.loads(pag_resp.text)
    # List to store all data_frame rows
    data_frame_list = list()
    # JSON key 'rank' contains the statistics
    # Loop to get the statistics and validate it, if no stats we store "" or 0
    for player_data in data["data"]['rank']:
        # We get the keys in the JSON, we'll access JSON as dictionary
        key_list = player_data.keys()
        # we define player_row to store statistics got or "" if str or 0 if num
        player_row = list()
        # Statistics extraction:
        vId = (player_data['id'] if 'id' in key_list else "")
        player_row.append(vId)
        vNom = (player_data['knownName'] if 'knownName' in key_list else "")
        player_row.append(vNom)
        vNomEquip = (player_data['teamName'] if 'teamName' in key_list else "")
        player_row.append(vNomEquip)
        vPosicio = (player_data['playerPosition']['name'] if 'playerPosition' in key_list else "")
        player_row.append(vPosicio)
        vGols = (player_data['goals'] if 'goals' in key_list else 0)
        player_row.append(vGols)
        vRankingGols = (player_data['rankGoals'] if 'rankGoals' in key_list else 0)
        player_row.append(vRankingGols)
        vPromigGols = (player_data['averageGoals'] if 'averageGoals' in key_list else 0)
        player_row.append(vPromigGols)
        vPartits = (player_data['games'] if 'games' in key_list else 0)
        player_row.append(vPartits)
        vTargetes = (player_data['cards'] if 'cards' in key_list else 0)
        player_row.append(vTargetes)
        vRanking_targetes = (player_data['rankCards'] if 'rankCards' in key_list else 0)
        player_row.append(vRanking_targetes)
        vTargetes_grogues = (player_data['yellowCards'] if 'yellowCards' in key_list else 0)
        player_row.append(vTargetes_grogues)
        vRanking_targetes_vermelles = (player_data['rankRedCards'] if 'rankRedCards' in key_list else 0)
        player_row.append(vRanking_targetes_vermelles)
        vAssistencies = (player_data['assists'] if 'assists' in key_list else 0)
        player_row.append(vAssistencies)
        vRanking_assistencies = (player_data['rankAssists'] if 'rankAssists' in key_list else 0)
        player_row.append(vRanking_assistencies)
        vPromig_assistencies = (player_data['averageAssists'] if 'averageAssists' in key_list else 0)
        player_row.append(vPromig_assistencies)
        passes = (player_data['passes'] if 'passes' in key_list else 0)
        player_row.append(passes)
        passes_bons = (player_data['successPasses'] if 'successPasses' in key_list else 0)
        player_row.append(passes_bons)
        ranking_passes_bons = (player_data['rankSuccessPasses'] if 'rankSuccessPasses' in key_list else 0)
        player_row.append(ranking_passes_bons)
        promig_passes_bons = (player_data['averageSuccessPasses'] if player_data['averageSuccessPasses'] else 0)
        player_row.append(promig_passes_bons)
        ranking_passes = (player_data['rankPasses'] if 'rankPasses' in key_list else 0)
        player_row.append(ranking_passes)
        gols_ok = (player_data['goalsConceded'] if 'goalsConceded' in key_list else 0)
        player_row.append(gols_ok)
        ranking_gols_ok = (player_data['rankGoalsConceded'] if 'rankGoalsConceded' in key_list else 0)
        player_row.append(ranking_gols_ok)
        promig_gols_ok = (player_data['averageGoalsConceded'] if 'averageGoalsConceded' in key_list else 0)
        player_row.append(promig_gols_ok)
        # Finally we add the row once built to the Data_Frame
        data_frame_list.append(player_row)
    # Data_frame structure generated using original attributes name:
    # std_jug = pd.DataFrame('id', 'playerId', 'knownName', 'teamName', 'playerPosition', 'goals', 'rankGoals',
    #                        'averageGoals', 'games', 'cards', 'rankCards', 'yellowCards', 'rankRedCards',
    #                        'assists', 'rankAssists', 'averageAssists', 'passes', 'successPasses',
    #                        'rankSuccessPasses', 'averageSuccessPasses', 'rankPasses', 'goalsConceded',
    #                        'rankGoalsConceded', 'averageGoalsConceded')

    # Data_frame generation: We use catalan names and the previously generated rows list:
    std_jug = pd.DataFrame(columns=('jug_id', 'nom', 'nomEquip', 'posicio', 'gols', 'ranking_gols', 'promig_gols',
                                    'partits', 'targetes', 'ranking_targetes', 'targetes_grogues',
                                    'ranking_targetes_vermelles', 'assistencies', 'ranking_assistencies',
                                    'promig_assistencies', 'passes', 'passes_bons', 'ranking_passes_bons',
                                    'promig_passes_bons', 'ranking_passes', 'gols_ok', 'ranking_gols_ok',
                                    'promig_gols_ok'),
                           data=data_frame_list)

    print("Web-scraping finalitzat...\nInici del backup a disk.")
    # We store the alphanumeric data as CSV on file estadistiques_jugadors.csv
    std_jug.to_csv("estadistiques_jugadors.csv", decimal=",", index=False)
    print("PROCÉS FINALITZAT  en " + str(int(np.round((time.time()-time_start)/60, 0))) + " minuts i " +
          str(int(np.round((time.time()-time_start) % 60, 0))) + " segons.")

except requests.Timeout as msgE:
    print("Temps d'espera excedit !")
    print(str(msgE))
