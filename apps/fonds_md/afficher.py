import outils
import os
import datetime

def main(L_fonds, usr):
    outils.ecriture_log("    AFFICHER\n")
    aujourdhui = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    argent_restant, historique = outils.affiche_fonds(L_fonds, usr)
    print("   · Afficher ·\n",
          f"\n {aujourdhui}\n")
    print(f" | Il vous reste {str(argent_restant)}€ sur votre compte !\n")
    print(" Voulez-vous voir l'historique des opérations\n effectuées sur votre compte ?\n",
          "\n 1. Oui",
          "\n 2. Non")
    choix = input("\nChoix : ")
    os.system("cls")
    if choix == "1":
        print("   · Afficher ·\n",historique)