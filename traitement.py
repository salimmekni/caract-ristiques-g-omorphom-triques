"""
- Création d'une carte aléatoire
- Périmetre : Circulaire
- Pour un pixel :
    a) On calcul Altitude_moyenne
    b) V = Altitude - Altitude_moyenne
    c) On va mettre ces infos dans une meme liste :
          Pour chaque Pixel (case):
            - sa valeur V
            - ses coordonnées
            - Sa prochaine couleur (initialement "")
          Exemple : [[2,[50,48],"Rouge"],[5,[78,100],"Jaune"]]
-  Attribution des nouveaux couleurs
    a) Tri du tableau
    b) On divise le tableau par 6 séquences :
       Couleurs : Rouge,Orange,Jaune,Vert,Cyan,Bleu
       La premiere sequance (les points les plus basses) aura la
       couleur Rouge, la derniere séquence (les points les plus hauts) aura la couelur Bleu
"""
import math
import numpy as np

def traitement(altitude: list):
    # init
    Liste = []

    rayon = 10

    def mask_circulaire(rayon):
        masque_carre = np.zeros((rayon*2+1, rayon*2+1))
        masque = []
        taille = masque_carre.shape[0]
        centre_x = rayon + 1
        centre_y = centre_x
        for i in range(taille):
            masque_tempo = []
            for j in range(taille):
                #print((centre_x-i-1), (centre_y-j-1))
                #print("rayon :", math.sqrt((centre_x-i-1)**2+(centre_y-j-1)**2))
                if math.sqrt((centre_x-i-1)**2+(centre_y-j-1)**2) <= rayon:
                    masque_tempo.append(1)
                else:
                    masque_tempo.append(0)
            masque.append(masque_tempo)
        #print(masque_carre)
        #print(masque)
        return masque

    def produit_mat_terme_a_terme(altitude, masque):
        #print(altitude.shape, len(masque), len(masque[0]))
        #print(altitude)
        #print(masque)
        taille = len(masque)
        taille2 = len(masque[0])
        produit = []
        for i in range(taille):
            ligne = []
            for j in range(taille2):
                ligne.append(altitude[i][j]*masque[i][j])
            produit.append(ligne)
        return produit

    def calcul_diff(altitude, x, y, rayon, masque):

        print(x, y)

        if (x - rayon > 0):
            xmin = x - rayon
        else:
            xmin = 0
            # correction du masque dans le cas où l'on est trop près du bord haut
            """print("correction haut")"""
            masque = masque[rayon-x:]
        if (x + rayon < altitude.shape[0]):
            xmax = x + rayon
        else:
            xmax = altitude.shape[0]
            # correction du masque dans le cas où l'on est trop près du bord bas
            """print("correction bas")"""
            masque = masque[:xmax-x+rayon]
        if (y - rayon > 0):
            ymin = y - rayon
        else:
            ymin = 0
            # correction du masque dans le cas où l'on est trop près du bord gauche
            """print("correction gauche")"""
            nouveau_masque = []
            for ligne in masque:
                ligne = ligne[rayon-y:]
                nouveau_masque.append(ligne)
            masque = nouveau_masque
        if (y + rayon < altitude.shape[1]):
            ymax = y + rayon
        else:
            ymax = altitude.shape[1]
            # correction du masque dans le cas où l'on est trop près du bord droit
            """print("correction droite")"""
            nouveau_masque = []
            for ligne in masque:
                ligne = ligne[:ymax-y+rayon]
                nouveau_masque.append(ligne)
            masque = nouveau_masque
        xmax += 1
        ymax += 1
        S = 0
        """if len(masque) != altitude[xmin:xmax, ymin:ymax].shape[0] or len(masque[0]) != altitude[xmin:xmax, ymin:ymax].shape[1]:
            print("problème")"""
        produit = produit_mat_terme_a_terme(altitude[xmin:xmax, ymin:ymax], masque)

        """print(xmax-xmin)
        print(ymax-ymin)"""
        for i in range(len(produit)):
            for j in range(len(produit[0])):
                S = S + produit[i][j]

        V = altitude[i][j] - S / (i * j)

        # mettre dans une liste
        Liste.append([V, [x, y], ""])

    def trier_liste(liste: list):
        for i in range(len(liste)):
            j = i
            while j > 0 and liste[j][0] < liste[j - 1][0]:
                var_tempo = liste[j]
                liste[j] = liste[j - 1]
                liste[j - 1] = var_tempo
                j -= 1
        return liste

    def attribution_couleur(liste: list):
        for i in range(len(liste)):
            if (i <= (len(liste)) // 6):
                liste[i][2] = "Rouge"
            elif (i <= (2 * len(liste)) // 6):
                liste[i][2] = "Orange"
            elif (i <= (3 * len(liste)) // 6):
                liste[i][2] = "Jaune"
            elif (i <= (4 * len(liste)) // 6):
                liste[i][2] = "Vert"
            elif (i <= (5 * len(liste)) // 6):
                liste[i][2] = "Cyan"
            else:
                liste[i][2] = "Bleu"

        return liste

    masque = mask_circulaire(rayon)

    for i in range(0, altitude.shape[0]):
        for j in range(0, altitude.shape[1]):
            calcul_diff(altitude, i, j, rayon, masque)

    Liste = trier_liste(Liste)
    Liste = attribution_couleur(Liste)

    return Liste




