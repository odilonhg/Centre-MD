from outils import Outils, Depart, Options, Autres
import datetime
import time
import sys
import logging
import os

f_log = "data_log.txt"
f_old_usr = "data_usr"
f_usr = "data_usr.csv"
f_cle = "data_cle"

usr_version = "2.0.0b"

logging.basicConfig (filename = f_log, level = logging.INFO, format = "%(asctime)s %(message)s", datefmt = "%d/%m/%Y %H:%M:%S") # INITIALISE LES LOGS
gestionnaire_log = logging.getLogger().handlers[0] # UTILE POUR ARRETER LE FONCTIONNEMENT DES LOGS
date = datetime.datetime.now() # DEFINIT LA DATE

os.system ("cls")
if not os.path.exists (f_usr) and not os.path.exists (f_old_usr):
    # CREATION CLE ENCRYPTAGE
    cle = Outils.Cle.ecriture_cle (f_cle)
    
    # CHOIX DE LA LANGUE
    f_langue, usr_langue = Depart.choix_langue ()
    liste_langue = Outils.lecture_langue (f_langue)
    os.system ("cls")
    
    print (f"   · {liste_langue[7][0]} ! ·\n")
    time.sleep (3)
    print (liste_langue[7][1])
    time.sleep (5)
    os.system ("cls")
    
    # CHOIX DU NOM
    usr_nom = Depart.choix_nom (liste_langue)
    os.system ("cls")
    
    # CHOIX DU SON
    f_son, usr_son = Depart.choix_son (liste_langue, usr_nom)
    os.system ("cls")
    
    # CHOIX DU MDP
    usr_mdp = Depart.choix_mdp (liste_langue, usr_nom)
    os.system ("cls")
    
    # DEFINITION DU NBR DE FOIS QUE LE USER A LANCE LE LOGICIEL (1ere fois)
    usr_nbr = 1
    
    # DEFINITION DES DONNEES CONTENUES DS f_usr
    usr = [[usr_langue, usr_nom, usr_son, f_son, usr_mdp, usr_nbr, usr_version, False, False, False, False, False]]
    
    Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
    
    print (f"   · {liste_langue[7][9]} ·\n")
    print (liste_langue[7][10])
    time.sleep (6)
    os.system ("cls")
    logging.info (f"{liste_langue[1][0]} {usr_nom} !\n")
    
else:
    # GESTION ERREUR CLE (nouveau fichier data_cle)
    if not os.path.exists(f_cle):
        cle = Outils.Cle.ecriture_cle (f_cle)
    else:
        cle = Outils.Cle.lecture_cle (f_cle)
    
    # GESTION ERREUR v1 (nouveau fichier data_usr)
    if os.path.exists (f_old_usr):
        Autres.erreur_data_usr (f_old_usr, f_usr, cle, usr_version)
    
    usr = Outils.CSV.lecture_encryptee_csv (f_usr, cle)
    
    # GESTION AFFICHAGE DANS LA BONNE LANGUE + 
    if usr[0][0] == "fr":
        f_langue = "langues\\FRENCH-fr"
    elif usr[0][0] == "en":
        f_langue = "langues\\ENGLISH-en"
    else:
        print ("ERREUR: Choix Langue\n\nLangue non prise en charge par la Team MD !\nPassage automatique en Français\n")
        f_langue = "langues\\FRENCH-fr"
    liste_langue = Outils.lecture_langue (f_langue)
    
    # GESTION MDP
    if usr[0][4] != False:
        while True:
            test_mdp = input (liste_langue[0][8])
            if test_mdp != usr[0][4]:
                os.system ("cls")
                print (f"{liste_langue[0][9]}\n")
                time.sleep (3)
            else:
                os.system ("cls")
                break
    
    # GESTION MESSAGE DE BIENVENUE
    if date.hour <= 12:
        print (f"{liste_langue[0][5]} {usr[0][1]} !\n")
    elif 12 < date.hour < 18:
        print (f"{liste_langue[0][6]} {usr[0][1]} !\n")
    else:
        print (f"{liste_langue[0][7]} {usr[0][1]} !\n")
    
    usr[0][5] += 1
    Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
    usr = Outils.CSV.lecture_encryptee_csv (f_usr, cle)

