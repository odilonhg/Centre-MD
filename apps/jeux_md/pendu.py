import outils
import os
import random

def main(nom, L_rep, usr):
    L_contacts = []
    for contact in L_rep:
        if contact["usr_id"] == usr["id"] and contact["nom"] != "":
            L_contacts.append(contact["prenom"])
    
    if L_contacts:
        contact_affichage = random.choice(L_contacts)
        contact = contact_affichage.lower()
    else:
        print(" Vous ne pouvez pas jouer au Pendu pour le moment !",
              "\n Revenez après avoir créé au moins un contact.",
              "\n Pour ce faire, retournez dans le Centre MD,",
              "\n puis accédez au Rep MD et faites \"Ajouter\"",
              "\n pour créer votre 1er contact !\n")
        return
    
    print("   · Le Pendu ·\n")
    tentatives_max = 6
    lettres_trouvees = []
    lettres_utilisees = []
    while True:
        test_lettre_utilisee = False
        while True:
            lettre = input("Saisissez une lettre : ").lower()
            os.system("cls")
            if not lettre.isdigit() and len(lettre) == 1:
                if lettre not in lettres_utilisees:
                    lettres_utilisees.append(lettre)
                else:
                    test_lettre_utilisee = True
                break
            print(" Ce n'est pas une lettre !\n")
        
        if lettre == "a":
            L_lettres = ["a", "à", "â", "ä", "ã", "á", "å", "æ", "A", "À", "Â", "Ä", "Ã", "Á", "Å", "Æ"]
        elif lettre == "e":
            L_lettres = ["e", "è", "é", "ê", "ë", "E", "È", "É", "Ê", "Ë"]
        elif lettre == "i":
            L_lettres = ["i", "ì", "í", "î", "ï", "I", "Ì", "Í", "Î", "Ï"]
        elif lettre == "o":
            L_lettres = ["o", "ò", "ó", "ô", "õ", "ö", "ø", "O", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø"]
        elif lettre == "u":
            L_lettres = ["u", "ù", "ú", "û", "ü", "U", "Ù", "Ú", "Û", "Ü"]
        elif lettre == "c":
            L_lettres = ["c", "ç", "C", "Ç"]
        else:
            L_lettres = [lettre.lower(), lettre.upper()]
        
        
        if not test_lettre_utilisee:
            test = False
            for lettre in L_lettres:
                if lettre in lettres_trouvees:
                    print(" Vous avez déjà trouvé cette lettre...")
                elif lettre in contact:
                    print(f" Bien joué, vous avez trouvé la lettre \"{lettre}\" !")
                    lettres_trouvees.append(lettre)
                    test = True
            
            if not test:
                tentatives_max -= 1
                print (f" Cette lettre n'est pas dans le prénom... Plus que {tentatives_max} tentatives !")
        else:
            print(" Cette lettre a déjà été utilisée...")
        
        contenu = ""
        for i in range(len(contact)):
            if contact[i] in lettres_trouvees:
                contenu += contact_affichage[i]
            else:
                contenu += "_"
        
        if not "_" in contenu:
            break
        elif tentatives_max == 0:
            os.system("cls")
            print(f" Dommage {nom}...\n",
                  f"\n Vous n'avez pas trouvé le prénom \"{contact_affichage}\"...\n",
                  "\n  ------  ",
                  "\n  |    0  ",
                  "\n  |    |  ",
                  "\n  |   / \ ",
                  "\n  |       ",
                  "\n -------  \n",)
            outils.ecriture_log(f"    LE PENDU : {nom} n'a pas trouvé \"{contact_affichage}\"...\n")
            return
        else:
            if tentatives_max == 6:
                print(f"\nLettres utilisées : {lettres_utilisees}",
                      f"\nTentatives restantes : {tentatives_max}\n",
                      f"\nPrénom à trouver : {contenu}\n")
            elif tentatives_max == 5:
                print("\n          " + f"Lettres utilisées : {lettres_utilisees}",
                      "\n          " + f"Tentatives restantes : {tentatives_max}",
                      "\n          ",
                      "\n          ",
                      "\n          ",
                      "\n -------  ",
                     f"\nPrénom à trouver : {contenu}\n")
            elif tentatives_max == 4:
                print("\n          " + f"Lettres utilisées : {lettres_utilisees}",
                      "\n  |       " + f"Tentatives restantes : {tentatives_max}",
                      "\n  |       ",
                      "\n  |       ",
                      "\n  |       ",
                      "\n -------  ",
                     f"\nPrénom à trouver : {contenu}\n")
            elif tentatives_max == 3:
                print("\n  ------  " + f"Lettres utilisées : {lettres_utilisees}",
                      "\n  |       " + f"Tentatives restantes : {tentatives_max}",
                      "\n  |       ",
                      "\n  |       ",
                      "\n  |       ",
                      "\n -------  ",
                     f"\nPrénom à trouver : {contenu}\n")
            elif tentatives_max == 2:
                print("\n  ------  " + f"Lettres utilisées : {lettres_utilisees}",
                      "\n  |    0  " + f"Tentatives restantes : {tentatives_max}",
                      "\n  |       ",
                      "\n  |       ",
                      "\n  |       ",
                      "\n -------  ",
                     f"\nPrénom à trouver : {contenu}\n")
            elif tentatives_max == 1:
                print("\n  ------  " + f"Lettres utilisées : {lettres_utilisees}",
                      "\n  |    0  " + f"Tentative restante : {tentatives_max}",
                      "\n  |    |  ",
                      "\n  |       ",
                      "\n  |       ",
                      "\n -------  ",
                     f"\nPrénom à trouver : {contenu}\n")
    
    nbr_tentatives = -(tentatives_max - 6)
    os.system("cls")
    print(f" Félicitations {nom} !\n",
          f"\n Vous avez trouvé le prénom \"{contact_affichage}\"",
          f"\n et il vous restait encore {tentatives_max} tentatives !\n")
    outils.ecriture_log(f"    LE PENDU : {nom} a trouvé \"{contact_affichage}\" en seulement {nbr_tentatives} tentatives échouées !\n")
    return