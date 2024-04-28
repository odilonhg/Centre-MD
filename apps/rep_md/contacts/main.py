import os

def contacts ():
    
    print ("   · Contacts ·\n")
    
    print (" 0. Retour")
    print (" 1. Ajouter")
    print (" 2. Rechercher")
    print (" 3. Afficher")
    print (" 4. Modifier")
    print (" 5. Supprimer\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            from apps.rep_md.contacts.ajouter import ajouter
            os.system ("cls")
            ajouter ()
            return contacts ()
        
        case "2":
            from apps.rep_md.contacts.rechercher import rechercher
            os.system ("cls")
            rechercher ()
            return contacts ()
        
        case "3":
            from apps.rep_md.contacts.afficher import afficher
            os.system ("cls")
            afficher ()
            return contacts ()
        
        case "4":
            from apps.rep_md.contacts.modifier import modifier
            os.system ("cls")
            modifier ()
            return contacts ()
        
        case "5":
            from apps.rep_md.contacts.supprimer import supprimer
            os.system ("cls")
            supprimer ()
            return contacts ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return contacts ()