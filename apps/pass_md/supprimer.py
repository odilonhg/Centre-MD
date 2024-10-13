import outils
import os

def main(L_pass, usr):
    print("   · Supprimer ·\n")
    mdp = input("Saisissez une information sur le mot de passe à supprimer : ")
    os.system("cls")
    L_pass_recherche = outils.recherche(L_pass, usr, mdp)
    for mdp in L_pass_recherche:
        while True:
            print("   · Supprimer ·\n",
                  f"\n Voulez-vous supprimer \"{mdp['nom']}\" ?\n",
                  "\n 1. Oui",
                  "\n 2. Non")
            choix = input("\nChoix : ")
            os.system("cls")
            if choix == "1":
                L_pass.remove(mdp)
                outils.ecriture_pass(L_pass)
                print(f" Le mot de passe de l'intitulé \"{mdp['nom']}\" a été supprimé avec succès...\n")
                outils.ecriture_log(f"    SUPPRIMER : {mdp['nom']}\n")
                break
            elif choix == "2":
                break
            else:
                print(" Choix impossible...\n")
        if choix == "1":
            break