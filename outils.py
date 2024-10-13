import os
import logging
import datetime
import pickle
import shutil
import requests

### FONCTIONS UTILES POUR LE CENTRE MD ###

def ecriture_CSV(L, F, delimiter = ";"):
    '''
    Ecrit le contenu d'une liste de dictionnaires dans un fichier CSV
    PRE: un tableau (L) contenant des dictionnaires / un fichier CSV (F)
    POST: un booléen (True si le contenu a été écrit et False si il n'a pas été écrit
    '''
    try:
        with open(F, "w") as f:
            ligneDesc = delimiter.join(L[0].keys()) + "\n"
            f.write(ligneDesc)
            for ligne in L:
                ligne = delimiter.join(ligne.values()) + "\n"
                f.write(ligne)
            return True
    except:
        return False

def lecture_CSV(F, delimiter = ";"):
    '''
    Lit le contenu d'un fichier CSV
    PRE: un fichier CSV (F)
    POST: un tableau de dictionnaires OU None si le fichier n'existe pas
    '''
    L = []
    if os.path.exists(F):
        with open(F, "r") as f:
            cles = f.readline().strip().split(delimiter)
            for ligne in f:
                donnee = ligne.strip().split(delimiter)
                L.append(dict(zip(cles, donnee)))
    return L

def ecriture_log(contenu):
    '''
    Ecrit un texte (contenu) dans le fichier logging
    PRE: une chaine de caractères (contenu)
    '''
    from main import F_log
    logging.basicConfig(filename = F_log,
                        level = logging.INFO,
                        format = "%(asctime)s %(message)s",
                        datefmt = "%d/%m/%Y %H:%M:%S")
    logging.info(contenu)
    logging.shutdown()

def ecriture_usr(usr):
    from main import L_usr, F_usr
    if usr["id"] == "1":
        L_usr[0] = usr
    elif usr["id"] == "2":
        L_usr[1] = usr
    else:
        return False
    return ecriture_CSV(L_usr, F_usr)

def lecture_usr():
    from main import F_usr
    return lecture_CSV(F_usr)

def recherche(L, usr, elm_a_trouver):
    '''
    Recherche dans un tableau de dictionnaires une chaine de caractères (tri par usr_id)
    PRE: un tableau de dictionnaires (L), un dictionnaire et une chaine de caractères (elm_a_trouver)
    POST: un tableau contenant les dictionnaires qui contiennent l'élement recherché
    '''
    if elm_a_trouver == "None":
        return []
    L_recherche = []
    for elm in L:
        if elm["usr_id"] == usr["id"]:
            elm_recherche = list(elm.values())
            elm_recherche = elm_recherche[1:]
            for elm_recherche_str in elm_recherche:
                if elm_a_trouver.lower() == elm_recherche_str.lower():
                    L_recherche.append(elm)
    return L_recherche

def options(usr):
    while True:
        print("   · Options ·\n",
              f"\n Version actuelle : v{usr['version']}\n",
              "\n 0. Retour\n")
        if usr["mdp"] == "":
            print(" 1. Mettre en place un mot de passe")
        else:
            print(" 1. Supprimer le mot de passe")
        print(" 2. Afficher vos Infos Utilisateur")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0":
            return
        
        elif choix == "1":
            if usr["mdp"] == "":
                while True:
                    usr["mdp"] = input ("Saisissez votre futur mot de passe : ")
                    os.system ("cls")
                    
                    while True:
                        print (" Pour vous connecter à votre compte,",
                               f"\n vous devrez désormais taper \"{usr['mdp']}\"\n",
                               "\n Vous confirmez ?\n",
                               "\n 1. Oui"
                               "\n 2. Non")
                        choix = input ("\nChoix : ")
                        os.system("cls")
                    
                        if choix == "1":
                            ecriture_usr(usr)
                            print (" Mot de passe crée !\n")
                            ecriture_log("    CREATION DU MOT DE PASSE !\n")
                            break
                        elif choix == "2":
                            break
                        print(" Choix impossible...\n")
                    if choix == "1":
                        break
            else:
                while True:
                    test_mdp = input ("Saisissez votre mot de passe : ")
                    os.system ("cls")
                    
                    if test_mdp == usr["mdp"]:
                        usr["mdp"] = ""
                        ecriture_usr(usr)
                        print (" Mot de passe supprimé !\n")
                        ecriture_log("    SUPPRRESSION DU MOT DE PASSE...\n")
                        break
                    print (" Mot de passe incorrect !\n")
        
        elif choix == "2":
            ecriture_log("    AFFICHER : Infos Utilisateur\n")
            from apps.rep_md.main import F_rep
            L_rep = lecture_CSV(F_rep)
            for contact in L_rep:
                if contact["usr_id"] == usr["id"] and contact["prenom"].lower() == usr["nom"].lower():
                    nom, prenom = contact["nom"], contact["prenom"]
                else:
                    nom, prenom = usr["nom"], ""
            print(f" {usr['id']}. | {nom} {prenom}",
                  "\n    |")
            if usr["mdp"] == "":
                print(f"    | Mdp | N'a pas de mot de passe...")
            else:
                print(f"    | Mdp | A un mot de passe (il est secret)")
            print(f"    | Nbr | A lancé le Centre MD {usr['nbr']} fois !\n")
                
        elif choix == "13":
            print(" Bienvenue aux Options !\n",
                  "\n Franchement c'est un peu vide ici...",
                  "\n Il est peux être temps que les Options",
                  "\n disparaissent...\n")
        else:
            print(" Choix impossible...\n")

