import outils
import os
import random

def main(L_pass, usr):
    nom = ""
    mdp = ""
    id = usr["id"]
    pass_id = str(int(usr["pass_md"]) + 1)
    usr["pass_md"] = str(int(usr["pass_md"]) + 1)
    while nom == "":
        print("   · Ajouter ·\n")
        nom = input("Saisissez l'intitulé du mot de passe : ")
        os.system("cls")
        if nom == "":
            print(" Format incorrect !\n")
    while mdp == "":
        print("   · Ajouter ·\n",
              "\n Que voulez-vous ?\n",
              "\n 1. Créer vous même votre mot de passe"
              "\n 2. Générer automatiquement un mot de passe robuste")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "1":
            print("   · Ajouter ·\n")
            mdp = input(f"Saisissez le mot de passe assigné à \"{nom}\" : ")
            os.system("cls")
            while len(mdp) < 12:
                print("Votre mot de passe n'est pas robuste, êtes-vous de vouloir continuer ?\n",
                        "\n 1. Oui",
                        "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                if choix == "1":
                    break
                elif choix == "2":
                    print("   · Ajouter ·\n")
                    mdp = input(f"Saisissez le mot de passe assigné à \"{nom}\" : ")
                else:
                    print(" Choix impossible...\n")
        
        elif choix == "2":
            car = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            while True:
                print("   · Ajouter ·\n",
                      "\n Autorisez-vous les caractères spéciaux ?\n",
                      "\n 1. Oui",
                      "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                if choix == "1":
                    car += "&~#{([-|_\^@)=+$]}*%!/:.;?,"
                    break
                elif choix == "2":
                    break
                print(" Choix impossible...\n")
            while True:
                print("   · Ajouter ·\n")
                nbr = input("Saisissez le nombre de caractères que contiendra le mot de passe (de 12 à 40) : ")
                os.system("cls")
                if nbr.isdigit() and 12 <= int(nbr) <= 40:
                    nbr = int(nbr)
                    break
                else:
                    print(" Format incorrect !\n")
            for i in range (nbr):
                mdp += random.choice (car)
        
        else:
            print(" Choix impossible...\n")
    
    mdp_cache = "*" * len(mdp)
    print(f" Le mot de passe pour \"{nom}\" a bien été enregistré !\n")
    outils.ecriture_log(f"    AJOUTER : {nom} | {mdp_cache}")
    L_pass.append({"usr_id": id, "id": pass_id, "nom": nom, "mdp": mdp})
    outils.ecriture_usr(usr)
    outils.ecriture_pass(L_pass)
    return