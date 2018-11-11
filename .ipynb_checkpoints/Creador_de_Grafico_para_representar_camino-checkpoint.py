from Lector_Cordenadas import *
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

def Dibujar_Grafo_Camino(lati, loni, camlat, camlon):
    output_file("gmap.html")
    map_options = GMapOptions(lat=-12.0431800, lng=-77.0282400, map_type="roadmap", zoom=5)
    # For GMaps to function, Google requires you obtain and enable an API key:
    #
    #     https://developers.google.com/maps/documentation/javascript/get-api-key
    #
    # Replace the value below with your personal API key:
    p = gmap("AIzaSyDf3f-fQDqjQo1Dr5WSO0FDO_nM-HA3qV4", map_options, title="Austin")
    #IMPORTANTE: Profesor, si cuenta con algun error al momento de visualizar el grafico, por favor
    #coloque su API key personal como primer parametro de la función que se esta llamando en la linea
    #de codigo anterior.
    source = ColumnDataSource(
        data=dict(lat=lati,
                  lon=loni))

    p.circle(x="lon", y="lat", size=10, fill_color="black", fill_alpha=0.8, source=source)
    p.line(camlon,camlat,line_color="red")
    show(p)

def Realizar_camino(lati, loni, camino):
    camlat = []
    camlon = []
    for i in camino:
        camlat.append(lati[i])
        camlon.append(loni[i])
    Dibujar_Grafo_Camino(lati, loni, camlat, camlon)

def Graficar(filename, camino):
    loni = []
    lati = []
    if (filename == "Grafo_25_Capitales_Regionales.txt"):
        loni,lati = Retorna_Cords_Criterio(1)
    elif (filename == "Grafo_171_Capitales_Provinciales.txt"):
        loni,lati = Retorna_Cords_Criterio(2)
    elif (filename == "Grafo_1678_Capitales_Distritales.txt"):
        loni,lati = Retorna_Cords_Criterio(3)
    elif (filename == "Grafo_75512_CentrosEducativos.txt"):
        loni,lati = Retorna_Cords_Criterio(4)
    elif (filename == "Grafo_145225_CentrosPoblados.txt"):
        loni,lati = Retorna_Cords_Criterio(0)
    Realizar_camino(lati, loni, camino)
    