### FONCTIONS UTILES POUR "REP MD" ###

def ecriture_rep(L_rep):
    from apps.rep_md.main import F_rep
    return ecriture_CSV(L_rep, F_rep)

def affiche_date(date):
    '''
    Renvoie une chaine de caractères contenant la date.
    PRE: une chaine de caractères (date) utilisant le formatage MD (JJ/MM/AAAA)
    POST: une chaine de caractères (JJ mois_en_lettres AAAA)
    '''
    format_date = {
    "01": "Janvier",
    "02": "Février",
    "03": "Mars",
    "04": "Avril",
    "05": "Mai",
    "06": "Juin",
    "07": "Juillet",
    "08": "Août",
    "09": "Septembre",
    "10": "Octobre",
    "11": "Novembre",
    "12": "Décembre"}
    
    L_date = date.split("/")
    mois = L_date[1]
    mois_lettres = format_date[mois]
    return f"{L_date[0]} {mois_lettres} {L_date[2]}"

def affiche_rep(L_rep, usr):
    '''
    Stoque dans une chaine de caractères le contenu à afficher
    PRE: un tableau de dictionnaires (L_rep) et un dictionnaire (usr)
    POST: une chaine de caractères (saut de ligne au début et à la fin)
    '''
    contenu = ""
    for contact in L_rep:
        if contact["usr_id"] == usr["id"]:
            test_contact_groupe = False
            test10 = False
            test100 = False
            contact_id = contact["id"]
            if 9 < int(contact_id) < 99:
                test10 = True
            elif int(contact_id) > 99:
                test100 = True
            
            contact_favori = contact["favori"]
            
            contact_nom = contact.get("nom")
            contact_prenom = contact["prenom"]
            contact_date = contact["date"]
            contact_num = contact["num"]
            contact_email = contact["email"]
            contact_adresse = contact["adresse"]
            contact_notes = contact["notes"]
            contact_groupes = contact["groupes"]
            
            groupe_nom = contact["nom_groupe"]
            
            if contact_groupes != "":
                test_contact_groupe = True
            
            if groupe_nom != "":
                if contact_favori == "True":
                    contenu += f"\n {contact_id}. * | Groupe : {groupe_nom}\n"
                else:
                    contenu += f"\n {contact_id}.   | Groupe : {groupe_nom}\n"
                
                from apps.rep_md.main import F_rep
                real_L_rep = lecture_CSV(F_rep)
                for contact_groupe in real_L_rep:
                    if contact_groupe["usr_id"] == usr["id"]:
                        test10_2 = False
                        test100_2 = False
                        if contact_id in contact_groupe["groupes"] and contact_groupe["nom_groupe"] == "":
                            contact_groupe_id = contact_groupe["id"]
                            if 9 < int(contact_groupe_id) < 99:
                                test10_2 = True
                            elif int(contact_groupe_id) > 99:
                                test100_2 = True
                            contact_groupe_favori = contact_groupe["favori"]
                            contact_groupe_nom = contact_groupe["nom"]
                            contact_groupe_prenom = contact_groupe["prenom"]
                            contact_groupe_date = contact_groupe["date"]
                            contact_groupe_num = contact_groupe["num"]
                            contact_groupe_email = contact_groupe["email"]
                            contact_groupe_adresse = contact_groupe["adresse"]
                            contact_groupe_notes = contact_groupe["notes"]
                            
                            if contact_groupe_favori == "True":
                                if test100:
                                    contenu += f"        |\n        | {contact_groupe_id}. * | {contact_groupe_nom} {contact_groupe_prenom}\n"
                                elif test10:
                                    contenu += f"       |\n       | {contact_groupe_id}. * | {contact_groupe_nom} {contact_groupe_prenom}\n"
                                else:
                                    contenu += f"      |\n      | {contact_groupe_id}. * | {contact_groupe_nom} {contact_groupe_prenom}\n"
                            else:
                                if test100:
                                    contenu += f"        |\n        | {contact_groupe_id}.   | {contact_groupe_nom} {contact_groupe_prenom}\n"
                                elif test10:
                                    contenu += f"       |\n       | {contact_groupe_id}.   | {contact_groupe_nom} {contact_groupe_prenom}\n"
                                else:
                                    contenu += f"      |\n      | {contact_groupe_id}.   | {contact_groupe_nom} {contact_groupe_prenom}\n"
                            
                            if contact_groupe_date:
                                date_affiche = affiche_date(contact_groupe_date)
                                if test100:
                                    if test100_2:
                                        contenu += f"        | Date   | {date_affiche}\n"
                                    elif test10_2:
                                        contenu += f"        | Date  | {date_affiche}\n"
                                    else:
                                        contenu += f"        | Date | {date_affiche}\n"
                                elif test10:
                                    if test100_2:
                                        contenu += f"       | Date   | {date_affiche}\n"
                                    elif test10_2:
                                        contenu += f"       | Date  | {date_affiche}\n"
                                    else:
                                        contenu += f"       | Date | {date_affiche}\n"
                                else:
                                    if test100_2:
                                        contenu += f"      | Date   | {date_affiche}\n"
                                    elif test10_2:
                                        contenu += f"      | Date  | {date_affiche}\n"
                                    else:
                                        contenu += f"      | Date | {date_affiche}\n"
                            
                            if contact_groupe_num:
                                if test100:
                                    if test100_2:
                                        contenu += f"        | Num    | {contact_groupe_num}\n"
                                    elif test10_2:
                                        contenu += f"        | Num   | {contact_groupe_num}\n"
                                    else:
                                        contenu += f"        | Num  | {contact_groupe_num}\n"
                                elif test10:
                                    if test100_2:
                                        contenu += f"       | Num    | {contact_groupe_num}\n"
                                    elif test10_2:
                                        contenu += f"       | Num   | {contact_groupe_num}\n"
                                    else:
                                        contenu += f"       | Num  | {contact_groupe_num}\n"
                                else:
                                    if test100_2:
                                        contenu += f"      | Num    | {contact_groupe_num}\n"
                                    elif test10_2:
                                        contenu += f"      | Num   | {contact_groupe_num}\n"
                                    else:
                                        contenu += f"      | Num  | {contact_groupe_num}\n"
                            
                            if contact_groupe_email:
                                if test100:
                                    if test100_2:
                                        contenu += f"        | Email  | {contact_groupe_email}\n"
                                    elif test10_2:
                                        contenu += f"        | Email | {contact_groupe_email}\n"
                                    else:
                                        contenu += f"        | Email| {contact_groupe_email}\n"
                                elif test10:
                                    if test100_2:
                                        contenu += f"       | Email  | {contact_groupe_email}\n"
                                    elif test10_2:
                                        contenu += f"       | Email | {contact_groupe_email}\n"
                                    else:
                                        contenu += f"       | Email| {contact_groupe_email}\n"
                                else:
                                    if test100_2:
                                        contenu += f"      | Email  | {contact_groupe_email}\n"
                                    elif test10_2:
                                        contenu += f"      | Email | {contact_groupe_email}\n"
                                    else:
                                        contenu += f"      | Email| {contact_groupe_email}\n"
                            
                            if contact_groupe_adresse:
                                if test100:
                                    if test100_2:
                                        contenu += f"        | Mail   | {contact_groupe_adresse}\n"
                                    elif test10_2:
                                        contenu += f"        | Mail  | {contact_groupe_adresse}\n"
                                    else:
                                        contenu += f"        | Mail | {contact_groupe_adresse}\n"
                                elif test10:
                                    if test100_2:
                                        contenu += f"       | Mail   | {contact_groupe_adresse}\n"
                                    elif test10_2:
                                        contenu += f"       | Mail  | {contact_groupe_adresse}\n"
                                    else:
                                        contenu += f"       | Mail | {contact_groupe_adresse}\n"
                                else:
                                    if test100_2:
                                        contenu += f"      | Mail   | {contact_groupe_adresse}\n"
                                    elif test10_2:
                                        contenu += f"      | Mail  | {contact_groupe_adresse}\n"
                                    else:
                                        contenu += f"      | Mail | {contact_groupe_adresse}\n"
                            
                            if contact_groupe_notes:
                                L_notes = contact_groupe_notes.split("|")
                                for note in L_notes:
                                    if test100:
                                        if test100_2:
                                            contenu += f"        | Note   | {note}\n"
                                        elif test10_2:
                                            contenu += f"        | Note  | {note}\n"
                                        else:
                                            contenu += f"        | Note | {note}\n"
                                    elif test10:
                                        if test100_2:
                                            contenu += f"       | Note   | {note}\n"
                                        elif test10_2:
                                            contenu += f"       | Note  | {note}\n"
                                        else:
                                            contenu += f"       | Note | {note}\n"
                                    else:
                                        if test100_2:
                                            contenu += f"      | Note   | {note}\n"
                                        elif test10_2:
                                            contenu += f"      | Note  | {note}\n"
                                        else:
                                            contenu += f"      | Note | {note}\n"
            else:
                if test_contact_groupe == False:
                    if contact_favori == "True":
                        if test100:
                            contenu += f"\n {contact_id}. * | {contact_nom} {contact_prenom}\n        |\n"
                        elif test10:
                            contenu += f"\n {contact_id}. * | {contact_nom} {contact_prenom}\n       |\n"
                        else:
                            contenu += f"\n {contact_id}. * | {contact_nom} {contact_prenom}\n      |\n"
                    else:
                        if test100:
                            contenu += f"\n {contact_id}.   | {contact_nom} {contact_prenom}\n        |\n"
                        elif test10:
                            contenu += f"\n {contact_id}.   | {contact_nom} {contact_prenom}\n       |\n"
                        else:
                            contenu += f"\n {contact_id}.   | {contact_nom} {contact_prenom}\n      |\n"
                    
                    if contact_date:
                        date_affiche = affiche_date(contact_date)
                        if test100:
                            contenu += f" Date   | {date_affiche}\n"
                        elif test10:
                            contenu += f" Date  | {date_affiche}\n"
                        else:
                            contenu += f" Date | {date_affiche}\n"
                    
                    if contact_num:
                        if test100:
                            contenu += f" Num    | {contact_num}\n"
                        elif test10:
                            contenu += f" Num   | {contact_num}\n"
                        else:
                            contenu += f" Num  | {contact_num}\n"
                    
                    if contact_email:
                        if test100:
                            contenu += f" Email  | {contact_email}\n"
                        elif test10:
                            contenu += f" Email | {contact_email}\n"
                        else:
                            contenu += f" Email| {contact_email}\n"
                    
                    if contact_adresse:
                        if test100:
                            contenu += f" Mail   | {contact_adresse}\n"
                        elif test10:
                            contenu += f" Mail  | {contact_adresse}\n"
                        else:
                            contenu += f" Mail | {contact_adresse}\n"
                    
                    if contact_notes:
                        L_notes = contact_notes.split("|")
                        for note in L_notes:
                            if test100:
                                contenu += f" Note   | {note}\n"
                            elif test10:
                                contenu += f" Note  | {note}\n"
                            else:
                                contenu += f" Note | {note}\n"
    return contenu                   

