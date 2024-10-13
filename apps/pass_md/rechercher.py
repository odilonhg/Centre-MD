import outils
import os

def main(L_pass, usr):
    print("   · Rechercher ·\n")
    mdp = input("Saisissez une information sur le mot de passe à trouver : ")
    outils.ecriture_log(f"    RECHERCHER : {mdp}\n")
    os.system("cls")
    L_pass_recherche = outils.recherche(L_pass, usr, mdp)
    contenu = outils.affiche_pass(L_pass_recherche, usr)
    if contenu != "":
        print("   · Rechercher ·\n", contenu)
    else:
        print(" Aucun mot de passe trouvé !\n")