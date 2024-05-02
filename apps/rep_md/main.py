from outils import lecture_csv, ecriture_csv
import logging
import os

f_rep = "data_rep.csv" # NE PAS MODIFIER LE NOM DE LA VARIABLE (liée à ttes les autres fonctions)

def rep_md ():
     
    print ("   · Rep MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Contacts")
    print (" 2. Favoris")
    print (" 3. Groupes")
    print (" 4. Anniversaires (NOUVEAU !)\n")
    
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
        
        case "4":
            from apps.rep_md.anniversaires.main import anniversaires
            os.system ("cls")
            anniversaires ()
            os.system ("cls")
            return rep_md ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return rep_md ()