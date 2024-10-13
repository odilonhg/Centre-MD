import outils
import os

def main(L_rep, usr):
    contenu = outils.affiche_rep(L_rep, usr)
    if contenu != "":
        print("   · Afficher ·\n", "\n * = Contact favori\n", contenu)
        outils.ecriture_log("    AFFICHER\n")
    else:
        print(" Vous n'avez pas encore créé de contact !\n")