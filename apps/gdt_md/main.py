from datetime import datetime, time
from os import system
from outils import lecture_pickle, ecriture_pickle

f_gdt = "data_gdt"
l_taches = []

def tps_tache (date):
    date_debut = datetime.now()
    date_fin = date
    date_fin = datetime.combine(date_fin, time.min)
    temps_restant = date_fin - date_debut
    jours_restants = temps_restant.days
    heures_restantes = temps_restant.seconds // 3600
    minutes_restantes = (temps_restant.seconds % 3600) // 60
    temps_restant = str(jours_restants) + ":" + str(heures_restantes) + ":" + str(minutes_restantes)
    return temps_restant

def afficher (l_taches):
    nbr_taches = 0
    lst_taches = ""
    
    for i, tache in enumerate (l_taches, start = 1):
        tps_restant = tps_tache (tache["date_maxi"])
        if tache["etat"] == True:
            lst_taches += f"\n{i}.   | {tache['description']}\n     | Date d'échéance : {tache['date_maxi']}\n     | Temps restant : {tps_restant}"
            nbr_taches += 1
        else:
            lst_taches += f"\n{i}. * | {tache['description']}\n     | Date d'échéance : {tache['date_maxi']}\n     | Temps restant : {tps_restant}"
            nbr_taches += 1
    
    if nbr_taches != 0:
        print ("   · Liste des Tâches ·")
        print ("* = tâche terminée")
        print (lst_taches)
    else:
        print ("Aucune tâche trouvée !")

def ajouter (description, date_maxi, l_taches):
    nouvelle_tache = {"description": description, "date_maxi": date_maxi, "etat": True}
    l_taches.append (nouvelle_tache)
    print ("Tâche ajoutée avec succès !\n")

def rechercher (desc, l_taches):
    nbr_taches = 0
    lst_taches = ""
    
    for i in range (len (l_taches)):
        if desc.lower () == l_taches[i]["description"].lower ():
            tps_restant = tps_tache (l_taches[i]["date_maxi"])
            lst_taches += f"\n  | {l_taches[i]['description']}\n  | Date d'échéance : {l_taches[i]['date_maxi']}\n  | Temps restant : {tps_restant}"
            nbr_taches += 1
    
    if nbr_taches != 0:
        print ("   · Tâches trouvées ·")
        print (lst_taches + "\n")
    else:
        print ("Aucune tâche trouvée !\n")

def finir (description, liste_taches):
    for tache in liste_taches:
        desc = tache["description"]
        if description.lower () == desc.lower ():
            choix = input (f"Vous confirmez vouloir mettre fin à la tâche \"{desc}\" : ").lower ()
            
            if choix == "oui":
                tache["etat"] = False
                return print ("Tâche marquée comme terminée !\n")
            else:
                print ()
    
    print ("Aucune tâche trouvée !\n")

def supprimer (l_taches):
    new_liste = []
    for i in range (len (l_taches)):
        if l_taches[i]["etat"] == True:
            new_liste.append (l_taches[i])
    ecriture_pickle (new_liste, f_gdt)

def gdt_md ():
    global l_taches
    try: l_taches = lecture_pickle (f_gdt)
    
    finally:
        print ("   · GDT MD ·\n")
        
        print (" 0. Retour")
        print (" 1. Ajouter")
        print (" 2. Rechercher")
        print (" 3. Afficher")
        print (" 4. Finir")
        print (" 5. Supprimer\n")
        
        choix = input ("Choix : ")
        
        match choix:
            
            case "0": return
            
            case "1":
                system ("cls")
                print ("--- Ajouter une Tâche ---")
                description = input ("\nNom de la tâche : ")
                date_maxi_str = input ("\nEntrer la date d'échéance (AAAA-MM-JJ) : ")
                date_maxi = datetime.strptime (date_maxi_str, "%Y-%m-%d").date ()
                system ("cls")
                ajouter (description, date_maxi, l_taches)
                ecriture_pickle (l_taches, f_gdt)
                return gdt_md ()
            
            case "2":
                system ("cls")
                desc = input ("Renseigner le nom de la tâche à retrouver : ")
                system ("cls")
                rechercher (desc, l_taches)
                return gdt_md ()
            
            case "3":
                system ("cls")
                afficher (l_taches)
                print ()
                return gdt_md ()
            
            case "4":
                system ("cls")
                afficher (l_taches)
                description = input ("\nSaisir le nom de la tâche terminée : ")
                system ("cls")
                finir (description, l_taches)
                ecriture_pickle (l_taches, f_gdt)
                return gdt_md ()
            
            case "5":
                verif_choice = False
                system ("cls")
                while verif_choice == False:
                    choice = input ("Vous confirmez vouloir supprimer les tâches marquées comme terminées : ").lower ()
                    if choice == "oui":
                        supprimer (l_taches)
                        system ("cls")
                        print ("Tâches supprimées avec succès !\n")
                        return gdt_md ()
                    elif choice == "non":
                        system ("cls")
                        print ("Action annulée !\n")
                        return gdt_md ()
                    else:
                        system ("cls")
                        print ("Veillez saisir \"oui\" ou \"non\" !\n")
            
            case _:
                system ("cls")
                print ("Choix impossible...\n")
                return gdt_md ()