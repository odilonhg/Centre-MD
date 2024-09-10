from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
from logging import info
from os import system

nom = ""
prenom = ""
jour = ""
mois = ""
annee = ""
num = ""
email = ""
L = []
nbr = {
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09"
}

def ajouter ():
    global nom, prenom, jour, mois, annee, num, email, L
    L = lecture_csv (f_rep)
    
    print ("   · Ajouter: Contacts ·\n")
    
    if nom == "" or prenom == "":
        print (" 0. Retour\n")
        print ("  · OBLIGATOIRE ·\n")
        print (" 1. Le nom")
        print (" 2. Le prénom\n")
    if nom != "" and prenom != "":
        print ("  · FACULTATIF ·\n")
        print (" 3. La date de naissance")
        print (" 4. Le numéro de téléphone")
        print (" 5. L'adresse email\n")
        
        print (" 6. Finaliser le contact\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            system ("cls")
            return
        
        case "1":
            if nom == "":
                system ("cls")
                nom = input ("Renseignez le nom de famille du contact : ").upper()
                system ("cls")
                print ("Nom de famille ajouté au contact !\n")
                return ajouter ()
            else:
                system ("cls")
                print ("Nom déjà renseigné !\n")
                return ajouter ()
        
        case "2":
            if prenom == "":
                system ("cls")
                prenom = input ("Renseignez le prénom du contact : ").capitalize()
                system ("cls")
                print ("Prénom ajouté au contact !\n")
                return ajouter ()
            else:
                system ("cls")
                print ("Prénom déjà renseigné !\n")
                return ajouter ()
        
        case "3":
            if nom != "" and prenom != "":
                if jour == "" or mois == "" or annee == "":
                    if jour == "":
                        system ("cls")
                        jour = input ("Renseignez le jour de naissance du contact : ")
                        if int (jour) > 31 or int (jour) < 1:
                            system ("cls")
                            print ("Valeur impossible...\n")
                            jour = ""
                            return ajouter ()
                        for nbrV1, nbrV2 in nbr.items ():
                            if jour == nbrV1:
                                jour = nbrV2
                                break
                    if mois == "":
                        system ("cls")
                        mois = input ("Renseignez le mois de naissance du contact : ")
                        if int (mois) > 12 or int (mois) < 1:
                            system ("cls")
                            print ("Valeur impossible...\n")
                            mois = ""
                            return ajouter ()
                        for nbrV1, nbrV2 in nbr.items ():
                            if mois == nbrV1:
                                mois = nbrV2
                                break
                    if annee == "":
                        system ("cls")
                        annee = input ("Renseignez l'année de naissance du contact : ")
                        if int (annee) > 2100 or int (annee) < 1900:
                            system ("cls")
                            print ("Valeur impossible...\n")
                            annee = ""
                            return ajouter ()
                    
                    system ("cls")
                    print ("Date de naissance ajouté au contact !\n")
                    return ajouter ()
                else:
                    system ("cls")
                    print ("Date de naissance déjà renseignée !\n")
                    return ajouter ()
            else:
                system ("cls")
                print ("Choix impossible...\n")
                return ajouter ()
        
        case "4":
            if nom != "" and prenom != "":
                if num == "":
                    system ("cls")
                    verif_num = False
                    num = input ("Renseignez le numéro de téléphone du contact : ")
                    if len(num) != 9 and len(num) != 10:
                        system ("cls")
                        print ("Valeur impossible...\n")
                        num = ""
                        return ajouter ()
                    elif num.isdigit () == False:
                        system ("cls")
                        print ("Valeur impossible...\n")
                        num = ""
                        return ajouter ()
                    else:
                        if len(num) == 9: num = "0" + num
                        system ("cls")
                        print ("Numéro de téléphone ajouté au contact !\n")
                        return ajouter()
                else:
                    system ("cls")
                    print ("Numéro de téléphone déjà renseigné !\n")
                    return ajouter()
            else:
                system ("cls")
                print ("Choix impossible...\n")
                return ajouter ()
        
        case "5":
            if nom != "" and prenom != "":
                if email == "":
                    system ("cls")
                    email = input ("Renseignez l'adresse email du contact : ")
                    system ("cls")
                    return ajouter()
                else:
                    system ("cls")
                    print ("Adresse email déjà renseignée !\n")
                    return ajouter()
            else:
                system ("cls")
                print ("Choix impossible...\n")
                return ajouter ()
        
        case "6":
            if nom != "" and prenom != "":
                if annee == "":
                    date = ""
                else:
                    date = f"{jour}.{mois}.{annee}"
                nouveau_contact = {"nom": nom, "prenom": prenom, "date": date, "num": num, "email": email, "favori": "False", "groupe": "", "nom_groupe": "", "num_groupe": "", "mbr_groupe": ""}
                L.append (nouveau_contact)
                ecriture_csv (L, f_rep)
                system ("cls")
                print (f"Le contact {nom} {prenom} a été crée !\n")
                info (f"    AJOUTER CONTACTS: {nom} {prenom}\n")
                nom = ""
                prenom = ""
                jour = ""
                mois = ""
                annee = ""
                num = ""
                email = ""
                return
            else:
                system ("cls")
                print ("Veuillez renseigner le nom et le prénom du contact pour continuer.\n")
                return ajouter ()
        
        case _:
            system ("cls")
            print ("Choix impossible...\n")
            return ajouter ()