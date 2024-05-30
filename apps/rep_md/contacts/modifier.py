from outils import Outils
from apps.rep_md.main import f_rep
from logging import info
from os import system

nbr_choice = "0"

def modifier ():
    global nbr_choice
    nbr_choice = "0"
    
    print ("   · Modifier: Contacts ·\n")
    
    print (" 0. Retour")
    print (" 1. Le nom")
    print (" 2. Le prénom")
    print (" 3. La date de naissance")
    print (" 4. Le numéro de téléphone")
    print (" 5. L'adresse email\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            system ("cls")
            return
        
        case "1": return modifier2 ("1")
        case "2": return modifier2 ("2")
        case "3": return modifier2 ("3")
        case "4": return modifier2 ("4")
        case "5": return modifier2 ("5")
        
        case _:
            system ("cls")
            print ("Choix impossible...\n")
            return modifier ()

def modifier2 (nbr):
    liste = Outils.CSV.lecture_csv (f_rep)
    choice2 = "non"
    system ("cls")
    contact = input ("Renseigner une information sur le contact à trouver : ").lower()
    
    for i in range (len (liste)):
        nom = liste[i]["nom"].lower ()
        prenom = liste[i]["prenom"].lower ()
        date_naissance = liste[i]["date"]
        num = liste[i]["num"]
        email = liste[i]["email"].lower ()
        favori = liste[i]["favori"]
        
        if date_naissance != "":
            jour, mois, annee = date_naissance.split('.')
            if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email or contact == favori:
                system ("cls")
                print (f"Modifier {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice2 = input ("Choix : ").lower ()
        else:
            if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                system ("cls")
                print (f"Modifier {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice2 = input ("Choix : ").lower ()
        
        if choice2 == "oui":
            match nbr:
                
                case "1":
                    system ("cls")
                    new_nom = input (f"Renseigner le nouveau nom de {nom.upper ()} {prenom.capitalize ()} : ").upper ()
                    liste[i]["nom"] = new_nom
                    Outils.CSV.ecriture_csv (liste, f_rep)
                    info (f"    MODIFIER CONTACTS: {nom.upper ()} -> {new_nom} | {nom.upper ()} {prenom.capitalize ()}\n")
                    system ("cls")
                    print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été modifié\n")
                    return ""
                
                case "2":
                    system ("cls")
                    new_prenom = input (f"Renseigner le nouveau prénom de {nom.upper ()} {prenom.capitalize ()} : ").capitalize ()
                    liste[i]["prenom"] = new_prenom
                    Outils.CSV.ecriture_csv (liste, f_rep)
                    info (f"    MODIFIER CONTACTS: {prenom.capitalize ()} -> {new_prenom} | {nom.upper ()} {prenom.capitalize ()}\n")
                    system ("cls")
                    print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été modifié\n")
                    return ""
                
                case "3":
                    system ("cls")
                    new_jour = input (f"Renseigner le jour de naissance de {nom.upper ()} {prenom.capitalize ()} : ")
                    new_mois = input (f"\nRenseigner le mois de naissance de {nom.upper ()} {prenom.capitalize ()} : ")
                    new_annee = input (f"\nRenseigner l'année de naissance de {nom.upper ()} {prenom.capitalize ()} : ")
                    new_date = f"{new_jour}.{new_mois}.{new_annee}"
                    liste[i]["date"] = new_date
                    Outils.CSV.ecriture_csv (liste, f_rep)
                    info (f"    MODIFIER CONTACTS: {date_naissance} -> {new_date} | {nom.upper ()} {prenom.capitalize ()}\n")
                    system ("cls")
                    print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été modifié\n")
                    return ""
                
                case "4":
                    system ("cls")
                    new_num = input (f"Renseigner le nouveau numéro de téléphone de {nom.upper ()} {prenom.capitalize ()} : ")
                    liste[i]["num"] = new_num
                    Outils.CSV.ecriture_csv (liste, f_rep)
                    info (f"    MODIFIER CONTACTS: {num} -> {new_num} | {nom.upper ()} {prenom.capitalize ()}\n")
                    system ("cls")
                    print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été modifié\n")
                    return ""
                
                case "5":
                    system ("cls")
                    new_email = input (f"Renseigner le nouvel email de {nom.upper ()} {prenom.capitalize ()} : ").lower ()
                    liste[i]["email"] = new_email
                    Outils.CSV.ecriture_csv (liste, f_rep)
                    logging.info (f"    MODIFIER CONTACTS: {email} -> {new_email} | {nom.upper ()} {prenom.capitalize ()}\n")
                    system ("cls")
                    print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été modifié\n")
                    return ""
                
                case _:
                    system ("cls")
                    print ("Choix impossible...\n")
                    return modifier ()
    
    system ("cls")
    print ("Aucun contact trouvé !\n")
    return ""