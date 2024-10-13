import outils
import os
import pygame
import threading
os.system("cls")

def main(L_mus, usr):
    test = False
    for musique in L_mus:
        if musique["usr_id"] == usr["id"] and musique.get("etat") == "True":
            test = True
    
    if not test:
        contenu = ""
        for musique in L_mus:
            if musique["usr_id"] == usr["id"]:
                contenu += f" {musique['id']}. {musique['nom']}\n "
        if contenu != "":
            print("   · Lancer ·\n\n", contenu)
            choix = input("Choix : ")
            os.system("cls")
            
            for musique in L_mus:
                if choix == musique["id"] and musique["usr_id"] == usr["id"]:
                    musique["etat"] = "True"
                    outils.ecriture_mus(L_mus)
                    outils.ecriture_log(f"    LANCER : {musique['nom']}\n")
                    lancer_arreter(L_mus, musique)
        else:
            print(" Vous n'avez ajouté aucune musique pour le moment !\n")
    else:
        for musique in L_mus:
            if musique["usr_id"] == usr["id"] and musique["etat"] == "True":
                musique["etat"] = "False"
        outils.ecriture_mus(L_mus)
        outils.ecriture_log(f"    ARRETER : {musique['nom']}\n")
        lancer_arreter(L_mus)

def lancer_arreter(L_mus, musique = {"etat": "False"}):
    global stop_mp3
    if musique["etat"] == "True":
        stop_mp3 = False
        pygame.mixer.init ()
        pygame.mixer.music.load (musique["chemin"])
        pygame.mixer.music.play ()
        

        def verifier_musique ():
            while not stop_mp3:
                if not pygame.mixer.music.get_busy ():
                    pygame.mixer.music.play ()
                pygame.time.Clock().tick (10)
        
        threading.Thread (target = verifier_musique, daemon = True).start ()
    
    else:
        stop_mp3 = True
        try:
            pygame.mixer.music.stop()
        except:
            pygame.mixer.init()
            pygame.mixer.music.stop()