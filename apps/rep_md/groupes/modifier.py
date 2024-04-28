from outils import lecture_csv, ecriture_csv
from apps.rep_md.main import f_rep
import logging
import os

def modifier ():
    liste = lecture_csv (f_rep)
    
    print ("   · Modifier un Groupe ·\n")
    
    print (" 0. Retour")
    print (" 1. Ajouter un membre")
    print (" 2. Supprimer un membre")
    print (" 3. Modifier le nom du groupe\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0": return ""
        
        case "1":
            os.system ("cls")
            nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
            
            for groupe in liste:
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
                    
                    contact = input ("\nSaisir le nom ou le prénom du contact à ajouter au groupe : ").upper ()
                    
                    for contacts in liste:
                        nom_c = contacts["nom"]
                        prenom_c = contacts["prenom"].upper ()
                        
                        if contact == nom_c or contact == prenom_c:
                            os.system ("cls")
                            print (f"Ajouter {nom_c} {prenom_c.capitalize ()} au groupe ?\n")
                            choice_contact = input ("Choix : ").lower ()
                                
                            if choice_contact == "oui":
                                    
                                int_nbr_mbr = int (nbr_mbr)
                                int_nbr_mbr += 1
                                nbr_mbr = str (int_nbr_mbr)
                                groupe["mbr_groupe"] = nbr_mbr
                                contacts["groupe"] += str (num)
                                ecriture_csv (liste, f_rep)
                                logging.info (f"    AJOUTER CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize ()}\n")
                                os.system ("cls")
                                print (f"Le contact {nom_c} {prenom_c.capitalize()} a été ajouté au groupe {nom} !\n")
                                return modifier ()
            
            os.system ("cls")
            print ("Aucun groupe trouvé !\n")
            return modifier ()
        
        case "2":
            os.system ("cls")
            nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
            
            for groupe in liste:
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
                    
                    contact = input ("\nSaisir le nom ou le prénom du contact à supprimer du groupe : ").upper ()
                    
                    for contacts in liste:
                        nom_c = contacts["nom"]
                        prenom_c = contacts["prenom"].upper ()
                        
                        if contact == nom_c or contact == prenom_c:
                            os.system ("cls")
                            print (f"Supprimer {nom_c} {prenom_c.capitalize ()} du groupe ?\n")
                            choice_contact = input ("Choix : ").lower ()
                                
                            if choice_contact == "oui":
                                    
                                int_nbr_mbr = int (nbr_mbr)
                                int_nbr_mbr -= 1
                                nbr_mbr = str (int_nbr_mbr)
                                groupe["mbr_groupe"] = nbr_mbr
                                contacts["groupe"] = contacts["groupe"].replace (num, "")
                                ecriture_csv (liste, f_rep)
                                logging.info (f"    SUPPRIMER CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize ()}\n")
                                os.system ("cls")
                                print (f"Le contact {nom_c} {prenom_c.capitalize()} a été supprimé du groupe {nom} !\n")
                                return modifier ()
            
            os.system ("cls")
            print ("Aucun groupe trouvé !\n")
            return modifier ()
        
        case "3":
            os.system ("cls")
            nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
            
            for groupe in liste:
                if nom_groupe == groupe["nom_groupe"].upper () or nom_groupe == groupe["num_groupe"]:
                    nom = groupe["nom_groupe"]
                    num = groupe["num_groupe"]
                    nbr_mbr = groupe["mbr_groupe"]
                    
                    os.system ("cls")
                    choice2 = input (f"Modifier {nom} : ").lower ()
                    
                    if choice2 == "oui":
                        contact = input (f"\nSaisir le nouveau nom du groupe : ")
                        groupe["nom_groupe"] = contact
                        os.system ("cls")
                        print (f"Le groupe {nom} a été modifié !\n")
                        logging.info (f"    MODIFIER GROUPE: {nom} -> {contact}\n")
                        ecriture_csv (liste, f_rep)
                        return modifier ()
            
            os.system ("cls")
            print ("Aucun groupe trouvé !\n")
            return ""
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return modifier ()