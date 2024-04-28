from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
import logging
import os

def supprimer ():
    liste = lecture_csv (f_rep)
    nom_groupe = input ("Saisir le nom ou le numéro du groupe à supprimer : ").upper ()
    
    for groupe in liste:
        if groupe["nom_groupe"] != "" or groupe["num_groupe"] != "":
            if nom_groupe == groupe["nom_groupe"].upper () or nom_groupe == groupe["num_groupe"]:
                nom = groupe["nom_groupe"]
                num = groupe["num_groupe"]
                nbr_mbr = groupe["mbr_groupe"]
                
                print (f"\n | {num}. {nom}")
                print (f" |    Membres : {nbr_mbr}/100")
                
                for membre in liste:
                    membre_num = list (membre["groupe"])
                    membre_nom = membre["nom"]
                    membre_prenom = membre["prenom"]
                    
                    if num in membre_num:
                        print (f" |")
                        print (f" |    {membre_nom} {membre_prenom}")
                
                choice = input (f"\nSupprimer {nom} : ").upper ()
                if choice == "OUI":
                    
                    os.system ("cls")
                    
                    for membre in liste:
                        membre["groupe"] = membre["groupe"].replace (num, "")
                    
                    for i in range (len (liste)):
                        if nom_groupe == liste[i]["nom_groupe"].upper () or nom_groupe == liste[i]["num_groupe"]:
                            del liste[i]
                            ecriture_csv (liste, f_rep)
                            print (f"Le groupe {nom} à été supprimé !\n")
                            logging.info (f"    SUPPRIMER GROUPE: {nom}\n")
                            return ""
    
    os.system ("cls")
    print ("Aucun groupe trouvé !\n")
    return ""