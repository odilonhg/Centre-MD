import outils
import os

base = os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD")
F_rep = os.path.join(base, "data_rep.csv")

def main(usr):
    while True:
        if os.path.exists(F_rep):
            L_rep = outils.lecture_CSV(F_rep)
        else:
            L_rep = []
            print(" Bienvenue dans le Rep MD !\n",
                  "\n Ici, vous pouvez créer des contacts, des groupes.",
                  "\n Vous pouvez aussi consulter les anniversaires de vos contacts !\n",
                  "\n Pour créer votre premier contact, tapez \"1\" pour \"Ajouter\" un contact !\n")
        print("   · Rep MD ·\n",
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
            print("   · Ajouter ·\n",
                  "\n 1. Contacts",
                  "\n 2. Groupes")
            choix = input("\nChoix : ")
            os.system("cls")
            from apps.rep_md.ajouter import main
            if choix == "1":
                main("contacts", L_rep, usr)
            elif choix == "2":
                main("groupes", L_rep, usr)
            else: print(" Choix impossible...\n")
        elif choix == "2":
            from apps.rep_md.rechercher import main
            main(L_rep, usr)
        elif choix == "3":
            from apps.rep_md.afficher import main
            main(L_rep, usr)
        elif choix == "4":
            from apps.rep_md.modifier import main
            main(L_rep, usr)
        elif choix == "5":
            from apps.rep_md.supprimer import main
            main(L_rep, usr)
        
        elif choix == "13":
            print(" Bienvenue dans le Rep MD !\n",
                  "\n Ici, vous pouvez créer des contacts, des groupes.",
                  "\n Vous pouvez aussi consulter les anniversaires de vos contacts !\n",
                  "\n Pour créer votre premier contact, tapez \"1\" pour \"Ajouter\" un contact !\n")
        else:
            print(" Choix impossible...\n")