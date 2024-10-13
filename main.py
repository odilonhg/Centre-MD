# MODULES NECESSAIRES : pygame, requests

import outils
import os
import datetime

F_usr = "data_usr.csv"
F_usr_v1 = "data_usr"
F_log = "data_log.txt"

if os.path.exists(F_usr):
    outils.comparer_version()
    try:
        os.remove("CentreMD_Installer.exe")
    except:
        pass
    L_usr = outils.lecture_usr()
elif os.path.exists(F_usr_v1):
    L_usr = outils.transition_v1(outils.lecture_pickle(F_usr_v1), F_usr)
    os.remove(F_usr_v1)
else:
    nom = os.getenv("username")
    while True:
        print(" -- Bienvenue ! --\n",
              "\n J'ai une question pour vous.",
              f"\n Vous appelez-vous {nom} ?\n",
              "\n 1. Oui",
              "\n 2. Non")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "1":
            break
        elif choix == "2":
            print(" Ah, mince alors, rectifions cela !\n")
            while True:
                nom = input("Renseignez votre nom ici : ")
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
            if choix == "1":
                break
        else:
            print(" Choix impossible...\n")
    print(f" C'est Super !\n\n Je suis enchanté de vous rencontrer {nom} !\n")
    
    print(f" -- Bienvenue {nom} ! --\n",
          "\n J'ai une autre question pour vous.",
          "\n Voulez-vous mettre en place un mot de passe ?\n",
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
    
    usr = {"id": "1",
           "nom": nom,
           "mdp": mdp,
           "nbr": "0",
           "version": "2.0.0",
           "rep_md": "0",
           "manager_md": "0",
           "pass_md": "0",
           "musiques_md": "0"}
    
    L_usr = [usr]
    outils.ecriture_CSV(L_usr, F_usr)
    print(" Voilà, j'ai fini mon petit questionnaire...\n",
          "\n Profitez bien du Centre MD !\n",
          "\n Et si vous avez besoin d'aide, essayez de taper \"13\".",
          "\n Si je le peux, je vous aiderez !\n")

if __name__ == "__main__":
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
                break
            elif choix == "2":
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
                version = "2.0.0"
                
                usr = {"id": "2",
                       "nom": nom,
                       "mdp": mdp,
                       "nbr": "0",
                       "version": "2.0.0",
                       "rep_md": "0",
                       "manager_md": "0",
                       "pass_md": "0",
                       "musiques_md": "0"}
                L_usr.append(usr)
                outils.ecriture_CSV(L_usr, F_usr)
                outils.ecriture_log(f"NOUVEAU COMPTE UTILISATEUR CREE : {nom}\n")
            else:
                print(" Choix impossible...\n")
        
        else:
            test = False
            for usr in L_usr:
                if choix == usr["id"]:
                    test = True
                    break
            if choix == "13":
                print(" Salut, comment allez-vous aujourd'hui ?\n")
            elif test:
                break
            else:
                print(" Choix impossible...\n")
    
    if usr["mdp"] != "":
        test = ""
        while test != usr["mdp"]:
            test = input("Saisissez votre mot de passe : ")
            os.system("cls")
            if test != usr["mdp"]:
                print(" Mot de passe incorrect !\n")
    
    usr["nbr"] = int(usr["nbr"])
    usr["nbr"] += 1
    usr["nbr"] = str(usr["nbr"])
    outils.ecriture_usr(usr)
    outils.ecriture_log(f"OUVERTURE: Centre MD (pour la {usr['nbr']}ème fois)\n")
    
    from apps.musiques_md.main import F_mus
    L_mus = outils.lecture_CSV(F_mus)
    for musique in L_mus:
        if musique["usr_id"] == usr["id"] and musique["etat"] == "True":
            if os.path.exists(musique["chemin"]):
                from apps.musiques_md.lancer_arreter import lancer_arreter
                lancer_arreter(L_mus, musique)
            else:
                musique["etat"] = "False"
                outils.ecriture_mus(L_mus)
                outils.ecriture_log(f"ARRET FORCE MUSIQUE : {musique['chemin']} (musique introuvable)\n")
    
    heure = datetime.datetime.now().hour
    if heure < 12:
        print(f" Bonjour {usr['nom']} !\n")
    elif 12 <= heure < 18:
        print(f" Bonsoir {usr['nom']} !\n")
    else:
        print(f" Bonne nuit {usr['nom']} !\n")
    
    from apps.rep_md.main import F_rep
    if os.path.exists (F_rep):
        L_rep = outils.lecture_CSV(F_rep)
        date = [datetime.datetime.now().day, datetime.datetime.now().month]
        
        for contact in L_rep:
            date_c = contact["date"]
            if date_c != "":
                date_c = date_c.split("/")
                for i in range (2):
                    date_c[i] = int(date_c[i])
                del date_c[-1]
            if date == date_c:
                nom_c = contact["nom"]
                prenom_c = contact["prenom"]
                print (f" N'oubliez pas qu'aujourd'hui,\n c'est l'anniversaire de {nom_c} {prenom_c} !\n")
    
    from apps.manager_md.main import F_manager
    if os.path.exists (F_manager):
        L_manager = outils.lecture_CSV(F_manager)
        L_manager = outils.recherche(L_manager, usr, "True")
        
        for tache in L_manager:
            if tache["date"] != "None":
                tps_annee, tps_mois, tps_jour = outils.tps_restant(tache["date"])
                if tps_annee <= 0:
                    nom = tache["nom"]
                    print(f" Avez-vous terminé votre tâche \"{nom}\" ?\n")
    
    while True:
        print(" -- Centre MD --\n",
              "\n 0. Arrêter\n",
              "\n 1. Rep MD",
              "\n 2. Manager MD",
              "\n 3. Fonds MD",
              "\n 4. Pass MD",
              "\n 5. Musiques MD",
              "\n 6. Jeux MD",
              "\n\n 7. Options")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0":
            break
        elif choix == "1":
            outils.ecriture_log("  OUVERTURE : Rep MD\n")
            from apps.rep_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Rep MD\n")
        elif choix == "2":
            outils.ecriture_log("  OUVERTURE : Manager MD\n")
            from apps.manager_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Manager MD\n")
        elif choix == "3":
            outils.ecriture_log("  OUVERTURE : Fonds MD\n")
            from apps.fonds_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Fonds MD\n")
        elif choix == "4":
            outils.ecriture_log("  OUVERTURE : Pass MD\n")
            from apps.pass_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Pass MD\n")
        elif choix == "5":
            outils.ecriture_log("  OUVERTURE : Musiques MD\n")
            from apps.musiques_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Musiques MD\n")
        elif choix == "6":
            outils.ecriture_log("  OUVERTURE : Jeux MD\n")
            from apps.jeux_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Jeux MD\n")
        elif choix == "7":
            outils.ecriture_log("  OUVERTURE : Options\n")
            outils.options(usr)
            outils.ecriture_log("  FERMETURE : Options\n")
        
        elif choix == "13":
            print(" Bonsoiir !\n",
                  "\n Te voici dans la version 2.0.0 du Centre MD.",
                  "\n Ici tu vas pouvoir créer des contacts,",
                  "\n écouter de la musique,",
                  "\n jouer à des jeux et bien d'autres choses !\n",
                  "\n Pour commencer, sélectionnez une application en tapant son numéro !\n")
        else:
            print(" Choix impossible...\n")