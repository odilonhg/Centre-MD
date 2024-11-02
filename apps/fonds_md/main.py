import outils
import os

base = os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD")
F_fonds = os.path.join(base, "data_fonds.csv")

def main(usr):
    while True:
        if os.path.exists(F_fonds):
            L_fonds = outils.lecture_fonds(F_fonds)
        else:
            print(" Bienvenue dans les Fonds MD !\n",
                  "\n Ici vous allez pouvoir créer des comptes permettant la gestion de votre argent !",
                  "\n Pour commencer tapez \"1\" pour ajouter votre première arrivée d'argent sur votre compte !!",
                  "\n Ensuite, vous pourrez tapez \"3\" si vous souhaitez afficher l'argent de votre compte.\n")
            L_fonds = []
        print("   · Fonds MD ·\n",
              "\n 0. Retour",
              "\n 1. Ajouter",
              "\n 2. Retirer",
              "\n 3. Afficher")
        
        choix = input ("\nChoix : ")
        os.system ("cls")
        
        if choix == "0": return
        
        elif choix == "1":
            from apps.fonds_md.ajouter import main
            main(L_fonds, usr)
        elif choix == "2":
            from apps.fonds_md.retirer import main
            main(L_fonds, usr)
        elif choix == "3":
            from apps.fonds_md.afficher import main
            main(L_fonds, usr)
        
        elif choix == "13":
            print(" Bienvenue dans les Fonds MD !\n",
                  "\n Ici vous allez pouvoir créer des comptes permettant la gestion de votre argent !",
                  "\n Pour commencer tapez \"1\" pour ajouter votre première arrivée d'argent sur votre compte !!",
                  "\n Ensuite, vous pourrez tapez \"3\" si vous souhaitez afficher l'argent de votre compte.\n")
        else:
            print(" Choix impossible...\n")