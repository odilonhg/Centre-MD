from cryptography.fernet import Fernet
import os
import gettext
from tkinter import filedialog
import shutil
import pygame
import threading
import json
import csv
import pickle
import logging
import sys

class Cle: #CHATGPT
    @staticmethod
    
    def ecriture_cle (chemin):
        cle = Fernet.generate_key ()
        with open (chemin, "wb") as f: f.write (cle)
        return cle
    
    def lecture_cle (chemin):
        with open (chemin, "rb") as f: return f.read ()

class Langues:
    @staticmethod
    
    def choix_langue ():
        while True:
            print ("   · Langues ·\n")
            print (" 1. Français")
            print (" 2. English\n")
            
            choix_langue= input ("Choix: ")
            
            match choix_langue:
                case "1": return "fr"
                case "2": return "en"
                case _:
                    os.system ("cls")
                    print (" Tu dois choisir entre 1 et 2!\n You must choose between 1 and 2!\n")
    
    # CHATGPT
    def modifier_langue (usr_langue):
        D_langue= os.path.join(os.path.abspath(os.path.dirname(__file__)), "langues")
        langue= gettext.translation ("messages", D_langue, languages= [usr_langue], fallback= True)
        langue.install()
        global _
        _= langue.gettext

class Musiques:
    @staticmethod
    
    #CHATGPT
    def selection_mp3 ():
        chemin_fichier= filedialog.askopenfilename(
            title= _("Sélectionnez un fichier MP3"),
            filetypes= [(_("Fichiers MP3"), "*.mp3")])
        
        if chemin_fichier!= "":
            nom_fichier= os.path.basename(chemin_fichier)
            chemin_fichier= Musiques.copier_mp3 (chemin_fichier, nom_fichier)
            return chemin_fichier
        else: return False
    
    def copier_mp3 (chemin, fichier):
        chemin_final= os.path.join (os.getcwd (), "audios")
        chemin_final= os.path.join (chemin_final, fichier)
        
        try: shutil.copy (chemin, chemin_final)
        except: chemin_final= False
        finally: return chemin_final
    
    def gestion_musique (chemin, choix):
        global stop_mp3
        if choix== "lire_musique":
            stop_mp3 = False
            pygame.mixer.init()
            pygame.mixer.music.load(chemin)
            pygame.mixer.music.play()
        
            def verifier_musique ():
                while not stop_mp3:
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play()
                    pygame.time.Clock().tick(10)
            
            threading.Thread (target = verifier_musique, daemon = True).start ()
            
        elif choix== "couper_musique":
            stop_mp3= True
            try: pygame.mixer.music.stop()
            except:
                pygame.mixer.init()
                pygame.mixer.music.stop()
        
        else: print ("ERREUR: CHOIX MUSIQUE IMPOSSIBLE")

class CSV:
    @staticmethod
    
    def ecriture_csv (L, F, delimiter= ";"):
        with open (F, "w") as Fcsv:
            ligneDesc= ";".join (L[0].keys())+ "\n"
            Fcsv.write (ligneDesc)
            for cle in range (len (L)):
                ligne= ";".join (L[cle].values ()) + "\n"
                Fcsv.write (ligne)
        
    def lecture_csv (F, delimiter= ";"):
        L= []
        
        try:
            with open(F, "r", newline= "") as Fcsv:
                reader = csv.DictReader (Fcsv, delimiter= delimiter)
                for row in reader:
                    L.append (row)
        except FileNotFoundError:
            print (f"Le fichier {F} n'a pas été trouvé.")
        except Exception as e:
            print (f"Une erreur s'est produite : {e}")
        return L
    
    def ecriture_encryptee_csv (donnees, fichier, cle):
        donnees_encryptees= CSV.encrypter_csv (donnees, cle)
        with open (fichier, "w", newline= "") as f:
            writer= csv.writer (f, delimiter= ";")
            for ligne in donnees_encryptees:
                writer.writerow ([ligne])
    
    #CHATGPT
    def encrypter_csv (donnees, cle):
        fernet= Fernet (cle)
        donnees_encryptees= []
        for ligne in donnees:
            ligne_json= json.dumps (ligne)
            ligne_bytes= ligne_json.encode ()  # Encoder la chaîne en bytes
            ligne_encryptee= fernet.encrypt (ligne_bytes)  # Chiffrer les bytes
            donnees_encryptees.append (ligne_encryptee.decode ())  # Ajouter la ligne chiffrée comme chaîne de caractères
        return donnees_encryptees
    
    def lecture_encryptee_csv (fichier, cle):
        fernet= Fernet (cle)
        donnees_decryptees= []
        with open (fichier, "r", newline= "") as f:
            reader= csv.reader (f, delimiter= ";")
            for ligne in reader:
                ligne_encryptee= ligne[0]
                ligne_decryptee= fernet.decrypt (ligne_encryptee.encode ()).decode ()  # Déchiffrer la ligne
                donnees_decryptees.append (json.loads (ligne_decryptee))  # Convertir la chaîne de caractères en liste
        return donnees_decryptees

