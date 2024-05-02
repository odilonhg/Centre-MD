from outils import lecture_csv
from apps.rep_md.main import f_rep
import logging
import os

def afficher ():
    liste = lecture_csv (f_rep)
    logging.info (f"    AFFICHER FAVORIS\n")
    
    print ("   · Afficher les Favoris ·")
    
    if len (liste) >= 1:
        
        for i in range (len (liste)):
            nom = liste[i]["nom"]
            prenom = liste[i]["prenom"]
            date_naissance = liste[i]["date"]
            num = liste[i]["num"]
            email = liste[i]["email"].lower ()
            favori = liste[i]["favori"]
            
            if favori == "True":
                print (f"\n |   {nom} {prenom}")
            
                if date_naissance != "": print (f" |   {date_naissance}")
                if num != "": print (f" |   {num}")
                if email != "": print (f" |   {email}")
        
        print ()
        return ""
    
    print ("Aucun contact trouvé !\n")
    return ""