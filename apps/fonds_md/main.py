import outils
import os
import logging
import datetime

F_fonds = "data_fonds.csv"

def fonds_md ():
    while True:
        if os.path.exists (F_fonds): L = outils.lecture_csv (F_fonds)
        else: L = []
        
        print ("   · Fonds MD ·\n")
        
        print (" 0. Retour")
        print (" 1. Créer")
        print (" 2. Ajouter (en création...)")
        print (" 3. Afficher")
        print (" 4. Modifier (en création...)")
        print (" 5. Supprimer (en création...)")
        
        choix = input ("\nChoix : ")
        
        if choix == "0": break
        
        elif choix == "1":
            os.system ("cls")
            creer (L)
        
        elif choix == "2":
            os.system ("cls")
            ajouter (L)
        
        elif choix == "3":
            os.system ("cls")
            afficher (L)
        
        elif choix == "4":
            os.system ("cls")
            modifier (L)
        
        elif choix == "5":
            os.system ("cls")
            supprimer (L)
        
        elif choix == "13":
            os.system ("cls")
            print (" Bien, vous voilà ici dans \"Fonds MD\" !\n",
                   "Cette application vous permet de créer des comptes\n",
                   "dans lesquels vous pourrez gérer votre argent afin\n",
                   "de mettre de côté, ou encore de suivre l'argent qu'il\n",
                   "vous reste pour le mois.\n")
            print (" Pour créer un compte, tapez \"1\" !\n")
        
        elif choix == "fonctions_md":
            os.system ("cls")
            fonctions_secrete_ultra_mega_3000 ()
        
        else:
            os.system ("cls")
            print (" Choix impossible...\n")

