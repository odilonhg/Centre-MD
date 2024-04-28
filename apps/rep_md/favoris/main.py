import os

def favoris ():
    
    print ("   · Favoris ·\n")
    
    print (" 0. Retour")
    print (" 1. Ajouter")
    print (" 2. Rechercher")
    print (" 3. Afficher")
    print (" 4. Supprimer\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            return ""
        
        case "1":
            from apps.rep_md.favoris.ajouter import ajouter
            os.system ("cls")
            ajouter ()
            return favoris ()
        
        case "2":
            from apps.rep_md.favoris.rechercher import rechercher
            os.system ("cls")
            rechercher ()
            return favoris ()
        
        case "3":
            from apps.rep_md.favoris.afficher import afficher
            os.system ("cls")
            afficher ()
            return favoris ()
        
        case "4":
            from apps.rep_md.favoris.supprimer import supprimer
            os.system ("cls")
            supprimer ()
            return favoris ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return favoris ()