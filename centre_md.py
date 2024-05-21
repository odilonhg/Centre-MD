from math import *
from random import *

print (" Bienvenue dans le Centre MD !\n")

L = []

verif_nom = False
while verif_nom == False:
    usr_nom = input ("Veuillez saisir votre prénom : ")
    choix_nom = input ("\nVous confirmer vouloir vous appelez " + usr_nom + " : ").lower ()
    
    if choix_nom == "oui": verif_nom = True

usr = [usr_nom, [False, False, False, False, False]]

print ("\nBienvenue à toi " + usr_nom + " dans le Centre MD !")

def main ():
    print ("\n -- Centre MD --\n")
    print ("  0. Arrêter")
    if usr[1][0] == True: print ("  1. Rep MD")
    if usr[1][1] == True: print ("  2. Manager MD (NON FONCTIONNEL)")
    if usr[1][2] == True: print ("  3. Pass MD (NON FONCTIONNEL)")
    if usr[1][3] == True: print ("  4. Jeux MD (NON FONCTIONNEL)")
    print ("  5. Options\n")
    if usr[1][4] == True: print ("  13. Fonctions MD (NON FONCTIONNEL)\n")
    
    choix_main = input ("Choix : ")
    
    if choix_main == "0": return
        
    elif choix_main == "1" and usr[1][0] == True:
        Rep_MD ()
        return main ()
        
#     elif choix_main == "2" and usr[1][1] == True:
#         Manager_MD ()
#         return main ()
#             
#     elif choix_main == "3" and usr[1][2] == True:
#         Pass_MD ()
#         return main ()
#         
#     elif choix_main == "4" and usr[1][3] == True:
#         Jeux_MD ()
#         return main ()
#         
#     elif choix_main == "13" and usr[1][4] == True:
#         Fonctions_MD ()
#         return main ()
        
    elif choix_main == "5":
        options ()
        return main ()
    
    else:
        print ("\nChoix impossible...")
        return main ()

def options ():
    print ("\n   · Options ·\n")
    print ("Version Actuelle : n0.1\n") # A MODIFIER
    
    print (" 0. Retour")
    
    if False in usr[1]: print (" 1. Installer des applis")
    if True in usr[1]: print (" 2. Désinstaller des applis")
    
    choix_options = input ("\nChoix : ")
    
    if choix_options == "0": return
        
    elif choix_options == "1":
        installer_apps ()
        return options ()
        
    elif choix_options == "2":
        desinstaller_apps ()
        return options ()
        
    else:
        print ("\nChoix impossible...")
        return options ()

def installer_apps ():
    global usr
    
    print ("\n  · Installer une App MD ·\n")
    print (" 0. Retour")
    if usr[1][0] == False: print (" 1. Rep MD")
    if usr[1][1] == False: print (" 2. Manager MD")
    if usr[1][2] == False: print (" 3. Pass MD")
    if usr[1][3] == False: print (" 4. Jeux MD")
    if usr[1][4] == False: print (" 5. Fonctions MD")
    
    choix_installer_apps = input ("\nChoix : ")
    
    if choix_installer_apps == "0": return
        
    elif choix_installer_apps == "1":
        usr[1][0] = True
        return installer_apps ()
        
    elif choix_installer_apps == "2":
        usr[1][1] = True
        return installer_apps ()
        
    elif choix_installer_apps == "3":
        usr[1][2] = True
        return installer_apps ()
        
    elif choix_installer_apps == "4":
        usr[1][3] = True
        return installer_apps ()
        
    elif choix_installer_apps == "5":
        usr[1][4] = True
        return installer_apps ()
            
    else:
        print ("\nChoix impossible...")
        return installer_apps ()

def desinstaller_apps ():
    global usr
    
    print ("  · Désinstaller une App MD ·\n")
    print (" 0. Retour")
    if usr[1][0] == True: print (" 1. Rep MD")
    if usr[1][1] == True: print (" 2. Manager MD")
    if usr[1][2] == True: print (" 3. Pass MD")
    if usr[1][3] == True: print (" 4. Jeux MD")
    if usr[1][4] == True: print (" 5. Fonctions MD")
    
    choix_desinstaller_apps = input ("\nChoix : ")
    
    if choix_desinstaller_apps == "0": return
        
    elif choix_desinstaller_apps == "1":
        usr[1][0] = False
        return desinstaller_apps ()
        
    elif choix_desinstaller_apps == "2":
        usr[1][1] = False
        return desinstaller_apps ()
        
    elif choix_desinstaller_apps == "3":
        usr[1][2] = False
        return desinstaller_apps ()
        
    elif choix_desinstaller_apps == "4":
        usr[1][3] = False
        return desinstaller_apps ()
        
    elif choix_desinstaller_apps == "5":
        usr[1][4] = False
        return desinstaller_apps ()
            
    else:
        print ("\nChoix impossible...")
        return desinstaller_apps ()

