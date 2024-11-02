# MODULES NECESSAIRES : pygame, requests
import os
import outils

if os.path.exists("CentreMD_Installer.exe"):
    os.remove("CentreMD_Installer.exe")

base = os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD")
if not os.path.exists(base):
    os.makedirs(base)

F_usr_v1 = "data_usr"

# VERIFICATION TRANSITION v2.0.0 #
F_usr_v2_0_0 = "data_usr.csv"
L_usr_v2_0_0 = outils.lecture_CSV(F_usr_v2_0_0)
if L_usr_v2_0_0:
    outils.transition_v2_0_0()

F_usr = os.path.join(base, "data_usr.csv")
L_usr = outils.lecture_CSV(F_usr)

F_log = os.path.join(base, "data_log.txt")

if __name__ == "__main__":
    if os.path.exists(F_usr):
        L_usr = outils.lecture_usr()
        nbr = 0
        for usr in L_usr:
            nbr += int(usr["nbr"])
        if nbr%5 == 0:
            outils.comparer_version()

    elif os.path.exists(F_usr_v1):
        L_usr = outils.transition_v1(outils.lecture_pickle(F_usr_v1), F_usr)
        os.remove(F_usr_v1)

    else:
        nom = os.getenv("username")
        while True:
            print(" -- Bienvenue ! --\n",
                  "\n J'ai une question pour vous.",
                  f"\n Vous appelez-vous {nom} ?\n",
                  "\n 1. Oui",
                  "\n 2. Non")
            choix = input("\nChoix : ")
            os.system("cls")
            
            if choix == "1":
                break
            elif choix == "2":
                print(" Ah, mince alors, rectifions cela !\n")
                while True:
                    nom = input("Renseignez votre nom ici : ")
                    os.system("cls")
                    while True:
                        print(f" Donc vous vous appelez {nom}.",
                              "\n C'est bien ça ?\n",
                              "\n 1. Oui",
                              "\n 2. Non")
                        choix = input("\nChoix : ")
                        os.system("cls")
                        if choix == "1":
                            break
                        elif choix == "2":
                            break
                        else:
                            print(" Choix impossible...\n")
                    if choix == "1":
                        break
                if choix == "1":
                    break
            else:
                print(" Choix impossible...\n")
        print(f" C'est Super !\n Je suis enchanté de vous rencontrer {nom} !\n")
        
        print(f" -- Bienvenue {nom} ! --\n",
              "\n J'ai une autre question pour vous.",
              "\n Voulez-vous mettre en place un mot de passe ?\n",
              "\n Ce mot de passe sera demandé à chaque fois que",
              "\n vous vous connecterez à votre compte MD",
              "\n\n Alors, voulez-vous le créer ?\n",
              "\n 1. Oui",
              "\n 2. Non")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "1":
            while True:
                mdp = input ("Saisissez votre futur mot de passe : ")
                os.system ("cls")
                
                while True:
                    print (" Pour vous connecter à votre compte,",
                           f"\n vous devrez donc taper \"{mdp}\"\n",
                           "\n Vous confirmez ?\n",
                           "\n 1. Oui"
                           "\n 2. Non")
                    choix = input ("\nChoix : ")
                    os.system("cls")
                
                    if choix == "1":
                        print (" Mot de passe crée !\n")
                        break
                    elif choix == "2":
                        break
                    print(" Choix impossible...\n")
                if choix == "1":
                    break
        else:
            mdp = ""
        
        usr = {"id": "1",
               "nom": nom,
               "mdp": mdp,
               "nbr": "0",
               "version": "2.0.0",
               "rep_md": "0",
               "manager_md": "0",
               "pass_md": "0",
               "musiques_md": "0"}
        
        outils.ecriture_usr(usr)
        print(" Voilà, j'ai fini mon petit questionnaire...\n",
              "\n Profitez bien du Centre MD !\n",
              "\n Et si vous avez besoin d'aide, essayez de taper \"13\".",
              "\n Si je le peux, je vous aiderez !\n")
    
    usr = outils.demarrage()
    while True:
        print(" -- Centre MD --\n",
              "\n 0. Arrêter",
              "\n 1. Se Déconnecter\n",
              "\n 2. Rep MD",
              "\n 3. Manager MD",
              "\n 4. Fonds MD",
              "\n 5. Pass MD",
              "\n 6. Musiques MD",
              "\n 7. Jeux MD",
              "\n\n 8. Options")
        choix = input("\nChoix : ")
        os.system("cls")
        
        if choix == "0":
            from apps.musiques_md.main import F_mus
            if os.path.exists(F_mus):
                L_mus = outils.lecture_CSV(F_mus)
                for musique in L_mus:
                    if musique["etat"] == "True":
                        from apps.musiques_md.lancer_arreter import lancer_arreter
                        lancer_arreter("feur")
                        break
            exit()
        elif choix == "1":
            from apps.musiques_md.main import F_mus
            if os.path.exists(F_mus):
                L_mus = outils.lecture_CSV(F_mus)
                for musique in L_mus:
                    if musique["etat"] == "True":
                        from apps.musiques_md.lancer_arreter import lancer_arreter
                        lancer_arreter("feur")
                        break
            usr = outils.demarrage()
        elif choix == "2":
            outils.ecriture_log("  OUVERTURE : Rep MD\n")
            from apps.rep_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Rep MD\n")
        elif choix == "3":
            outils.ecriture_log("  OUVERTURE : Manager MD\n")
            from apps.manager_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Manager MD\n")
        elif choix == "4":
            outils.ecriture_log("  OUVERTURE : Fonds MD\n")
            from apps.fonds_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Fonds MD\n")
        elif choix == "5":
            outils.ecriture_log("  OUVERTURE : Pass MD\n")
            from apps.pass_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Pass MD\n")
        elif choix == "6":
            outils.ecriture_log("  OUVERTURE : Musiques MD\n")
            from apps.musiques_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Musiques MD\n")
        elif choix == "7":
            outils.ecriture_log("  OUVERTURE : Jeux MD\n")
            from apps.jeux_md.main import main
            main(usr)
            outils.ecriture_log("  FERMETURE : Jeux MD\n")
        elif choix == "8":
            outils.ecriture_log("  OUVERTURE : Options\n")
            outils.options(usr)
            outils.ecriture_log("  FERMETURE : Options\n")
        
        elif choix == "13":
            print(" Bonsoiir !\n",
                  "\n Ici tu vas pouvoir créer des contacts,",
                  "\n écouter de la musique,",
                  "\n jouer à des jeux et bien d'autres choses !\n",
                  "\n Pour commencer, sélectionnez une application en tapant son numéro !\n")
        else:
            print(" Choix impossible...\n")