import outils
import os

def main(usr):
    from apps.rep_md.main import F_rep
    L_rep = outils.lecture_CSV(F_rep)
    nom = usr["nom"]
    while True:
        print("   · Jeux MD ·\n",
              "\n 0. Retour",
              "\n 1. Le Chiffre Juste",
              "\n 2. Le Pendu")
        
        choix = input ("\nChoix : ")
        os.system ("cls")
        
        if choix == "0":
            return
        
        elif choix == "1":
            from apps.jeux_md.chiffre_juste import main
            main(nom)
        elif choix == "2":
            from apps.jeux_md.pendu import main
            main(nom, L_rep, usr)
#         elif choix == "3":
#             from apps.jeux_md.puissance4 import main
#             main(nom, L_rep, usr)
#         elif choix == "4":
#             from apps.jeux_md.morpion import main
#             main(nom, L_rep, usr)
#         elif choix == "5":
#             from apps.jeux_md.mots_meles import main
#             main(nom)
#         elif choix == "6":
#             from apps.jeux_md.colonisation_md import main
#             main(usr, L_rep)
        
        elif choix == "13":
            print(" Bienvenue dans les Jeux MD !\n",
                  "\n Ici, vous allez pouvoir jouer à des jeux.",
                  "\n N'hésitez pas à essayer nos jeux !\n",
                  "\n  - Le Chiffre Juste : Un jeu dans lequel tu dois trouver un nombre entre 0 et 100",
                  "\n  - Le Pendu : Un classique, je le présente pas !\n",)
#                   "\n  - Le Puissance 4 : Vous voulez vraiment que je vous explique ? (à deux)",
#                   "\n  - Le Morpion : Un jeu de stratégie olala (à deux)",
#                   "\n  - Mots Mêlés : Retrouve les mots cachés !",
#                   "\n  - Colinisation MD : Mon jeu à moi !\n")
        else:
            print(" Choix impossible...\n")