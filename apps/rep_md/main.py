from os import system

f_rep = "data_rep.csv" # NE PAS MODIFIER LE NOM DE LA VARIABLE (liée à ttes les autres fonctions)
F_rep = "data_rep.csv"

def rep_md ():
     
    print ("   · Rep MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Contacts")
    print (" 2. Favoris")
    print (" 3. Groupes")
    print (" 4. Annivs\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            from apps.rep_md.contacts.main import contacts
            system ("cls")
            contacts ()
            system ("cls")
            return rep_md ()
        
        case "2":
            from apps.rep_md.favoris.main import favoris
            system ("cls")
            favoris ()
            system ("cls")
            return rep_md ()
        
        case "3":
            from apps.rep_md.groupes.main import groupes
            system ("cls")
            groupes ()
            system ("cls")
            return rep_md ()
        
        case "4":
            from apps.rep_md.anniversaires.main import anniversaires
            system ("cls")
            anniversaires ()
            system ("cls")
            return rep_md ()
        
        case _:
            system ("cls")
            print ("Choix impossible...\n")
            return rep_md ()