import os

def anniversaires ():
    
    print ("   · Anniversaires ·\n")
    
    print (" 0. Retour")
    print (" 1. Afficher\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            from apps.rep_md.anniversaires.afficher import afficher
            os.system ("cls")
            afficher ()
            return anniversaires ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return anniversaires ()