logging.info (f"{liste_langue[1][1]}: {liste_langue[1][8]}\n")

while True: # Lancement boucle Centre MD
    usr = Outils.CSV.lecture_encryptee_csv (f_usr, cle)
    print (f" -- {liste_langue[8][0]} --\n")
    
    print (f"  0. {liste_langue[8][1]}")
    if usr[0][7]: print (f"  1. {liste_langue[10][0]}")
    if usr[0][8]: print (f"  2. {liste_langue[11][0]}")
    if usr[0][9]: print (f"  3. {liste_langue[12][0]}")
    if usr[0][10]: print (f"  4. {liste_langue[13][0]}")
    print (f"\n  5. {liste_langue[9][0]}\n")
    if usr[0][11]: print (f"  13. {liste_langue[14][0]}\n")
    
    choix = input (liste_langue[0][3]).lower ()
    
    if choix == "0":
        logging.info (f"{liste_langue[1][2]}: {liste_langue[1][8]}\n")
        sys.exit (0)
        
    elif choix == "1":
        if usr[0][7]:
            from apps.rep_md.main import rep_md
            logging.info (f"  {liste_langue[1][1]}: {liste_langue[2][0]}\n")
            os.system ("cls")
            rep_md ()
            os.system ("cls")
            logging.info (f"  {liste_langue[1][2]}: {liste_langue[2][0]}\n")
        else:
            os.system ("cls")
            print (f"{liste_langue[0][10]}\n")
        
    elif choix == "2":
        if usr[0][8]:
            from apps.manager_md.main import manager_md
            logging.info (f"  {liste_langue[1][1]}: {liste_langue[3][0]}\n")
            os.system ("cls")
            manager_md ()
            os.system ("cls")
            logging.info (f"  {liste_langue[1][2]}: {liste_langue[3][0]}\n")
        else:
            os.system ("cls")
            print (f"{liste_langue[0][10]}\n")
        
    elif choix == "3":
        if usr[0][9]:
            from apps.pass_md.main import pass_md
            logging.info (f"  {liste_langue[1][1]}: {liste_langue[4][0]}\n")
            os.system ("cls")
            pass_md ()
            os.system ("cls")
            logging.info (f"  {liste_langue[1][2]}: {liste_langue[4][0]}\n")
        else:
            os.system ("cls")
            print (f"{liste_langue[0][10]}\n")
        
    elif choix == "4":
        if usr[0][10]:
            from apps.jeux_md.main import jeux_md
            logging.info (f"  {liste_langue[1][1]}: {liste_langue[5][0]}\n")
            os.system ("cls")
            jeux_md ()
            os.system ("cls")
            logging.info (f"  {liste_langue[1][2]}: {liste_langue[5][0]}\n")
        else:
            os.system ("cls")
            print (f"{liste_langue[0][10]}\n")
        
    elif choix == "13":
        if usr[0][11]:
            from apps.fonctions_md.main import fonctions_md
            logging.info (f"  {liste_langue[1][1]}: {liste_langue[6][0]}\n")
            os.system ("cls")
            fonctions_md ()
            os.system ("cls")
            logging.info (f"  {liste_langue[1][2]}: {liste_langue[6][0]}\n")
        else:
            os.system ("cls")
            print (f"{liste_langue[0][10]}\n")
        
    elif choix == "5":
        logging.info (f"  {liste_langue[1][1]}: {liste_langue[1][9]}\n")
        os.system ("cls")
        Options.main (liste_langue, usr, f_usr, f_log, usr_version, cle, f_cle, gestionnaire_log)
        os.system ("cls")
        logging.info (f"  {liste_langue[1][2]}: {liste_langue[1][9]}\n")
        
    elif choix == f"{liste_langue[0][4]}":
        os.system ("cls")
        print (liste_langue[15][0])
        print (liste_langue[15][1] + "\n")
        
    else:
        os.system ("cls")
        print (f"{liste_langue[0][10]}\n")