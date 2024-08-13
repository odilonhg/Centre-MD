from apps.rep_md.main import F_rep
import outils
import os
import logging

def afficher (choix):
    if choix== "contacts":
        L= outils.CSV.lecture_csv (F_rep)
        contact_trouve = 0
        contact_trouve_affichage = ""
        logging.info (_("_AFFICHER CONTACTS_")+ "\n")
        
        for i in range (len (L)):
            nom= L[i]["nom"].lower ()
            prenom= L[i]["prenom"].lower ()
            date_naissance= L[i]["date"]
            num= L[i]["num"]
            email= L[i]["email"].lower ()
            favori= L[i]["favori"]
            
            if nom!= "" and prenom!= "":
                contact_trouve += 1
                if favori== "True":
                    contact_trouve_affichage+= (f"\n | * {nom.upper ()} {prenom.capitalize ()}\n")
                else:
                    contact_trouve_affichage+= (f"\n |   {nom.upper ()} {prenom.capitalize ()}\n")
                
                if date_naissance!= "": contact_trouve_affichage+= (f" |   {date_naissance}\n")
                if num!= "": contact_trouve_affichage+= (f" |   {num}\n")
                if email!= "": contact_trouve_affichage+= (f" |   {email}\n")
        
        if contact_trouve != 0:
            print (_("-AFFICHER : Contacts-"))
            print (contact_trouve_affichage)
            return
        
        else:
            print (_("Aucun contact existant"))
            return
    
    elif choix== "groupes":
        L= outils.CSV.lecture_csv (F_rep)
        
        groupe_trouve= 0
        groupe_trouve_affichage= ""
        
        for i in range (len (L)):
            nom= L[i]["nom_groupe"]
            num= L[i]["num_groupe"]
            nbr_mbr= L[i]["mbr_groupe"]
            
            if nom!= "":
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
                        else:
                            groupe_trouve_affichage+= (
                                f" |"
                                f"\n |    {membre_nom} {membre_prenom}\n")
                        
                        if membre_date!= "": groupe_trouve_affichage+= (f" |    {membre_date}\n")
                        if membre_num_tel!= "": groupe_trouve_affichage+= (f" |    {membre_num_tel}\n")
                        if membre_email!= "": groupe_trouve_affichage+= (f" |    {membre_email}\n")
                
        if groupe_trouve!= 0:
            print (_("-AFFICHER : Groupes-"))
            print (groupe_trouve_affichage)
            return
        else:
            print (_("Aucun groupe existant"))
            return