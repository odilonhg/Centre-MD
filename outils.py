import os
import logging
import pickle
import pygame

def options (usr, F_usr, F_log, gestionnaire_log):
    while True:
        print ("   · Options ·\n")
        print ("Version 1.3.0\n") # A MODIFIER
        
        print (" 0. Retour")
        
        if usr[0][1]: print (" 1. Couper la musique")
        else: print (" 1. Lancer la musique")
        print (" 2. Changer la musique")
        
        if usr[0][3]: print (" 3. Supprimer le mot de passe")
        else: print (" 3. Mettre en place un mot de passe")
        
        print (" 4. Afficher tes infos utilisateur")
        print (" 5. Afficher les logs")
        print ("\n 6. Réinitialiser le Centre MD")
        
        choix = input ("\nChoix : ")
        
        match choix:
            
            case "0": return "0"
            
            case "1":
                if usr[0][1]:
                    couper_son ()
                    usr[0][1] = False
                    ecriture_pickle (usr, F_usr)
                    logging.info ("    FERMETURE: Musique\n")
                    os.system ("cls")
                
                else:
                    if usr[0][2] == None:
                        usr[0][1], usr[0][2] = selection_son ()
                    else:
                        usr[0][1] = True
                    if usr[0][1]:
                        lancer_son (usr[0][2])
                        logging.info ("    OUVERTURE: Musique\n")
                    ecriture_pickle (usr, F_usr)
                    os.system ("cls")
            
            case "2":
                verif_son = False
                old_son = usr[0][2]
                os.system ("cls")
                if usr[0][1]: verif_son = True
                usr[0][1], usr[0][2] = selection_son ()
                if usr[0][1]:
                    if verif_son:
                        usr[0][1] = True
                        couper_son ()
                        lancer_son (usr[0][2])
                    else: usr[0][1] = False
                os.system ("cls")
                logging.info (f"    CHANGEMENT MUSIQUE: {nom_son(old_son)} -> {nom_son(usr[0][2])}\n")
                ecriture_pickle (usr, F_usr)
            
            case "3": gestion_mdp (usr, F_usr)
            
            case "4":
                os.system ("cls")
                logging.info ("    AFFICHAGE: Infos utilisateur\n")
                
                print (f" | Carte d'Identité de {usr[0][0]}")
                
                if usr[0][1]: print (f" | Ecoute actuellement : {nom_son (usr[0][2])}")
                else: print (" | N'écoute pas de musique... (oh nion)")
                    
                if usr[0][3]: print (" | A un mot de passe (il est secret défense)")
                else: print (" | N'a pas de mot de passe... (oh nion)")
                
                print (f" | A lancé son Centre MD {usr[0][4]} fois au total !")
                
                print (f" | Est actuellement à la version {usr[0][5]}\n")
                
            case "5":
                logging.info ("    AFFICHAGE: Logs (slt)\n") # A MODIFIER
                contenu_logs = lecture_fichier (F_log)
                os.system ("cls")
                print (contenu_logs.rstrip ("\n") + "\n")
            
            case "6":
                if usr[0][3]:
                    os.system ("cls")
                    while True:
                        test_mdp = input ("Entrer votre mot de passe : ")
                        if test_mdp == usr[0][3]: break
                        else:
                            os.system ("cls")
                            print (" Mot de passe incorrect...\n")
                
                os.system ("cls")
                print ("ATTENTION, CETTE ACTION EST IRREVERSIBLE !\n")
                while True:
                    print (" Souhaitez-vous continuer malgré tout ?\n")
                    print (" 1. Oui")
                    print (" 2. Non")
                    choix_final = input ("\nChoix : ")
                    if usr[0][1]: couper_son ()
                    
                    if choix_final == "1":
                        from apps.rep_md.main import F_rep
                        if os.path.exists (F_rep): os.remove (F_rep)
                        from apps.gdt_md.main import F_gdt
                        if os.path.exists (F_gdt): os.remove (F_gdt)
                        gestionnaire_log.close()
                        os.remove (F_log)
                        os.remove (F_usr)
                        os.system ("cls")
                        print ("REINITIALISATION TERMINEE !\n")
                        input ("Appuyer sur Entrée pour quitter")
                        logging.info ("REINITIALISATION TERMINEE !\n")
                        break
                        
                    elif choix_final == "2":
                        os.system ("cls")
                        print (" Action annulée !\n")
                        break
                    
            case _:
                os.system ("cls")
                print (" Choix impossible...\n")
            
        if choix == "6": return "6"

def gestion_mdp (usr, F_usr):
    if usr[0][3]:
        while True:
            os.system ("cls")
            test_mdp = input ("Saisir votre mot de passe : ")
            
            if test_mdp == usr[0][3]:
                usr[0][3] = False
                ecriture_pickle (usr, F_usr)
                os.system ("cls")
                print ("Mot de passe supprimé !\n")
                logging.info ("    SUPPRRESSION DU MOT DE PASSE...\n")
                break
            else:
                os.system ("cls")
                print ("Mot de passe incorrect !\n")
    else:
        while True:
            os.system ("cls")
            usr[0][3] = input ("Saisir votre mot de passe : ")
            
            os.system ("cls")
            print (f"Vous confirmez que le mot de passe requis à l'ouverture du logiciel sera \"{usr[0][3]}\" ?\n")
            print (" 1. Oui")
            print (" 2. Non")
            choix_mdp_2 = input ("\nChoix : ")
        
            if choix_mdp_2 == "1":
                ecriture_pickle (usr, F_usr)
                os.system ("cls")
                print ("Mot de passe crée !\n")
                logging.info ("    CREATION DU MOT DE PASSE !\n")
            else: usr[0][3] = False

def selection_son ():
    print (" Bien, vas chercher ta musique dans ton explorateur de fichiers.")
    print (" Ensuite, fais un clique-droit sur ta musique et appuies sur \"Copier en tant que chemin d'accès\" !")
    chemin = input ("\nChemin d'accès : ")
    chemin = chemin.replace ("\"", "")
    if os.path.isfile(chemin):
        return True, chemin
    else: return False, None

def lancer_son (musique):
    if os.path.exists (musique):
        pygame.mixer.init()
        pygame.mixer.music.load(musique)
        pygame.mixer.music.play(-1)  # -1 pour jouer en boucle
    else:
        return "ERREUR"

def couper_son (): pygame.mixer.music.stop()

def nom_son (chemin):
    liste_chemin = chemin.split ("\\")
    return liste_chemin[-1]

def lecture_pickle (fichier): # Permet de lire un fichier en utilisant le module pickle
    try:
        with open (fichier, "rb") as f:
            liste = pickle.load (f)
    except: liste = []
    finally: return liste

def ecriture_pickle (liste, fichier): # Permet d'écrire des données sur un fichier en utilisant le module pickle
    
    with open (fichier, "wb") as f:
        pickle.dump (liste, f)

def lecture_csv(fichier, delimiter = ";"):
    liste=[]
    try:
        with open (fichier, "r") as csvfile:
            cles=csvfile.readline().strip().split(delimiter)
            
            for ligne in csvfile:
                datas=ligne.strip().split(delimiter)
                liste.append(dict(zip(cles,datas)))
    except: return []
    finally: return liste

def ecriture_csv(liste, fichier):
    with open (fichier, "w") as csvfile:
        ligneDesc = ";".join(liste[0].keys()) + "\n"
        csvfile.write (ligneDesc)
        for cle in range(len(liste)):
            ligne = ";".join(liste[cle].values()) + "\n"
            csvfile.write (ligne)

def lecture_fichier (fichier):
    with open (fichier, "r") as f:
        return f.read()