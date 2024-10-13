import outils
import os

F_manager = "data_manager.csv"
F_manager_v1 = "data_gdt"

def main(usr):
    while True:
        if os.path.exists(F_manager):
            L_manager = outils.lecture_CSV(F_manager)
        else:
            L_manager = []
            print(" Bienvenue dans le Manager MD !\n",
                  "\n Ici, vous pouvez créer des tâches et les accomplir.",
                  "\n Vous pouvez aussi les consulter et voir leurs dates d'échéance à tout moment !\n",
                  "\n Pour créer votre première tâche, tapez \"1\" pour \"Ajouter\" une tâche !\n")
        
        print("   · Manager MD ·\n",
              "\n 0. Retour",
              "\n 1. Ajouter",
              "\n 2. Afficher",
              "\n 3. Modifier",
              "\n 4. Finir")
        
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0": return
        
        elif choix == "1":
            from apps.manager_md.ajouter import main
            main(L_manager, usr)
        elif choix == "2":
            from apps.manager_md.afficher import main
            main(L_manager, usr)
        elif choix == "3":
            from apps.manager_md.modifier import main
            main(L_manager, usr)
        elif choix == "4":
            from apps.manager_md.finir import main
            main(L_manager, usr)
        
        elif choix == "13":
            print(" Bienvenue dans le Manager MD !\n",
                  "\n Ici, vous pouvez créer des tâches et les accomplir.",
                  "\n Vous pouvez aussi les consulter et voir leurs dates d'échéance à tout moment !\n",
                  "\n Pour créer votre première tâche, tapez \"1\" pour \"Ajouter\" une tâche !\n")
        else:
            print(" Choix impossible...\n")