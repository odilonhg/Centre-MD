from outils import lecture_csv, ecriture_csv
import logging
import os

f_rep = "data_rep.csv"

if os.path.exists ("data_rep_md.csv") == True: # PROTECTION POUR LES POSSESSEURS DE LA V0.2 (déplacement des données vers le nouveau fichier)
    liste = lecture_csv ("data_rep_md.csv")
    ecriture_csv (liste, f_rep)
    os.remove ("data_rep_md.csv")
    logging.info ("DEPLACEMENT DES DONNEES DU Rep MD POUR LA MAJ 1.0 (data_rep_md.csv -> data_rep.csv)\n")

def rep_md ():
     
    print ("   · Rep MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Contacts")
    print (" 2. Favoris")
    print (" 3. Groupes\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            from apps.rep_md.contacts.main import contacts
            os.system ("cls")
            contacts ()
            os.system ("cls")
            return rep_md ()
        
        case "2":
            from apps.rep_md.favoris.main import favoris
            os.system ("cls")
            favoris ()
            os.system ("cls")
            return rep_md ()
        
        case "3":
            from apps.rep_md.groupes.main import groupes
            os.system ("cls")
            groupes ()
            os.system ("cls")
            return rep_md ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return rep_md ()