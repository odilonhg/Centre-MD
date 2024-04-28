import logging
import os

def jeux_md ():
    
    print ("   · Jeux MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Chiffre Juste")
    print (" 2. Pendu")
    print (" 3. Puissance 4")
    print (" 4. Morpion")
    print (" 5. Mots Mêlés (NOUVEAU)\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            from apps.jeux_md.chiffre_juste import chiffre_juste
            os.system ("cls")
            logging.info ("    OUVERTURE JEU: Chiffre Juste\n")
            chiffre_juste ()
            logging.info ("    FERMETURE JEU: Chiffre Juste\n")
            return jeux_md ()
        
        case "2":
            from apps.jeux_md.pendu import pendu
            os.system ("cls")
            logging.info("    OUVERTURE JEU: Pendu\n")
            pendu ()
            logging.info("    FERMETURE JEU: Pendu\n")
            return jeux_md ()
        
        case "3":
            from apps.jeux_md.puissance_4 import puissance_4
            os.system ("cls")
            puissance_4 () # GESTION LOGGING INTEGREE
            return jeux_md ()
        
        case "4":
            from apps.jeux_md.morpion import morpion
            os.system ("cls")
            morpion () # GESTION LOGGING INTEGREE
            return jeux_md ()
        
        case "5":
            from apps.jeux_md.mots_meles import mots_meles
            os.system ("cls")
            logging.info ("    OUVERTURE JEU: Mots Mêlés\n")
            mots_meles (2, 6) # CREER 4 MOTS DE LONGUEUR MAXI 8
            logging.info ("    FERMETURE JEU: Mots Mêlés\n")
            return jeux_md ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return jeux_md ()