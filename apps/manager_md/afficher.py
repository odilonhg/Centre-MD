import outils
import os

def main(L_manager, usr):
    contenu = outils.affiche_manager(L_manager, usr)
    
    if contenu != "":
        print("   · Afficher ·\n",
              "* = Tâche importante !")
        print(contenu)
        outils.ecriture_log("    AFFICHER\n")
    
    else:
        print(" Vous n'avez pas encore créé de tâche !\n")