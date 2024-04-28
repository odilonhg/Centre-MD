import os

def groupes ():
    
    print ("   · Groupes ·\n")
    
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
            from apps.rep_md.groupes.ajouter import ajouter
            os.system ("cls")
            ajouter ()
            return groupes ()
        
        case "2":
            from apps.rep_md.groupes.rechercher import rechercher
            os.system ("cls")
            rechercher ()
            return groupes ()
        
        case "3":
            from apps.rep_md.groupes.afficher import afficher
            os.system ("cls")
            afficher ()
            return groupes ()
        
        case "4":
            from apps.rep_md.groupes.modifier import modifier
            os.system ("cls")
            modifier ()
            os.system ("cls")
            return groupes ()
        
        case "5":
            from apps.rep_md.groupes.supprimer import supprimer
            os.system ("cls")
            supprimer ()
            return groupes ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return contacts ()