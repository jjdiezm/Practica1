# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:48:33 2019

@author: qdeda
"""

import requests
from bs4 import BeautifulSoup

url1="https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario#jornada1"
url2="http://www.leroymerlin.es/productos/outlet/calefaccion_y_climatizacion_outlet.html"
req = requests.get(url2)

soup=BeautifulSoup(req.text,"lxml")
events = soup.find_all("h3")

i=0
for e in events:
    if i>=0: 
        #print("Tot el link: ",e)
        print("Només text del link: ", e.find("a").contents,"\n")
        i+=1

