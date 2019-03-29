# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:26:21 2019

@author: qdeda
"""

from bs4 import BeautifulSoup

with open("marca1.html") as fp:
    soup = BeautifulSoup(fp,'lxml')

p=soup.find("ul",class_="plantillas-equipos")

for k in p:
    print(k)