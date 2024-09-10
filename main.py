# MODULES NECESSAIRES: pygame, PySide2

import outils
import os
import logging
import datetime

F_log = "data_log.txt"
F_usr = "data_usr"
usr_version = "1.3.0"

logging.basicConfig(filename = F_log, level = logging.INFO, format = "%(asctime)s %(message)s", datefmt = "%d/%m/%Y %H:%M:%S")
gestionnaire_log = logging.getLogger().handlers[0]
date = datetime.datetime.now()

os.system ("cls")
if os.path.exists (F_usr) == False:
    lgc_infos = [True, True, True, True, True]
    usr_nom = os.getenv ("username")
    
    print (f" Bienvenue {usr_nom} !\n")
    print (f" Déjà, vous appelez-vous réellement {usr_nom} ?\n")
    
    while True:
        print (" 1. Oui")
        print (" 2. Non")
        choix_nom = input ("\nChoix : ")
        if choix_nom == "1": break
        elif choix_nom == "2":
            while True:
                os.system ("cls")
                usr_nom = input ("Veuillez saisir votre prénom : ")
                os.system ("cls")
                print (f" Vous vous appelez donc {usr_nom} ?\n")
                print (" 1. Oui")
                print (" 2. Non")
                choix_nom = input ("\nChoix : ")
                if choix_nom == "1": break
        else:
            os.system ("cls")
            print (" Choix impossible...\n")
            print (f" Vous appelez-vous réellement {usr_nom} ?")
        
        if choix_nom == "1": break
        
    os.system ("cls")
    while True:
        print (f" {usr_nom}, voulez-vous une ambiance sonore ?\n")
        print (" 1. Oui")
        print (" 2. Non")
        choix_son = input ("\nChoix : ")
        
        if choix_son == "1":
            usr_son = True
            os.system ("cls")
            usr_son, F_son = outils.selection_son ()
            if usr_son:
                outils.lancer_son (F_son)
                break
            else:
                os.system ("cls")
                print (" Le chemin d'accès est incorrect ! Désolé...\n")
        elif choix_son == "2":
            usr_son = False
            F_son = None
            break
        else:
            os.system ("cls")
            print (" Choix impossible...\n")
    
    os.system ("cls")
    while True:
        print (" Enfin, souhaitez-vous mettre en place un mot de passe ?\n")
        print (" 1. Oui")
        print (" 2. Non")
        choix_mdp = input ("\nChoix : ")
        if choix_mdp == "1":
            while True:
                os.system ("cls")
                usr_mdp = input ("Veuillez saisir votre mot de passe : ")
                os.system ("cls")
                print (f" Votre mot de passe requis à l'ouverture du logiciel sera \"{usr_mdp}\", vous confirmez ?\n")
                print (" 1. Oui")
                print (" 2. Non")
                choix_mdp = input ("\nChoix : ")
                if choix_mdp == "1": break
            break
        
        elif choix_mdp == "2":
            usr_mdp = False
            break
        
        else:
            os.system ("cls")
            print (" Choix impossible...\n")
    
    usr_nbr = 1
    usr_infos = [usr_nom, usr_son, F_son, usr_mdp, usr_nbr, usr_version]
    usr = [usr_infos, lgc_infos]
    outils.ecriture_pickle (usr, F_usr)
    
    os.system ("cls")
    logging.info (f"BIENVENUE: {usr_nom} !\n")
    print (f" Bienvenue à vous {usr_nom} dans le Centre MD !\n")