def creer (L):
    while True:
        date = datetime.datetime.now ()
        print ("   · Créer ·\n")
        
        print (" 0. Retour")
        print (" 1. Compte à Usage unique")
        print (" 2. Compte répeter (chaque mois)")
        
        choix = input ("\nChoix : ")
        
        os.system ("cls")
        if choix == "0": break
        
        elif choix == "1":
            while True:
                montant = input ("Entrez le montant actuel : ")
                if montant.isdigit (): break
                else:
                    os.system ("cls")
                    print (" Format incorrect... (entrez un nombre)\n")
            while True:
                montant_max = input ("\nEntrez le montant à atteindre : ")
                if montant_max.isdigit (): break
                else:
                    os.system ("cls")
                    print (" Format incorrect... (entrez un nombre)\n")
            while True:
                date_max = input ("\nEntrez la date maximal que vous vous laissez pour atteindre votre objectif (JJ.MM.AAAA) : ")
                if len (date_max) == 10 and len (date_max.split (".")) == 3:
                    date_liste = date_max.split (".")
                    if date_liste[0].isdigit () and date_liste[1].isdigit () and date_liste[2].isdigit ():
                        date_max = f"{int (date_liste[0])}.{int (date_liste[1])}.{int (date_liste[2])}"
                        break
                    else:
                        os.system ("cls")
                        print (" Format incorrect... (suivez le format demandé)\n")
                else:
                    os.system ("cls")
                    print (" Format incorrect... (suivez le format demandé)\n")
            
            os.system ("cls")
            date = f"{date.day}.{date.month}.{date.year}"
            date_L = date.split (".")
            date_L = [int (date_L[0]), int (date_L[1]), int (date_L[2])]
            date_max_L = date_max.split (".")
            date_max_L = [int (date_max_L[0]), int (date_max_L[1]), int (date_max_L[2])]
            
            j_restant = date_max_L[0] - date_L[0]
            m_restant = date_max_L[1] - date_L[1]
            a_restant = date_max_L[2] - date_L[2]
            tps_restant = j_restant + (m_restant * 30) + (a_restant * 365)
            
            while True:
                print (f" Il vous reste donc {tps_restant} jours !\n")
                if tps_restant < 90:
                    argent_a_mettre_semaine = (int (montant_max) - int (montant)) / (tps_restant / 7)
                    argent_a_mettre_semaine = int (argent_a_mettre_semaine)
                    if argent_a_mettre_semaine < 0: print (f" Il faudra donc en moyenne retirer {-argent_a_mettre_semaine}€ par semaine.")
                    else: print (f" Il faudra donc en moyenne ajouter {argent_a_mettre_semaine}€ par semaine.")
                else:
                    argent_a_mettre_mois = (int (montant_max) - int (montant)) / (tps_restant / 30)
                    argent_a_mettre_mois = int (argent_a_mettre_mois)
                    if argent_a_mettre_mois < 0: print (f" Il faudra donc en moyenne retirer {-argent_a_mettre_mois}€ par mois.")
                    else: print (f" Il faudra donc en moyenne ajouter {argent_a_mettre_mois}€ par mois.")
                
                print ("\n Vous confirmez vouloir créer ce compte ?\n")
                print (" 1. Oui")
                print (" 2. Non")
                
                choix = input ("\nChoix : ")
                
                if choix == "1":
                    os.system ("cls")
                    print ("Bien, pour finir, donnez lui un nom à ce compte !")
                    while True:
                        nom = input ("\nEntrez son nom : ")
                        os.system ("cls")
                        print (f" Vous l'appelez donc bien \"{nom}\" ?\n")
                        print (" 1. Oui")
                        print (" 2. Non")
                        choix = input ("\nChoix : ")
                        
                        if choix == "1": break
                        else: os.system ("cls")
                
                elif choix == "2":
                    os.system ("cls")
                    break
                
                else:
                    os.system ("cls")
                    print (" Choix impossible...\n")
                
                nouveau_compte = {"nom": nom, "date": date, "date_max": date_max, "montant": montant, "montant_max": montant_max, "periode": "None"}
                L.append (nouveau_compte)
                outils.ecriture_csv (L, F_fonds)
                os.system ("cls")
                logging.info (f"    CREER COMPTE: {nom}\n")
                print (f" Le nouveau compte \"{nom}\" à été crée !\n")
                break
        
        elif choix == "2":
            while True:
                print (" Quelle période de renouvellement souhaitez-vous ?\n")
                print (" 1. Chaque semaine")
                print (" 2. Chaque mois")
                print (" 3. Chaque année")
                choix = input ("\nChoix : ")
                
                if choix == "1":
                    periode = "semaine"
                    break
                elif choix == "2":
                    periode = "mois"
                    break
                elif choix == "3":
                    periode = "annee"
                    break
                else:
                    os.system ("cls")
                    print (" Choix impossible...\n")
            
            os.system ("cls")
            while True:
                montant = input ("Entrez le montant actuel : ")
                if montant.isdigit (): break
                else:
                    os.system ("cls")
                    print (" Format incorrect... (entrez un nombre)\n")
            while True:
                montant_max = input ("\nEntrez le montant à atteindre : ")
                if montant_max.isdigit (): break
                else:
                    os.system ("cls")
                    print (" Format incorrect... (entrez un nombre)\n")
            
            os.system ("cls")
            while True:
                if choix == "1":
                    print (" Votre compte se réinitialisera chaque semaine !\n")
                    argent_a_mettre_semaine = (int (montant_max) - int (montant))
                    argent_a_mettre_semaine = int (argent_a_mettre_semaine)
                    if argent_a_mettre_semaine < 0: print (f" Il faudra donc retirer {-argent_a_mettre_semaine}€ chaque semaine.")
                    else: print (f" Il faudra donc ajouter {argent_a_mettre_semaine}€ chaque semaine.")
                elif choix == "2":
                    print (" Votre compte se réinitialisera chaque mois !\n")
                    argent_a_mettre_mois = (int (montant_max) - int (montant))
                    argent_a_mettre_mois = int (argent_a_mettre_mois)
                    if argent_a_mettre_mois < 0: print (f" Il faudra donc retirer {-argent_a_mettre_mois}€ chaque mois.")
                    else: print (f" Il faudra donc ajouter {argent_a_mettre_mois}€ chaque mois.")
                elif choix == "3":
                    print (" Votre compte se réinitialisera chaque année !\n")
                    argent_a_mettre_annee = (int (montant_max) - int (montant))
                    argent_a_mettre_annee = int (argent_a_mettre_annee)
                    if argent_a_mettre_annee < 0: print (f" Il faudra donc retirer {-argent_a_mettre_annee}€ chaque année.")
                    else: print (f" Il faudra donc ajouter {argent_a_mettre_annee}€ chaque année.")
                
                print ("\n Vous confirmez vouloir créer ce compte ?\n")
                print (" 1. Oui")
                print (" 2. Non")
                
                choix = input ("\nChoix : ")
                
                if choix == "1":
                    os.system ("cls")
                    print ("Bien, pour finir, donnez lui un nom à ce compte !")
                    while True:
                        nom = input ("\nEntrez son nom : ")
                        os.system ("cls")
                        print (f" Vous l'appelez donc bien \"{nom}\" ?\n")
                        print (" 1. Oui")
                        print (" 2. Non")
                        choix = input ("\nChoix : ")
                        
                        if choix == "1": break
                        else: os.system ("cls")
                
                elif choix == "2":
                    os.system ("cls")
                    break
                
                else:
                    os.system ("cls")
                    print (" Choix impossible...\n")
                
                nouveau_compte = {"nom": nom, "date": f"{datetime.datetime.now ().day}.{datetime.datetime.now ().month}.{datetime.datetime.now ().year}", "date_max": "None", "montant": montant, "montant_max": montant_max, "periode": periode}
                L.append (nouveau_compte)
                outils.ecriture_csv (L, F_fonds)
                os.system ("cls")
                logging.info (f"    CREER COMPTE A PERIODE: {nom}\n")
                print (f" Le nouveau compte \"{nom}\" à été crée !\n")
                break
        
        else: print (" Choix impossible...\n")
        break

