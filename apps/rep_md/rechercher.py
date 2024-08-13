from apps.rep_md.main import F_rep
import outils
import os
import logging

def rechercher (choix):
    if choix== "contacts":
        L= outils.CSV.lecture_csv (F_rep)
        
        print (_("-RECHERCHER : Contacts-"))
        contact= input (_("Renseigner une information sur le contact à trouver")).lower()
        logging.info (_("_RECHERCHER CONTACTS_")+ contact+ "\n")
        
        contact_trouve= 0
        contact_trouve_affichage= ""
        
        for i in range (len (L)):
            nom= L[i]["nom"].lower ()
            prenom= L[i]["prenom"].lower ()
            date_naissance= L[i]["date"]
            num= L[i]["num"]
            email= L[i]["email"].lower ()
            favori= L[i]["favori"]
        
            if date_naissance != "":
                jour, mois, annee = date_naissance.split('.')
                
                if contact== nom or contact== prenom or contact== date_naissance or contact== jour or contact== mois or contact== annee or contact== num or contact== email:
                    contact_trouve+= 1
                    if favori== "True":
                        if date_naissance!= "" and num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif date_naissance!= "" and num== "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}\n")
                        elif date_naissance!= "" and num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {num}\n")
                        elif date_naissance!= "" and num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}\n")
                        else: contact_trouve_affichage+= (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
                    else:
                        if date_naissance!= "" and num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif date_naissance!= "" and num== "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}\n")
                        elif date_naissance!= "" and num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {num}\n")
                        elif date_naissance!= "" and num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {date_naissance}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {email}\n")
                        elif date_naissance== "" and num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}\n")
                        else: contact_trouve_affichage+= (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
                
            else:
                if contact == nom or contact == prenom or contact == num or contact == email:
                    contact_trouve += 1
                    if favori== "True":
                        if num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}\n")
                        elif num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n | * {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {email}\n")
                        else: contact_trouve_affichage+= (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
                    else:
                        if num!= "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}"
                                f"\n |   {email}\n")
                        elif num!= "" and email== "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {num}\n")
                        elif num== "" and email!= "":
                            contact_trouve_affichage+= (
                                f"\n |   {nom.upper ()} {prenom.capitalize ()}"
                                f"\n |   {email}\n")
                        else: contact_trouve_affichage+= (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")

        if contact_trouve!= 0:
            os.system ("cls")
            print (_("-CONTACTS TROUVES-"))
            print (contact_trouve_affichage)
            return
        else:
            os.system ("cls")
            print (_("Aucun contact trouvé"))
            return

    elif choix== "groupes":
        L= outils.CSV.lecture_csv (F_rep)
        
        print (_("-RECHERCHER : Groupes-"))
        nom_groupe= input (_("Renseigner une information sur le groupe à trouver")).lower ()
        logging.info (_("_RECHERCHER CONTACTS_")+ nom_groupe+ "\n")
        
        groupe_trouve= 0
        groupe_trouve_affichage= ""
        
        for i in range (len (L)):
            nom= L[i]["nom_groupe"]
            num= L[i]["num_groupe"]
            nbr_mbr= L[i]["mbr_groupe"]
            
            if nom.lower ()== nom_groupe:
                groupe_trouve+= 1
                groupe_trouve_affichage+= (
                    f"\n | {num}. {nom}"
                    f"\n |    "+ _("Membres")+ f" : {nbr_mbr}\n")
                
                for y in range (len (L)):
                    membre_num= list (L[y]["groupe"])
                    membre_nom= L[y]["nom"]
                    membre_prenom= L[y]["prenom"]
                    membre_num_tel= L[y]["num"]
                    membre_email= L[y]["email"]
                    membre_date= L[y]["date"]
                    membre_favori= L[y]["favori"]
                    
                    if num in membre_num:
                        if membre_favori== "True":
                            groupe_trouve_affichage+= (
                                f" |"
                                f"\n | *  {membre_nom} {membre_prenom}\n")
                            if membre_date!= "":
                                groupe_trouve_affichage+= (f" |    {membre_date}\n")
                            if membre_num_tel!= "":
                                groupe_trouve_affichage+= (f" |    {membre_num_tel}\n")
                            if membre_email!= "":
                                groupe_trouve_affichage+= (f" |    {membre_email}\n")
                        else:
                            groupe_trouve_affichage+= (
                                f" |"
                                f"\n |    {membre_nom} {membre_prenom}\n")
                            if membre_date!= "":
                                groupe_trouve_affichage+= (f" |    {membre_date}\n")
                            if membre_num_tel!= "":
                                groupe_trouve_affichage+= (f" |    {membre_num_tel}\n")
                            if membre_email!= "":
                                groupe_trouve_affichage+= (f" |    {membre_email}\n")
                
        if groupe_trouve!= 0:
            os.system ("cls")
            print (_("-GROUPES TROUVES-"))
            print (groupe_trouve_affichage)
            return
        else:
            os.system ("cls")
            print (_("Aucun groupe trouvé"))
            return