### FONCTIONS UTILES POUR "MANAGER MD" ###

def ecriture_manager(L_manager):
    from apps.manager_md.main import F_manager
    return ecriture_CSV(L_manager, F_manager)

def tps_restant(date):
    '''
    Renvoie le temps restant entre la date fournie (date) et la date du jour
    PRE: une chaine de caractères avec ce format "AAAA-MM-JJ"
    POST: un tuple contenant le nombre d'années, de mois et de jours restants
    '''
    date_aujourdhui = str(datetime.datetime.strptime(f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}", "%Y-%m-%d").date ())
    date_aujourdhui_annee, date_aujourdhui_mois, date_aujourdhui_jour = date_aujourdhui.split("-")
    date_annee, date_mois, date_jour = date.strip().split("-")
    tps_annee, tps_mois, tps_jour = int(date_annee) - int(date_aujourdhui_annee), int(date_mois) - int(date_aujourdhui_mois), int(date_jour) - int(date_aujourdhui_jour)
    if tps_annee > 0 or tps_mois > 0 or tps_jour > 0:
        if tps_jour < 0:
            tps_mois -= 1
            tps_jour += 31
        if tps_mois < 0:
            tps_annee -= 1
            tps_mois += 12
    return tps_annee, tps_mois, tps_jour

def affiche_manager(L_manager, usr):
    '''
    Stoque dans une chaine de caractères le contenu à afficher
    PRE: un tableau de dictionnaires (L_manager) et un dictionnaire (usr)
    POST: une chaine de caractères (saut de ligne au début et à la fin)
    '''
    contenu = ""
    for tache in L_manager:
        if tache["usr_id"] == usr["id"]:
            test_10 = False
            test_100 = False
            tache_id = tache["id"]
            if 9 < int(tache_id) < 99:
                test_10 = True
            elif int(tache_id) > 99:
                test_100 = True
                
            tache_nom = tache["nom"]
            tache_date = tache["date"]
            tache_favori = tache["favori"]
            tache_etat = tache["etat"]
            
            if tache_etat == "True":
                if tache_favori == "True":
                    contenu += f"\n {tache_id}. * | {tache_nom}\n"
                else:
                    contenu += f"\n {tache_id}.   | {tache_nom}\n"
                
                if tache_date != "None":
                    tps_annee, tps_mois, tps_jour = tps_restant(tache_date)
                    if tps_annee >= 0:
                        if tps_mois > 0 or tps_mois > 0:
                            if test_100:
                                contenu += "        | Temps restant\n"
                            elif test_10:
                                contenu += "       | Temps restant\n"
                            else:
                                contenu += "      | Temps restant\n"
                            
                            if tps_annee == 1:
                                if test_100:
                                    contenu += f"        | {tps_annee} année \n"
                                elif test_10:
                                    contenu += f"       | {tps_annee} année \n"
                                else:
                                    contenu += f"      | {tps_annee} année \n"
                            elif tps_annee > 1:
                                if test_100:
                                    contenu += f"        | {tps_annee} années \n"
                                elif test_10:
                                    contenu += f"       | {tps_annee} années \n"
                                else:
                                    contenu += f"      | {tps_annee} années \n"
                            if tps_mois > 0:
                                if test_100:
                                    contenu += f"        | {tps_mois} mois \n"
                                elif test_10:
                                    contenu += f"       | {tps_mois} mois \n"
                                else:
                                    contenu += f"      | {tps_mois} mois \n"
                            if tps_jour == 1:
                                if test_100:
                                    contenu += f"        | {tps_jour} jour \n"
                                elif test_10:
                                    contenu += f"       | {tps_jour} jour \n"
                                else:
                                    contenu += f"      | {tps_jour} jour \n"
                            elif tps_jour > 1:
                                if test_100:
                                    contenu += f"        | {tps_jour} jours \n"
                                elif test_10:
                                    contenu += f"       | {tps_jour} jours \n"
                                else:
                                    contenu += f"      | {tps_jour} jours \n"
                        else:
                            if test_100:
                                contenu += "        | C'EST L'HEURE !!!\n"
                            elif test_10:
                                contenu += "       | C'EST L'HEURE !!!\n"
                            else:
                                contenu += "      | C'EST L'HEURE !!!\n"
                    
                    else:
                        if test_100:
                            contenu += "        | C'EST L'HEURE !!!\n"
                        elif test_10:
                            contenu += "       | C'EST L'HEURE !!!\n"
                        else:
                            contenu += "      | C'EST L'HEURE !!!\n"
    return contenu

### FONCTIONS UTILES POUR "FONDS MD" ###

def ecriture_fonds(L_fonds, delimiter = ";", encoding = "utf-8"):
    from apps.fonds_md.main import F_fonds
    try:
        with open(F_fonds, "w", encoding = encoding) as f:
            for ligne in L_fonds:
                f.write(delimiter.join(ligne) + "\n")
            return True
    except:
            return False

def lecture_fonds(F_fonds, delimiter = ";", encoding = "utf-8"):
    L_fonds = []
    with open(F_fonds, "r", encoding = encoding) as f:
        lignes = f.readlines()
        for ligne in lignes:
            L_fonds.append(ligne.strip().split(delimiter))
        return L_fonds

def affiche_fonds(L_fonds, usr):
    '''
    Renvoie l'argent total restant sur le compte
    PRE: une liste de listes (L_fonds)
    POST: Un entier (le total restant) et une chaine de caractères (l'historique des actions faites sur le compte)
    '''
    total = 0
    historique = ""
    for ligne in L_fonds:
        if usr["id"] == ligne[0]:
            historique += f"\n {ligne[3]} | {ligne[1]} : {ligne[2]}€\n"
            total += int(ligne[2])
    historique += f"\n {str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M'))} | TOTAL ACTUEL : {total}€\n"
    return total, historique
    
### FONCTIONS UTILES POUR "PASS MD" ###

def ecriture_pass(L_pass):
    from apps.pass_md.main import F_pass
    return ecriture_CSV(L_pass, F_pass)

def affiche_pass(L_pass, usr):
    contenu = ""
    for L_mdp in L_pass:
        if L_mdp["usr_id"] == usr["id"]:
            if len(L_mdp["id"]) >= 3:
                contenu += f"\n {L_mdp['id']}. | {L_mdp['nom']}\n      | {L_mdp['mdp']}\n"
            elif len(L_mdp["id"]) == 2:
                contenu += f"\n {L_mdp['id']}. | {L_mdp['nom']}\n     | {L_mdp['mdp']}\n"
            else:
                contenu += f"\n {L_mdp['id']}. | {L_mdp['nom']}\n    | {L_mdp['mdp']}\n"
    return contenu

### FONCTIONS UTILES POUR "MUSIQUES MD" ###

def ecriture_mus(L_mus):
    from apps.musiques_md.main import F_mus
    return ecriture_CSV(L_mus, F_mus)

### FONCTIONS UTILES POUR LES TRANSITIONS ENTRE LES VERSIONS ###

# v1.0.0 / v1.3.0 -> v2.0.0

def lecture_pickle(F):
    '''Cette fonction lit un fichier pickle et renvoie les données stockées dans ce fichier.'''
    with open(F, "rb") as f:
        return pickle.load(f)

def transition_v1(L_usr_v1, F_usr):
    L_usr_v1 = L_usr_v1[0]
    if len(L_usr_v1) == 3:
        nom = L_usr_v1[0]
        mdp = L_usr_v1[2]
        nbr = "0"
        musiques_md = "0"
    
    elif len(L_usr_v1) == 4:
        nom = L_usr_v1[0]
        mdp = L_usr_v1[2]
        nbr = str(L_usr_v1[3])
        musiques_md = "0"
    
    else:
        nom = L_usr_v1[0]
        mdp = L_usr_v1[3]
        nbr = str(L_usr_v1[4])
        
        chemin_fichier = L_usr_v1[2]
        if os.path.exists(chemin_fichier):
            nom_fichier = os.path.basename (chemin_fichier)
            chemin_final = os.path.join (os.getcwd (), "audios")
            chemin_final = os.path.join (chemin_final, nom_fichier)
            if not os.path.exists("audios"):
                os.mkdir("audios")
            shutil.copy(chemin_fichier, chemin_final)
            new_mus = {"usr_id": "1",
                       "id": "1",
                       "nom": nom_fichier,
                       "chemin": chemin_final,
                       "etat": "True"}
            L_mus = [new_mus]
            ecriture_mus(L_mus)
            musiques_md = "1"
        else:
            musiques_md = "0"
    
    if mdp == False:
        mdp = ""
    usr = {"id": "1",
           "nom": nom,
           "mdp": mdp,
           "nbr": nbr,
           "version": "2.0.0",
           "rep_md": "0",
           "manager_md": "0",
           "pass_md": "0",
           "musiques_md": musiques_md}
    L_usr = [usr]
    ecriture_CSV(L_usr, F_usr)
    
    from apps.rep_md.main import F_rep
    if os.path.exists(F_rep):
        L_rep_v1 = lecture_CSV(F_rep)
        L_rep = []
        id = 0
        
        for usr_v1 in L_rep_v1:
            id += 1
            
            date_split = usr_v1["date"].strip().split(".")
            if date_split != [""]:
                date = f"{date_split[0]}/{date_split[1]}/{date_split[2]}"
            else:
                date = ""
            
            if usr_v1["favori"] == "":
                favori = "False"
            else:
                favori = "True"
            
            usr_v1["groupes"] = ""
            if usr_v1["groupe"] != "":
                id_groupe = 0
                for groupe_v1 in L_rep_v1:
                    id_groupe += 1
                    if groupe_v1["num_groupe"] != "" and groupe_v1["num_groupe"] in usr_v1["groupe"]:
                        usr_v1["groupes"] += str(id_groupe)
            
            L_rep.append({"usr_id": "1",
                          "id": str(id),
                          "favori": favori,
                          "nom": usr_v1["nom"],
                          "prenom": usr_v1["prenom"],
                          "date": date,
                          "num": usr_v1["num"],
                          "email": usr_v1["email"],
                          "adresse": "",
                          "notes": "",
                          "groupes": usr_v1["groupes"],
                          "nom_groupe": usr_v1["nom_groupe"],
                          "nbr_groupe": usr_v1["mbr_groupe"]})
        ecriture_CSV(L_rep, F_rep)
    
    from apps.manager_md.main import F_manager_v1, F_manager
    if os.path.exists(F_manager_v1):
        L_manager_v1 = lecture_pickle(F_manager_v1)
        L_manager = []
        
        id = 0
        for tache in L_manager_v1:
            id += 1
            new_tache = {"usr_id": "1",
                          "id": str(id),
                          "nom": tache["description"],
                          "date": str(tache["date_maxi"]),
                          "favori": "False",
                          "etat": str(tache["etat"])}
            L_manager.append(new_tache)
        ecriture_CSV(L_manager, F_manager)
        os.remove(F_manager_v1)
    
    ecriture_log("MAJ EFFECTUEE : v1 -> v2.0.0\n")
    print(" Bienvenue dans la v2.0.0 du Centre MD !\n",
          "\n Au programme, de nouvelles applications.",
          "\n Une optimisation du Centre en profondeur.",
          "\n Et la possibilité d'avoir 2 Utilisateurs !!\n",
          "\n Profitez bien de votre expérience !\n")
    return L_usr

# v2.0.0 -> LA SUITE:

def telecharger(version):
    url = f"https://github.com/odilonhg/Centre-MD/releases/download/{version}/CentreMD_Installer.exe"
    response = requests.get(url)
    with open('CentreMD_Installer.exe', 'wb') as f:
        f.write(response.content)
    print("Mise à jour téléchargée.")
    os.system("start CentreMD_Installer.exe")
    return

def obtenir_derniere_version():
    url = "https://api.github.com/repos/odilonhg/Centre-MD/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'tag_name' in data:
            return data['tag_name']
        else:
            return None
    else:
        return None

def comparer_version():
    
    def version_tuple(version):
        return tuple(map(int, version.strip("v").split('.')))
        
    def connexion_internet():
        try:
            # Vérifier la connexion Internet en faisant une requête rapide vers un site de confiance
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False
    
    if connexion_internet():
        L_usr = lecture_usr()
        if len(L_usr) == 1:
            version_actuelle = L_usr[0]["version"]
        else:
            version_1 = L_usr[0]["version"]
            version_2 = L_usr[1]["version"]
            version_tuple_1 = version_tuple(version_1)
            version_tuple_2 = version_tuple(version_2)
            version_actuelle = version_1 if version_tuple_1 > version_tuple_2 else version_2
        
        derniere_version = obtenir_derniere_version()
        if derniere_version != None:
        
            if version_tuple(derniere_version) > version_tuple(version_actuelle):
                while True:
                    print(f"Une nouvelle version est disponible : {derniere_version}\n",
                          "\n Voulez-vous l'installer ?\n (Nous vous recommandons de l'installer afin de profiter\n des dernières applications et services MD)\n",
                          "\n 1. Oui",
                          "\n 2. Non")
                    choix = input("\nChoix : ")
                    os.system("cls")
                    if choix == "1":
                        telecharger(derniere_version)
                        derniere_version = derniere_version.strip("v")
                        if len(L_usr) == 1:
                            L_usr[0]["version"] = derniere_version
                        else:
                            L_usr[0]["version"] = derniere_version
                            L_usr[1]["version"] = derniere_version
                        from main import F_usr
                        ecriture_CSV(L_usr, F_usr)
                        exit()
                    elif choix == "2":
                        return
                    else:
                        print(" Choix impossible...\n")
