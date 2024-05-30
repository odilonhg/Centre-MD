from cryptography.fernet import Fernet
from tkinter import filedialog
import shutil #NOUVEAU MODULE
import pygame #NOUVEAU MODULE
import threading #NOUVEAU MODULE
import pickle
import json
import csv
import sys
import logging
import os

class Outils:
    @staticmethod
    
    def lecture_langue (chemin, delimiter = ";"):
        L = []
        
        with open (chemin, "r") as f:
            for ligne in f:
                donnees = ligne.strip ().split (delimiter)
                L.append (donnees)
        
        return L
    
    def lecture_fichier (fichier):
        with open (fichier, "r") as f:
            return f.read()
    
    class Cle:
        
        def ecriture_cle (chemin):
            cle = Fernet.generate_key ()
            with open (chemin, "wb") as f: f.write (cle)
            return cle
        
        def lecture_cle (chemin):
            with open (chemin, "rb") as f: cle = f.read ()
            return cle
    
    class Musique:
        stop_mp3 = False
        
        # GENERE PAR CHATGPT
        def selection_mp3 ():
            chemin_fichier = filedialog.askopenfilename(
                title = "Sélectionnez un fichier MP3",
                filetypes = [("Fichiers MP3", "*.mp3")])
            
            if chemin_fichier != "":
                nom_fichier = os.path.basename(chemin_fichier)
                chemin_fichier = Outils.Musique.copier_mp3 (chemin_fichier, nom_fichier)
                return chemin_fichier
            else: return False
        
        def copier_mp3 (chemin, fichier):
            chemin_final = os.path.join (os.getcwd (), "audios")
            chemin_final = os.path.join (chemin_final, fichier)
            
            try: shutil.copy (chemin, chemin_final)
            except: chemin_final = False
            finally: return chemin_final
        
        def gestion_mp3 (chemin, choix):
            global stop_mp3
            if choix == "lire_musique":
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
                
            elif choix == "couper_musique":
                stop_mp3 = True
                try: pygame.mixer.music.stop()
                except:
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
    
    class CSV:
        
        def ecriture_csv(liste, fichier, delimiter = ";"):
            
            with open (fichier, "w") as csvfile:
                ligneDesc = ";".join(liste[0].keys()) + "\n"
                csvfile.write (ligneDesc)
                
                for cle in range(len(liste)):
                    ligne = ";".join(liste[cle].values()) + "\n"
                    csvfile.write (ligne)
        
        def lecture_csv(fichier, delimiter = ";"):
            liste=[]
            
            try:
                with open (fichier, "r") as csvfile:
                    cles=csvfile.readline().strip().split(delimiter)
                    
                    for ligne in csvfile:
                        datas=ligne.strip().split(delimiter)
                        liste.append(dict(zip(cles,datas)))
                    
            finally : return liste
        
        def ecriture_encryptee_csv (donnees, fichier, cle):
            donnees_encryptees = Outils.CSV.encrypter_csv (donnees, cle)
            with open (fichier, "w", newline = "") as f:
                writer = csv.writer (f, delimiter = ";")
                for ligne in donnees_encryptees:
                    writer.writerow ([ligne])
        
        def lecture_encryptee_csv (fichier, cle):
            liste = Outils.CSV.decrypter_csv (fichier, cle)
            return liste
                
        
        # GENERE PAR CHATGPT
        def encrypter_csv (donnees, cle):
            fernet = Fernet(cle)
            donnees_encryptees = []
            for ligne in donnees:
                ligne_json = json.dumps(ligne)
                ligne_bytes = ligne_json.encode()  # Encoder la chaîne en bytes
                ligne_encryptee = fernet.encrypt(ligne_bytes)  # Chiffrer les bytes
                donnees_encryptees.append(ligne_encryptee.decode())  # Ajouter la ligne chiffrée comme chaîne de caractères
            return donnees_encryptees
        
        # GENERE PAR CHATGPT
        def decrypter_csv (fichier, cle):
            fernet = Fernet(cle)
            donnees_decryptees = []
            with open(fichier, "r", newline="") as f:
                reader = csv.reader(f, delimiter=";")
                for ligne in reader:
                    ligne_encryptee = ligne[0]
                    ligne_decryptee = fernet.decrypt(ligne_encryptee.encode()).decode()  # Déchiffrer la ligne
                    donnees_decryptees.append(json.loads(ligne_decryptee))  # Convertir la chaîne de caractères en liste
            donnees_decryptees = Outils.CSV.convertir_csv (donnees_decryptees)
            return donnees_decryptees
        
        def convertir_csv (donnees):
            resultat = []
            for ligne in donnees:
                ligne_convertie = [
                    ligne[0],
                    ligne[1],
                    ligne[2],
                    ligne[3],
                    ligne[4],
                    ligne[5], # usr_nbr
                    ligne[6],
                    ligne[7],
                    ligne[8],
                    ligne[9],
                    ligne[10],
                    ligne[11]]
                resultat.append(ligne_convertie)
            return resultat
        