class Options:
    @staticmethod
    
    def main (usr, F_usr, F_log, usr_version, cle, F_cle, gestionnaire_log):
        while True:
            print (_("-Options-"))
            print (f"v{usr_version}\n")
            
            print (_("Retour"))
            
            print (_("Changer la langue"))
            
            if usr[0][2]: print (_("Couper la musique"))
            else: print (_("Lancer la musique"))
            
            print (_("Changer de musique"))
            
            print (_("Gérer les applis"))
            
            if usr[0][4]== False: print (_("Mettre en place le mdp"))
            else: print (_("Supprimer le mdp"))
            
            print (_("Afficher les logs"))
            
            print (_("Afficher les infos usr"))
            
            print ("\n"+ _("Réinitialiser le Centre MD"))
            
            choix_options= input (_("Choix")).lower ()
            os.system ("cls")
            
            if choix_options== "0": break
            
            elif choix_options== "1":
                old_langue= usr[0][0]
                usr[0][0]= Langues.choix_langue ()
                Langues.modifier_langue (usr[0][0])
                CSV.ecriture_encryptee_csv (usr, F_usr, cle)
                logging.info ("    "+ _("_CHANGEMENT LANGUE_")+ f"{old_langue} -> {usr[0][0]}\n")
                os.system ("cls")
                
            elif choix_options== "2":
                if usr[0][2]:
                    usr[0][2]= False
                    CSV.ecriture_encryptee_csv (usr, F_usr, cle)
                    logging.info ("    "+ _("_FERMETURE_")+ _("_Musique_")+ "\n")
                    Musiques.gestion_musique (usr[0][3], "couper_musique")
                else:
                    usr[0][2]= True
                    CSV.ecriture_encryptee_csv (usr, F_usr, cle)
                    if usr[0][3]!= False:
                        logging.info ("    "+ _("_OUVERTURE_")+ _("_Musique_")+ "\n")
                        Musiques.gestion_musique (usr[0][3], "lire_musique")
                    else:
                        usr[0][3] = Musiques.selection_mp3 ()
                        CSV.ecriture_encryptee_csv (usr, F_usr, cle)
                        logging.info ("    "+ _("_CHANGEMENT MUSIQUE_")+ usr[0][3]+ "\n")
                        logging.info ("    "+ _("_OUVERTURE_")+ _("_Musique_")+ "\n")
                        Musiques.gestion_musique (usr[0][3], "lire_musique")
            
            elif choix_options== "3":
                usr[0][3]= Musiques.selection_mp3 ()
                CSV.ecriture_encryptee_csv (usr, F_usr, cle)
                if usr[0][2]: Musiques.gestion_musique (usr[0][3], "lire_musique")
                logging.info ("    "+ _("_CHANGEMENT MUSIQUE_")+ str(usr[0][3])+ "\n")
            
            elif choix_options== "4":
                Options.gestion_apps (usr, F_usr, cle)
                os.system ("cls")
            
            elif choix_options== "5":
                Options.gestion_mdp (usr, F_usr, cle)
                os.system ("cls")
            
            elif choix_options== "6":
                logging.info ("    "+ _("_AFFICHAGE_")+ _("_Logs_")+ "\n")
                contenu_logs= Options.lecture_logs (F_log)
                print (contenu_logs.rstrip ("\n") + "\n")
            
            elif choix_options== "7":
                logging.info ("    "+ _("_AFFICHAGE_")+ _("_Infos User_")+ "\n")
                print (f"{usr}\n")
            
            elif choix_options== "8":
                if usr[0][4]!= False:
                    test_mdp= input (_("Entre le mot de passe"))
                    os.system ("cls")
                    if test_mdp!= usr[0][4]: break
                
                print (_("ATTENTION, CETTE ACTION EST IRREVERSIBLE !"))
                while True:
                    choix_final= input (_("Choix")).lower ()
                    
                    if choix_final== _("oui"):
                        from apps.rep_md.main import F_rep
                        if os.path.exists (F_rep): os.remove (F_rep)
                        from apps.manager_md.main import F_gdt
                        if os.path.exists (F_gdt): os.remove (F_gdt)
                        gestionnaire_log.close ()
                        if os.path.exists (F_log): os.remove (F_log)
                        if os.path.exists (F_usr): os.remove (F_usr)
                        if os.path.exists (F_cle): os.remove (F_cle)
                        os.system ("cls")
                        print (_("REINITIALISATION TERMINEE"))
                        print (_("Appuis sur Entrée pour quitter"))
                        fin= input ()
                        logging.info ("REINITIALISATION TERMINEE...\n")
                        sys.exit(0)
                        
                    elif choix_final== _("non"):
                        os.system ("cls")
                        print (_("Action annulée"))
                        break
                    
                    else:
                        os.system ("cls")
                        print (_("Tu dois répondre oui ou non"))
                
            elif choix_options== _("aide"):
                print (_("aide_options"))
            
            else:
                os.system ("cls")
                print (_("Choix impossible"))
    
    def gestion_apps (usr, F_usr, cle):
        while True:
            print (_("-Gérer les applis-"))
        
            print (_("Retour"))
            if usr[0][7]: print (" 1. "+ _("_DESINSTALLER_")+ _("_Rep MD_")+ " (v2.1)")
            else: print (" 1. "+ _("_INSTALLER_")+ _("_Rep MD_")+ " (v2.1)")
            if usr[0][8]: print (" 2. "+ _("_DESINSTALLER_")+ _("_Manager MD_")+ " (v2.0)")
            else: print (" 2. "+ _("_INSTALLER_")+ _("_Manager MD_")+ " (v2.0)")
            if usr[0][9]: print (" 3. "+ _("_DESINSTALLER_")+ _("_Pass MD_")+ " (v1.0)")
            else: print (" 3. "+ _("_INSTALLER_")+ _("_Pass MD_")+ " (v1.0)")
            if usr[0][10]: print (" 4. "+ _("_DESINSTALLER_")+ _("_Jeux MD_")+ " (v1.1)")
            else: print (" 4. "+ _("_INSTALLER_")+ _("_Jeux MD_")+ " (v1.1)")
            if usr[0][11]: print (" 5. "+ _("_DESINSTALLER_")+ _("_Fonctions MD_")+ " (v1.1)\n")
            else: print (" 5. "+ _("_INSTALLER_")+ _("_Fonctions MD_")+ " (v1.1)\n")
            
            choix_gestion_apps= input (_("Choix")).lower ()
            
            if choix_gestion_apps== "0": break
            
            elif choix_gestion_apps== "1":
                if usr[0][7]:
                    usr[0][7]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Rep MD_")+ "\n")
                else:
                    usr[0][7]= True
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Rep MD_")+ "\n")
            
            elif choix_gestion_apps== "2":
                if usr[0][8]:
                    usr[0][8]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Manager MD_")+ "\n")
                else:
                    usr[0][8]= True
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Manager MD_")+ "\n")
            
            elif choix_gestion_apps== "3":
                if usr[0][9]:
                    usr[0][9]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Pass MD_")+ "\n")
                else:
                    usr[0][9]= True
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Pass MD_")+ "\n")
            
            elif choix_gestion_apps== "4":
                if usr[0][10]:
                    usr[0][10]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Jeux MD_")+ "\n")
                else:
                    usr[0][10]= True
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Jeux MD_")+ "\n")

            elif choix_gestion_apps== "5":
                if usr[0][11]:
                    usr[0][11]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Fonctions MD_")+ "\n")
                else:
                    usr[0][11]= True
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Fonctions MD_")+ "\n")
            
            elif choix_gestion_apps== _("aide"):
                os.system ("cls")
                print (_("aide_gestion_apps"))
            
            else:
                os.system ("cls")
                print (_("Choix impossible"))
            
            CSV.ecriture_encryptee_csv (usr, F_usr, cle)
            os.system ("cls")
    
    def gestion_mdp (usr, F_usr, cle):
        if usr[0][4]:
            while True:
                verif_mdp= input (_("Entre le mot de passe"))
                if verif_mdp== usr[0][4]:
                    usr[0][4]= False
                    logging.info ("    "+ _("_DESINSTALLER_")+ _("_Mot de passe_"))
                    os.system ("cls")
                    print (_("Mot de passe supprimé"))
                    return CSV.ecriture_encryptee_csv (usr, F_usr, cle)
            
        else:
            while True:
                usr[0][4]= input (_("Entre le mot de passe"))
                os.system ("cls")
                print (_("Tu confirmes vouloir comme mot de passe")+ str (usr[0][4])+ " ?")
                choix_mdp = input (_("Choix")).lower ()
                if choix_mdp== _("oui"):
                    os.system ("cls")
                    logging.info ("    "+ _("_INSTALLER_")+ _("_Mot de passe_"))
                    print (_("Mot de passe crée")+ str (usr[0][4])+ "\n")
                    break
                elif choix_mdp== _("non"): os.system ("cls")
                else:
                    os.system ("cls")
                    print (_("Tu dois répondre oui ou non"))
            return CSV.ecriture_encryptee_csv (usr, F_usr, cle)
        
    def lecture_logs (F_log):
        with open (F_log, "r") as f:
            return f.read()

