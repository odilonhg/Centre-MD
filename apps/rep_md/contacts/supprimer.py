from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
import logging
import os

def supprimer():
    choice = "non"
    liste = lecture_csv (f_rep)
    
    contact = input ("Renseigner une information sur le contact à supprimer : ").lower()
    
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
                os.system ("cls")
                print (f"Supprimer {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice = input ("Choix : ").lower ()
        else:
            if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                os.system ("cls")
                print (f"Supprimer {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice = input ("Choix : ").lower ()
        
        if choice == "oui":
            os.system ("cls")
            del (liste[i])
            ecriture_csv (liste, f_rep)
            print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été supprimé des contacts !\n")
            logging.info (f"    SUPPRIMER CONTACTS: {nom.upper ()} {prenom.capitalize ()}\n")
            return ""
    
    os.system ("cls")
    print ("Aucun contact trouvé !\n")
    return ""