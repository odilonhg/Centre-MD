from outils import Outils
from apps.rep_md.main import f_rep
from logging import info

def afficher ():
    liste = Outils.CSV.lecture_csv (f_rep)
    contact_trouve = 0
    contact_trouve_affichage = ""
    info (f"    AFFICHER CONTACTS\n")
    
    for i in range (len (liste)):
        nom = liste[i]["nom"].lower ()
        prenom = liste[i]["prenom"].lower ()
        date_naissance = liste[i]["date"]
        num = liste[i]["num"]
        email = liste[i]["email"].lower ()
        favori = liste[i]["favori"]
        
        if nom != "" and prenom != "":
            if date_naissance != "":
                jour, mois, annee = date_naissance.split('.')
            
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
        print ("   · Afficher: Contacts ·")
        print (contact_trouve_affichage)
        return
    
    else:
        print ("Aucun contact existant !\n")
        return