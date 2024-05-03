from outils import lancer_mp3, couper_mp3, ecriture_pickle, lecture_pickle, lecture_fichier

import logging
import os
import time
import datetime
import sys
import random

f_log = "data_log.txt"
f_usr = "data_usr"
f_son = "#audio\maya_danse.mp3"

logging.basicConfig(filename = f_log, level = logging.INFO, format = "%(asctime)s %(message)s", datefmt = "%d/%m/%Y %H:%M:%S")
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if os.path.exists (f_usr) == False:
    lgc_infos = [False, False, False, False, False]
    
    print ("Bienvenue dans le Centre MD !\n")
    
    verif_nom = False
    while verif_nom == False:
        
        usr_nom = input ("Veuillez saisir votre prénom : ")
        usr_nom = "Maya"
        
        os.system ("cls")
        choix_nom = input (f"Vous confirmer vouloir vous appelez \"{usr_nom}\" : ").lower ()
        os.system ("cls")
        
        if choix_nom == "oui": verif_nom = True
        else:
            print ("Dommage pour toi...\n")
            verif_nom = True
    
    verif_son = False
    while verif_son == False:
        
        choix_son = input ("Confirmez vouloir une ambiance sonore : ").lower ()
        os.system ("cls")
        
        if choix_son == "oui":
            verif_son = True
            usr_son = True
            lancer_mp3 (f_son)
        elif choix_son == "non":
            print ("Dommage pour toi...\n")
            verif_son = True
            usr_son = True
            lancer_mp3 (f_son)
        else: print ("Tu dois répondre \"oui\" ou \"non\"\n")
    
    usr_mdp = False
    
    usr_infos = [usr_nom, usr_son, usr_mdp]
    usr = [usr_infos, lgc_infos]
    
    ecriture_pickle (usr, f_usr)
    
    os.system ("cls")
    logging.info (f"Bienvenue à toi {usr_nom} dans le Centre MD !\n")
    print (f"Bienvenue à toi {usr_nom} dans le Centre MD !\n")


else:
    
    logging.info ("OUVERTURE: Centre MD\n")
    
    usr = lecture_pickle (f_usr)
    
    if usr[0][2] != False:
        
        verif_mdp = False
        while verif_mdp == False:
            test_mdp = input ("Entrer votre mot de passe : ")
            os.system ("cls")
            
            if test_mdp != usr[0][2]:
                print ("Mot de passe incorrect !\n")
                time.sleep(3)
            else: verif_mdp = True
        
    mess_slt = [
        f"Bonjour {usr[0][0]} !\n Horloge : {date}.",
        f"Salut {usr[0][0]} !\nHorloge : {date}.",
        f"Holà {usr[0][0]} !\nHorloge : {date}.",
        f"Coucou {usr[0][0]} !\nHorloge : {date}.",
        f"Hello {usr[0][0]} !\nHorloge : {date}.",
        f"Salutations {usr[0][0]} !\nHorloge : {date}.",
        f"Hey {usr[0][0]} !\nHorloge : {date}.",
        f"Wesh {usr[0][0]} !\nT'as trouvé mon message secret, mais ne le dis à personne !",
        f"Bien le bonjour {usr[0][0]}, j'espère que tu vas bien !\nHorloge : {date}",
        f"Hé {usr[0][0]}, comment tu vas ?\nHorloge : {date}",
        f"Date de publication : 2 Mai 2024\nHorloge : {date}" # A MODIFIER
    ]
    
    lancer_mp3 (f_son)
    
    print (mess_slt [random.randint(0, len (mess_slt) - 1)] + "\n")
    

