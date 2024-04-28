from outils import lecture_csv, ecriture_csv
import logging
import os

ancien_f_rep = "data_rep_md.csv"
f_rep = "data_rep.csv" # NE PAS MODIFIER LE NOM DE LA VARIABLE (liée à ttes les autres fonctions)

if os.path.exists (ancien_f_rep) == True: # PROTECTION POUR LES POSSESSEURS DE LA V0.2 (déplacement des données vers le nouveau fichier)
    liste = lecture_csv (ancien_f_rep)
    ecriture_csv (liste, f_rep)
    os.remove (ancien_f_rep)
    logging.info (f"  DEPLACEMENT DES DONNEES DU Rep MD POUR LA MAJ : {ancien_f_rep} -> {f_rep}\n")

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