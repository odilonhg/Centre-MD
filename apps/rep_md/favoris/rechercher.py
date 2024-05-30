from outils import Outils
from apps.rep_md.main import f_rep
from logging import info
from os import system

def rechercher ():
    liste = Outils.CSV.lecture_csv (f_rep)
    
    print ("   · Rechercher: Favoris ·\n")
    
    contact = input (" Renseigner une information sur le favori à trouver : ").lower()
    info (f"    RECHERCHER FAVORIS: {contact}\n")
    
    contact_trouve = 0
    contact_trouve_affichage = ""
    
    for i in range (len (liste)):
        nom = liste[i]["nom"].lower ()
        prenom = liste[i]["prenom"].lower ()
        date_naissance = liste[i]["date"]
        num = liste[i]["num"]
        email = liste[i]["email"].lower ()
        favori = liste[i]["favori"]
        
        if favori == "True":
            if date_naissance != "":
                jour, mois, annee = date_naissance.split('.')
            
                if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email or contact == favori:
                    contact_trouve += 1
                    if date_naissance != "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {date_naissance}"
                            f"\n |   {num}"
                            f"\n |   {email}\n")
                    elif date_naissance != "" and num == "" and email == "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {date_naissance}\n")
                    elif date_naissance != "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {date_naissance}"
                            f"\n |   {num}\n")
                    elif date_naissance != "" and num == "" and email != "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {date_naissance}"
                            f"\n |   {email}\n")
                    elif date_naissance == "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {num}"
                            f"\n |   {email}\n")
                    elif date_naissance == "" and num == "" and email != "":
                        contact_trouve_affichage.append (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {email}\n")
                    elif date_naissance == "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {num}\n")
                    else: contact_trouve_affichage += (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
                    
            
            else:
                if contact == nom or contact == prenom or contact == num or contact == email or contact == favori:
                    contact_trouve += 1
                    if num != "" and email != "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {num}"
                            f"\n |   {email}\n")
                    elif num != "" and email == "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {num}\n")
                    elif num == "" and email != "":
                        contact_trouve_affichage += (
                            f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                            f"\n |   {email}\n")
                    else: contact_trouve_affichage += (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
        
    if contact_trouve != 0:
        system ("cls")
        print ("   · Favoris trouvés ·") 
        print (contact_trouve_affichage)
        return
    
    else:
        system ("cls")
        print ("Aucun contact trouvé !\n")
        return