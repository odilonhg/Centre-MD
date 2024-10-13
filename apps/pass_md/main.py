import outils
import os

F_pass = "data_pass.csv"

def main(usr):
    while True:
        if os.path.exists(F_pass):
            L_pass = outils.lecture_CSV(F_pass)
        else:
            print(" Bienvenue dans Pass MD !\n"
                  "\n Ici, vous pourrez gérer vos mots de passe et les consulter à tout moment.",
                  "\n Tapez \"1\" pour créer votre 1er mot de passe !\n")
            L_pass = []
        print("   · Pass MD ·\n",
              "\n 0. Retour",
              "\n 1. Ajouter",
              "\n 2. Rechercher",
              "\n 3. Afficher",
              "\n 4. Modifier",
              "\n 5. Supprimer")
        
        choix = input ("\nChoix : ")
        os.system ("cls")
        
        if choix == "0": return
        
        elif choix == "1":
            from apps.pass_md.ajouter import main
            main(L_pass, usr)
        elif choix == "2":
            from apps.pass_md.rechercher import main
            main(L_pass, usr)
        elif choix == "3":
            from apps.pass_md.afficher import main
            main(L_pass, usr)
        elif choix == "4":
            from apps.pass_md.modifier import main
            main(L_pass, usr)
        elif choix == "5":
            from apps.pass_md.supprimer import main
            main(L_pass, usr)
        
        elif choix == "13":
            print(" Bienvenue dans Pass MD !\n"
                  "\n Ici, vous pourrez gérer vos mots de passe et les consulter à tout moment.",
                  "\n Tapez \"1\" pour créer votre 1er mot de passe !\n")
        else:
            print(" Choix impossible...\n")