class Options:
    @staticmethod
    
    def main (liste_langue, usr, f_usr, f_log, usr_version, cle, f_cle, gestionnaire_log):
        while True:
            print (f"   · {liste_langue[9][0]} ·\n")
            print (f"v{usr_version}\n")
            
            print (f" 0. {liste_langue[8][2]}")
            
            if usr[0][2]: print (f" 1. {liste_langue[9][1]}")
            else: print (f" 1. {liste_langue[9][2]}")
            
            print (f" 2. {liste_langue[9][3]}")
            
            print (f" 3. {liste_langue[9][4]}")
            
            if usr[0][4] != False: print (f" 4. {liste_langue[9][5]}")
            else: print (f" 4. {liste_langue[9][6]}")
            
            print (f" 5. {liste_langue[9][7]}")
            
            print (f" 6. {liste_langue[9][8]}\n")
            
            print (f" 7. {liste_langue[9][9]}\n")
            
            choix_options = input (liste_langue[0][3]).lower ()
            os.system ("cls")
            
            if choix_options == "0": return
            
            elif choix_options == "1":
                if usr[0][2] != False:
                    usr[0][2] = False
                    Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
                    logging.info (f"  {liste_langue[1][2]}: {liste_langue[1][10]}\n")
                    Outils.Musique.gestion_mp3 (usr[0][3], "couper_musique")
                else:
                    usr[0][2] = True
                    Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
                    if usr[0][3] != False:
                        logging.info (f"  {liste_langue[1][1]}: {liste_langue[1][10]}\n")
                        Outils.Musique.gestion_mp3 (usr[0][3], "lire_musique")
                    else:
                        usr[0][3] = Outils.Musique.selection_mp3 ()
                        Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
                        logging.info (f"  {liste_langue[1][3]}: {liste_langue[1][10]}\n")
                        logging.info (f"  {liste_langue[1][1]}: {liste_langue[1][10]}\n")
                        Outils.Musique.gestion_mp3 (usr[0][3], "lire_musique")
            
            elif choix_options == "2":
                usr[0][3] = Outils.Musique.selection_mp3 ()
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
                logging.info (f"  {liste_langue[1][3]}: {liste_langue[1][10]}\n")
            
            elif choix_options == "3":
                Options.gestion_apps (liste_langue, usr, f_usr, cle)
                os.system ("cls")
            
            elif choix_options == "4":
                Options.gestion_mdp (liste_langue, usr, f_usr, cle)
                os.system ("cls")
            
            elif choix_options == "5":
                logging.info (f"    {liste_langue[1][6]}: Logs\n")
                contenu_logs = Outils.lecture_fichier (f_log)
                os.system ("cls")
                print (contenu_logs.rstrip ("\n") + "\n")
            
            elif choix_options == "6":
                print (f"{usr}\n")
            
            elif choix_options == "7":
                if usr[0][4] != False:
                    os.system ("cls")
                    test_mdp = input (liste_langue[0][8])
                    if test_mdp != usr[0][4]: return
                
                os.system ("cls")
                print (f"{liste_langue[9][10]}\n")
                while True:
                    choix_final = input (liste_langue[0][3]).lower ()
                    
                    if choix_final == liste_langue[0][0]:
                        from apps.rep_md.main import f_rep
                        if os.path.exists (f_rep): os.remove (f_rep)
                        from apps.manager_md.main import f_gdt
                        if os.path.exists (f_gdt): os.remove (f_gdt)
                        gestionnaire_log.close()
                        if os.path.exists (f_log): os.remove (f_log)
                        if os.path.exists (f_usr): os.remove (f_usr)
                        if os.path.exists (f_cle): os.remove (f_cle)
                        os.system ("cls")
                        print (f"{liste_langue[9][11]}\n")
                        fin = input (f"{liste_langue[9][12]}")
                        logging.info (f"{liste_langue[9][11]}\n")
                        sys.exit(0)
                        
                    elif choix_final == liste_langue[0][1]:
                        os.system ("cls")
                        print (f"{liste_langue[0][11]}\n")
                        return
                    
                    else:
                        os.system ("cls")
                        print (f"{liste_langue[0][2]}\n")
                
            elif choix_options == f"{liste_langue[0][4]}":
                print (liste_langue[15][2])
                print (liste_langue[15][3] + "\n")
            
            else: print (f"{liste_langue[0][10]}\n")
    
    def gestion_apps (liste_langue, usr, f_usr, cle):
        while True:
            print (f"  · {liste_langue[9][13]} ·\n")
        
            print (f" 0. {liste_langue[8][2]}")
            if usr[0][7] == False: print (f" 1. {liste_langue[9][14]}: {liste_langue[10][0]} (v2.1)")
            else: print (f" 1. {liste_langue[9][15]}: {liste_langue[10][0]} (v2.1)")
            if usr[0][8] == False: print (f" 2. {liste_langue[9][14]}: {liste_langue[11][0]} (v2.0)")
            else: print (f" 2. {liste_langue[9][15]}: {liste_langue[11][0]} (v2.0)")
            if usr[0][9] == False: print (f" 3. {liste_langue[9][14]}: {liste_langue[12][0]} (v1.0)")
            else: print (f" 3. {liste_langue[9][15]}: {liste_langue[12][0]} (v1.0)")
            if usr[0][10] == False: print (f" 4. {liste_langue[9][14]}: {liste_langue[13][0]} (v1.1)")
            else: print (f" 4. {liste_langue[9][15]}: {liste_langue[13][0]} (v1.1)")
            if usr[0][11] == False: print (f" 5. {liste_langue[9][14]}: {liste_langue[14][0]} (v1.1)\n")
            else: print (f" 5. {liste_langue[9][15]}: {liste_langue[14][0]} (v1.1)\n")
            
            choix_gestion_apps = input (liste_langue[0][3]).lower ()
            
            if choix_gestion_apps == "0": return
            
            elif choix_gestion_apps == "1":
                if usr[0][7] == False:
                    usr[0][7] = True
                    logging.info (f"{liste_langue[1][4]}: {liste_langue[10][0]}\n")
                else:
                    usr[0][7] = False
                    logging.info (f"{liste_langue[1][5]}: {liste_langue[10][0]}\n")
                
                os.system ("cls")
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
            
            elif choix_gestion_apps == "2":
                if usr[0][8] == False:
                    usr[0][8] = True
                    logging.info (f"{liste_langue[1][4]}: {liste_langue[11][0]}\n")
                else:
                    usr[0][8] = False
                    logging.info (f"{liste_langue[1][5]}: {liste_langue[11][0]}\n")
                
                os.system ("cls")
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
            
            elif choix_gestion_apps == "3":
                if usr[0][9] == False:
                    usr[0][9] = True
                    logging.info (f"{liste_langue[1][4]}: {liste_langue[12][0]}\n")
                else:
                    usr[0][9] = False
                    logging.info (f"{liste_langue[1][5]}: {liste_langue[12][0]}\n")
                
                os.system ("cls")
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
            
            elif choix_gestion_apps == "4":
                if usr[0][10] == False:
                    usr[0][10] = True
                    logging.info (f"{liste_langue[1][4]}: {liste_langue[13][0]}\n")
                else:
                    usr[0][10] = False
                    logging.info (f"{liste_langue[1][5]}: {liste_langue[13][0]}\n")
                
                os.system ("cls")
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
            
            elif choix_gestion_apps == "5":
                if usr[0][11] == False:
                    usr[0][11] = True
                    logging.info (f"{liste_langue[1][4]}: {liste_langue[14][0]}\n")
                else:
                    usr[0][11] = False
                    logging.info (f"{liste_langue[1][5]}: {liste_langue[14][0]}\n")
                
                os.system ("cls")
                Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
            
            elif choix_gestion_apps == f"{liste_langue[0][4]}":
                os.system ("cls")
                print (liste_langue[15][4])
                print (liste_langue[15][5])
                print (liste_langue[15][6] + "\n")
            
            else:
                os.system ("cls")
                print (f"{liste_langue[0][10]}\n")
    
    def gestion_mdp (liste_langue, usr, f_usr, cle):
        if usr[0][4] == False:
            while True:
                usr[0][4] = input (liste_langue[7][7])
                verif_mdp = input (f"{liste_langue[7][8]} \"{usr[0][4]}\" : ").lower ()
                if verif_mdp == liste_langue[0][0]:
                    break
                elif verif_mdp == liste_langue[0][1]:
                    os.system ("cls")
                else:
                    os.system ("cls")
                    print (f"{liste_langue[0][2]}\n")
            return Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
        
        else:
            while True:
                verif_mdp = input (liste_langue[0][8])
                if verif_mdp == usr[0][4]:
                    usr[0][4] = False
                    return Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)

