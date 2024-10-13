import outils
import os
import datetime

def main (L_manager, usr):
    while True:
        print("   · Modifier ·\n",
              "\n 0. Retour",
              "\n 1. Nom de la tâche",
              "\n 2. Date d'échéance")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0": return
        
        elif choix == "1":
            print("   · Modifier ·\n",
                   outils.affiche_manager(L_manager, usr))
            choix = input("Entrez une information sur la tâche à modifier : ")
            os.system("cls")
            taches = outils.recherche(L_manager, usr, choix)
            if taches != []:
                for tache in taches:
                    while True:
                        print(f" Modifier \"{tache['nom']}\" ?\n",
                               "\n 1. Oui",
                               "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        
                        if choix == "1":
                            tache_nom = input("Saisissez le nouveau nom de la tâche : ")
                            os.system ("cls")
                            print(f" La tâche \"{tache['nom']}\" à été mise à jour !\n")
                            outils.ecriture_log(f"    MODIFIER : {tache['nom']} -> {tache_nom}\n")
                            tache["nom"] = tache_nom
                            outils.ecriture_manager(L_manager)
                            break
                        elif choix == "2":
                            print(" Action annulée...\n")
                            break
                        else:
                            print(" Choix impossible...\n")
                    break
            else:
                print(" Aucune tâche trouvée !\n")
            
        elif choix == "2":
            print("   · Modifier ·\n",
                   outils.affiche_manager(L_manager, usr))
            choix = input("Entrez une information sur la tâche à modifier : ")
            os.system("cls")
            taches = outils.recherche(L_manager, usr, choix)
            if taches != []:
                for tache in taches:
                    while True:
                        print(f" Modifier \"{tache['nom']}\" ?\n",
                               "\n 1. Oui",
                               "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        
                        if choix == "1":
                            while True:
                                tache_jour = input("Saisissez le jour d'échéance de la tâche : ")
                                os.system("cls")
                                if tache_jour.isdigit() and 0 < int(tache_jour) <= 31:
                                    break
                                print(" Format incorrect !\n")
                            while True:
                                tache_mois = input("Saisissez le mois d'échéance de la tâche : ")
                                os.system("cls")
                                if tache_mois.isdigit() and 0 < int(tache_mois) <= 12:
                                    break
                                print(" Format incorrect !\n")
                            while True:
                                tache_annee = input("Saisissez l'année d'échéance de la tâche : ")
                                os.system("cls")
                                if tache_annee.isdigit() and datetime.datetime.now().year <= int(tache_annee) <= 2100:
                                    print(f" La tâche \"{tache['nom']}\" à été mise à jour !\n")
                                    break
                                print(" Format incorrect !\n")
                            
                            tache_date = str(datetime.datetime.strptime(f"{tache_annee}-{tache_mois}-{tache_jour}", "%Y-%m-%d").date())
                            
                            outils.ecriture_log(f"    MODIFIER : {tache['date']} -> {tache_date}\n")
                            tache["date"] = tache_date
                            outils.ecriture_manager(L_manager)
                            break
                        elif choix == "2":
                            print(" Action annulée...\n")
                            break
                        else:
                            print(" Choix impossible...\n")
                    break
            else:
                print(" Aucune tâche trouvée !\n")
        
        elif choix == "13":
            print(" Bienvenue !\n",
                  "Ici, vous allez pouvoir modifier vos tâches.\n",
                  "Vous pouvez modifier leur nom ainsi que leur dâte d'échéance !\n")
        
        else:
            print(" Choix impossible...\n")