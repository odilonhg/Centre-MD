from logging import info
from os import system

def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-----")

def verifier_victoire(plateau, joueur):
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(joueur) == 3:
            return True

    # Vérifier les colonnes
    for i in range(3):
        if [plateau[j][i] for j in range(3)].count(joueur) == 3:
            return True

    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True

    return False

def morpion():
    info("    OUVERTURE JEU: Morpion\n")

    plateau = [[" "]*3 for _ in range(3)]
    joueurs = ["X", "O"]
    noms_joueurs = []

    for i in range(2):
        nom = input(f"Nom du joueur {i+1}: ")
        noms_joueurs.append(nom)
        system ("cls")

    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur_actuel = joueurs[tour % 2]

        print(f"\nC'est au tour de {noms_joueurs[tour % 2]} ({joueur_actuel}) de jouer.\n")

        while True:
            try:
                ligne = int(input("Choisissez la ligne (1-3) : ")) - 1
                colonne = int(input("Choisissez la colonne (1-3) : ")) - 1
                print()
                if plateau[ligne][colonne] == " ":
                    plateau[ligne][colonne] = joueur_actuel
                    system ("cls")
                    break
                else:
                    system ("cls")
                    print("Cette case est déjà occupée !\n")
            except (ValueError, IndexError):
                system ("cls")
                print("Veuillez entrer des coordonnées valides !\n")
                break

        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            system ("cls")
            print(f"Le joueur {noms_joueurs[tour % 2]} a gagné !\n")
            info(f"    VICTOIRE DU JOUEUR \"{noms_joueurs[tour % 2]}\" !\n                        FERMETURE JEU: Morpion\n")
            break

        if all(all(cell != " " for cell in ligne) for ligne in plateau):
            afficher_plateau(plateau)
            system ("cls")
            print("Match nul !\n")
            info("    MATCH NUL !\n                        FERMETURE JEU: Morpion\n")
            break

        tour += 1