class Depart:
    @staticmethod
    
    def choix_langue ():
        while True:
            print ("   · Langues ·\n")
            print (" 1. Français")
            print (" 2. English\n")
            
            choix_langue = input ("Choix : ")
            
            match choix_langue:
                case "1":
                    usr_langue = "fr"
                    f_langue = "langues\\FRENCH-fr"
                    return f_langue, usr_langue
                case "2":
                    usr_langue = "en"
                    f_langue = "langues\\ENGLISH-en"
                    return f_langue, usr_langue
                case _:
                    os.system ("cls")
                    print ("Tu dois choisir entre 1 et 2 !\nYou must choose between 1 and 2 !\n")
    
    def choix_nom (liste_langue):
        while True:
            print (f"   · {liste_langue[7][0]} ! ·\n")
            usr_nom = input (liste_langue[7][2])
            os.system ("cls")
            
            print (f"   · {liste_langue[7][0]} ! ·\n")
            choix_nom = input (f"{liste_langue[7][3]} {usr_nom} : ").lower ()
            
            if choix_nom == liste_langue[0][0]: return usr_nom
            elif choix_nom == liste_langue[0][1]: os.system ("cls")
            else:
                os.system ("cls")
                print (f"{liste_langue[0][2]}\n")
    
    def choix_son (liste_langue, usr_nom):
        while True:
            print (f"   · {liste_langue[7][0]} {usr_nom} ! ·\n")
            print (liste_langue[7][4])
            print (f"{liste_langue[7][5]}\n")
            choix_son = input (liste_langue[0][3]).lower ()
            
            if choix_son == liste_langue[0][0]:
                f_son = Outils.Musique.selection_mp3 ()
                usr_son = True
                Outils.Musique.gestion_mp3 (f_son, "lire_musique")
                return f_son, usr_son
            elif choix_son == liste_langue[0][1]:
                return False, False
            else:
                os.system ("cls")
                print (f"{liste_langue[0][2]}\n")
    
    def choix_mdp (liste_langue, usr_nom):
        while True:
            print (f"   · {liste_langue[7][0]} {usr_nom} ! ·\n")
            print (f"{liste_langue[7][6]}\n")
            choix_mdp = input (liste_langue[0][3]).lower ()
            os.system ("cls")
            
            if choix_mdp == liste_langue[0][0]:
                while True:
                    print (f"   · {liste_langue[7][0]} {usr_nom} ! ·\n")
                    usr_mdp = input (liste_langue[7][7])
                    choix_mdp = input (f"{liste_langue[7][8]} {usr_mdp} : ").lower ()
                    if choix_mdp == liste_langue[0][0]: return usr_mdp
                    elif choix_mdp == liste_langue[0][1]: os.system ("cls")
                    else:
                        os.system ("cls")
                        print (f"{liste_langue[0][2]}\n")
            elif choix_mdp == liste_langue[0][1]: return False
            else:
                os.system ("cls")
                print (f"{liste_langue[0][2]}\n")
    
