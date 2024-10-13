import outils
import os
from tkinter import filedialog
import shutil

def main(L_mus, usr):
    id = str(int(usr["musiques_md"]) + 1)
    usr["musiques_md"] = str(int(usr["musiques_md"]) + 1)
    F_chemin = filedialog.askopenfilename(title="Trouve une bonne musique",
                                          filetypes=[("Fichiers MP3", "*.mp3"),
                                                     ("Fichiers OGG", "*.ogg"),
                                                     ("Fichiers WAV", "*.wav"),
                                                     ("Tous les fichiers audio", "*.mp3 *.ogg *.wav")])
    if F_chemin != "":
        nom_fichier = os.path.basename (F_chemin)
        chemin_final = os.path.join (os.getcwd (), "audios")
        chemin_final = os.path.join (chemin_final, nom_fichier)
        test = True
        for mus in L_mus:
            if mus["nom"] == nom_fichier:
                test = False
                print(f" Vous avez déjà enregistré \"{mus['nom']}\" dans votre bibliothèque MD !\n")
        if test:
            while True:
                print("   · Ajouter ·\n",
                      f"\n Vous confirmez vouloir ajouter \"{nom_fichier}\" à la liste des musiques ?\n",
                      "\n 1. Oui",
                      "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                if choix == "1":
                    shutil.copy(F_chemin, chemin_final)
                    break
                elif choix == "2":
                    print(" Action annulée...\n")
                    return False
                else:
                    print(" Choix impossible...\n")
            new_mus = {"usr_id": usr["id"], "id": id, "nom": nom_fichier, "chemin": chemin_final, "etat": "False"}
            L_mus.append(new_mus)
            print(f" La musique \"{nom_fichier}\" a été ajouté à votre liste de musiques !\n")
            outils.ecriture_log(f"    AJOUTER : {nom_fichier}\n")
            outils.ecriture_mus(L_mus)
            outils.ecriture_usr(usr)
