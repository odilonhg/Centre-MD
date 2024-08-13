from apps.rep_md.main import F_rep
import outils
import os
import logging

def ajouter (choix):
    if choix== "contacts":
        nom= ""
        prenom= ""
        jour= ""
        mois= ""
        annee= ""
        num= ""
        email= ""
        L= outils.CSV.lecture_csv (F_rep)
        nbr= {
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
        
        while True:
            print (_("-AJOUTER : Contacts-"))
            if nom== "" or prenom== "":
                print (_("Retour"))
                print (_("-OBLIGATOIRE-"))
                print (_("NOM"))
                print (_("PRENOM"))
            elif nom != "" and prenom != "":
                print (_("-FACULTATIF-"))
                print (_("DATE DE NAISSANCE"))
                print (_("NUMERO DE TELEPHONE"))
                print (_("ADRESSE EMAIL"))
                print (_("FIN CONTACT"))
            
            choix_ajouter= input (_("Choix")).lower ()
            os.system ("cls")

            if choix_ajouter== "0":
                if nom== "" or prenom== "":
                    break
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "1":
                if nom== "" or prenom== "":
                    if nom== "":
                        nom= input (_("SAISIR NOM")).upper ()
                        os.system ("cls")
                        print (_("Nom de famille ajouté"))
                    else: print (_("Nom déjà ajouté"))
                else: print (_("Choix impossible"))

            elif choix_ajouter== "2":
                if nom== "" or prenom== "":
                    if prenom== "":
                        prenom= input (_("SAISIR PRENOM")).capitalize ()
                        os.system ("cls")
                        print (_("Prénom ajouté"))
                    else: print (_("Prénom déjà ajouté"))
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "3":
                if nom!= "" and prenom!= "":
                    if jour== "":
                        while True:
                            jour= input (_("SAISIR JOUR")+ f"{nom} {prenom} : ")
                            if int (jour)> 31 or int (jour)< 1:
                                os.system ("cls")
                                print (_("Valeur impossible"))
                                jour= ""
                            else:
                                os.system ("cls")
                                print (_("Jour ajouté"))
                                for nbrV1, nbrV2 in nbr.items ():
                                    if jour== nbrV1:
                                        jour= nbrV2
                                        break
                                break
                    if mois== "":
                        while True:
                            mois= input (_("SAISIR MOIS")+ f"{nom} {prenom} : ")
                            if int (mois)> 12 or int (mois)< 1:
                                os.system ("cls")
                                print (_("Valeur impossible"))
                                mois= ""
                            else:
                                os.system ("cls")
                                print (_("Mois ajouté"))
                                for nbrV1, nbrV2 in nbr.items ():
                                    if mois== nbrV1:
                                        mois= nbrV2
                                        break
                                break
                    if annee== "":
                        while True:
                            annee= input (_("SAISIR ANNEE")+ f"{nom} {prenom} : ")
                            if int (annee)> 2100 or int (annee)< 1900:
                                os.system ("cls")
                                print (_("Valeur impossible"))
                                annee= ""
                            else:
                                os.system ("cls")
                                print (_("Année ajoutée"))
                                break
                    else:
                        print (_("Date de naissance déjà ajoutée"))
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "4":
                if nom!= "" and prenom!= "":
                    if num== "":
                        num= input (_("SAISIR NUM")+ f"{nom} {prenom} : ")
                        if len (num)!= 9 and len (num)!= 10:
                            os.system ("cls")
                            print (_("Valeur impossible"))
                            num= ""
                        elif num.isdigit ()== False:
                            os.system ("cls")
                            print (_("Valeur impossible"))
                            num= ""
                        else:
                            if len (num)== 9: num= "0"+ num
                            os.system ("cls")
                            print (_("Numéro de téléphone ajouté"))
                    else:
                        print (_("Numéro de téléphone déjà ajouté"))
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "5":
                if nom!= "" and prenom!= "":
                    if email== "":
                        email= input (_("SAISIR EMAIL")+ f"{nom} {prenom} : ")
                        os.system ("cls")
                        print (_("Adresse email ajoutée"))
                    else:
                        print (_("Adresse email déjà ajoutée"))
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "6":
                if nom!= "" and prenom!= "":
                    if annee== "":
                        date= ""
                    else:
                        date= f"{jour}.{mois}.{annee}"
                    choix_favori= input (_("Mettre")+ f"{nom} {prenom}"+ _("en favori : ")).upper ()
                    if choix_favori== _("OUI"):
                        favori= "True"
                    else:
                        favori= "False"
                    nouveau_contact= {"nom": nom, "prenom": prenom, "date": date, "num": num, "email": email, "favori": favori, "groupe": "", "nom_groupe": "", "num_groupe": "", "mbr_groupe": ""}
                    L.append (nouveau_contact)
                    outils.CSV.ecriture_csv (L, F_rep)
                    os.system ("cls")
                    print (nom, prenom+ _("a été crée (contact)"))
                    if favori== "True":
                        print (nom, prenom+ _("est maintenant en favori !"))
                    logging.info (_("_AJOUTER CONTACTS_")+ f"{nom} {prenom}\n")
                    break
                else: print (_("Choix impossible"))
            
            else: print (_("Choix impossible"))
    
    elif choix== "groupes":
        num= 1
        nom= ""
        nbr_mbr= 0
        
        while True:
            L= outils.CSV.lecture_csv (F_rep)
            num_existant= [int(groupe["num_groupe"]) for groupe in L if groupe["num_groupe"].isdigit()]
            while num in num_existant:
                num+= 1
            
            print (_("-AJOUTER : Groupes-"))
            if nom== "":
                print (_("Retour"))
                print (_("-OBLIGATOIRE-"))
                print (_("NOM GROUPES"))
            else:
                print (_("-FACULTATIF-"))
                print (_("MEMBRES GROUPES"))
                print (_("FIN GROUPES"))
            
            choix_ajouter= input (_("Choix")).lower ()
            os.system ("cls")
            
            if choix_ajouter== "0":
                if nom== "": break
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "1":
                if nom== "":
                    nom= input (_("Saisir nom groupe"))
                    if nom!= "":
                        os.system ("cls")
                        print (_("Nom groupe ajouté"))
                        logging.info (_("_AJOUTER GROUPES_")+ nom+ "\n")
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "2":
                if nom!= "":
                    nbr_recherche= False
                    contact= input (_("Saisir le nom ou le prénom du contact à ajouter au groupe")).upper ()
                    os.system ("cls")
                    for contacts in L:
                        nom_c= contacts["nom"]
                        prenom_c= contacts["prenom"].upper ()
                        if contact== nom_c or contact== prenom_c:
                            nbr_recherche= True
                            confirmation_ajouter= input (_("_Ajouter_")+ f" {nom_c} {prenom_c.capitalize()} : ").upper ()
                            if confirmation_ajouter== _("OUI"):
                                nbr_mbr+= 1
                                contacts["groupe"]+= str (num)
                                outils.CSV.ecriture_csv (L, F_rep)
                                logging.info (_("_AJOUTER CONTACT DANS GROUPE_")+ f"{nom_c} {prenom_c.capitalize()}\n")
                                os.system ("cls")
                                print (nom_c, prenom_c.capitalize ()+ _("a été ajouté au groupe")+ nom+ " !\n")
                            else: os.system ("cls")
                    if nbr_recherche== False: print (_("Aucun contact trouvé")+ "\n")
                else: print (_("Choix impossible"))
            
            elif choix_ajouter== "3":
                if nom!= "":
                    g_new = {"nom": "", "prenom": "", "date": "", "num": "", "email": "", "favori": "", "groupe": "", "nom_groupe": nom, "num_groupe": str (num), "mbr_groupe": str (nbr_mbr)}
                    L.append (g_new)
                    outils.CSV.ecriture_csv (L, F_rep)
                    print (_("Le groupe")+ nom+ _("a été crée (groupe)"))
                    break
                else: print (_("Choix impossible"))
            
            else: print (_("Choix impossible"))