def choix ():
    global usr
    print (" --- Centre MD ---\n")
    
    print ("  0. Arrêter")
    if usr[1][0] == True: print ("  1. Rep MD")
    if usr[1][1] == True: print ("  2. Jeux MD")
    if usr[1][2] == True: print ("  3. Tâches MD")
    if usr[1][3] == True: print ("  4. MDP MD")
    print ("  5. Options\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            logging.info ("FERMETURE: Centre MD\n")
            sys.exit (0)
        
        case "1":
            if usr[1][0] == True:
                os.system ("cls")
                from apps.rep_md.main import rep_md
                logging.info ("  OUVERTURE: Rep MD\n")
                rep_md ()
                logging.info ("  FERMETURE: Rep MD\n")
                os.system ("cls")
                return choix ()
        
        case "2":
            if usr[1][1] == True:
                os.system ("cls")
                from apps.jeux_md.main import jeux_md
                logging.info ("  OUVERTURE: Jeux MD\n")
                jeux_md ()
                logging.info ("  FERMETURE: Jeux MD\n")
                os.system ("cls")
                return choix ()
            
        case "3":
            if usr[1][2] == True:
                os.system ("cls")
                logging.info ("  OUVERTURE: GDT MD\n")
                from apps.gdt_md.main import gdt_md
                gdt_md ()
                logging.info ("  FERMETURE: GDT MD\n")
                os.system ("cls")
                return choix ()
        
        case "4":
            if usr[1][3] == True:
                os.system ("cls")
                from apps.mdp_md.main import mdp_md
                logging.info ("  OUVERTURE: MDP MD\n")
                mdp_md ()
                logging.info ("  FERMETURE: MDP MD\n")
                os.system ("cls")
                return choix ()
        
        case "13":
            if usr[1][4] == True:
                os.system ("cls")
                from apps.fs_md.main import fs_md
                logging.info ("  OUVERTURE: FS MD\n")
                fs_md ()
                logging.info ("  FERMETURE: FS MD\n")
                os.system ("cls")
                return choix ()
        
        case "5":
            os.system ("cls")
            logging.info ("  OUVERTURE: Options\n")
            options ()
            logging.info ("  FERMETURE: Options\n")
            os.system ("cls")
            return choix ()
    
    os.system ("cls")
    print ("Choix impossible...\n")
    return choix ()

def options ():
    global usr
    print ("   · Options ·\n")
    print ("Version 1.1\n") # A MODIFIER
    
    print (" 0. Retour")
    
    if usr[0][1] == True: print (" 1. Couper la musique")
    else: print (" 1. Lancer la musique")
    
    if False in usr[1]: print (" 2. Installer des applis")
    if True in usr[1]: print (" 3. Désinstaller des applis")
    
    if usr[0][2] != False: print (" 4. Supprimer le mot de passe")
    else: print (" 4. Mettre en place un mot de passe")
    
    print (" 5. Affichage des logs\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            os.system ("cls")
            print ("T'as trop cru tu pouvais couper la Maya Danse ?\n")
            lancer_mp3 (f_son)
            logging.info ("    OUVERTURE: MAYA L'ABEILLE\n")
            return options ()
        
        case "2":
            os.system ("cls")
            install_apps ()
            os.system ("cls")
            return options ()
        
        case "3":
            os.system ("cls")
            uninstall_apps ()
            os.system ("cls")
            return options ()
        
        case "4":
            gestion_mdp ()
            return options ()
        
        case "5":
            logging.info ("    AFFICHAGE DES LOGS (cc)\n")
            contenu_logs = lecture_fichier (f_log)
            os.system ("cls")
            print (contenu_logs.rstrip ("\n") + "\n")
            return options ()
            
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return options ()

def install_apps ():
    global usr
    print ("  · Installer une Application MD ·\n")
    
    print (" 0. Retour")
    if usr[1][0] == False: print (" 1. Rep MD (version 2.0)")
    if usr[1][1] == False: print (" 2. Jeux MD (version 1.0)")
    if usr[1][2] == False: print (" 3. GDT MD (version 1.1)")
    if usr[1][3] == False: print (" 4. MDP MD (version 1.0)")
    
    choice = input ("\nChoix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            usr[1][0] = True
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return install_apps ()
        
        case "2":
            usr[1][1] = True
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return install_apps ()
        
        case "3":
            usr[1][2] = True
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return install_apps ()
        
        case "4":
            usr[1][3] = True
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return install_apps ()
            
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return install_apps ()

def uninstall_apps ():
    global usr
    print ("  · Désinstaller une Application MD ·\n")
    
    print (" 0. Retour")
    if usr[1][0] == True: print (" 1. Rep MD")
    if usr[1][1] == True: print (" 2. Jeux MD")
    if usr[1][2] == True: print (" 3. Tâches MD")
    if usr[1][3] == True: print (" 4. MDP MD")
    print ()
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            usr[1][0] = False
            os.system ("cls")
            print ("Supprimer les données du logiciel ?\n")
            choice_rep = input  ("Choix : ").lower ()
            if choice_rep == "oui":
                from apps.rep_md.main import f_rep
                if os.path.exists (f_rep): os.remove (f_rep)
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
        
        case "2":
            usr[1][1] = False
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
        
        case "3":
            usr[1][2] = False
            os.system ("cls")
            print ("Supprimer les données du logiciel ?\n")
            choice_gdt = input  ("Choix : ").lower ()
            if choice_gdt == "oui":
                from apps.taches_md.main import f_gdt
                if os.path.exists (f_gdt): os.remove (f_gdt)
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
        
        case "4":
            usr[1][3] = False
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
            
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return uninstall_apps ()

def gestion_mdp ():
    global usr
    
    if usr[0][2] == False:
        verif_mdp = False
        while verif_mdp == False:
            
            os.system ("cls")
            usr[0][2] = input ("Saisir votre mot de passe (\"ANNULER\" pour annuler): ")
            
            if usr[0][2] == "ANNULER":
                os.system ("cls")
                print ("Action annulée !\n")
                return
            
            os.system ("cls")
            choix_mdp_2 = input (f"Vous confirmez que le mot de passe requis à l'ouverture du logiciel sera \"{usr[0][2]}\" : ").lower ()
        
            if choix_mdp_2 == "oui":
                ecriture_pickle (usr, f_usr)
                verif_mdp = True
                os.system ("cls")
                print ("Mot de passe crée !\n")
    
    else:
        os.system ("cls")
        test_mdp = input ("Saisir votre mot de passe : ")
        
        if test_mdp == usr[0][2]:
            usr[0][2] = False
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            print ("Mot de passe supprimé !\n")
        else:
            os.system ("cls")
            print ("Mot de passe incorrect !\n")

choix ()