# Practica1

## Webscraping - Liga de Fútbol.

### Q_WebScraping1.py

Obté les plantilles de la lliga de Primera Divisió del Futbol Espanyol - Temporada 2018-2019.
Les dades obtingudes queden emmatgazemades en dos fitxers segons el tipus de continguts:
a) jugadors.csv
  Conté les dades alfanumèriques:
    'idDB':  codi assignat al jugador en la base de dades.
     'Nom':  nom del jugador.
   'Equip':  equip en el que juga.
  'Funcio':  funció al camp, posició de joc.
  'Dorsal':  número que porta a la samarreta.
  
b) fotos.pickle
  Conté en format binari les fotografies de tots els 595 jugadors inscrits. En le cas de no disposar de fotografia se li assigna una   imatge per defecte de color fosc, i per cada fotografia les dades alfanumèriques identificatives en format:
  nomEquip_dorsal_nomJugador)
  
### Q_WebScraping2.py

Obté les dades de les estadístiques dels 100 millors jugadors de la lliga.
c) Estadístiques.csv

Els atributs inclosos en les estadístiques son:

                    'jug_id':  id assignat en la base de dades.  Ex: '01_0101_2018_19054'
                       'nom':  nom i cognoms del jugador.        
                  'nomEquip':  nom de l'equip on juga.
                   'posicio':  posició en el camp.
                      'gols':  Nº de gols marcats.
              'ranking_gols':  posició en ranking de gols marcats.
               'promig_gols':  promig de gols marcats.
                   'partits':  Nº de partits jugats.
                  'targetes':  Nº de targetes que li han mostrat.
          'ranking_targetes':  Posició en el ranking de targetes.
          'targetes_grogues':  Nº de targetes grogues rebudes.
'ranking_targetes_vermelles':  Posició en el ranking de targetes
                               vermelles.
              'assistencies':  Nº d'assistències realitzades.
      'ranking_assistencies':  Posició en el ranking de assistències.
       'promig_assistencies':  Promig d'assistències.
                    'passes':  
               'passes_bons':  
       'ranking_passes_bons':  
        'promig_passes_bons':  
            'ranking_passes':  
                   'gols_ok':  
           'ranking_gols_ok':  
            'promig_gols_ok':
  
