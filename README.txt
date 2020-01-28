README -ohje ohjelman ajamiseen-

Nimi:       Opiskelija nro.     sähköposti:
Emil Dark   2564926             edark18@student.oulu.file

Ohjelman toimiaksi oikein testidata tiedoston sekä itse ohjelma 
tiedostot (main.py ja weightedgraph.py) täytyy olla samassa 
kansiossa. (testidata tiedosto nimeä annettaessa ohjelma vaatii,
että sen perästä löytyy .txt)

Ohjelma on ohjelmoitu python 3.6.0 
käytetyt kirjastot: - math
                    - collections: deque ja defaultdict
                    - time
                    
Ohjelma käynnistetään käskyllä 
    -python main.py
,jonka jälkeen ohjelma kysyy testidata tiedoston nimeä
    -Type filename: (esim. graph_ADS2018_200.txt)
    
Ohjelman tulostus:
    
PARAMETERS
        Endpoint: 200                       #Ohjelman tunnistama loppupiste
        Edges to add to graph: 8256         #Tiedoston ilmoittama reuna määrä
        Edges added to the graph: 8256      #Kuinka monta reunaa ohjelma lisäsi

KRUSKAL - CREATE MST
        Following are the edges in the constructed MST  #ohjelma kykenee tulostamaa MST reunat, ohjeet alhaalla*

DIJKSTRA - FIND SHORTEST PATH
         Path from 1 to 200 with cumulative weights:    #Polku pisteiden välillä mikä halutaan löytää
         1 : 0  + 0                                     #Piste: polun yht. paino + seuraavaan paino
         15 : 119  + 119                                
         60 : 192  + 73
         72 : 282  + 90
         119 : 376  + 94
         84 : 458  + 82
         127 : 520  + 62
         88 : 601  + 81
         77 : 662  + 61
         31 : 734  + 72
         70 : 792  + 58
         65 : 851  + 59
         51 : 903  + 52
         54 : 982  + 79                     #Löydetty polku luetaan ensimmäiseltä riviltä ylhäältä alas
         35 : 1041  + 59                    #Tässä datassa se on:
         30 : 1092  + 51                    #1->15->60->72->119->84->127->88->77->31->70->..jne..->200
         21 : 1149  + 57
         39 : 1233  + 84
         19 : 1317  + 84
         38 : 1407  + 90
         37 : 1496  + 89
         28 : 1586  + 90
         48 : 1669  + 83
         89 : 1760  + 91
         129 : 1818  + 58
         151 : 1903  + 85
         200 : 1964  + 61
         Heaviest edge is:  119             #ohjelman löytämä korkein reuna

--- 0.10388016700744629 seconds ---         #ohjelman ajamiseen kestänyt aika

*Debug:    
    Ohjelma pystyy tulostamaan Minimum spanning tree reunat jos
    kommetti merkin (#) poistaa main.py riviltä 98
                        
