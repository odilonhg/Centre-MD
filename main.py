import outils
import os
import logging
import datetime
import gettext
import time

F_log= "data_log.txt"
F_old_usr= "data_usr"
F_usr= "data_usr.csv"
F_cle= "data_cle"

usr_version= "2.0.0"

logging.basicConfig (filename= F_log, level= logging.INFO, format= "%(asctime)s %(message)s", datefmt= "%d/%m/%Y %H:%M:%S") # INITIALISE LES LOGS
gestionnaire_log= logging.getLogger().handlers[0] # UTILE POUR ARRETER LE FONCTIONNEMENT DES LOGS
date= datetime.datetime.now() # DEFINIT LA DATE

os.system ("cls")
if not os.path.exists (F_usr) and not os.path.exists (F_old_usr):
    # CREATION CLE ENCRYPTAGE
    cle = outils.Cle.ecriture_cle (F_cle)
    
    # CHOIX DE LA LANGUE
    usr_langue= outils.Langues.choix_langue ()
    outils.Langues.modifier_langue (usr_langue)
    os.system ("cls")
    
    print (_("Bienvenue !"))
    time.sleep (3)
    print (_("Je vais t'aider à configurer ton Centre MD !"))
    time.sleep (5)
    os.system ("cls")
    
    # CHOIX DU NOM
    usr_nom = outils.choix_nom ()
    os.system ("cls")
    
    # CHOIX DU SON
    F_son, usr_son = outils.choix_son (usr_nom)
    os.system ("cls")
    1
    # CHOIX DU MDP
    usr_mdp = outils.choix_mdp (usr_nom)
    os.system ("cls")
    
    # DEFINITION DU NBR DE FOIS QUE LE USR A LANCE LE LOGICIEL (1ere fois)
    usr_nbr = 1
    
    # DEFINITION DES DONNEES CONTENUES DS f_usr
    usr = [[usr_langue, usr_nom, usr_son, F_son, usr_mdp, usr_nbr, usr_version, False, False, False, False, False]]
    outils.CSV.ecriture_encryptee_csv (usr, F_usr, cle)
    
    print (_("CONFIGURATION TERMINEE !"))
    print (_("Si tu as besoin d'aide, tape aide !"))
    time.sleep (6)
    os.system ("cls")
    logging.info (_("_Bienvenue nom_")+ usr_nom+ " ·\n")

else:
    # GESTION ERREUR CLE (nouveau fichier data_cle)
    if not os.path.exists(F_cle):
        cle= outils.Cle.ecriture_cle (F_cle)
        test_v1= True
    else:
        cle= outils.Cle.lecture_cle (F_cle)
        test_v1= False
    
    # GESTION TRANSITION DONNEES v1 VERS v2
    if test_v1:
        outils.Autres.erreur_data_usr (F_old_usr, F_usr, cle, usr_version)
    
    usr= outils.CSV.lecture_encryptee_csv (F_usr, cle)
    
    # GESTION AFFICHAGE DANS LA BONNE LANGUE
    outils.Langues.modifier_langue (usr[0][0])
    
    # GESTION MDP
    if usr[0][4]!= False:
        while True:
            test_mdp= input (_("Entre le mot de passe"))
            if test_mdp!= usr[0][4]:
                os.system ("cls")
                print (_("Mot de passe incorrect"))
                time.sleep (3)
            else:
                os.system ("cls")
                break
    
    # GESTION MUSIQUE
    if usr[0][2]== True:
        if usr[0][3]== False:
            usr[0][2]= False
            outils.CSV.ecriture_encryptee_csv (usr, F_usr, cle)
        elif os.path.exists (usr[0][3])== False:
            usr[0][3]= False
            usr[0][2]= False
            outils.CSV.ecriture_encryptee_csv (usr, F_usr, cle)
        else:
            outils.Musiques.gestion_musique (usr[0][3], "lire_musique")
    
    # GESTION MESSAGE DE BIENVENUE
    if date.hour <= 12:
        print (_("Bonjour nom")+ f"{usr[0][1]} !\n")
    elif 12 < date.hour < 18:
        print (_("Bonsoir nom")+ f"{usr[0][1]} !\n")
    else:
        print (_("Bonne nuit nom")+ f"{usr[0][1]} !\n")
    
    usr[0][5] += 1
    outils.CSV.ecriture_encryptee_csv (usr, F_usr, cle)
    
logging.info (_("_OUVERTURE_")+ _("_Centre MD_")+ "\n")

while True: # Lancement boucle Centre MD
    usr = outils.CSV.lecture_encryptee_csv (F_usr, cle)
    print (_("-Centre MD-"))
    
    print (_("Arrêter"))
    if usr[0][7]: print (_("Rep MD"))
    if usr[0][8]: print (_("Manager MD"))
    if usr[0][9]: print (_("Pass MD"))
    if usr[0][10]: print (_("Jeux MD"))
    print (_("Options"))
    if usr[0][11]: print (_("Fonctions MD"))
    
    choix= input (_("Choix")).lower ()
    
    if choix== "0":
        outils.Musiques.gestion_musique (usr[0][3], "couper_musique")
        logging.info (_("_FERMETURE_")+ _("_Centre MD_")+ "\n")
        break
    
    elif choix== "1" and usr[0][7]:
        from apps.rep_md.main import rep_md
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Rep MD_")+ "\n")
        os.system ("cls")
        rep_md ()
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Rep MD_")+ "\n")
    
    elif choix== "2" and usr[0][8]:
        from apps.manager_md.main import manager_md
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Manager MD_")+ "\n")
        os.system ("cls")
        manager_md ()
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Manager MD_")+ "\n")
    
    elif choix== "3" and usr[0][9]:
        from apps.pass_md.main import pass_md
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Pass MD_")+ "\n")
        os.system ("cls")
        pass_md ()
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Pass MD_")+ "\n")
    
    elif choix== "4" and usr[0][10]:
        from apps.jeux_md.main import jeux_md
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Jeux MD_")+ "\n")
        os.system ("cls")
        jeux_md ()
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Jeux MD_")+ "\n")

    elif choix== "5":
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Options_")+ "\n")
        os.system ("cls")
        outils.Options.main (usr, F_usr, F_log, usr_version, cle, F_cle, gestionnaire_log)
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Options_")+ "\n")
    
    elif choix== "13" and usr[0][11]:
        from apps.fonctions_md.main import fonctions_md
        logging.info ("  "+ _("_OUVERTURE_")+ _("_Fonctions MD_")+ "\n")
        os.system ("cls")
        fonctions_md ()
        os.system ("cls")
        logging.info ("  "+ _("_FERMETURE_")+ _("_Fonctions MD_")+ "\n")
    
    elif choix== _("aide"):
        os.system ("cls")
        print (_("aide_centre_md"))
    
    else:
        os.system ("cls")
        print (_("Choix impossible"))