# Pràctica 1: Web scraping
Projecte de web scraping per 
* Disposar de les estadístiques dels jugadors més rellevants de la lliga de futbol en la temporada 2018-2019.
* Disposar de les imatges per poder aplicar algorismes ML de 'face-recognition'.

## Per començar
Aquesta Pràctica es desenvolupa amb Python 3.6+

### Prerequisits
Es requereix tenir instalades les llibreries:
*	_Requests_: gestió de peticions al web 
*	_BeautifulSoup_: anàlisi de documents HTML i navegació per l’arbre d’elements del document per el raspat d’informació
*	_numpy_: biblioteca de funciones matemàtiques d’alt nivell per operar amb aquests vectors i matrius
* _pandas_: bàsicament per la gestió de ‘DataFrames’
* _json_: gestió del format ‘JSON’ per l’obtenció de les dades
* _Pickle_: compressió binaria d’informació en fitxers
* _skimage_: lectura i visualització d’imatges
*	_matplotlib.pyplot_: biblioteca de funcions per el control de la visualització gràfica ‘matplotlib’ per Python

Exemple d'instal·lació:
``` Shell
python -m pip install BeautifulSoup
```

Exemples d'execució:
``` Shell
python WebScraping1.py
python WebScraping2.py
python Visualitza_Jugadors.py
python Llegir_CSV.py
```

### Wiki
Es pot consultar la wiki a [aquest mateix repositori](https://github.com/jjdiezm/Practica1/wiki)

## Eines de desenvolupament
[PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)  
[NotePad ++](https://notepad-plus-plus.org/)

## Contribucions
Aquest codi es destina a presentar una pràctica del Master de Ciència de Dades i no s'esperan contribucions de tercers.

## Authors
### Quim de Dalmases Juanet 
* Usuari UOC: quimdalmases
* Usuari GitHub: [QuimDJ](https://github.com/QuimDJ)

### Juanjo Díez Moya 
* Usuari UOC: jdiezm
* Usuari GitHub: [jjdiezm](https://github.com/jjdiezm)

## Llicència
Aquest projecte es lliura sota llicència [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca)  
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca"><img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width="100" alt="CC BY-NC-SA Button"></a>

## Reconneixements
El [diari MARCA](http://www.marca.es) és líder a Espanya en informació esportiva en format paper i digital. Cada temporada ofereix les estadístiques més rellevants que es poden obtenir, i que sense l’esforç dels mitjans de comunicació seria quasi inviable disposar d’aquestes dades.  
