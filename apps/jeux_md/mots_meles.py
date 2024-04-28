import random
import string
import os

mots = [
    "python",
    "programmation",
    "intelligence",
    "algorithmique",
    "ordinateur",
    "développeur",
    "apprentissage",
    "machine",
    "réseau",
    "internet",
    "données",
    "cryptographie",
    "sécurité",
    "analyse",
    "débogage",
    "interface",
    "utilisateur",
    "gestionnaire",
    "système",
    "exploitation"
]

# Fonction pour générer aléatoirement une liste de mots à trouver
def generer_mots(nb_mots, longueur_max, liste_mots):
    mots = []
    while len(mots) < nb_mots:
        mot = random.choice(liste_mots)
        if len(mot) <= longueur_max and mot not in mots:
            mots.append(mot)
    return mots

# Fonction pour générer aléatoirement une liste de mots à trouver
def generer_mots(nb_mots, longueur_max, liste_mots):
    mots = []
    while len(mots) < nb_mots:
        mot = random.choice(liste_mots)
        if len(mot) <= longueur_max and mot not in mots:
            mots.append(mot)
    return mots

# Fonction pour créer une grille de mots mêlés
def creer_grille(mots):
    # Déterminer la taille de la grille en fonction du nombre de mots et de leur longueur
    max_longueur_mot = max(len(mot) for mot in mots)
    taille_grille = max(len(mots) * max_longueur_mot, 4)

    # Générer une grille vide
    grille = [[' ' for _ in range(taille_grille)] for _ in range(taille_grille)]

    # Insérer les mots à trouver dans la grille de manière aléatoire
    for mot in mots:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, taille_grille - len(mot))
            y = random.randint(0, taille_grille - 1)
            for i, lettre in enumerate(mot):
                grille[y][x + i] = lettre
        elif orientation == 'vertical':
            x = random.randint(0, taille_grille - 1)
            y = random.randint(0, taille_grille - len(mot))
            for i, lettre in enumerate(mot):
                grille[y + i][x] = lettre

    # Remplir les espaces vides de la grille avec des lettres aléatoires
    lettres_possibles = string.ascii_lowercase
    for i in range(taille_grille):
        for j in range(taille_grille):
            if grille[i][j] == ' ':
                grille[i][j] = random.choice(lettres_possibles)

    return grille

# Afficher la grille
def afficher_grille(grille):
    for ligne in grille:
        print(' '.join(ligne))
    print()

# Fonction principale pour jouer au jeu de mots mêlés
def mots_meles(nb_mots, longueur_max):
    mots_a_trouver = generer_mots(nb_mots, longueur_max, mots)
    print("Bienvenue dans le jeu des mots mêlés !")
    print("Vous devez trouver les mots cachés dans la grille de lettres.\n")

    grille = creer_grille(mots_a_trouver)
    afficher_grille(grille)

    print("Nombre de mots à trouver :", len(mots_a_trouver))

    mots_trouves = set()
    while len(mots_trouves) < len(mots_a_trouver):
        mot_trouve = input("Entrez un mot trouvé (ou 'q' pour quitter) : ").lower()
        if mot_trouve == 'q':
            os.system ("cls")
            print("Merci d'avoir joué ! À la prochaine.\n")
            return
        if mot_trouve in mots_a_trouver:
            os.system ("cls")
            print(f"Bravo ! Vous avez trouvé le mot {mot_trouve} !\n")
            mots_trouves.add(mot_trouve)
            afficher_grille(grille)
        else:
            os.system ("cls")
            print("Désolé, ce n'est pas le bon mot.\n")
            afficher_grille(grille)
    
    os.system ("cls")
    print("Félicitations ! Vous avez trouvé tous les mots dans la grille.\n")
    return