class Autres:
    @staticmethod
    
    def erreur_data_usr (f_old_usr, f_usr, cle, usr_version):
        old_usr = Autres.lecture_pickle (f_old_usr)
        # REDEFINITION DES VARIABLES POUR FAIRE LA TRANSITION
        if old_usr[0][2] == old_usr[0][-1]: usr_nbr = 1
        else: usr_nbr = old_usr[0][3]
        usr_nom = old_usr[0][0]
        usr_son = old_usr[0][1]
        usr_mdp = old_usr[0][2]
        
        if usr_son == True:
            f_son = Outils.Musique.selection_mp3 ()
            if f_son == False:
                usr_son = False
        else:
            f_son = False
        
        f_langue, usr_langue = Depart.choix_langue ()
        liste_langue = Outils.lecture_langue (f_langue)
        
        usr = [[usr_langue, usr_nom, usr_son, f_son, usr_mdp, usr_nbr, usr_version, old_usr[1][0], old_usr[1][1], old_usr[1][2], old_usr[1][3], old_usr[1][4]]]
        Outils.CSV.ecriture_encryptee_csv (usr, f_usr, cle)
        logging.info (f"{liste_langue[1][7]}: v1 -> v2\n")
        os.remove (f_old_usr)
        os.system ("cls")
    
    # LIRE UN FICHIER (pickle)
    def lecture_pickle (fichier):
        try:
            with open (fichier, "rb") as f:
                liste = pickle.load (f)
        except: liste = []
        finally: return liste
    
    # ECRIRE UN FICHIER (pickle)
    def ecriture_pickle (liste, fichier):
        with open (fichier, "wb") as f:
            pickle.dump (liste, f)