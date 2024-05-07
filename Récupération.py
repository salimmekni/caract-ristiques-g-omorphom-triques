"""
Préparation de la carte :
  - on eneleve les bords s'il y en a
  - On sépare la légende de la carte (on genere une           nouvelle image pour l'echelle)

Calcul de l'altitude :
Rq : l'echelle de notre carte et celui de La bibliotheque rasterio n'est pas le meme

  -Vrai Altitude d'un pixel=
(Altitude_bib * Max_notre_echelle)/Max_echelle_bib

Input : Carte avec légende

output : 1) Carte sans bords ni échelle
         2) Matrice des altitudes
"""
import rasterio
from rasterio.plot import show

def récupération():
    map = rasterio.open('estuaryimg_geog.tif', 'r')
    #show(map)
    altitude = map.read(1)
    """for i in range(3282, 3290):
        for j in range(5000, 5010):
            if (altitude[i][j] != 0):
                print(altitude[i, j], end=" | ")"""

    return altitude



