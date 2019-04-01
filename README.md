# Practica1

## Webscraping - Liga de Fútbol.

### Q_WebScraping1.py
<p>
Obté les plantilles de la lliga de Primera Divisió del Futbol Espanyol - Temporada 2018-2019.
Les dades obtingudes queden emmatgazemades en dos fitxers segons el tipus de continguts:
<ol>
<li> jugadors.csv</li>
<p>
  Conté les dades alfanumèriques:
    'idDB':  codi assignat al jugador en la base de dades.
     'Nom':  nom del jugador.
   'Equip':  equip en el que juga.
  'Funcio':  funció al camp, posició de joc.
    'Dorsal':  número que porta a la samarreta.
</p>  
<li> fotos.pickle</li>
<p>
    Conté en format binari les fotografies de tots els 595 jugadors inscrits. En el cas de no disposar de fotografia se li assigna una   imatge per defecte de color fosc, i per cada fotografia les dades alfanumèriques identificatives en format:
  nomEquip_dorsal_nomJugador
</p>
</ol>
</p>

### Q_WebScraping2.py
<p>
Obté les dades de les estadístiques dels 100 millors jugadors de la lliga.
<ol>
  <li> Estadístiques.csv </li>
<p>
Els atributs inclosos en les estadístiques son:

                    'jug_id':  id assignat en la base de dades.                 Ex: '01_0101_2018_19054'
                       'nom':  nom i cognoms del jugador.                       Ex: 'Messi'       
                  'nomEquip':  nom de l'equip on juga.                          Ex: 'Barcelona'
                   'posicio':  posició en el camp.                              Ex: 'Delantero'
                      'gols':  nº de gols marcats.                              Ex: 31
              'ranking_gols':  posició en ranking de gols marcats.              Ex: 1
               'promig_gols':  promig de gols marcats.                          Ex: 1.15
                   'partits':  nº de partits jugats.                            Ex: 27
                  'targetes':  nº de targetes que li han mostrat.               Ex: 2
          'ranking_targetes':  posició en el ranking de targetes.               Ex: 240
          'targetes_grogues':  nº de targetes grogues rebudes.                  Ex: 2
          'ranking_targetes_vermelles':  posició en el ranking de targetes vermelles.     Ex: 233
              'assistencies':  nº d'assistències realitzades.                   Ex: 12
      'ranking_assistencies':  posició en el ranking de assistències.           Ex: 1
       'promig_assistencies':  promig d'assistències.                           Ex: 0.44
                    'passes':  nº de passes.                                    Ex: 1532
               'passes_bons':  nº de passes bons.                               Ex: 1258
       'ranking_passes_bons':  posició en el ranking de passes bons.            Ex: 15
        'promig_passes_bons':  promig de passes bons.                           Ex: 82.11
            'ranking_passes':  posició en el ranking de                         Ex: 12
                   'gols_ok':  nº de gols comptabilitzats en la base de dades.  Ex: 20
           'ranking_gols_ok':  posició en el ranking de gols ok.                Ex: 170
            'promig_gols_ok':  promig de gols ok.                               Ex: 0.74
  
</p>
</ol>
</p>
