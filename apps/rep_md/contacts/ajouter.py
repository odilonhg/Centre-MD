from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
import logging
import os

nom = ""
prenom = ""
jour = ""
mois = ""
annee = ""
num = ""
email = ""
liste = []

def ajouter ():
    global nom, prenom, jour, mois, annee, num, email, liste
    liste = lecture_csv (f_rep)
    
    print ("   · Ajouter un Contact ·\n")
    
    print (" 0. Retour")
    print (" 1. Le nom")
    print (" 2. Le prénom")
    print (" 3. La date de naissance")
    print (" 4. Le numéro de téléphone")
    print (" 5. l'adresse email\n")
    
    print (" 6. Finaliser le contact\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            os.system ("cls")
            return ""
        
        case "1":
            if nom == "":
                nom = input ("\nRenseigner le nom de famille du contact : ").upper()
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                print ("Nom déjà renseigné\n")
                return ajouter()
        
        case "2":
            if prenom == "":
                prenom = input ("\nRenseigner le prénom du contact : ").capitalize()
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                print ("Prénom déjà renseigné\n")
                return ajouter()
        
        case "3":
            if jour == "":
                jour = input ("\nRenseigner le jour de naissance du contact (de 1 à 31) : ")
                mois = input ("\nRenseigner le mois de naissance du contact (de 1 à 12) : ")
                annee = input ("\nRenseigner votre année de naissance : ")
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                print ("Date de naissance déjà renseignée\n")
                return ajouter()
            
        case "4":
            if num == "":
                verif_num = False
                while verif_num == False:
                    
                    num = input ("\nRenseignez le numéro de téléphone du contact (\"ANNULER\" pour annuler) : ")
                    
                    if num.isdigit (): verif_num = True
                    elif num == "ANNULER":
                        num = ""
                        verif_num = True
                    else:
                        os.system ("cls")
                        print ("Ce n'est pas un numéro de téléphone, veuillez réessayer")
                        
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                print ("Numéro de téléphone déjà renseigné\n")
                return ajouter()
        
        case "5":
            if email == "":
                email = input ("\nRenseigner l'adresse email du contact : ")
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                print ("Adresse email déjà renseignée\n")
                return ajouter()
        
        case "6": return fin()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return ajouter ()

def fin():
    global nom, prenom, jour, mois, annee, num, email, liste
    
    if jour == "":
        date = ""
    else:
        date = f"{jour}.{mois}.{annee}"
    os.system ("cls")
    
    if nom == "":
        nom = input ("Nom obligatoire !\n\nRenseignez le nom de famille du contact ici : ").upper()
        return fin()
    if prenom == "":
        prenom = input ('\nPrénom obligatoire !\n\nRenseignez le prénom du contact ici : ').capitalize()
        return fin()
    
    choice = input ("Voulez-vous que ce contact soit en favori ? ").upper()
    
    if choice == "OUI":
        favori = "True"
    else:
        favori = "False"
        
    c_new = {"nom": nom, "prenom": prenom, "date": date, "num": num, "email": email, "favori": favori, "groupe": "", "nom_groupe": "", "num_groupe": "", "mbr_groupe": ""}
    
    liste.append (c_new)
    
    ecriture_csv (liste, f_rep)
    
    os.system ("cls")
    print (f"Le contact {nom} {prenom} a été crée !\n")
    logging.info(f"    AJOUTER CONTACT: {nom} {prenom}\n")
    
    nom = ""
    prenom = ""
    jour = ""
    mois = ""
    annee = ""
    num = ""
    email = ""
    
    return ""