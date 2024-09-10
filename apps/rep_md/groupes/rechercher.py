from outils import lecture_csv
from apps.rep_md.main import f_rep
from logging import info
from os import system

def rechercher ():
    liste = lecture_csv (f_rep)
    
    print ("   · Rechercher: Groupes ·\n")
    nom_groupe = input ("Renseigner le nom ou le numéro du groupe à trouver : ").upper ()
    info (f"    RECHERCHER GROUPES: {nom_groupe}\n")
    
    system ("cls")
    print ("   · Groupes Trouvés ·")
    
    for groupe in liste:
        if nom_groupe == groupe["nom_groupe"].upper () or nom_groupe == groupe["num_groupe"]:
            nom = groupe["nom_groupe"]
            num = groupe["num_groupe"]
            nbr_mbr = groupe["mbr_groupe"]
            
            if nom != "":
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