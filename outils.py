import os
import logging
import datetime
import random
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
    if len(L_usr) == 0:
        L_usr.append(usr)
    elif len(L_usr) == 1:
        if usr["id"] == "1":
            L_usr[0] = usr
        elif usr["id"] == "2":
            L_usr.append(usr)
    elif len(L_usr) == 2:
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

def demarrage():
    ''' Permet le lancement des intégrations etc en fonction de l'utilisateur '''
    def choix_usr():
        ''' Définit l'utilisateur actuel '''
        L_usr = lecture_usr()
        while True:
            print(" -- Bienvenue ! --\n")
            if len(L_usr) == 1:
                print(f" {L_usr[0]['id']}. {L_usr[0]['nom']}",
                      "\n 2. Créer un utilisateur")
            else:
                for usr in L_usr:
                    print(f" {usr['id']}. {usr['nom']}")
            choix = input("\nChoix : ")
            os.system("cls")
            
            if len(L_usr) == 1:
                if choix == "1":
                    usr = L_usr[0]
                    return usr
                elif choix == "2":
                    from main import F_usr
                    print(" -- Bienvenue ! --\n")
                    
                    while True:
                        nom = input("Saisissez votre nom : ")
                        os.system("cls")
                        while True:
                            print(f" Donc vous vous appelez {nom}.",
                                  "\n C'est bien ça ?\n",
                                  "\n 1. Oui",
                                  "\n 2. Non")
                            choix = input("\nChoix : ")
                            os.system("cls")
                            if choix == "1":
                                break
                            elif choix == "2":
                                break
                            else:
                                print(" Choix impossible...\n")
                        if choix == "1":
                            break
                    
                    print(" Voulez-vous mettre en place un mot de passe ?\n",
                          "\n Ce mot de passe sera demandé à chaque fois que",
                          "\n vous vous connecterez à votre compte MD",
                          "\n\n Alors, voulez-vous le créer ?\n",
                          "\n 1. Oui",
                          "\n 2. Non")
                    choix = input("\nChoix : ")
                    os.system("cls")
                    
                    if choix == "1":
                        while True:
                            mdp = input ("Saisissez votre futur mot de passe : ")
                            os.system ("cls")
                            
                            while True:
                                print (" Pour vous connecter à votre compte,",
                                       f"\n vous devrez donc taper \"{mdp}\"\n",
                                       "\n Vous confirmez ?\n",
                                       "\n 1. Oui"
                                       "\n 2. Non")
                                choix = input ("\nChoix : ")
                                os.system("cls")
                            
                                if choix == "1":
                                    print (" Mot de passe crée !\n")
                                    break
                                elif choix == "2":
                                    break
                                print(" Choix impossible...\n")
                            if choix == "1":
                                break
                    else:
                        mdp = ""
                    
                    nbr = "1"
                    version = "2.0.1"
                    
                    usr = {"id": "2",
                           "nom": nom,
                           "mdp": mdp,
                           "nbr": "0",
                           "version": version,
                           "rep_md": "0",
                           "manager_md": "0",
                           "pass_md": "0",
                           "musiques_md": "0"}
                    L_usr.append(usr)
                    ecriture_CSV(L_usr, F_usr)
                    ecriture_log(f"NOUVEAU COMPTE UTILISATEUR CREE : {nom}\n")
                else:
                    print(" Choix impossible...\n")
            
            else:
                for usr in L_usr:
                    if choix == usr["id"]:
                        return usr
                if choix == "13":
                    print(" Salut, comment allez-vous aujourd'hui ?\n")
                else:
                    print(" Choix impossible...\n")
    
    usr = choix_usr()
    # TEST MDP #
    if usr["mdp"]:
        test = ""
        while test != usr["mdp"]:
            test = input("Saisissez votre mot de passe : ")
            os.system("cls")
            if test != usr["mdp"]:
                print(" Mot de passe incorrect !\n")
    
    usr["nbr"] = int(usr["nbr"])
    usr["nbr"] += 1
    usr["nbr"] = str(usr["nbr"])
    ecriture_usr(usr)
    ecriture_log(f"OUVERTURE: Centre MD (pour la {usr['nbr']}ème fois)\n")
    
    integrations = []
    urgences = []
    
    # INTEGRATION MUSIQUES MD #
    from apps.musiques_md.main import F_mus
    if os.path.exists (F_mus):
        L_mus = lecture_CSV(F_mus)
        if L_mus != []:
            tab_mus = []
            for musique in L_mus:
                if musique["usr_id"] == usr["id"]:
                    if musique["etat"] == "True":
                        if os.path.exists(musique["chemin"]):
                            from apps.musiques_md.lancer_arreter import lancer_arreter
                            lancer_arreter(L_mus, musique)
                        else:
                            musique["etat"] = "False"
                            ecriture_mus(L_mus)
                            ecriture_log(f"ARRET FORCE MUSIQUE : {musique['chemin']} (musique introuvable)\n")
                    else:
                        tab_mus.append(musique["nom"])
            if tab_mus != []:
                choix_mus = random.choice(tab_mus)
                integrations.append(f" Pourquoi ne pas écouter \"{choix_mus}\" aujourd'hui ?\n Si vous souhaitez l'écouter, lancez la depuis Musiques MD !\n")
    
    # AFFICHAGE MOT DE BIENVENUE #
    heure = datetime.datetime.now().hour
    if heure < 12:
        print(f" Bonjour {usr['nom']} !\n")
    elif 12 <= heure < 18:
        print(f" Bonsoir {usr['nom']} !\n")
    else:
        print(f" Bonne nuit {usr['nom']} !\n")
    
    # INTEGRATION REP MD #
    from apps.rep_md.main import F_rep
    if os.path.exists (F_rep):
        L_rep = lecture_CSV(F_rep)
        date = [datetime.datetime.now().day, datetime.datetime.now().month]
        
        for contact in L_rep:
            if contact["usr_id"] == usr["id"]:
                nom_c = contact["nom"]
                prenom_c = contact["prenom"]
                
                date_c = contact["date"]
                if contact["nom_groupe"] == "":
                    if date_c != "":
                        date_c = date_c.split("/")
                        for i in range (2):
                            date_c[i] = int(date_c[i])
                        del date_c[-1]
                        if date == date_c:
                            urgences.append(f" N'oubliez pas qu'aujourd'hui,\n c'est l'anniversaire de {nom_c} {prenom_c} !")
                    
                    else:
                        integrations.append(f" Hey, vous n'avez pas ajouté la date de naissance de {nom_c} {prenom_c}, pensez à le faire !\n Pour l'ajouter, allez dans le Rep MD, puis dans Modifier.\n")
                    
                    if contact["num"] == "":
                        integrations.append(f" Hey, vous n'avez pas ajouté le numéro de téléphone de {nom_c} {prenom_c} !\n Pour l'ajouter, allez dans le Rep MD, puis dans Modifier.\n")
                    if contact["email"] == "":
                        integrations.append(f" Hey, vous n'avez pas ajouté l'adresse email de {nom_c} {prenom_c} !\n Pour l'ajouter, allez dans le Rep MD, puis dans Modifier.\n")
                    if contact["adresse"] == "":
                        integrations.append(f" Connaissez-vous l'adresse postale de {nom_c} {prenom_c} ?\n Si vous souhaitez l'ajouter, allez dans le Rep MD, puis dans Modifier.\n")
    
    # INTEGRATIONS MANAGER MD #
    from apps.manager_md.main import F_manager
    if os.path.exists (F_manager):
        L_manager = lecture_CSV(F_manager)
        for tache in L_manager:
            if tache["etat"] == "True":
                nom = tache["nom"]
                if tache["date"] != "None":
                    tps_annee, tps_mois, tps_jour = tps_restant(tache["date"])
                    if tps_annee < 0:
                        urgences.append(f" Avez-vous terminé votre tâche \"{nom}\" ?")
                    elif tps_annee == 0 and tps_mois == 0 and tps_jour == 0:
                        urgences.append(f" Avez-vous terminé votre tâche \"{nom}\" ?")
                    else:
                        integrations.append(f" N'oubliez pas votre tache \"{nom}\" !\n\n Si vous l'avez terminé, vous pouvez la noter\n comme étant finie depuis Manager MD.\n")
                else:
                    integrations.append(f" N'oubliez pas votre tache \"{nom}\" !\n\n Si vous l'avez terminé, vous pouvez la noter\n comme étant finie depuis Manager MD.\n")
    
    # INTEGRATIONS FONDS MD #
    from apps.fonds_md.main import F_fonds
    if os.path.exists (F_fonds):
        L_fonds = lecture_fonds(F_fonds)
        date_fonds = ""
        for action in L_fonds:
            if action[0] == usr["id"]:
                date_fonds = L_fonds[-1][3].split(" ")[0]
        if date_fonds != "":
            integrations.append(f" Votre solde actuel à changé depuis le {date_fonds} ?\n Si c'est le cas vous pouvez le modifier depuis Fonds MD.\n")
    
    # INTEGRATIONS JEUX MD #
    liste_jeux = ["Pendu", "Chiffre Juste"]
    for jeu in liste_jeux:
        integrations.append(f" Pourquoi ne pas s'essayer 2 minutes au {jeu} ?\n\n Si vous souhaitez y jouer,\n il vous suffit de vous rendre dans Jeux MD !\n")
    
    if urgences:
        print(" --- ACTIONS URGENTES ---\n")
        for urgence in urgences:
            print(urgence + "\n")
    
    print(" --- SUGGESTIONS ---\n\n" + random.choice(integrations))
    
    return usr

