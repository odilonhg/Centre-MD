import pickle
import sys
import os
import random
import csv

sortie_console = sys.stdout # Sauvegarde dans une variable la destination "console" des messages
sys.stdout = open (os.devnull, 'w') # Définie la destination des futures messages (ils ne s'afficheront pas dans la console)
import pygame
sys.stdout = sortie_console # Redéfinie la destination des futures messages sur la console

def charger_musique (musique): # Charge la musique pour éviter les rechargement multiples
    pygame.init ()
    pygame.mixer.init ()
    pygame.mixer.music.load (musique)

def duree_musique (musique): return pygame.mixer.Sound (musique).get_length()

def lancer_mp3 (musique):
    charger_musique(musique)
    pygame.mixer.music.play () # Définie où débutera la musique

def couper_mp3 (musique): pygame.mixer.music.stop()

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

def lecture_fichier (fichier):
    with open (fichier, "r") as f:
        return f.read()

pygame.quit()