import outils
import os
import datetime

def main (L_manager, usr):
    tache_nom = ""
    tache_jour = ""
    tache_mois = ""
    tache_annee = ""
    while True:
        print ("   · Ajouter ·\n",
               "\n 0. Retour")
        if tache_nom == "":
            print ("\n OBLIGATOIRE :\n"
                   "\n 1. Nom de la tâche")
        else:
            print("\n OPTIONNEL :\n",
                  "\n 2. Date d'échéance\n",
                  "\n 3. Finaliser la tâche !")
        
        choix = input ("\nChoix : ")
        os.system ("cls")
        
        if choix == "0":
            print (" Action annulée...\n")
            return
        
        if tache_nom == "":
            if choix == "1":
                tache_nom = input ("Saisissez le nom de la tâche : ")
                os.system ("cls")
                if tache_nom != "":
                    print (f" Le nom \"{tache_nom}\" à été assigné à la tâche !\n")
                else:
                    print(" Action annulée...\n")
            elif choix == "13":
                print (" C'est ici que vous allez pouvoir créer votre tâche !\n\n",
                       "Vous devez au minimum fournir le nom de la tâche pour l'enregistrer.\n")
            else:
                print (" Choix impossible...\n")
        
        else:
            if choix == "2":
                if tache_jour == "" or tache_mois == "" or tache_annee == "":
                    if tache_jour == "":
                        while True:
                            tache_jour = input ("Saisissez le jour d'échéance de la tâche : ")
                            os.system ("cls")
                            if tache_jour.isdigit () and int(tache_jour) > 0 and int(tache_jour) <= 31:
                                print (f" Le jour \"{tache_jour}\" à été assigné à la tâche !\n")
                                break
                            print (" Format incorrect !\n")
                    if tache_mois == "":
                        while True:
                            tache_mois = input ("Saisissez le mois d'échéance de la tâche : ")
                            os.system ("cls")
                            if tache_mois.isdigit () and int(tache_mois) > 0 and int(tache_mois) <= 12:
                                print (f" Le mois \"{tache_mois}\" à été assigné à la tâche !\n")
                                break
                            print (" Format incorrect !\n")
                    if tache_annee == "":
                        while True:
                            tache_annee = input ("Saisissez l'année d'échéance de la tâche : ")
                            os.system ("cls")
                            if tache_annee.isdigit () and int(tache_annee) >= datetime.datetime.now ().year and int(tache_annee) <= 2100:
                                print (f" La date \"{tache_jour}/{tache_mois}/{tache_annee}\" à été assigné à la tâche !\n")
                                break
                            print (" Format incorrect !\n")
                else:
                    print (" La date d'échéance est déjà renseignée...\n")
            elif choix == "3":
                while True:
                    print ("   · Ajouter ·\n",
                           "\n Souhaitez-vous marquer cette tâche comme étant importante ?\n",
                           "\n 1. Oui",
                           "\n 2. Non")
                    choix = input ("\nChoix : ")
                    if choix == "1":
                        tache_favori = "True"
                        break
                    elif choix == "2":
                        tache_favori = "False"
                        break
                    os.system ("cls")
                    print (" Choix impossible...\n")
                os.system ("cls")
                
                usr["manager_md"] = int (usr["manager_md"])
                usr["manager_md"] += 1
                usr["manager_md"] = str (usr["manager_md"])
                
                if tache_annee != "":
                    tache = {"usr_id": usr["id"],
                             "id": usr["manager_md"],
                             "nom": tache_nom,
                             "date": str (datetime.datetime.strptime (f"{tache_annee}-{tache_mois}-{tache_jour}", "%Y-%m-%d").date ()),
                             "favori": tache_favori,
                             "etat": "True"}
                else:
                    tache = {"usr_id": usr["id"],
                             "id": usr["manager_md"],
                             "nom": tache_nom,
                             "date": "None",
                             "favori": tache_favori,
                             "etat": "True"}
                L_manager.append (tache)
                
                outils.ecriture_manager(L_manager)
                outils.ecriture_usr(usr)
                
                print(f" La tâche \"{tache_nom}\" a été ajouté à la liste des tâches !\n")
                outils.ecriture_log(f"    AJOUTER : {tache_nom}\n")
                return
        
            elif choix == "13":
                print (" Super ! Maintenant vous pouvez enregistrer votre tâche !\n\n",
                       "N'oubliez pas d'enregistrer une date d'échéance si vous le souhaitez.\n")
            else:
                print (" Choix impossible...\n")