def options(usr):
    while True:
        print("   · Options ·\n",
              f"\n Version actuelle : v{usr['version']}\n",
              "\n 0. Retour\n")
        if usr["mdp"]:
            print(" 1. Supprimer le mot de passe")
        else:
            print(" 1. Mettre en place un mot de passe")
        print(" 2. Afficher vos Infos Utilisateur",
              "\n 3. Rechercher une MàJ")
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
            if L_rep:
                test = True
                for contact in L_rep:
                    if contact["usr_id"] == usr["id"] and contact["prenom"].lower() == usr["nom"].lower():
                        nom, prenom = contact["nom"], contact["prenom"]
                        test = False
                        break
                if test:
                    nom, prenom = usr["nom"], ""
            else:
                nom, prenom = usr["nom"], ""
            print(f" {usr['id']}. | {nom} {prenom}",
                  "\n    |")
            if usr["mdp"] == "":
                print(f"    | Mdp | N'a pas de mot de passe...")
            else:
                print(f"    | Mdp | A un mot de passe (il est secret)")
            print(f"    | Nbr | A lancé le Centre MD {usr['nbr']} fois !\n")
        
        elif choix == "3":
            print(" Recherche de MàJ...")
            if comparer_version():
                os.system("cls")
                print(" MàJ annulée...\n")
            else:
                os.system("cls")
                print(" Aucune MàJ disponible...\n")
        
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
                                tab_date = contact_groupe_date.split("/")
                                tps_annee, tps_mois, tps_jour = tps_restant(f"{tab_date[2]}-{tab_date[1]}-{tab_date[0]}")
                                total_jour_restant = tps_jour + 30 * tps_mois
                                if total_jour_restant == 0:
                                    if test100:
                                        if test100_2:
                                            contenu += f"        | Date   | {date_affiche}\n        | Anniv  | C'EST AUJOURD'HUI !\n"
                                        elif test10_2:
                                            contenu += f"        | Date  | {date_affiche}\n        | Anniv | C'EST AUJOURD'HUI !\n"
                                        else:
                                            contenu += f"        | Date | {date_affiche}\n        | Anniv| C'EST AUJOURD'HUI !\n"
                                    elif test10:
                                        if test100_2:
                                            contenu += f"       | Date   | {date_affiche}\n       | Anniv  | C'EST AUJOURD'HUI !\n"
                                        elif test10_2:
                                            contenu += f"       | Date  | {date_affiche}\n       | Anniv | C'EST AUJOURD'HUI !\n"
                                        else:
                                            contenu += f"       | Date | {date_affiche}\n       | Anniv| C'EST AUJOURD'HUI !\n"
                                    else:
                                        if test100_2:
                                            contenu += f"      | Date   | {date_affiche}\n      | Anniv  | C'EST AUJOURD'HUI !\n"
                                        elif test10_2:
                                            contenu += f"      | Date  | {date_affiche}\n      | Anniv | C'EST AUJOURD'HUI !\n"
                                        else:
                                            contenu += f"      | Date | {date_affiche}\n      | Anniv| C'EST AUJOURD'HUI !\n"
                                elif total_jour_restant == 1:
                                    if test100:
                                        if test100_2:
                                            contenu += f"        | Date   | {date_affiche}\n        | Anniv  | Dans {total_jour_restant} jour.\n"
                                        elif test10_2:
                                            contenu += f"        | Date  | {date_affiche}\n        | Anniv | Dans {total_jour_restant} jour.\n"
                                        else:
                                            contenu += f"        | Date | {date_affiche}\n        | Anniv| Dans {total_jour_restant} jour.\n"
                                    elif test10:
                                        if test100_2:
                                            contenu += f"       | Date   | {date_affiche}\n       | Anniv  | Dans {total_jour_restant} jour.\n"
                                        elif test10_2:
                                            contenu += f"       | Date  | {date_affiche}\n       | Anniv | Dans {total_jour_restant} jour.\n"
                                        else:
                                            contenu += f"       | Date | {date_affiche}\n       | Anniv| Dans {total_jour_restant} jour.\n"
                                    else:
                                        if test100_2:
                                            contenu += f"      | Date   | {date_affiche}\n      | Anniv  | Dans {total_jour_restant} jour.\n"
                                        elif test10_2:
                                            contenu += f"      | Date  | {date_affiche}\n      | Anniv | Dans {total_jour_restant} jour.\n"
                                        else:
                                            contenu += f"      | Date | {date_affiche}\n      | Anniv| Dans {total_jour_restant} jour.\n"
                                else:
                                    if test100:
                                        if test100_2:
                                            contenu += f"        | Date   | {date_affiche}\n        | Anniv  | Dans {total_jour_restant} jours.\n"
                                        elif test10_2:
                                            contenu += f"        | Date  | {date_affiche}\n        | Anniv | Dans {total_jour_restant} jours.\n"
                                        else:
                                            contenu += f"        | Date | {date_affiche}\n        | Anniv| Dans {total_jour_restant} jours.\n"
                                    elif test10:
                                        if test100_2:
                                            contenu += f"       | Date   | {date_affiche}\n       | Anniv  | Dans {total_jour_restant} jours.\n"
                                        elif test10_2:
                                            contenu += f"       | Date  | {date_affiche}\n       | Anniv | Dans {total_jour_restant} jours.\n"
                                        else:
                                            contenu += f"       | Date | {date_affiche}\n       | Anniv| Dans {total_jour_restant} jours.\n"
                                    else:
                                        if test100_2:
                                            contenu += f"      | Date   | {date_affiche}\n      | Anniv  | Dans {total_jour_restant} jours.\n"
                                        elif test10_2:
                                            contenu += f"      | Date  | {date_affiche}\n      | Anniv | Dans {total_jour_restant} jours.\n"
                                        else:
                                            contenu += f"      | Date | {date_affiche}\n      | Anniv| Dans {total_jour_restant} jours.\n"
                            
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
                        tab_date = contact_date.split("/")
                        tps_annee, tps_mois, tps_jour = tps_restant(f"{tab_date[2]}-{tab_date[1]}-{tab_date[0]}")
                        total_jour_restant = tps_jour + 30 * tps_mois
                        if total_jour_restant == 0:
                            if test100:
                                contenu += f" Date   | {date_affiche}\n Anniv  | C'EST AUJOURD'HUI !\n"
                            elif test10:
                                contenu += f" Date  | {date_affiche}\n Anniv | C'EST AUJOURD'HUI !\n"
                            else:
                                contenu += f" Date | {date_affiche}\n Anniv| C'EST AUJOURD'HUI !\n"
                        elif total_jour_restant == 1:
                            if test100:
                                contenu += f" Date   | {date_affiche}\n Anniv  | Dans {total_jour_restant} jour.\n"
                            elif test10:
                                contenu += f" Date  | {date_affiche}\n Anniv | Dans {total_jour_restant} jour.\n"
                            else:
                                contenu += f" Date | {date_affiche}\n Anniv| Dans {total_jour_restant} jour.\n"
                        else:
                            if test100:
                                contenu += f" Date   | {date_affiche}\n Anniv  | Dans {total_jour_restant} jours.\n"
                            elif test10:
                                contenu += f" Date  | {date_affiche}\n Anniv | Dans {total_jour_restant} jours.\n"
                            else:
                                contenu += f" Date | {date_affiche}\n Anniv| Dans {total_jour_restant} jours.\n"
                    
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
                    if tps_annee < 0:
                        if test_100:
                            contenu += "        | C'EST L'HEURE !!!\n"
                        elif test_10:
                            contenu += "       | C'EST L'HEURE !!!\n"
                        else:
                            contenu += "      | C'EST L'HEURE !!!\n"
                    
                    elif tps_annee == 0 and tps_mois == 0 and tps_jour == 0:
                        if test_100:
                            contenu += "        | C'EST L'HEURE !!!\n"
                        elif test_10:
                            contenu += "       | C'EST L'HEURE !!!\n"
                        else:
                            contenu += "      | C'EST L'HEURE !!!\n"
                    
                    else:
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
           "version": "2.0.1",
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

