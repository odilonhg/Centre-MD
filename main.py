from outils import lancer_mp3, couper_mp3, ecriture_pickle, lecture_pickle

import logging
import os
import time
import datetime
import sys
import random

f_log = "data_log.txt"
f_usr = "data_usr"

usr_infos = [False, False, False]
lgc_infos = [False, False, False, False, False]

logging.basicConfig(filename = f_log, level = logging.INFO, format = "%(asctime)s %(message)s", datefmt = "%d/%m/%Y %H:%M:%S")


if os.path.exists (f_usr) == False:
    verif_nom = False
    
    print ("Bienvenue dans le Centre MD !\n")
    
    while verif_nom == False:
        
        usr_nom = input ("Veuillez saisir votre prénom : ")
        
        os.system ("cls")
        choice_nom = input (f"Vous confirmer vouloir vous appelez \"{usr_nom}\" : ").lower ()
        
        if choice_nom == "oui":
            verif_nom = True
        else: os.system ("cls")
        
    os.system ("cls")
    print ("Voulez-vous une ambiance sonore ? (désactivable par la suite)\n")
    choix_son = input ("Choix : ").lower ()
    
    if choix_son == "oui":
        usr_son = True
        lancer_mp3 ("#audio\musique_fond.mp3")
    else: usr_son = False
    
    os.system ("cls")
    print ("Enfin, voulez-vous mettre en place un mot de passe ? (modifiable / désactivable par la suite)\n")
    choix_mdp = input ("Choix : ").lower ()
    
    if choix_mdp == "oui":
        verif_mdp = False
        while verif_mdp == False:
            os.system ("cls")
            usr_mdp = input ("Saisir votre mot de passe : ")
            os.system ("cls")
            print (f"Votre mot de passe requis à l'ouverture du logiciel sera \"{usr_mdp}\", vous confirmez ?\n")
            choix_mdp_2 = input ("Choix : ").lower ()
        
            if choix_mdp_2 == "oui":
                usr_infos = [usr_nom, usr_son, usr_mdp]
                usr = [usr_infos, lgc_infos]
                verif_mdp = True
    
    else:
        usr_infos = [usr_nom, usr_son, False]
        usr = [usr_infos, lgc_infos]
    
    ecriture_pickle (usr, f_usr)
    
    os.system ("cls")
    logging.info (f"Bienvenue à toi {usr_nom} dans le Centre MD !\n")
    print (f"Bienvenue à toi {usr_nom} dans le Centre MD !\n")


else:
    
    logging.info ("OUVERTURE: Centre MD\n")
    
    usr = lecture_pickle (f_usr)
    usr_nom = usr[0][0]
    usr_son = usr[0][1]
    
    if usr[0][2] != False:
        verif_mdp = False
        usr_mdp = usr[0][2]
        while verif_mdp == False:
            test_mdp = input ("Entrer votre mot de passe : ")
            os.system ("cls")
            
            if test_mdp != usr_mdp:
                print ("Mot de passe incorrect !\n")
                time.sleep(3)
            else: verif_mdp = True
    
    lgc_infos = usr[1]
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    mess_slt = [
        f"Bonjour {usr_nom}\n! Horloge : {date}.",
        f"Salut {usr_nom} !\nHorloge : {date}.",
        f"Holà {usr_nom} !\nHorloge : {date}.",
        f"Coucou {usr_nom} !\nHorloge : {date}.",
        f"Hello {usr_nom} !\nHorloge : {date}.",
        f"Salutations {usr_nom} !\nHorloge : {date}.",
        f"Hey {usr_nom} !\nHorloge : {date}.",
        f"Wesh {usr_nom} !\nT'as trouvé mon message secret, mais ne le dis à personne !",
        f"Hey hey {usr_nom}, savais-tu que MD c'était pour MaximeDylan (les 2 créateurs de la Team) ?\nHorloge : {date}.",
        f"Bien le bonjour {usr_nom}, j'espère que tu vas bien !\nHorloge : {date}",
        f"Hé {usr_nom}, comment tu vas ?\nHorloge : {date}",
    ]
    
    if usr[0][1] == True:
        lancer_mp3 ("#audio\musique_fond.mp3")
    
    print (mess_slt [random.randint(1, len (mess_slt) - 1)] + "\n")
    