class Autres:
    @staticmethod
    
    def erreur_data_usr (F_old_usr, F_usr, cle, usr_version):
        old_usr= Autres.lecture_pickle (F_old_usr)
        # REDEFINITION DES VARIABLES POUR FAIRE LA TRANSITION
        if old_usr[0][2]== old_usr[0][-1]: usr_nbr = 1
        else: usr_nbr= old_usr[0][3]
        usr_nom= old_usr[0][0]
        usr_son= old_usr[0][1]
        usr_mdp= old_usr[0][2]
        
        usr_langue= Langues.choix_langue ()
        Langues.modifier_langue (usr_langue)
        
        if usr_son== True:
            F_son= Musiques.selection_mp3 ()
            if F_son== False: usr_son = False
        else: F_son = False
        
        usr= [[usr_langue, usr_nom, usr_son, F_son, usr_mdp, usr_nbr, usr_version, old_usr[1][0], old_usr[1][1], old_usr[1][2], old_usr[1][3], old_usr[1][4]]]
        CSV.ecriture_encryptee_csv (usr, F_usr, cle)
        logging.info (_("MISE A JOUR DU CENTRE MD")+ ": v1 -> v2\n")
        os.remove (F_old_usr)
        os.system ("cls")
    
    # LIRE UN FICHIER (pickle)
    def lecture_pickle (fichier):
        try:
            with open (fichier, "rb") as f:
                liste= pickle.load (f)
        except: liste= []
        finally: return liste

