"""
On colore la map par les nouvelles couleurs pixel par pixel
Input : Carte normale
Output: Carte colorée
"""
import matplotlib.pyplot as plt

def viz(matrice, liste: list):
    # Creation d'une carte vide
    def creer_carte_vide(matrice: list):
        carte = []
        pixel_vide = [0, 0, 0]
        for i in range(matrice.shape[0]):
            ligne = []
            for j in range(matrice.shape[1]):
                ligne.append(pixel_vide)
            carte.append(ligne)
        return carte

    # Coloration du pixel
    def couleur_en_rgb(couleur: str):
        if couleur == "Rouge":
            couleur_rgb = [255, 0, 0]
        elif couleur == "Orange":
            couleur_rgb = [243, 96, 17]
        elif couleur == "Jaune":
            couleur_rgb = [243, 236, 17]
        elif couleur == "Vert":
            couleur_rgb = [73, 243, 17]
        elif couleur == "Cyan":
            couleur_rgb = [17, 243, 234]
        elif couleur == "Bleu":
            couleur_rgb = [17, 53, 243]
        return couleur_rgb

    def colorer_pixel(carte: list, pixel_coords: list, couleur: str):
        color = couleur_en_rgb(couleur)
        coord_x = pixel_coords[0]
        coord_y = pixel_coords[1]
        carte[coord_x][coord_y] = color
        return carte

    # Affichage de la carte
    def afficher_carte(carte: list):
        plt.matshow(carte)
        plt.title("Carte")
        plt.show()

    carte = creer_carte_vide(matrice)

    for i in range(len(liste)):
        colorer_pixel(carte, liste[i][1], liste[i][2])

    afficher_carte(carte)