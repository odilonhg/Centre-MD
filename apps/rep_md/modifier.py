from apps.rep_md.main import F_rep
import outils
import os
import logging

def modifier (choix):
    if choix== "contacts":
        nbr_choice = "0"
        
        while True:
            L= outils.CSV.lecture_csv (F_rep)
            
            print (_("-MODIFIER : Contacts-"))
            print (_("Retour"))
            print (_("NOM"))
            print (_("PRENOM"))
            print (_("DATE DE NAISSANCE"))
            print (_("NUMERO DE TELEPHONE"))
            print (_("ADRESSE EMAIL"))
            
            choix_modifier= input (_("Choix"))
            
            if choix_modifier== "0":
                os.system ("cls")
                break
            
            os.system ("cls")
            nbr_recherche= False
            contact= input (_("Renseigner le nom ou le prénom du contact à modifier")).upper ()
            if contact== "":
                os.system ("cls")
                break
            os.system ("cls")
            for i in range (len (L)):
                nom= L[i]["nom"]
                prenom= L[i]["prenom"].upper ()
                if contact== nom or contact== prenom:
                    nbr_recherche= True
                    while True:
                        confirmation_modifier= input (_("_Modifier_")+ f" {nom} {prenom.capitalize()} : ").upper ()
                        if confirmation_modifier== _("OUI"):
                            logging.info ("  "+ _("_AJOUTER CONTACT DANS GROUPE_")+ f"{nom} {prenom.capitalize()}\n")
                            
                            if choix_modifier== "1":
                                os.system ("cls")
                                while True:
                                    new_nom= input (_("SAISIR NOM")).upper ()
                                    os.system ("cls")
                                    while True:
                                        confirmation_modifier= input (_("_Modifier_")+ f" {nom} -> {new_nom} : ").upper ()
                                        if confirmation_modifier== _("OUI"):
                                            L[i]["nom"]= new_nom
                                            outils.CSV.ecriture_csv (L, F_rep)
                                            logging.info (_("_MODIFIER CONTACTS_")+ f"{nom} -> {new_nom}\n")
                                            os.system ("cls")
                                            print (_("Le contact")+ nom, prenom.capitalize ()+ _("a été modifié"))
                                            break
                                        elif confirmation_modifier== _("NON"):
                                            os.system ("cls")
                                            break
                                        else:
                                            os.system ("cls")
                                            print (_("Tu dois répondre oui ou non"))
                                    
                                    if confirmation_modifier== _("OUI"): break
                            
                            elif choix_modifier== "2":
                                os.system ("cls")
                                while True:
                                    new_prenom= input (_("SAISIR PRENOM")).capitalize ()
                                    os.system ("cls")
                                    while True:
                                        confirmation_modifier= input (_("_Modifier_")+ f" {prenom.capitalize ()} -> {new_prenom} : ").upper ()
                                        if confirmation_modifier== _("OUI"):
                                            L[i]["prenom"]= new_prenom
                                            outils.CSV.ecriture_csv (L, F_rep)
                                            logging.info (_("_MODIFIER CONTACTS_")+ f"{prenom.capitalize ()} -> {new_prenom}\n")
                                            os.system ("cls")
                                            print (_("Le contact")+ nom, prenom.capitalize ()+ _("a été modifié"))
                                            break
                                        elif confirmation_modifier== _("NON"):
                                            os.system ("cls")
                                            break
                                        else:
                                            os.system ("cls")
                                            print (_("Tu dois répondre oui ou non"))
                                    
                                    if confirmation_modifier== _("OUI"): break
                            
                            elif choix_modifier== "3":
                                os.system ("cls")
                                date= L[i]["date"]
                                while True:
                                    while True:
                                        new_jour= input (_("SAISIR JOUR")+ f"{nom} {prenom.capitalize ()} : ")
                                        if int (jour)> 31 or int (jour)< 1:
                                            os.system ("cls")
                                            print (_("Valeur impossible"))
                                            jour= ""
                                        else: break
                                    os.system ("cls")
                                    while True:
                                        new_mois= input (_("SAISIR MOIS")+ f"{nom} {prenom.capitalize ()} : ")
                                        if int (mois)> 12 or int (mois)< 1:
                                            os.system ("cls")
                                            print (_("Valeur impossible"))
                                            mois= ""
                                        else: break
                                    os.system ("cls")
                                    while True:
                                        new_annee= input (_("SAISIR ANNEE")+ f"{nom} {prenom.capitalize ()} : ")
                                        if int (annee)> 2100 or int (annee)< 1900:
                                            os.system ("cls")
                                            print (_("Valeur impossible"))
                                            annee= ""
                                        else: break
                                    os.system ("cls")
                                    new_date= f"{new_jour}.{new_mois}.{new_annee}"
                                    while True:
                                        confirmation_modifier= input (_("_Modifier_")+ f" {date} -> {new_date} : ").upper ()
                                        if confirmation_modifier== _("OUI"):
                                            L[i]["date"]= new_date
                                            outils.CSV.ecriture_csv (L, F_rep)
                                            logging.info (_("_MODIFIER CONTACTS_")+ f"{date} -> {new_date}\n")
                                            os.system ("cls")
                                            print (_("Le contact")+ nom, prenom.capitalize ()+ _("a été modifié"))
                                            break
                                        elif confirmation_modifier== _("NON"):
                                            os.system ("cls")
                                            break
                                        else:
                                            os.system ("cls")
                                            print (_("Tu dois répondre oui ou non"))                                    
                                    
                                    if confirmation_modifier== _("OUI"): break
                            
                            elif choix_modifier== "4":
                                os.system ("cls")
                                num= L[i]["num"]
                                while True:
                                    while True:
                                        new_num= input (_("SAISIR NUM")+ f"{nom} {prenom.capitalize ()} : ")
                                        if len (new_num)!= 9 and len (new_num)!= 10:
                                            os.system ("cls")
                                            print (_("Valeur impossible"))
                                            new_num= ""
                                        elif new_num.isdigit ()== False:
                                            os.system ("cls")
                                            print (_("Valeur impossible"))
                                            new_num= ""
                                        else:
                                            if len (new_num)== 9: new_num= "0"+ new_num
                                            break
                                    os.system ("cls")
                                    while True:
                                        confirmation_modifier= input (_("_Modifier_")+ f" {num} -> {new_num} : ").upper ()
                                        if confirmation_modifier== _("OUI"):
                                            L[i]["num"]= new_num
                                            outils.CSV.ecriture_csv (L, F_rep)
                                            logging.info (_("_MODIFIER CONTACTS_")+ f"{num} -> {new_num}\n")
                                            os.system ("cls")
                                            print (_("Le contact")+ nom, prenom.capitalize ()+ _("a été modifié"))
                                            break
                                        elif confirmation_modifier== _("NON"):
                                            os.system ("cls")
                                            break
                                        else:
                                            os.system ("cls")
                                            print (_("Tu dois répondre oui ou non"))                                    
                                    
                                    if confirmation_modifier== _("OUI"): break
                            
                            elif choix_modifier== "5":
                                os.system ("cls")
                                email= L[i]["email"]
                                while True:
                                    new_email= input (_("SAISIR EMAIL")+ f"{nom} {prenom.capitalize ()} : ")
                                    os.system ("cls")
                                    while True:
                                        confirmation_modifier= input (_("_Modifier_")+ f" {email} -> {new_email} : ").upper ()
                                        if confirmation_modifier== _("OUI"):
                                            L[i]["email"]= new_email
                                            outils.CSV.ecriture_csv (L, F_rep)
                                            logging.info (_("_MODIFIER CONTACTS_")+ f"{email} -> {new_email}\n")
                                            os.system ("cls")
                                            print (_("Le contact")+ nom, prenom.capitalize ()+ _("a été modifié"))
                                            break
                                        elif confirmation_modifier== _("NON"):
                                            os.system ("cls")
                                            break
                                        else:
                                            os.system ("cls")
                                            print (_("Tu dois répondre oui ou non"))                                    
                                    
                                    if confirmation_modifier== _("OUI"): break
                            
                            else:
                                os.system ("cls")
                                print (_("Choix impossible"))
                            
                            break
                        
                        elif confirmation_modifier== _("NON"):
                            os.system ("cls")
                            break
                        
                        else:
                            os.system ("cls")
                            print (_("Tu dois répondre oui ou non"))
                        
            if nbr_recherche== False: print (_("Aucun contact trouvé"))
    
    elif choix== "groupes":
        nbr_choice = "0"
        
        while True:
            L= outils.CSV.lecture_csv (F_rep)
            
            print (_("-MODIFIER : Groupes-"))
            print (_("Retour"))
            print (_("Ajouter un membre"))
            print (_("Supprimer un membre"))
            print (_("Modifier le nom du groupe"))
            
            choix_modifier= input (_("Choix"))
            
            if choix_modifier== "0":
                os.system ("cls")
                break
            
            os.system ("cls")
            nbr_recherche= False
            groupe= input (_("Renseigner le nom du groupe à modifier")).upper ()
            if groupe== "":
                os.system ("cls")
                break
            os.system ("cls")
            for i in range (len (L)):
                nom_groupe= L[i]["nom_groupe"]
                num_groupe= L[i]["num_groupe"]
                nbr_mbr_groupe= L[i]["mbr_groupe"]
                
                if nom_groupe.upper ()== groupe:
                    nbr_mbr_groupe= int (nbr_mbr_groupe)
                    nbr_recherche= True
                    confirmation_modifier= input (_("_Modifier_")+ f" {nom_groupe} : ").upper ()
                    if confirmation_modifier== _("OUI"):
                        os.system ("cls")
                        
                        if choix_modifier== "1":
                            nbr_recherche2= False
                            contact= input (_("Renseigner une information sur le contact à trouver")).lower ()
                            for y in range (len (L)):
                                nom= L[y]["nom"].lower ()
                                prenom= L[y]["prenom"].lower ()
                                date_naissance= L[y]["date"]
                                num= L[y]["num"]
                                email= L[y]["email"].lower ()
                                favori= L[y]["favori"]
                                
                                if date_naissance != "": jour, mois, annee = date_naissance.split('.')
                                else: jour, mois, annee= None, None, None
                                
                                if contact== nom or contact== prenom or contact== date_naissance or contact== jour or contact== mois or contact== annee or contact== num or contact== email:
                                    nbr_recherche2= True
                                    confirmation_ajouter= input (_("_Ajouter_")+ f" {nom.upper ()} {prenom.capitalize()} : ").upper ()
                                    if confirmation_ajouter== _("OUI"):
                                        nbr_mbr_groupe+= 1
                                        L[i]["mbr_groupe"]= str (nbr_mbr_groupe)
                                        L[y]["groupe"]+= str(num_groupe)
                                        outils.CSV.ecriture_csv (L, F_rep)
                                        logging.info (_("_AJOUTER CONTACT DANS GROUPE_")+ f"{nom.upper ()} {prenom.capitalize()}\n")
                                        os.system ("cls")
                                        print (nom.upper (), prenom.capitalize ()+ _("a été ajouté au groupe")+ nom_groupe+ " !\n")
                                    else: os.system ("cls")
                                
                            if nbr_recherche2== False: print (_("Aucun contact trouvé"))
                        
                        elif choix_modifier== "2":
                            nbr_recherche2= False
                            contact= input (_("Renseigner une information sur le contact à trouver")).lower ()
                            for y in range (len (L)):
                                nom= L[y]["nom"].lower ()
                                prenom= L[y]["prenom"].lower ()
                                date_naissance= L[y]["date"]
                                num= L[y]["num"]
                                email= L[y]["email"].lower ()
                                favori= L[y]["favori"]
                                
                                if date_naissance != "": jour, mois, annee = date_naissance.split('.')
                                else: jour, mois, annee= None, None, None
                                
                                if contact== nom or contact== prenom or contact== date_naissance or contact== jour or contact== mois or contact== annee or contact== num or contact== email:
                                    nbr_recherche2= True
                                    confirmation_ajouter= input (_("_Supprimer_")+ f" {nom.upper ()} {prenom.capitalize()} : ").upper ()
                                    if confirmation_ajouter== _("OUI"):
                                        nbr_mbr_groupe-= 1
                                        L[i]["mbr_groupe"]= str (nbr_mbr_groupe)
                                        L[y]["groupe"]= L[y]["groupe"].replace (num_groupe, "")
                                        outils.CSV.ecriture_csv (L, F_rep)
                                        logging.info (_("_SUPPRIMER CONTACT DANS GROUPE_")+ f"{nom.upper ()} {prenom.capitalize()}\n")
                                        os.system ("cls")
                                        print (nom.upper (), prenom.capitalize ()+ _("a été supprimé du groupe")+ nom_groupe+ " !\n")
                                    else: os.system ("cls")
                                
                            if nbr_recherche2== False: print (_("Aucun contact trouvé"))
                        
                        elif choix_modifier== "3":
                            new_nom= input (_("Saisir nom groupe"))
                            L[i]["nom_groupe"]= new_nom
                            outils.CSV.ecriture_csv (L, F_rep)
                            logging.info (_("_MODIFIER GROUPES_")+ f"{nom_groupe} -> {new_nom}\n")
                            print (nom_groupe+ _("a été modifié"))