import outils
import os

def main(L_rep, usr):
    print("   · Rechercher ·\n")
    contact = input("Saisissez une information sur le contact / groupe à trouver : ")
    outils.ecriture_log(f"    RECHERCHER : {contact}\n")
    os.system("cls")
    L_rep_recherche = outils.recherche(L_rep, usr, contact)
    for contact in L_rep_recherche:
        if contact["nom_groupe"] != "":
            L_rep_recherche = outils.recherche(L_rep, usr, contact["id"])
            break
        contact["groupes"] = ""
    contenu = outils.affiche_rep(L_rep_recherche, usr)
    if contenu != "":
        print("   · Rechercher ·\n", contenu)
    else:
        print(" Aucun contact / groupe trouvé !\n")