# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:20:46 2019

@author: qdeda
"""

import numpy as np
from bs4 import BeautifulSoup
import requests
import re

urls=["https://www.marca.com/futbol/primera-division/calendario.html?intcmp=MENUMIGA&s_kw=calendario",
      "https://www.marca.com/futbol/primera/equipos.html?intcmp=MENUMIGA&s_kw=equipos-y-jugadores"]
pag_link ='https://github.com/QuimDJ/Practica1/blob/Dev/headers/test.html'
# obtenir codi font de la website

pag_resp = requests.get(pag_link)
file = open("Exported.html", "wb")
file.write(BeautifulSoup(pag_resp.text,"lxml").encode("utf-8"))
file.close() #This close() is important