def choix ():
    
    print (" --- Centre MD ---\n")
    
    print ("  0. Arrêter")
    if usr[1][0] == True: print ("  1. Rep MD")
    if usr[1][1] == True: print ("  2. Jeux MD")
    if usr[1][2] == True: print ("  3. Tâches MD")
    if usr[1][3] == True: print ("  4. MDP MD")
    print ("  5. Options\n")
    if usr[1][4] == True: print ("  13. Fonctions Spéciales\n")
    
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
            
            os.system ("cls")
            print ("Choix impossible...\n")
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
            
            os.system ("cls")
            print ("Choix impossible...\n")
            return choix ()
            
        case "3":
            if usr[1][2] == True:
                os.system ("cls")
                from apps.taches_md.main import taches_md
                logging.info ("  OUVERTURE: Taches MD\n")
                taches_md ()
                logging.info ("  FERMETURE: Taches MD\n")
                os.system ("cls")
                return choix ()
            
            os.system ("cls")
            print ("Choix impossible...\n")
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
            
            os.system ("cls")
            print ("Choix impossible...\n")
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
            
            os.system ("cls")
            print ("Choix impossible...\n")
            return choix ()
        
        case "5": # Entre dans les Options
            os.system ("cls")
            logging.info ("  OUVERTURE: Options\n")
            options ()
            logging.info ("  FERMETURE: Options\n")
            os.system ("cls")
            return choix ()
        
        case _: # Affiche un message d'erreur si l'utilisateur rentre autre chose
            os.system ("cls")
            print ("Choix impossible...\n")
            return choix ()

def options ():
    
    print ("   · Options ·\n")
    
    print (" 0. Retour")
    
    if usr[0][1] == True: print (" 1. Couper la musique")
    else: print (" 1. Lancer la musique")
    
    print (" 2. Installer des applis")
    print (" 3. Désinstaller des applis")
    
    if usr[0][2] != False: print (" 4. Modifier / Supprimer le mot de passe\n")
    else: print (" 4. Mettre en place un mot de passe\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            if usr[0][1] == True:
                couper_mp3 ("#audio\musique_fond.mp3")
                usr[0][1] = False
                ecriture_pickle (usr, f_usr)
                logging.info ("    FERMETURE: Musique\n")
                os.system ("cls")
                return options ()
            
            else:
                lancer_mp3 ("#audio\musique_fond.mp3")
                usr[0][1] = True
                ecriture_pickle (usr, f_usr)
                logging.info ("    OUVERTURE: Musique\n")
                os.system ("cls")
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
            os.system ("cls")
            gestion_mdp ()
            return options ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return options ()

def install_apps ():
    
    print ("  · Installer une Application MD ·\n")
    
    print (" 0. Retour")
    if usr[1][0] == False: print (" 1. Rep MD (version 1.0)")
    if usr[1][1] == False: print (" 2. Jeux MD (version 1.0)")
    if usr[1][2] == False: print (" 3. Tâches MD (version 1.0)")
    if usr[1][3] == False: print (" 4. MDP MD (version 1.0)")
    if usr[1][4] == False: print (" 5. Fonctions Spéciales (version 1.0)")
    print ()
    
    choice = input ("Choix : ")
    
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
        
        case "5":
            usr[1][4] = True
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return install_apps ()
            
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return install_apps ()

def uninstall_apps ():
    
    print ("  · Désinstaller une Application MD ·\n")
    
    print (" 0. Retour")
    if usr[1][0] == True: print (" 1. Rep MD")
    if usr[1][1] == True: print (" 2. Jeux MD")
    if usr[1][2] == True: print (" 3. Tâches MD")
    if usr[1][3] == True: print (" 4. MDP MD")
    if usr[1][4] == True: print (" 5. Fonctions Spéciales")
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
                if os.path.exists (f_gdt): os.remove (f_gdt)
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
        
        case "4":
            usr[1][3] = False
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
        
        case "5":
            usr[1][4] = False
            ecriture_pickle (usr, f_usr)
            os.system ("cls")
            return uninstall_apps ()
            
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return uninstall_apps ()

def gestion_mdp ():
    usr_mdp = usr[0][2]
    if usr_mdp != False:
        while verif_mdp == False:
            os.system ("cls")
            usr_mdp = input ("Saisir votre mot de passe : ")
            os.system ("cls")
            print (f"Votre mot de passe requis à l'ouverture du logiciel sera \"{usr_mdp}\", vous confirmez ?\n")
            choix_mdp_2 = input ("Choix : ").lower ()
        
            if choix_mdp_2 == "oui":
                usr_infos = [usr_nom, usr_son, usr_mdp]
                usr = [usr_infos, lgc_infos]
                verif_mdp = True
                os.system ("cls")
                print ("Mot de passe crée !\n")
    
    else:
        usr_infos = [usr_nom, usr_son, False]
        usr = [usr_infos, lgc_infos]
        os.system ("cls")
        print ("Mot de passe supprimé !\n")

choix ()