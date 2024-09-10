from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
from logging import info
from os import system

def ajouter ():
    liste = lecture_csv (f_rep)
    choice = "non"
    
    print ("   · Ajouter: Favoris ·\n")
    
    contact = input (" Renseigner une information sur le contact à ajouter aux favoris: ").lower()
    
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
                print (f"Ajouter {nom.upper ()} {prenom.capitalize ()} aux favoris ?\n")
                choice = input ("Choix : ").lower ()
        else:
            if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                system ("cls")
                print (f"Ajouter {nom.upper ()} {prenom.capitalize ()} aux favoris ?\n")
                choice = input ("Choix : ").lower ()
        
        if choice == "oui":
            liste[i]["favori"] = "True"
            ecriture_csv (liste, f_rep)
            system ("cls")
            print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été ajouté aux favoris\n")
            info (f"    AJOUTER FAVORIS: {nom.upper ()} {prenom.capitalize ()}\n")
            return
    
    system ("cls")
    print ("Aucun contact trouvé !\n")
    return