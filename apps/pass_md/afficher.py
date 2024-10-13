import outils
import os

def main(L_pass, usr):
    contenu = outils.affiche_pass(L_pass, usr)
    if contenu != "":
        print("   · Afficher ·\n", contenu)
        outils.ecriture_log("    AFFICHER\n")
    else:
        print(" Vous n'avez pas encore créé de mot de passe !\n")