# v2.0.0 -> v2.0.1:

def transition_v2_0_0():
    # Chemin du dossier AppData/Local/TeamMD/CentreMD
    dossier_final = os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD")

    fichiers_a_ignorer = {"CentreMD.exe", "unins000.dat", "unins001.dat", "unins000.exe", "unins001.exe", "main.py", "outils.py", "apps", "LICENSE.txt", "README.md"}

    # Parcourt les éléments du répertoire courant
    for item_name in os.listdir():
        # Ignorer les fichiers spécifiés
        if item_name in fichiers_a_ignorer:
            continue

        src_path = os.path.join(os.getcwd(), item_name)  # Chemin complet de la source
        dest_path = os.path.join(dossier_final, item_name)  # Chemin de destination
        
        # Déplacer les fichiers individuels
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)

        # Copier le dossier "audios" et tout son contenu
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)  # Copie récursive
            shutil.rmtree(src_path)  # Supprime le dossier original une fois copié
    
    # VERIFICATION USR SUR v2.0.1 #
    L_usr = lecture_usr()
    for usr in L_usr:
        if usr["version"] != "2.0.1":
            usr["version"] = "2.0.1"
            ecriture_usr(usr)
    
    # TRANSITION MUSIQUES MD (changement emplacement musiques)
    from apps.musiques_md.main import F_mus, base
    L_mus = lecture_CSV(F_mus)
    for musique in L_mus:
        musique["chemin"] = os.path.join(base, f"audios\{musique['nom']}")
    if L_mus:
        ecriture_mus(L_mus)
    
    print(" Bienvenue dans la v2.0.1 du Centre MD !\n",
          "\n Au programme, de nouvelles intégrations.",
          "\n Une amélioration du Centre MD.",
          "\n Et des corrections de bugs !!!\n",
          "\n Profitez bien de cette nouvelle expérience !\n")