else:
    usr = outils.lecture_pickle (F_usr)
    
    if len(usr[0]) == 4:
        usr_nom = usr[0][0]
        usr_son = usr[0][1]
        usr_mdp = usr[0][2]
        usr_nbr = usr[0][3]
        
        if usr_son:
            usr_son, F_son = outils.selection_son ()
        else: F_son = None
        
        usr_infos = [usr_nom, usr_son, F_son, usr_mdp, usr_nbr, usr_version]
        usr = [usr_infos, usr[1]]
        outils.ecriture_pickle (usr, F_usr)
        os.system ("cls")
        print (" Bienvenue dans la version 1.3.0 du Centre MD !")
        print ("\n Tu vas pouvoir découvrir la nouvelle application : Fonds MD")
        print ("\n J'espère que tu te plairas à tester\n les quelques modifications qu'apportent la v1.3.0 du Centre MD !\n")
        confirmation = input ("Appuyer sur Entrée pour continuer...")
        os.system ("cls")
    
    if usr[0][3] != False:
        while True:
            test_mdp = input ("Entrer votre mot de passe : ")
            os.system ("cls")
            if test_mdp != usr[0][3]: print (" Mot de passe incorrect...\n")
            else: break
    
    if usr[0][2] != usr[0][-1]: usr[0][4] += 1
    else:
        usr_nom = usr[0][0]
        usr_son = usr[0][1]
        if usr_son:
            usr_son, F_son = outils.selection_son ()
        else:
            os.system ("cls")
            print (" Le chemin d'accès est incorrect ! Désolé...\n")
        usr_mdp = usr[0][3]
        usr_nbr = 1
        
        usr_infos = [usr_nom, usr_son, F_son, usr_mdp, usr_nbr, usr_version]
        lgc_infos = usr[1]
        usr = [usr_infos, lgc_infos]
    outils.ecriture_pickle (usr, F_usr)
    
    if usr[0][1]:
        test = outils.lancer_son (usr[0][2])
        if test == "ERREUR":
            usr[0][1] = False
            usr[0][2] = None
            outils.ecriture_pickle (usr, F_usr)
    
    # INTEGRATION DE L'APPLICATION REP MD (annonce lors de l'anniversaire d'un contact !)
    logging.info (f"OUVERTURE: Centre MD ({usr[0][4]}ème fois)\n")
    if date.hour < 12:
        print (f" Bonjour {usr[0][0]} !\n")
    elif date.hour > 12 and date.hour < 18:
        print (f" Bonsoir {usr[0][0]} !\n")
    else:
        print (f" Bonne nuit {usr[0][0]} !\n")
    
    from apps.rep_md.main import F_rep
    if os.path.exists (F_rep):
        rep = outils.lecture_csv (F_rep)
        date = [date.day, date.month]
        
        for i in range (len (rep)):
            date_c = rep[i]["date"]
            date_c = date_c.split (".")
            if date_c != [""]:
                for y in range (2):
                    date_c[y] = int (date_c[y])
                del date_c[-1]
            if date == date_c:
                nom_c = rep[i]["nom"]
                prenom_c = rep[i]["prenom"]
                print (f" N'oubliez pas, aujourd'hui,\n c'est l'anniversaire de {nom_c} {prenom_c} !\n")
        
    
while True:
    print (" --- Centre MD ---\n")
    
    print ("  0. Arrêter")
    if usr[1][0] == True: print ("  1. Rep MD")
    if usr[1][1] == True: print ("  2. Jeux MD")
    if usr[1][2] == True: print ("  3. GDT MD")
    if usr[1][3] == True: print ("  4. MDP MD")
    if usr[1][4] == True: print ("  5. Fonds MD (BETA !)")
    print ("\n  6. Options")
    
    choix = input ("\nChoix : ")
    
    match choix:
        
        case "0":
            logging.info ("FERMETURE: Centre MD\n")
            break
        
        case "1":
            if usr[1][0] == True:
                os.system ("cls")
                from apps.rep_md.main import rep_md
                logging.info ("  OUVERTURE: Rep MD\n")
                rep_md ()
                logging.info ("  FERMETURE: Rep MD\n")
                os.system ("cls")
        
        case "2":
            if usr[1][1] == True:
                os.system ("cls")
                from apps.jeux_md.main import jeux_md
                logging.info ("  OUVERTURE: Jeux MD\n")
                jeux_md ()
                logging.info ("  FERMETURE: Jeux MD\n")
                os.system ("cls")
            
        case "3":
            if usr[1][2] == True:
                os.system ("cls")
                logging.info ("  OUVERTURE: GDT MD\n")
                from apps.gdt_md.main import gdt_md
                gdt_md ()
                logging.info ("  FERMETURE: GDT MD\n")
                os.system ("cls")
        
        case "4":
            if usr[1][3] == True:
                os.system ("cls")
                from apps.mdp_md.main import mdp_md
                logging.info ("  OUVERTURE: MDP MD\n")
                mdp_md ()
                logging.info ("  FERMETURE: MDP MD\n")
                os.system ("cls")
        
        case "5":
            if usr[1][4] == True:
                os.system ("cls")
                from apps.fonds_md.main import fonds_md
                logging.info ("  OUVERTURE: Fonds MD\n")
                fonds_md ()
                logging.info ("  FERMETURE: Fonds MD\n")
                os.system ("cls")
        
        case "6":
            os.system ("cls")
            logging.info ("  OUVERTURE: Options\n")
            test = outils.options (usr, F_usr, F_log, gestionnaire_log)
            if test != "6":
                logging.info ("  FERMETURE: Options\n")
                os.system ("cls")
            else: break
                
        case _:
            os.system ("cls")
            print (" Choix impossible...\n")