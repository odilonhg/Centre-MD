import outils
import os

def main(L_rep, usr):
    print("   · Modifier ·\n")
    contact = input("Saisissez une information sur le contact / groupe à modifier : ")
    os.system("cls")
    if contact == "":
        print(" Action annulée...\n")
        return
    L_rep_recherche = outils.recherche(L_rep, usr, contact)
    for contact in L_rep_recherche:
        test = False
        if contact["nom"]:
            while True:
                print(f" Voulez-vous modifier {contact['nom']} {contact['prenom']} ?\n",
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
                return modifier_contact(contact, L_rep, usr)
        else:
            while True:
                print(f" Voulez-vous modifier {contact['nom_groupe']} ?\n",
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
                return modifier_groupe(contact, L_rep, usr)

def modifier_contact(contact, L_rep, usr):
    while True:
        print(f"   · Modifier: {contact['nom']} {contact['prenom']} ·\n",
              "\n 0. Retour\n",
              "\n 1. Nom de Famille",
              "\n 2. Prénom",
              "\n 3. Date de Naissance",
              "\n 4. Numéro de Téléphone",
              "\n 5. Adresse Email",
              "\n 6. Adresse de Domicile",
              "\n 7. Notes Additionnelles")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0":
            outils.ecriture_rep(L_rep)
            print(" Contact mis à jour avec succès !\n")
            return
        
        elif choix == "1":
            new_nom = input(f"Saisissez le nouveau nom de famille de {contact['nom']} {contact['prenom']} : ").upper()
            os.system("cls")
            print(" Nom de famille mis à jour !\n")
            outils.ecriture_log(f"    MODIFIER CONTACT : {contact['nom']} -> {new_nom} | {contact['nom']} {contact['prenom']}\n")
            contact["nom"] = new_nom
        elif choix == "2":
            new_prenom = input(f"Saisissez le nouveau prénom de {contact['nom']} {contact['prenom']} : ").capitalize()
            os.system("cls")
            print(" Prénom mis à jour !\n")
            outils.ecriture_log(f"    MODIFIER CONTACT : {contact['prenom']} -> {new_prenom} | {contact['nom']} {contact['prenom']}\n")
            contact["prenom"] = new_prenom
        elif choix == "3":
            while True:
                new_jour = input(f"Saisissez le nouveau jour de naissance de {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_jour.isdigit() and 0 < len(new_jour) <= 2 and 0 < int(new_jour) <= 31:
                    if len(new_jour) == 1:
                        new_jour = "0" + new_jour
                    break
                print(" Format incorrect !\n")
            while True:
                new_mois = input(f"Saisissez le nouveau mois de naissance de {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_mois.isdigit() and 0 < len(new_mois) <= 2 and 0 < int(new_mois) <= 12:
                    if len(new_mois) == 1:
                        new_mois = "0" + new_mois
                    break
                print(" Format incorrect !\n")
            while True:
                new_annee = input(f"Saisissez la nouvelle année de naissance de {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_annee.isdigit() and len(new_annee) == 4 and 1900 < int(new_annee) <= 2100:
                    print(" Date de naissance mise à jour !\n")
                    new_date = f"{new_jour}/{new_mois}/{new_annee}"
                    outils.ecriture_log(f"    MODIFIER CONTACT : {contact['date']} -> {new_date} | {contact['nom']} {contact['prenom']}\n")
                    contact["date"] = new_date
                    break
                print(" Format incorrect !\n")
        elif choix == "4":
            while True:
                new_num = input(f"Saisissez le nouveau numéro de téléphone de {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_num.isdigit() and 0 < len(new_num) <= 10:
                    if len(new_num) == 9:
                        new_num = "0" + new_num
                    print(" Nom de famille mis à jour !\n")
                    outils.ecriture_log(f"    MODIFIER CONTACT : {contact['num']} -> {new_num} | {contact['nom']} {contact['prenom']}\n")
                    contact["num"] = new_num
                    break
                print(" Format incorrect !\n")
        elif choix == "5":
            while True:
                new_email = input(f"Saisissez la nouvelle adresse email de {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if "@" in new_email:
                    print(" Adresse email mise à jour !\n")
                    outils.ecriture_log(f"    MODIFIER CONTACT : {contact['email']} -> {new_email} | {contact['nom']} {contact['prenom']}\n")
                    contact["email"] = new_email
                    break
                print(" Format incorrect !\n")
        elif choix == "6":
            while True:
                new_rue = input(f"Saisissez le nouveau numéro ainsi que le nom de la rue dans laquelle réside {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_rue == "":
                    print(" Format incorrect !\n")
                else:
                    break
            while True:
                new_code_postal = input(f"Saisissez le nouveau code postal dans lequel réside {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_code_postal.isdigit() and 0< len(new_code_postal) <= 5:
                    break
                print(" Format incorrect !\n")
            while True:
                new_ville = input(f"Saisissez le nom de la nouvelle ville dans laquelle réside {contact['nom']} {contact['prenom']} : ")
                os.system("cls")
                if new_ville == "":
                    print(" Format incorrect !\n")
                else:
                    break
            new_adresse = f"{new_rue} {new_code_postal} {new_ville}"
            print(f" Adresse de domicile mise à jour !\n")
            outils.ecriture_log(f"    MODIFIER CONTACT : {contact['adresse']} -> {new_adresse} | {contact['nom']} {contact['prenom']}\n")
            contact["adresse"] = new_adresse
        elif choix == "7":
            if contact["notes"] != "":
                i = 0
                L_note = contact["notes"].split("|")
                for note in L_note:
                    i += 1
                    print(f" {i}. {note}")
                while True:
                    choix = input("Entrez le numéro de la note à supprimer : ")
                    os.system("cls")
                    if choix.isdigit() and 0 <= int(choix) - 1 < len(L_note):
                        del_note = L_note[int(choix)-1]
                        del L_note[int(choix)-1]
                        break
                    print(" Format incorrect !\n")
                contenu = ""
                for note in L_note:
                    if contenu == "":
                        contenu += note
                    else:
                        contenu += "|" + note
                print(f" Notes mise à jour !\n")
                outils.ecriture_log(f"    MODIFIER CONTACT : SUPPRESSION DE LA NOTE \"{del_note}\" | {contact['nom']} {contact['prenom']}\n")
                contact["notes"] = contenu
            else:
                while True:
                    new_note = input(f"Saisissez la note qui sera attribuée à {contact['nom']} {contact['prenom']} : ")
                    os.system("cls")
                    if new_note != "":
                        contact["notes"] = new_note
                        print(f" Notes mise à jour !\n")
                        outils.ecriture_log(f"    MODIFIER CONTACT : AJOUT DE LA NOTE \"{new_note}\" | {contact['nom']} {contact['prenom']}\n")
                        break
                    print(" Format incorrect !\n")
        elif choix == "8":
            print(" Euh, tu t'es cru dans la fonction \"Ajouter\" ?",
                  "\n Ici si tu veux arrêter tu dois simplement retourner en arrière avec 0 !")
        elif choix == "13":
            print(" Franchement je sais pas quoi te dire, essaies de taper 8 pour voir...\n")
        else:
            print(" Choix impossible...\n")

def modifier_groupe(groupe, L_rep, usr):
    while True:
        print(f"   · Modifier: {groupe['nom_groupe']} ·\n",
              "\n 0. Retour\n",
              "\n 1. Nom du Groupe",
              "\n 2. Ajouter un membre dans le Groupe",
              "\n 3. Supprimer un membre du Groupe")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0":
            outils.ecriture_rep(L_rep)
            print(" Groupe mis à jour avec succès !\n")
            return
        
        elif choix == "1":
            new_nom = input(f"Saisissez le nouveau nom du groupe \"{groupe['nom_groupe']}\" : ")
            os.system("cls")
            print(" Nom du groupe mis à jour !\n")
            outils.ecriture_log(f"    MODIFIER GROUPE : {groupe['nom_groupe']} -> {new_nom} | {groupe['nom_groupe']}\n")
            groupe["nom_groupe"] = new_nom
        elif choix == "2":
            contact = input(f"Saisissez une information sur le contact à ajouter au groupe \"{groupe['nom_groupe']}\" : ")
            os.system("cls")
            if contact == "":
                print(" Action annulée...\n")
                return
            L_contact = outils.recherche(L_rep, usr, contact)
            for contact in L_contact:
                if contact["nom"] != "" and groupe["id"] not in contact["groupes"]:
                    test = False
                    while True:
                        print(f" Souhaitez-vous ajouter {contact['nom']} {contact['prenom']} au groupe \"{groupe['nom_groupe']}\" ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        
                        if choix == "1":
                            test = True
                            break
                        elif choix == "2":
                            break
                        elif choix == "13":
                            print(" Qu'est ce que je fais là moi...\n")
                        else:
                            print(" Choix impossible...\n")
                    if test:
                        for contact2 in L_rep:
                            if contact == contact2:
                                contact2["groupes"] += groupe["id"]
                                groupe["nbr_groupe"] = str(int(groupe["nbr_groupe"]) + 1)
                                print(f" Le contact {contact['nom']} {contact['prenom']} a été ajouté au groupe \"{groupe['nom_groupe']}\" !\n")
                                outils.ecriture_log(f"    MODIFIER GROUPE : AJOUT DU MEMBRE \"{contact['nom']} {contact['prenom']}\" | {groupe['nom_groupe']}\n")
        elif choix == "3":
            for contact in L_rep:
                if contact["usr_id"] == usr["id"] and contact["nom"] != "" and groupe["id"] in contact["groupes"]:
                    test = False
                    while True:
                        print(f" Souhaitez-vous supprimer {contact['nom']} {contact['prenom']} du groupe \"{groupe['nom_groupe']}\" ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        
                        if choix == "1":
                            test = True
                            break
                        elif choix == "2":
                            break
                        elif choix == "13":
                            print(" Qu'est ce que je fais là moi...\n")
                        else:
                            print(" Choix impossible...\n")
                    if test:
                        test10 = False
                        test100 = False
                        new_groupes = ""
                        if len(groupe["id"]) == 2:
                            test10 = True
                        elif len(groupe["id"]) == 3:
                            test100 = True
                            
                        i = 0
                        if test10:
                            while i < len(contact["groupes"]) - 1:
                                if contact["groupes"][i]+contact["groupes"][i+1] != groupe["id"]:
                                    new_groupes += contact["groupes"][i]
                                    if i + 1 == len(contact["groupes"]) - 1:
                                        new_groupes += contact["groupes"][i+1]
                                else:
                                    i += 1
                                i += 1
                        elif test100:
                            while i < len(contact["groupes"]) - 2:
                                if contact["groupes"][i]+contact["groupes"][i+1]+contact["groupes"][i+2] != groupe["id"]:
                                    new_groupes += contact["groupes"][i]
                                    if i + 2 == len(contact["groupes"]) - 2:
                                        new_groupes += contact["groupes"][i+1]+contact["groupes"][i+2]
                                else:
                                    i += 2
                                i += 1
                        else:
                            for elm in contact["groupes"]:
                                if elm != groupe["id"]:
                                    new_groupes += elm
                        
                        contact["groupes"] = new_groupes
                        groupe["nbr_groupe"] = str(int(groupe["nbr_groupe"]) - 1)
                        print(f" Le contact {contact['nom']} {contact['prenom']} a été supprimé du groupe \"{groupe['nom_groupe']}\" !\n")
                        outils.ecriture_log(f"    MODIFIER GROUPE : SUPPRESSION DU MEMBRE \"{contact['nom']} {contact['prenom']}\" | {groupe['nom_groupe']}\n")