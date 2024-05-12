from outils import lecture_csv
from apps.rep_md.main import f_rep
from logging import info

def afficher ():
    info (f"    AFFICHER GROUPES\n")
    print ("   · Afficher: Groupes ·")
    liste = lecture_csv (f_rep)
    
    for groupe in liste:
        
        nom = groupe["nom_groupe"]
        num = groupe["num_groupe"]
        nbr_mbr = groupe["mbr_groupe"]
        
        if num != "":
            print (f"\n | {num}. {nom}")
            print (f" |    Membres : {nbr_mbr}/100")
            
            for membre in liste:
                membre_num = list (membre["groupe"])
                membre_nom = membre["nom"]
                membre_prenom = membre["prenom"]
                membre_num_tel = membre["num"]
                membre_email = membre["email"]
                membre_date = membre["date"]
                
                if num in membre_num:
                    
                    print (f" |")
                    print (f" |    {membre_nom} {membre_prenom}")
                    if membre_date != "":
                        print (f" |    {membre_date}")
                    if membre_num_tel != "":
                        print (f" |    {membre_num_tel}")
                    if membre_email != "":
                        print (f" |    {membre_email}")
    
    print ()
    return