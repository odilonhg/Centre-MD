import outils
import os
import random

def main(nom, L_rep, usr):
    L_contacts = []
    for contact in L_rep:
        if contact["usr_id"] == usr["id"] and contact["nom"] != "":
            L_contacts.append(contact["prenom"])
    
    if L_contacts:
        contact = random.choice(L_contacts)
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
    while True:
        while True:
            lettre = input("Saisissez une lettre : ")
            os.system("cls")
            if not lettre.isdigit() and len(lettre) == 1:
                break
            print(" Ce n'est pas une lettre !\n")
        
        if lettre == "a" or lettre == "A":
            L_lettres = ["a", "à", "â", "ä", "ã", "á", "å", "æ", "A", "À", "Â", "Ä", "Ã", "Á", "Å", "Æ"]
        elif lettre == "e" or lettre == "E":
            L_lettres = ["e", "è", "é", "ê", "ë", "E", "È", "É", "Ê", "Ë"]
        elif lettre == "i" or lettre == "I":
            L_lettres = ["i", "ì", "í", "î", "ï", "I", "Ì", "Í", "Î", "Ï"]
        elif lettre == "o" or lettre == "O":
            L_lettres = ["o", "ò", "ó", "ô", "õ", "ö", "ø", "O", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø"]
        elif lettre == "u" or lettre == "U":
            L_lettres = ["u", "ù", "ú", "û", "ü", "U", "Ù", "Ú", "Û", "Ü"]
        elif lettre == "c" or lettre == "C":
            L_lettres = ["c", "ç", "C", "Ç"]
        else:
            L_lettres = [lettre.lower(), lettre.upper()]
        
        test = False
        for lettre in L_lettres:
            if lettre in lettres_trouvees:
                print(" Vous avez déjà trouvé cette lettre...\n")
            elif lettre in contact:
                print(f" Bien joué, vous avez trouvé la lettre \"{lettre}\" !\n")
                lettres_trouvees.append(lettre)
                test = True
        
        if not test:
            tentatives_max -= 1
            print (f" Cette lettre n'est pas dans le prénom... Plus que {tentatives_max} tentatives !\n")
        
        contenu = ""
        for lettre in contact:
            if lettre in lettres_trouvees:
                contenu += lettre
            else:
                contenu += "_"
        
        if not "_" in contenu:
            break
        else:
            print(contenu)
    
    nbr_tentatives = -(tentatives_max - 6)
    print(f" Félicitations {nom} !\n",
          f"\n Vous avez trouvé le prénom \"{contact}\"",
          f"\n et il vous restait encore {tentatives_max} tentatives !\n")
    outils.ecriture_log(f"    LE PENDU : {nom} a trouvé \"{contact}\" en seulement {nbr_tentatives} tentatives échouées !\n")
    return