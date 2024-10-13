import outils
import os

def main(L_pass, usr):
    print("   · Modifier ·\n")
    mdp = input("Saisissez une information sur le mot de passe à modifier : ")
    os.system("cls")
    L_pass_recherche = outils.recherche(L_pass, usr, mdp)
    for mdp in L_pass_recherche:
        while True:
            print(f" Voulez-vous \"{mdp['nom']}\" ?\n",
                  "\n 1. Oui",
                  "\n 2. Non")
            choix = input("\nChoix : ")
            os.system("cls")
            if choix == "1":
                while True:
                    print(f"   · Modifier : {mdp['nom']} ·\n")
                    new_mdp = input(" Saisissez le nouveau mot de passe : ")
                    os.system("cls")
                    while len(new_mdp) < 12:
                        print("Votre mot de passe n'est pas robuste, êtes-vous de vouloir continuer ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            break
                        elif choix == "2":
                            print(f"   · Modifier : {mdp['nom']} ·\n")
                            new_mdp = input(" Saisissez le nouveau mot de passe : ")
                            os.system("cls")
                        else:
                            print(" Choix impossible...\n")
                    if len(new_mdp) <= 40:
                        break
                    print(" Format incorrect ! (40 caractères maximum)\n")
            elif choix == "2":
                break
            else:
                print(" Choix impossible...\n")
            
            if choix == "1":
                break
        
        if choix == "1":
            print(" Mot de passe mis à jour !\n")
            outils.ecriture_log(f"    MODIFIER : {mdp['mdp']} -> new_mdp | {mdp['nom']}\n")
            mdp["mdp"] = new_mdp
            outils.ecriture_pass(L_pass)
            break