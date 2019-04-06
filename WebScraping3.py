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
import time

# URL's to web-scraping
urls = ["https://www.marca.com/futbol/primera-division/pichichi.html",
        "https://www.marca.com/futbol/primera-division/zamora.html",
        "https://www.marca.com/futbol/primera-division/miguel-munoz.html"]

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


def explode_html(html_source):
    """ Function to explode the html of the pages and return a list of rows to insert on the data frame.
        Uses BeautifulSoup

    :param html_source: html
    :return: list of rows
    """
    pag_content = BeautifulSoup(html_source, "lxml")
    # Browse HTML marks tree: We choose tbody class ue-table-trophies__tbody where the info is.
    tbody = pag_content.find("tbody", class_='ue-table-trophies__tbody')
    # List to store all the rows
    row_list = list()
    if tbody:
        # Get the tr list
        trs = tbody.find_all('tr')
        for tr in trs:
            # we define player_row to store statistics got or "" if str or 0 if num
            player_row = list()
            # The pages has th and td
            ths = tr.find_all('th')
            # Order in ranking
            player_row.append(ths[0].get_text())
            # Player name and team
            aux_text_list = ths[1].get_text().split("(")
            # Player name
            player_row.append(aux_text_list[0].strip())
            # Player team
            player_row.append(aux_text_list[1].replace(')', ''))
            tds = tr.find_all('td')
            # The number of tds vary on the three pages so we implement a flexible procedure
            for td in tds:
                player_row.append(td.get_text())
            row_list.append(player_row)
    return row_list


columns_dict = dict()
columns_dict["pichichi_stats"] = ('ranking', 'nom', 'nomEquip', 'golsTotals', 'GolsPeu', 'GolsCap', 'GolsPenal',
                                  'GolsFalta')
columns_dict["zamora_stats"] = ('ranking', 'nom', 'nomEquip', 'Coeficient', 'GolsRebuts', 'PartitsJugats')
columns_dict["miguel-munoz_stats"] = ('ranking', 'nom', 'nomEquip', 'Valoracio')
for pag_link in urls:
    try:
        # Data frame definition
        # To control the execution time of our web-scraping process
        time_start = time.time()
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
        data_frame_list = explode_html(pag_resp.text)
        page = pag_link.split('/')[5]
        page = page.replace('.html', '_stats')
        stats = pd.DataFrame(columns=columns_dict[page],
                             data=data_frame_list)
        print("Web-scraping finalitzat...\nInici del backup a disk.")
        csv_file = page + '.csv'
        # We store the alphanumeric data as CSV on a different file per page
        stats.to_csv(csv_file, decimal=",", index=False)
        time_exec = str(int(np.round((time.time() - time_start) / 60, 0)))
        print("Pàgina " + page + " processada  en " + time_exec + " minuts i ",
              str(int(np.round((time.time() - time_start) % 60, 0))) + " segons.")
        print("Desat al fitxer: " + csv_file)

    except requests.Timeout as msgE:
        print("Temps d'espera excedit !")
        print(str(msgE))
