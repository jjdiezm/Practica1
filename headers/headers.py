# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:44:48 2019

@author: qdeda
"""
# Llibreries per implementar Web scraping.
from bs4 import BeautifulSoup
import requests
# Llibreria per generar User_Agent
from user_agent import generate_user_agent

pag_link ='file:///D:/_UOC/CursMaster/11-Tipologia_i_Cicle_de_Vida_de_Dades/PRACTICA_1/code/Practica1/headers/test.html'
# obtenir codi font de la website
pag_resp = requests.get(pag_link, timeout=5)
# raspat html
pag_content = BeautifulSoup(pag_resp.content, "html.parser")

# Accés al contingut HTML de la pàgina web.
prices = pag_content.find_all(class_='main_price')
# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# Accedir al contingut
prices = pag_content.find_all('div', attrs={'class':'main_price'})

# generació de diferents 'user agent'
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}

 # implementació de proxys alternatius
 # FONT:  https://www.sslproxies.org/
proxies = {'http' : 'http://145.253.253.52:8080', 'https': 'http://34.244.2.233:8123'}
pag_resp = requests.get(pag_link, proxies=proxies, timeout=5)  

# Honeypots:
# Vigilar : Display:None
# No fer més de 4 nivells de profunditat en links. 


try:
    pag_resp = requests.get(pag_link, timeout=5)
    #pag_resp = requests.get(pag_link, timeout=5, headers=headers)
    if pag_resp.status_code == 200:
        # fer scraping
    else:
        print(pag_resp.status_code)
        # tornar a provar
except requests.Timeout as e:
    print("Temps d'espera excedit !")
    print(str(e))
except # altres excepcions