from outils import lecture_csv
from apps.rep_md.main import f_rep
import logging
import os

def rechercher ():
    liste = lecture_csv (f_rep)
    
    print ("   · Rechercher un Contact ·\n")
    
    contact = input (" Renseigner une information sur le contact à trouver : ").lower()
    logging.info (f"    RECHERCHER CONTACTS: {contact}\n")
    
    contact_trouve = 0 # A OPTIMISER A L'AVENIR !!!
    
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
                contact_trouve += 1
        
        else:
            if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                contact_trouve += 1
        
        if contact_trouve != 0:
            os.system ("cls")
            print ("   · Contacts trouvés ·\n")
            print ("* = contact favori")
            
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
                        if favori == "True":
                            print (f"\n | * {nom.upper ()} {prenom.capitalize ()}")
                        else:
                            print (f"\n |   {nom.upper ()} {prenom.capitalize ()}")
                        
                        print (f" |   {date_naissance}")
                        
                        if num != "":
                            print (f" |   {num}")
                        if email != "":
                            print (f" |   {email}")
                
                else:
                    if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                        if favori == "True":
                            print (f"\n | * {nom.upper ()} {prenom.capitalize ()}")
                        else:
                            print (f"\n |   {nom.upper ()} {prenom.capitalize ()}")
                        
                        if date_naissance != "":
                            print (f" |   {date_naissance}")
                        if num != "":
                            print (f" |   {num}")
                        if email != "":
                            print (f" |   {email}")
            print ()
            return ""
    
    os.system ("cls")
    print ("Aucun contact trouvé !\n")
    return ""