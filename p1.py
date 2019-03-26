# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:48:33 2019

@author: qdeda
"""

import requests
from bs4 import BeautifulSoup

url ='https://www.python.org/events/python-events/'
req = requests.get(url)
print(req.text[1:200])

soup=BeautifulSoup(req.text,"html5lib")
events = soup.find('ul').findAll('li')