def choix_nom ():
    while True:
        print (_("Bienvenue !"))
        usr_nom= input (_("Entre ton nom ici: "))
        os.system ("cls")
        
        print (_("Bienvenue !"))
        while True:
            choix_nom= input (_("Tu confirmes vouloir t'appeler") + usr_nom + ": ").lower ()
            
            
            if choix_nom== _("oui"): return usr_nom
            elif choix_nom== _("non"):
                os.system ("cls")
                break
            else:
                os.system ("cls")
                print (_("Tu dois répondre oui ou non"))

def choix_son (usr_nom):
    while True:
        print (_("Bienvenue nom")+ usr_nom+ " ! ·\n")
        print (_("Tu peux mettre en place une musique qui se lancera avec le Centre MD !"))
        print (_("Veux tu la mettre en place ?"))
        choix_son= input (_("Choix")).lower ()
        
        if choix_son== _("oui"):
            F_son= Musiques.selection_mp3 ()
            if F_son!= False:
                usr_son= True
                Musiques.gestion_musique (F_son, "lire_musique")
            else: usr_son= False
            return F_son, usr_son
        elif choix_son== _("non"): return False, False
        else:
            os.system ("cls")
            print (_("Tu dois répondre oui ou non"))

def choix_mdp (usr_nom):
    while True:
        print (_("Bienvenue nom")+ usr_nom+ " ! ·\n")
        print (_("Enfin, veux-tu mettre en place un mot de passe ?"))
        choix_mdp= input (_("Choix")).lower ()
        
        if choix_mdp== _("oui"):
            while True:
                os.system ("cls")
                print (_("Bienvenue nom")+ usr_nom+ " ! ·\n")
                usr_mdp= input (_("Entre le mot de passe"))
                os.system ("cls")
                while True:
                    print (_("Bienvenue nom")+ usr_nom+ " ! ·\n")
                    choix_mdp= input (_("Tu confirmes vouloir comme mot de passe")+ f"\"{usr_mdp}\" : ").lower ()
                    if choix_mdp== _("oui"): return usr_mdp
                    elif choix_mdp== _("non"): break
                    else:
                        os.system ("cls")
                        print (_("Tu dois répondre oui ou non"))
        
        elif choix_mdp== _("non"): return False
        else:
            os.system ("cls")
            print (_("Tu dois répondre oui ou non"))
