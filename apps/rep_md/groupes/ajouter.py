from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
import logging
import os

num = 1
nom = ""
nbr_mbr = 0

def ajouter ():
    global num, nom, nbr_mbr
    liste = lecture_csv (f_rep)
    num_existant = [int(groupe["num_groupe"]) for groupe in liste if groupe["num_groupe"].isdigit()]
    
    while num in num_existant:
        num += 1
    
    print ("   · Ajouter un Groupe ·\n")
    
    print (" 0. Retour")
    print (" 1. Le nom du groupe")
    print (" 2. Les membres du groupe (optionnel)\n")
    
    print (" 3. Finaliser le groupe !\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            os.system ("cls")
            return ""
        
        case "1":
            if nom == "":
                os.system ("cls")
                nom = input ("Renseigner le nom du groupe : ")
                logging.info (f"    AJOUTER GROUPE: {nom}\n")
                os.system ("cls")
                return ajouter()
            else:
                os.system ("cls")
                return ajouter ()
        
        case "2":
            os.system ("cls")
            contact = input ("Saisir le nom ou le prénom du contact à ajouter au groupe : ").upper ()
            
            for contacts in liste:
                nom_c = contacts["nom"]
                prenom_c = contacts["prenom"].upper ()
                
                if contact == nom_c or contact == prenom_c:
                    choice2 = input (f"\nAjouter {nom_c} {prenom_c.capitalize ()} : ").upper ()
                    
                    if choice2 == "OUI":
                        nbr_mbr += 1
                        contacts["groupe"] += str (num)
                        ecriture_csv (liste, f_rep)
                        logging.info (f"    AJOUTER CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize ()}\n")
                        os.system ("cls")
                        print (f"Le contact {nom_c} {prenom_c.capitalize ()} a été ajouté au groupe {nom}\n")
                        return ajouter ()
            
            os.system ("cls")
            print ("Aucun contact trouvé !\n")
            return ajouter ()
        
        case "3":
            os.system ("cls")
            if nom == "":
                nom = input ("Saisir le nom du groupe : ")
                os.system ("cls")
            
            g_new = {"nom": "", "prenom": "", "date": "", "num": "", "email": "", "favori": "", "groupe": "", "nom_groupe": nom, "num_groupe": str (num), "mbr_groupe": str (nbr_mbr)}
            liste.append (g_new)
            ecriture_csv (liste, f_rep)
            
            print (f"Le groupe {nom} a été crée !\n")
            nom = ""
            nbr_mbr = 0
            return ""
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return ajouter ()