# LA SUITE:

def telecharger(version):
    
    def version_tuple(version):
        return tuple(map(int, version.strip("v").split(".")))
    
    def version_maxi(L_usr):
        maxi = version_tuple(L_usr[0]["version"])
        version = L_usr[0]["version"]
        for usr in L_usr:
            if version_tuple(usr["version"]) > maxi:
                maxi = version_tuple(usr["version"])
                version = usr["version"]
        return version
    
    url = f"https://github.com/odilonhg/Centre-MD/releases/download/{version}/CentreMD_Installer.exe"
    response = requests.get(url)
    with open(os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD\CentreMD_Installer.exe"), "wb") as f:
        f.write(response.content)
    print("Mise à jour téléchargée.")
    
    L_usr = lecture_usr()
    version_actuelle = version_maxi(L_usr)
    ecriture_log(f"MAJ EFFECTUEE : v{version_actuelle} -> {version}\n")
    os.system("start CentreMD_Installer.exe")
    return

def obtenir_derniere_version():
    url = "https://api.github.com/repos/odilonhg/Centre-MD/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "tag_name" in data:
            return data["tag_name"]
        else:
            return None
    else:
        return None

def comparer_version():
    
    def version_tuple(version):
        return tuple(map(int, version.strip("v").split(".")))
        
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
                        for usr in L_usr:
                            usr["version"] = derniere_version
                            ecriture_usr(usr)
                        exit()
                    elif choix == "2":
                        return True
                    else:
                        print(" Choix impossible...\n")
        
        else:
            return False