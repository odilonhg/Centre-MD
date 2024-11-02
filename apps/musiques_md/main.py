import outils
import os

base = os.path.join(os.path.expanduser("~\\AppData\\"), "Local\TeamMD\CentreMD")
F_mus = os.path.join(base, "data_mus.csv")

def main(usr):
    while True:
        if os.path.exists(F_mus):
            L_mus = outils.lecture_CSV(F_mus)
        else:
            print(" Bienvenue dans Musiques MD !\n"
                  "\n Ici, vous pourrez lancer des musiques et enregistrer des morceaux à jouer plus tard.",
                  "\n Tapez \"1\" pour ajouter votre 1ère musique !\n")
            L_mus = []
        print("   · Musiques MD ·\n",
              "\n 0. Retour",
              "\n 1. Ajouter une musique")
        
        test = False
        for musique in L_mus:
            if musique["usr_id"] == usr["id"] and musique.get("etat") == "True":
                test = True
        
        if test:
            print(" 2. Arrêter la musique")
        else:
            print(" 2. Lancer une musique")
        
        choix = input ("\nChoix : ")
        os.system ("cls")
        
        if choix == "0": return
        
        elif choix == "1":
            from apps.musiques_md.ajouter import main
            main(L_mus, usr)
        elif choix == "2":
            from apps.musiques_md.lancer_arreter import main
            main(L_mus, usr)
        
        elif choix == "13":
            print(" Bienvenue dans Musiques MD !\n"
                  "\n Ici, vous pourrez lancer des musiques et enregistrer des morceaux à jouer plus tard.",
                  "\n Tapez \"1\" pour ajouter votre 1ère musique !\n")
        else:
            print(" Choix impossible...\n")