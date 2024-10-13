import outils
import os

def main(L_manager, usr):
    print("   · Modifier ·\n",
          outils.affiche_manager(L_manager, usr))
    choix = input("Entrez une information sur la tâche à modifier : ")
    os.system ("cls")
    taches = outils.recherche(L_manager, usr, choix)
    
    if taches != []:
        for tache in taches:
            while True:
                print(f" Finir \"{tache['nom']}\" ?\n",
                       "\n 1. Oui",
                       "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                
                if choix == "1":
                    tache["etat"] = "False"
                    print(f" La tâche \"{tache['nom']}\" à été marquée comme terminée !\n")
                    outils.ecriture_log(f"    FINIR : {tache['nom']}\n")
                    outils.ecriture_manager(L_manager)
                    break
                elif choix == "2":
                    print(" Action annulée...\n")
                    break
                else:
                    print(" Choix impossible...\n")
    else:
        print (" Aucune tâche trouvée !\n")