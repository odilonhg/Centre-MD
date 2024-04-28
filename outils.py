from mutagen.mp3 import MP3
import pickle
import sys
import os
import random
import subprocess
import csv

def duree_musique (musique):
    audio = MP3(musique)
    duree_sec = int(audio.info.length)
    return duree_sec

def lancer_mp3 (chemin_musique):
    
    original_stdout = sys.stdout # Sauvegarde dans une variable la destination "console" des messages
    sys.stdout = open(os.devnull, 'w') # Définie la destination des futures messages (ils ne s'afficheront pas dans la console)
    import pygame
    pygame.init ()
    soundtrack = chemin_musique
    pygame.mixer.music.load (soundtrack)
    duree = duree_musique (chemin_musique)
    pygame.mixer.music.play (start = random.randint(1, duree - 60)) # Définie où débutera la musique
    sys.stdout = original_stdout # Redéfinie la destination des futures messages sur la console

def couper_mp3 (chemin_musique):
    
    original_stdout = sys.stdout # Sauvegarde dans une variable la destination "console" des messages
    sys.stdout = open(os.devnull, 'w') # Définie la destination des futures messages (ils ne s'afficheront pas dans la console)
    import pygame
    pygame.init()
    soundtrack = chemin_musique
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.stop()
    sys.stdout = original_stdout # Redéfinie la destination des futures messages sur la console

import os
import subprocess

def lecture_pickle (fichier): # Permet de lire un fichier en utilisant le module pickle
    
    try:
        with open (fichier, "rb") as f:
            liste = pickle.load (f)
        
    except: liste = []
    
    finally: return liste

def ecriture_pickle (liste, fichier): # Permet d'écrire des données sur un fichier en utilisant le module pickle
    
    with open (fichier, "wb") as f:
        pickle.dump (liste, f)

def lecture_csv(fichier, delimiter = ";"):
    liste=[]
    
    try:
        with open (fichier, "r") as csvfile:
            cles=csvfile.readline().strip().split(delimiter)
            
            for ligne in csvfile:
                datas=ligne.strip().split(delimiter)
                liste.append(dict(zip(cles,datas)))
            
    except:
        return []
    
    return liste

def ecriture_csv(liste, fichier, delimiter = ";"):
    
    with open (fichier, "w") as csvfile:
        ligneDesc = ";".join(liste[0].keys()) + "\n"
        csvfile.write (ligneDesc)
        
        for cle in range(len(liste)):
            ligne = ";".join(liste[cle].values()) + "\n"
            csvfile.write (ligne)