class Rep_MD:
    def __init__ (self):
        bcl_rep_md = True
        while bcl_rep_md:
            
            print ("\n   · Rep MD ·\n")
            print (" 0. Retour")
            print (" 1. Contacts")
            print (" 2. Favoris (NON FONCTIONNEL)")
            print (" 3. Groupes (NON FONCTIONNEL)")
            print (" 4. Annivs (NON FONCTIONNEL)\n")
            
            choix_rep_md = input ("Choix : ")
            
            if choix_rep_md == "0": bcl_rep_md = False
                
            elif choix_rep_md == "1":
                Rep_MD.contacts (self)
                
#             elif choix_rep_md == "2":
#                 Rep_MD.favoris (self)
#                 
#             elif choix_rep_md == "3":
#                 Rep_MD.groupes (self)
#                 
#             elif choix_rep_md == "4":
#                 Rep_MD.anniversaires (self)
                
            else:
                print ("\nChoix impossible...")
        
        return
    
    def contacts (self):
        bcl_contacts = True
        while bcl_contacts:
            
            print ("\n   · Contacts ·\n")
            print (" 0. Retour")
            print (" 1. Ajouter")
            print (" 2. Rechercher")
            print (" 3. Afficher")
            print (" 4. Modifier")
            print (" 5. Supprimer\n")
            
            choix_contacts = input ("Choix : ")
            
            if choix_contacts == "0": bcl_contacts = False
                
            elif choix_contacts == "1":
                Rep_MD.Contacts.ajouter (self)
                
            elif choix_contacts == "2":
                Rep_MD.Contacts.rechercher (self)
                
            elif choix_contacts == "3":
                Rep_MD.Contacts.afficher (self)
                
            elif choix_contacts == "4":
                Rep_MD.Contacts.modifier (self)
                
            elif choix_contacts == "5":
                Rep_MD.Contacts.supprimer (self)
                
            else:
                print ("\nChoix impossible...")
        
        return
    
    class Contacts:
        def ajouter (self):
            nom = ""
            prenom = ""
            jour = ""
            mois = ""
            annee = ""
            num = ""
            email = ""
            nbr = {
                "1": "01",
                "2": "02",
                "3": "03",
                "4": "04",
                "5": "05",
                "6": "06",
                "7": "07",
                "8": "08",
                "9": "09"
            }
            
            bcl_contacts_ajouter = True
            while bcl_contacts_ajouter:
                
                print ("\n   · Ajouter: Contacts ·\n")
                
                if nom == "" or prenom == "":
                    print (" 0. Retour\n")
                    print ("  · OBLIGATOIRE ·\n")
                    print (" 1. Le nom")
                    print (" 2. Le prénom\n")
                if nom != "" and prenom != "":
                    print ("  · FACULTATIF ·\n")
                    print (" 3. La date de naissance")
                    print (" 4. Le numéro de téléphone")
                    print (" 5. L'adresse email\n")
                    
                    print (" 6. Finaliser le contact\n")
                
                choix_ajouter = input ("Choix : ")
                
                if choix_ajouter == "0": bcl_contacts_ajouter = False
                
                elif choix_ajouter == "1":
                    if nom == "":
                        nom = input ("\nRenseignez le nom de famille du contact : ")
                        print ("\nNom de famille ajouté au contact !")
                    else: print ("\nNom déjà renseigné !")
                
                elif choix_ajouter == "2":
                    if prenom == "":
                        prenom = input ("\nRenseignez le prénom du contact : ")
                        print ("\nPrénom ajouté au contact !")
                    else: print ("\nPrénom déjà renseigné !")
                
                elif choix_ajouter == "3":
                    if nom != "" and prenom != "":
                        if jour == "" or mois == "" or annee == "":
                            if jour == "":
                                jour = input ("\nRenseignez le jour de naissance du contact : ")
                                if int (jour) > 31 or int (jour) < 1:
                                    print ("\nValeur impossible...")
                                    jour = ""
                                for nbrV1, nbrV2 in nbr.items ():
                                    if jour == nbrV1:
                                        jour = nbrV2
                                        break
                            if mois == "":
                                mois = input ("\nRenseignez le mois de naissance du contact : ")
                                if int (mois) > 12 or int (mois) < 1:
                                    print ("\nValeur impossible...")
                                    mois = ""
                                for nbrV1, nbrV2 in nbr.items ():
                                    if mois == nbrV1:
                                        mois = nbrV2
                                        break
                            if annee == "":
                                annee = input ("\nRenseignez l'année de naissance du contact : ")
                                if int (annee) > 2100 or int (annee) < 1900:
                                    print ("\nValeur impossible...\n")
                                    annee = ""
                            print ("\nDate de naissance ajouté au contact !")
                        else: print ("\nDate de naissance déjà renseignée !")
                    else: print ("\nChoix impossible...")
                
                elif choix_ajouter == "4":
                    if nom != "" and prenom != "":
                        if num == "":
                            num = input ("\nRenseignez le numéro de téléphone du contact : ")
                            if len(num) != 9 and len(num) != 10:
                                print ("\nValeur impossible...")
                                num = ""
                            elif num.isdigit () == False:
                                print ("\nValeur impossible...")
                                num = ""
                            else:
                                if len(num) == 9: num = "0" + num
                                print ("\nNuméro de téléphone ajouté au contact !")
                        else: print ("\nNuméro de téléphone déjà renseigné !")
                    else: print ("\nChoix impossible...")
                
                elif choix_ajouter == "5":
                    if nom != "" and prenom != "":
                        if email == "": email = input ("\nRenseignez l'adresse email du contact : ")
                        else: print ("\nAdresse email déjà renseignée !")
                    else: print ("\nChoix impossible...")
                
                elif choix_ajouter == "6":
                    if nom != "" and prenom != "":
                        if annee == "": date = ""
                        else: date = jour+"."+mois+"."+annee
                        nouveau_contact = {"nom": nom, "prenom": prenom, "date": date, "num": num, "email": email, "favori": "False", "groupe": "", "nom_groupe": "", "num_groupe": "", "mbr_groupe": ""}
                        L.append (nouveau_contact)
                        print ("\nLe contact "+nom+" "+prenom+" a été crée !")
                        bcl_contacts_ajouter = False
                    else: print ("\nVeuillez renseigner le nom et le prénom du contact pour continuer.")
                
                else: print ("\nChoix impossible...")
            
            return
        
        def rechercher (self):
            print ("\n   · Rechercher: Contacts ·\n")
            contact = input (" Renseigner une information sur le contact à trouver : ").lower()
            
            contact_trouve = 0
            contact_trouve_affichage = ""
            
            for i in range (len (L)):
                nom = L[i]["nom"].lower ()
                prenom = L[i]["prenom"].lower ()
                date_naissance = L[i]["date"]
                num = L[i]["num"]
                email = L[i]["email"].lower ()
                
                if date_naissance != "": jour, mois, annee = date_naissance.split('.')
                else: jour, mois, annee = "", "", ""
                
                if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email:
                    contact_trouve += 1
                    if date_naissance != "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, num, email)
                        )
                    elif date_naissance != "" and num == "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance)
                        )
                    elif date_naissance != "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, num)
                        )
                    elif date_naissance != "" and num == "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, email)
                        )
                    elif date_naissance == "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), num, email)
                        )
                    elif date_naissance == "" and num == "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), email)
                        )
                    elif date_naissance == "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), num)
                        )
                    else:
                        contact_trouve_affichage += (
                            "\n\n |   %s %s" % 
                            (nom.upper (), prenom.capitalize ())
                        )
                
                
            if contact_trouve != 0:
                print ("\n   · Contacts trouvés ·"+contact_trouve_affichage)
                return
            
            else:
                print ("\nAucun contact trouvé !")
                return
        
        def afficher (self):
            contact_trouve = 0
            contact_trouve_affichage = ""
            
            for i in range (len (L)):
                nom = L[i]["nom"].lower ()
                prenom = L[i]["prenom"].lower ()
                date_naissance = L[i]["date"]
                num = L[i]["num"]
                email = L[i]["email"].lower ()
                
                if nom != "" and prenom != "":
                    if date_naissance != "": jour, mois, annee = date_naissance.split('.')
                    else: jour, mois, annee = "", "", ""
                    
                    contact_trouve += 1
                    if date_naissance != "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, num, email)
                        )
                    elif date_naissance != "" and num == "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance)
                        )
                    elif date_naissance != "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, num)
                        )
                    elif date_naissance != "" and num == "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), date_naissance, email)
                        )
                    elif date_naissance == "" and num != "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), num, email)
                        )
                    elif date_naissance == "" and num == "" and email != "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), email)
                        )
                    elif date_naissance == "" and num != "" and email == "":
                        contact_trouve_affichage += (
                            "\n\n |   %s %s\n |   %s" % 
                            (nom.upper (), prenom.capitalize (), num)
                        )
                    else:
                        contact_trouve_affichage += (
                            "\n\n |   %s %s" % 
                            (nom.upper (), prenom.capitalize ())
                        )
                
            if contact_trouve != 0:
                print ("\n   · Afficher: Contacts ·"+contact_trouve_affichage)
                return
            
            else:
                print ("\nAucun contact existant !")
                return
        
        def modifier (self):
            choix = None
            bcl_contacts_modifier = True
            while bcl_contacts_modifier:
                
                print ("\n   · Modifier: Contacts ·\n")
                print (" 0. Retour")
                print (" 1. Le nom")
                print (" 2. Le prénom")
                print (" 3. La date de naissance")
                print (" 4. Le numéro de téléphone")
                print (" 5. L'adresse email\n")
                
                choix_modifier = input ("Choix : ")
                contact = input ("\nRenseigner une information sur le contact à trouver : ").lower()
                
                
                if choix_modifier == "0": return
                
                elif choix_modifier == "1":
                    choix = 1
                    bcl_contacts_modifier = False
                
                elif choix_modifier == "2":
                    choix = 2
                    bcl_contacts_modifier = False
                
                elif choix_modifier == "3":
                    choix = 3
                    bcl_contacts_modifier = False
                
                elif choix_modifier == "4":
                    choix = 4
                    bcl_contacts_modifier = False
                
                elif choix_modifier == "5":
                    choix = 5
                    bcl_contacts_modifier = False
                
                else:
                    print ("\nChoix impossible...")
            
            for i in range (len (L)):
                nom = L[i]["nom"].lower ()
                prenom = L[i]["prenom"].lower ()
                date_naissance = L[i]["date"]
                num = L[i]["num"]
                email = L[i]["email"].lower ()
                favori = L[i]["favori"]
                
                if date_naissance != "":
                    jour, mois, annee = date_naissance.split('.')
                    if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email or contact == favori:
                        print ("\nModifier "+nom.upper ()+" "+prenom.capitalize ()+" ?\n")
                        choix2 = input ("Choix : ").lower ()
                else:
                    if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                        print ("\nModifier "+nom.upper ()+" "+prenom.capitalize ()+" ?\n")
                        choix2 = input ("Choix : ").lower ()
                
                if choix2 == "oui":
                    
                    if choix == 1:
                        new_nom = input ("\nRenseigner le nouveau nom de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        L[i]["nom"] = new_nom
                        print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été modifié")
                        return
                    
                    elif choix == 2:
                        new_prenom = input ("\nRenseigner le nouveau prénom de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        L[i]["prenom"] = new_prenom
                        print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été modifi")
                        return
                    
                    elif choix == 3:
                        new_jour = input ("\nRenseigner le nouveau jour de naissance de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        new_mois = input ("\nRenseigner le nouveau mois de naissance de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        new_annee = input ("\nRenseigner la nouvelle année de naissance de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        new_date = new_jour+"."+new_mois+"."+new_annee
                        L[i]["date"] = new_date
                        print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été modifié")
                        return
                    
                    elif choix == 4:
                        new_num = input ("\nRenseigner le nouveau numéro de téléphone de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        L[i]["num"] = new_num
                        print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été modifié")
                        return
                    
                    elif choix == 5:
                        new_email = input ("\nRenseigner le nouvel email de "+nom.upper ()+" "+prenom.capitalize ()+" : ")
                        L[i]["email"] = new_email
                        print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été modifié")
                        return
        
        def supprimer (self):
            choice = "non"
            print ("\n   · Supprimer: Contacts ·\n")
            contact = input ("Renseigner une information sur le contact à supprimer : ").lower()
            
            for i in range (len (L)):
                nom = L[i]["nom"].lower ()
                prenom = L[i]["prenom"].lower ()
                date_naissance = L[i]["date"]
                num = L[i]["num"]
                email = L[i]["email"].lower ()
                favori = L[i]["favori"]
                
                if date_naissance != "":
                    jour, mois, annee = date_naissance.split (".")
                    if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email or contact == favori:
                        print ("\nSupprimer "+nom.upper ()+" "+prenom.capitalize ()+" ?\n")
                        choice = input ("Choix : ").lower ()
                else:
                    if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                        print ("\nSupprimer "+nom.upper ()+" "+prenom.capitalize ()+" ?\n")
                        choice = input ("Choix : ").lower ()
                
                if choice == "oui":
                    del (L[i])
                    print ("\nLe contact "+nom.upper ()+" "+prenom.capitalize ()+" a été supprimé des contacts !")
                    return
            
            print ("\nAucun contact trouvé !")
            return

main ()