def ajouter (L):
    while True:
        print ("   · Ajouter ·\n")
        compte = input ("Entrez le nom du compte : ")
        
        L_recherche = rechercher (L, compte)
        
        if L_recherche != []:
            for i in range (len (L_recherche)):
                nom = L_recherche[i][0]
                os.system ("cls")
                while True:
                    print (f" Ajouter au compte {nom} ?\n")
                    print (" 1. Oui")
                    print (" 2. Non")
                    choix = input ("\nChoix : ")
                    if choix == "1":
                        compte = L_recherche[i]
                        break
                    elif choix == "2": break
                if choix == "1": break
        
        os.system ("cls")
        print (compte)
        break

def afficher (L):
    while True:
        date = datetime.datetime.now ()
        date = [date.day, date.month, date.year]
        print ("   · Afficher ·")
        comptes = ""
        
        for i in range (len (L)):
            nom = L[i]["nom"]
            periode = L[i]["periode"]
            if periode == "None":
                date = L[i]["date"]
                date_max = L[i]["date_max"]
                date_L = date.split (".")
                date_L = [int (date_L[0]), int (date_L[1]), int (date_L[2])]
                date_max_L = date_max.split (".")
                date_max_L = [int (date_max_L[0]), int (date_max_L[1]), int (date_max_L[2])]
                
                j_restant = date_max_L[0] - date_L[0]
                m_restant = date_max_L[1] - date_L[1]
                a_restant = date_max_L[2] - date_L[2]
                tps_restant = j_restant + (m_restant * 30) + (a_restant * 365)
            else:
                if periode == "semaine": tps_restant = 6 - datetime.datetime.now ().weekday ()
                elif periode == "mois": tps_restant = (datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month + 1, 1) - datetime.datetime.now()).days if datetime.datetime.now().month != 12 else (datetime.datetime(datetime.datetime.now().year + 1, 1, 1) - datetime.datetime.now()).days
                elif periode == "annee": tps_restant = (datetime.datetime(datetime.datetime.now().year, 12, 31) - datetime.datetime.now()).days
                else:
                    print ("ERREUR PERIODE\n")
                    tps_restant = 0
            montant = L[i]["montant"]
            montant_max = L[i]["montant_max"]
            
            comptes += f"\n | {nom}\n | {montant}€ -> {montant_max}€\n"
            if periode == "None": comptes += f" | Il lui reste {tps_restant} jours\n"
            else: comptes += f" | Renouvellement dans {tps_restant} jours\n"
        
        if comptes == "": print (" Aucun comptes trouvés...\n")
        else: print (comptes)
            
        break

def modifier (L):
    while True:
        print ("   · Modifier ·\n")
        
        break

def supprimer (L):
    while True:
        print ("   · Supprimer ·\n")
        
        break

def rechercher (L, compte):
    L_recherche = []
    for i in range (len (L)):
        nom = L[i]["nom"]
        if compte.lower () == nom.lower ():
            montant = L[i]["montant"]
            montant_max = L[i]["montant_max"]
            if L[i]["date"] != "None":
                date = L[i]["date"]
                date_max = L[i]["date_max"]
                L_recherche.append ([nom, date, date_max, montant, montant_max])
            else:
                periode = L[i]["periode"]
                L_recherche.append ([nom, periode, montant, montant_max])
    return L_recherche