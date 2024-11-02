import outils
import os

def main(choix, L_rep, usr):
    if choix == "contacts":
        usr_id = usr["id"]
        id = str(int(usr["rep_md"]) + 1)
        nom = ""
        prenom = ""
        jour = ""
        mois = ""
        annee = ""
        date = ""
        num = ""
        email = ""
        adresse = ""
        note = ""
        
        while True:
            print("   · Ajouter: Contacts ·\n",
                  "\n 0. Retour")
            if nom == "" or prenom == "":
                print("\n   - OBLIGATOIRE -\n",
                      "\n 1. Nom de Famille",
                      "\n 2. Prénom")
            else:
                print("\n   - FACULTATIF -\n",
                      "\n 3. Date de Naissance",
                      "\n 4. Numéro de Téléphone",
                      "\n 5. Adresse Email",
                      "\n 6. Adresse de Domicile",
                      "\n 7. Notes Additionnelles\n",
                      "\n8. Finaliser le contact !")
            
            choix = input("\nChoix : ")
            os.system("cls")
            
            if choix == "0":
                if nom != "" and prenom != "":
                    while True:
                        print(" Souhaitez-vous quitter ? (les données seront perdues)\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            test = True
                            break
                        elif choix == "2":
                            break
                        else:
                            print(" Choix impossible...\n")
                if test:
                    print (" Action annulée...\n")
                    return
            
            if nom == "" or prenom == "":
                if choix == "1":
                    if nom == "":
                        print ("   · Ajouter: Contacts ·\n")
                        nom = input ("Saisissez le nom de famille du contact : ").upper ()
                        os.system ("cls")
                        if nom == "":
                            print(" Action annulée...\n")
                        else:
                            print (f" Le nom de famille \"{nom}\" à été ajouté au contact !\n")
                    else:
                        print (" Nom de famille déjà renseigné...\n")
                elif choix == "2":
                    if prenom == "":
                        print("   · Ajouter: Contacts ·\n")
                        prenom = input("Saisissez le prénom du contact : ").capitalize ()
                        os.system("cls")
                        if prenom == "":
                            print(" Action annulée...\n")
                        else:
                            print(f" Le prénom \"{prenom}\" à été ajouté au contact !\n")
                    else:
                        print(" Prénom déjà renseigné...\n")
                
                elif choix == "13":
                    print(" Bienvenue dans l'onglet de création de contacts !\n"
                          "\n Ici, vous pouvez créer des contacts afin d'enrichir votre répertoire.",
                          "\n Pour commencer, vous devez obligatoirement ajouter :\n"
                          "\n - Le nom de famille du contact (en tapant \"1\")",
                          "\n - Le prénom du contact (en tapant \"2\")\n",
                          "\n Je vous laisse essayer par vous même !\n")
                else:
                    print (" Choix impossible...\n")
            
            else:
                if choix == "3":
                    if jour == "" or mois == "" or annee == "":
                        if jour == "":
                            print("   · Ajouter: Contacts ·\n")
                            while True:
                                jour = input(f"Saisissez le jour de naissance de {nom} {prenom} : ")
                                os.system("cls")
                                if jour.isdigit() and 0 < len(jour) <= 2 and 0 < int(jour) <= 31:
                                    if len(jour) == 1:
                                        jour = "0" + jour
                                    print(f" Le jour de naissance \"{jour}\" à été ajouté au contact !\n")
                                    break
                                print (" Format incorrect !\n")
                        if mois == "":
                            print("   · Ajouter: Contacts ·\n")
                            while True:
                                mois = input(f"Saisissez le mois de naissance de {nom} {prenom} : ")
                                os.system("cls")
                                if mois.isdigit() and 0 < len(mois) <= 2 and 0 < int(mois) <= 12:
                                    if len(mois) == 1:
                                        print(mois)
                                        mois = "0" + mois
                                    print(f" Le mois de naissance \"{mois}\" à été ajouté au contact !\n")
                                    break
                                print (" Format incorrect !\n")
                        if annee == "":
                            print ("   · Ajouter: Contacts ·\n")
                            while True:
                                annee = input(f"Saisissez l'année de naissance de {nom} {prenom} : ")
                                os.system("cls")
                                if annee.isdigit() and len(annee) == 4 and 1900 <= int(annee) <= 2100:
                                    date = f"{jour}/{mois}/{annee}"
                                    print(f" La date de naissance \"{date}\" à été ajouté au contact !\n")
                                    break
                                print(" Format incorrect !\n")
                        else:
                            print(" Date de naissance déjà renseignée...\n")
                elif choix == "4":
                    if num == "":
                        print("   · Ajouter: Contacts ·\n")
                        while True:
                            num = input(f"Saisissez le numéro de téléphone de {nom} {prenom} : ")
                            os.system("cls")
                            if num.isdigit() and 0 < len(num) >= 10:
                                if len (num) == 9:
                                    num = "0" + num
                                print (f" Le numéro de téléphone \"{num}\" à été ajouté au contact !\n")
                                break
                            print(" Format incorrect !\n")
                    else:
                        print(" Numéro de téléphone déjà renseigné...\n")
                elif choix == "5":
                    if email == "":
                        print("   · Ajouter: Contacts ·\n")
                        while True:
                            email = input(f"Saisissez l'adresse email de {nom} {prenom} : ")
                            os.system("cls")
                            if "@" in email:
                                print(f" L'adresse email \"{email}\" à été ajouté au contact !\n")
                                break
                            print(" Format incorrect !\n")
                    else:
                        print(" Adresse email déjà renseignée...\n")
                elif choix == "6":
                    if adresse == "":
                        print("   · Ajouter: Contacts ·\n")
                        while True:
                            rue = input(f"Saisissez le numéro ainsi que le nom de la rue dans laquelle réside {nom} {prenom} : ")
                            os.system("cls")
                            if rue == "":
                                print(" Format incorrect !\n")
                            else:
                                break
                        print("   · Ajouter: Contacts ·\n")
                        while True:
                            code_postal = input(f"Saisissez le code postal dans lequel réside {nom} {prenom} : ")
                            os.system("cls")
                            if code_postal.isdigit() and 0< len(code_postal) <= 5:
                                break
                            print(" Format incorrect !\n")
                        print("   · Ajouter: Contacts ·\n")
                        while True:
                            ville = input(f"Saisissez le nom de la ville dans laquelle réside {nom} {prenom} : ")
                            os.system("cls")
                            if ville == "":
                                print(" Format incorrect !\n")
                            else:
                                break
                        adresse = f"{rue} {code_postal} {ville}"
                        print(f" L'adresse de domicile \"{adresse}\" à été ajouté au contact !\n")
                    else:
                        print(" Adresse de domicile déjà renseignée...\n")
                elif choix == "7":
                    print("   · Ajouter: Contacts ·\n")
                    if note == "":
                        note = input(f"Saisissez une note à conserver à propos de {nom} {prenom} : ")
                    else:
                        note += "|" + input (f"Saisissez une note supplémentaire à conserver à propos de {nom} {prenom} : ")
                    os.system ("cls")
                    if note == "":
                        print(" Action annulée...\n")
                    else:
                        print (f" La note à été ajouté au contact !\n")
                elif choix == "8":
                    while True:
                        print("   · Ajouter: Contacts ·\n",
                             f"\n Souhaitez-vous ajouter {nom} {prenom} aux favoris ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            favori = "True"
                            break
                        elif choix == "2":
                            favori = "False"
                            break
                        print (" Choix impossible...\n")
                    
                    usr["rep_md"] = str(int(usr["rep_md"]) + 1)
                    contact = {"usr_id": usr_id, "id": id, "favori": favori, "nom": nom, "prenom": prenom, "date": date, "num": num, "email": email, "adresse": adresse, "notes": note, "groupes": "", "nom_groupe": "", "nbr_groupe": ""}
                    L_rep.append (contact)
                    outils.ecriture_usr(usr)
                    outils.ecriture_rep(L_rep)
                    
                    print(f"{nom} {prenom} a été ajouté à la liste des contacts !\n")
                    outils.ecriture_log(f"    AJOUTER CONTACTS : {nom} {prenom}\n")
                    return
                elif choix == "13":
                    print(" Vous arrivez au terme de la création de votre contact...",
                          "\n On aura vécu de bonnes aventures,"
                          "\n mais toutes les aventures ont une fin...\n")
                else:
                    print(" Choix impossible...\n")
    
    elif choix == "groupes":
        usr_id = usr["id"]
        id = str(int(usr["rep_md"]) + 1) 
        nom = ""
        nbr = 0
        
        while True:
            print("   · Ajouter: Contacts ·\n",
                  "\n 0. Retour")
            if nom == "":
                print("\n   - OBLIGATOIRE -\n",
                      "\n 1. Nom du Groupe")
            else:
                print("\n   - FACULTATIF -\n",
                      "\n 2. Ajout de contacts",
                      "\n\n3. Finaliser le groupe !")
            
            choix = input("\nChoix : ")
            os.system("cls")
            
            if choix == "0":
                if nom != "":
                    while True:
                        print(" Souhaitez-vous quitter ? (les données seront perdues)\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            test = True
                        elif choix == "2":
                            break
                        else:
                            print(" Choix impossible...\n")
                if test:
                    print (" Action annulée...\n")
                    return
            
            if nom == "":
                if choix == "1":
                    print ("   · Ajouter: Groupes ·\n")
                    nom = input ("Saisissez le nom du groupe : ")
                    os.system ("cls")
                    if nom:
                        print (f" Le nom de famille \"{nom}\" à été ajouté au contact !\n")
                    else:
                        print(" Action annulée...\n")
                elif choix == "13":
                    print(" Bienvenue dans la création de groupes !",
                          "\n C'est ici que vous allez pouvoir mettre en relation différents contacts.",
                          "\n\n Pour commencer, tapez 1 !\n")
                else:
                    print(" Choix impossible...\n")
            
            else:
                if choix == "2":
                    print("   · Ajouter: Groupes ·\n")
                    contact = input(" Saisissez une information à propos du contact à ajouter : ")
                    contacts = outils.recherche(L_rep, usr, contact)
                    if contacts == []:
                        os.system("cls")
                        print(" Aucun contact trouvé !\n")
                    for contact in contacts:
                        if id in contact["groupes"]:
                            break
                        if contact["prenom"] == "None":
                            break
                        os.system("cls")
                        while True:
                            print(f" Souhaitez-vous ajouter {contact['nom']} {contact['prenom']} au groupe ?\n",
                                   "\n 1. Oui",
                                   "\n 2. Non")
                            choix = input("\nChoix : ")
                            os.system("cls")
                            if choix == "1":
                                contact["groupes"] += id
                                nbr += 1
                                print(f" Le contact {contact['nom']} {contact['prenom']} à été ajouté au groupe !\n")
                                break
                            elif choix == "2":
                                break
                            elif choix == "13":
                                print(" Vous pensez vraiment que c'est utile ici ???\n")
                            else:
                                print(" Choix impossible...\n")
                elif choix == "3":
                    while True:
                        print("   · Ajouter: Groupes ·\n",
                             f"\n Souhaitez-vous ajouter le groupe {nom} aux favoris ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            favori = "True"
                            break
                        elif choix == "2":
                            favori = "False"
                            break
                        print (" Choix impossible...\n")
                    usr["rep_md"] = str(int(usr["rep_md"]) + 1)
                    contact = {"usr_id": usr_id, "id": id, "favori": favori, "nom": "", "prenom": "", "date": "", "num": "", "email": "", "adresse": "", "notes": "", "groupes": "", "nom_groupe": nom, "nbr_groupe": str(nbr)}
                    L_rep.append (contact)
                    outils.ecriture_usr(usr)
                    outils.ecriture_rep(L_rep)
                    
                    print(f"Le groupe \"{nom}\" a été ajouté à la liste des groupes !\n")
                    outils.ecriture_log(f"    AJOUTER GROUPES : {nom}\n")
                    return
                elif choix == "13":
                    print(" Tu y est presque !",
                          "\n Maintenant vous n'avez plus qu'à ajouter des contacts au nouveau groupe ou à le finaliser.",
                          "\n\n Pour terminer la création de ton groupe, tapez 3 !\n")
                else:
                    print(" Choix impossible...\n")
    
    else:
        print("ERREUR : Choix impossible.\n")