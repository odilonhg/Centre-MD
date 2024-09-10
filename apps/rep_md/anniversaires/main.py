from os import system

def anniversaires ():
    
    print ("   · Anniversaires ·\n")
    
    print (" 0. Retour")
    print (" 1. Ajouter (en cours de création...)")
    print (" 2. Afficher\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return
        
        case "1":
            system ("cls")
            print ("Option prochainement disponible...\n")
            return anniversaires ()
        
        case "2":
            from apps.rep_md.anniversaires.afficher import afficher
            system ("cls")
            afficher ()
            return anniversaires ()
        
        case _:
            system ("cls")
            print ("Choix impossible...\n")
            return anniversaires ()