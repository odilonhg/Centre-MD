import logging
import os

j1 = ""
j2 = ""

def creer_grille():
    grille = [["0"] * 7 for _ in range(6)]
    return grille

def ajouter_pion(grille, joueur):
    global j1, j2
    
    if joueur == "1":
        print (f"Au tour de {j1} !")
    elif joueur == "2":
        print (f"Au tour de {j2} !")
    
    colonne = int(input("Choisissez votre colonne (1-7) : ")) - 1
    print ()

    if colonne < 0 or colonne > 6:
        print("Choix Impossible...")
        return False

    for i in range(5, -1, -1):
        if grille[i][colonne] == "0":
            grille[i][colonne] = joueur
            return True

    print("Colonne pleine. Veuillez choisir une autre colonne.")
    return False

def afficher_grille(desc, grille):
    
    for val in desc:
        print("{:4}".format(val), end="")
    print("\n")

    for ligne in grille:
        for val in ligne:
            print("{:4}".format(val), end="")
        print()
    print()

def verifier_victoire(grille, joueur):
    
    for ligne in grille:
        for j in range(4):
            if all(ligne[j + k] == joueur for k in range(4)):
                return True
            
    for j in range(7):
        for i in range(3):
            if all(grille[i + k][j] == joueur for k in range(4)):
                return True
            
    for i in range(3):
        for j in range(4, 7):
            if all(grille[i + k][j - k] == joueur for k in range(4)):
                return True
            
    for i in range(3):
        for j in range(4):
            if all(grille[i + k][j + k] == joueur for k in range(4)):
                return True

    return False

def puissance_4():
    global j1, j2
    
    j1 = input ("Joueur 1, saisissez votre nom : ").capitalize ()
    os.system ("cls")
    j2 = input ("Joueur 2, saisissez votre nom : ").capitalize ()
    print ()
    grille = creer_grille()
    ligne1 = ['1', '2', '3', '4', '5', '6', '7']
    joueurs = ['1', '2']
    tour = 0
    
    logging.info ("    OUVERTURE JEU: Puissance 4\n")

    while True:
        os.system ("cls")
        joueur = joueurs[tour % 2]
        afficher_grille(ligne1, grille)
        
        if ajouter_pion(grille, joueur):
            if verifier_victoire(grille, joueur):
                
                afficher_grille(ligne1, grille)
                if joueur == "1":
                    joueur = j1
                elif joueur == "2":
                    joueur = j2
                print(f"Le joueur \"{joueur}\" a gagné !\n")
                logging.info (f"    VICTOIRE DU JOUEUR \"{joueur}\" !\n")
                logging.info ("    FERMETURE JEU: Puissance 4\n")
                return ""
            
            tour += 1
            
        else:
            continue