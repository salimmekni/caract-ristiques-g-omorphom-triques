import numpy as np

from Récupération import récupération
from traitement import traitement
from visualisation import viz

import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import math

def main():
  # on récupere la matrice des altitudes
  matricee = récupération()
  """taille = 200
  matrice = np.zeros((taille + 1, taille + 1))
  for i in range(taille + 1):
    for j in range(taille + 1):
      matrice[i][j] = matricee[i + 4510][j + 2010]"""
  # Liste est une liste de liste, chaque element correspond a un pixel, pour lequel on a : ses coordonnées , sa valeur de différance d atltitude ainsi que sa prochaine couleur
  Liste = traitement(matricee)

  # visualisation de la liste
  viz(matricee, Liste)

main()
