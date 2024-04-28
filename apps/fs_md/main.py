from outils import lecture_csv, ecriture_csv
import logging
import sys
import time
import os

def fs_md ():
    print("   · FS MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Fonction Spéciale V1.0")
    print (" 2. Fonction Spéciale V2.0")
    print (" 3. Fonction Spéciale V3.0")
    print (" 4. Fonction Spéciale Ultime (BETA)\n")
    
    choice = input ("Choix : ")

    match choice:
        
        case "0":
            return ""
        case "1":
            return fs_v1()
        case "2":
            return fs_v2()
        case "3":
            return fs_v3()
        case "4":
            return fs_ultime()
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        case _:
            return ""

def confirm_action(phrase):
    action = input(f"\nTapez '{phrase}' pour confirmer ou 'non' pour annuler : ").lower()
    if action == phrase:
        return True
    elif action == 'non':
        print('\nAction annulée')
        return False
    else:
        print('\nAction Impossible...')
        return confirm_action()

def fs_v1():
    os.system ("cls")
    logging.info("    LANCEMENT FONCTION SPECIALE: VERSION 1.0 !\n")
    print("Ouverture de \"Fonction Spéciale V1.0\"")
    print("\nATTENTION, cette action est irréversible !!!")

    if confirm_action("oui"):
        print("\nEtes-vous sûr de continuer ??? : ")
        if confirm_action("oui"):
            print("\nDernière chance, si tu es sûr, tape 'je confirme sur l'honneur que je suis sûr de vouloir continuer' : ")
            if confirm_action("je confirme sur l'honneur que je suis sûr de vouloir continuer"):
                print("\nToute dernière chance, tout peut s'arrêter ici, là maintenant, tu en as bien conscience ? (Si tu veux continuer, tape 'oui' : ")
                if confirm_action("oui"):
                    print("\nAu revoir...")
                    return la_fin_v1()
                else:
                    print('\nBalourd...')
                    return fs_md ()
            else:
                print('\nPourquoi faire tout cela pour annuler ???')
                return fs_md ()
        else:
            print('\nTu écris trop vite je crois... courage !')
            return fs_md ()
    else:
        return fs_md ()

def la_fin_v1():
    os.system ("cls")

    print("Les Crédits :")
    print("\nLes Créateurs")
    print("\nGORLAS Maxime")
    print("MESNAGE Dylan")
    print("\nLes Cerveaux")
    print("\nLEMERCIER Guénaël")
    print("Mr MOUCHEL")
    print("\nRemerciement Spécial :")
    print("\nMr MOUCHEL")
    print("\nMerci d'avoir essayé notre programme, maintenant, tous les repertoires ont été réinitialisés !")
    time.sleep(2)
    sys.exit("FERMETURE FORCEE")

def fs_v2():
    os.system ("cls")
    logging.info("    LANCEMENT FONCTION SPECIALE: VERSION 2.0 !\n")
    print("ATTENTION, cette action est irréversible !!!")
    
    if confirm_action("oui"):
        print("\nEtes-vous sûr de continuer ??? : ")
        if confirm_action("oui"):
            print("\nDernière chance, si tu es sûr, tape 'je confirme sur l'honneur que je suis sûr de vouloir continuer' : ")
            if confirm_action("je confirme sur l'honneur que je suis sûr de vouloir continuer"):
                print("\nToute dernière chance, tout peut s'arrêter ici, là maintenant, tu en as bien conscience ? (Si tu veux continuer, tape 'oui' : ")
                if confirm_action("oui"):
                    print("\nAu revoir...")
                    return la_fin_v2()
                else:
                    print('\nBalourd...')
                    return fs_md ()
            else:
                print('\nPourquoi faire tout cela pour annuler ???')
                return fs_md ()
        else:
            print('\nTu écris trop vite je crois... courage !')
            return fs_md ()
    else:
        return fs_md ()

def la_fin_v2():
    import pygame
    pygame.init()
    
    soundtrack = "#audio/the_end.mp3"
    
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.play(start=75)
    
    os.system ("cls")
    print("Les Crédits :\n")

    time.sleep(5)
    print("\nLes Créateurs")

    time.sleep(3)
    print("\nGORLAS Maxime")

    time.sleep(3)
    print("MESNAGE Dylan\n")

    time.sleep(5)
    os.system ("cls")
    print("Les Crédits :\n")
    print("\nLes Cerveaux")

    time.sleep(3)
    print("\nLEMERCIER Guénaël")

    time.sleep(3)
    print("Mr MOUCHEL\n")

    time.sleep(5)
    os.system ("cls")
    print("Les Crédits :\n")
    print("\nRemerciements Spéciaux")

    time.sleep(3)
    print("\nMr MOUCHEL")

    time.sleep(3)
    print("Toi, qui as essayé notre répertoire !")

    time.sleep(5)
    os.system ("cls")
    print("Merci d'avoir essayé notre programme, le répertoire est à présent réinitialisé !")

    time.sleep(5)
    sys.exit("FERMETURE FORCEE")

def fs_v3():
    os.system ("cls")
    logging.info("    TENTATIVE DE LANCEMENT: FONCTION SPECIALE VERSION 3.0 !\n")
    print("ERREUR CRITIQUE !")
    print("LA VERSION 3.0 EST TROP NULLE, ELLE NE PEUT ETRE LANCEE !\n")
    from main import choix
    return choix()

def fs_ultime():
    os.system ("cls")
    logging.info("    LANCEMENT FONCTION SPECIALE: VERSION ULTIME 0.1 !\n")

    print("-- Une Fin Spéciale --\n")
    time.sleep(2)
    print("Félicitations ! Tu as parcouru tout le répertoire de contacts.")
    time.sleep(3)
    print("\nMais ce n'est pas la fin de l'aventure...")
    print("Du moins pas encore...")
    time.sleep(2)
    print("\nPrépare-toi pour une histoire interactive !")
    time.sleep(4)
    
    os.system ("cls")
    print("Bienvenue sur la planète Globul")
    print("Quel est ton nom jeune héros ? ")
    nom = input("Ton nom : ").capitalize()
    os.system ("cls")
    time.sleep(2)
    print(f"Le grand et fort héros {nom} décida de partir à la découverte de cette planète !")
    time.sleep(3)
    print("Il courut dans une grande forêt à proximité de son lieu d'atterrissage.")
    time.sleep(2)
    print("Mais où doit-il aller exactement ?")
    time.sleep(2)
    os.system ("cls")
    print("Choisis une direction pour continuer :\n")
    print("1. Gauche")
    print("2. Droite")
    print()
    choix = input("Choix : ")
    
    if choix == "1":
        os.system ("cls")
        print("Il choisit de tourner à gauche...")
        time.sleep(2)
        print(f"\n{nom} rencontre un magicien !")
        time.sleep(2)
        print("\nMagicien: \"Bonjour jeune héros, je cherche Modyle, reine de Globul...")
        time.sleep(3)
        print(f"\nMais {nom} ne sait pas où elle pourrait se situer.")
        time.sleep(3)
        print("\nMagicien: Je sais ! Suis-moi et on pourra peut-être la retrouver !")
        time.sleep(3)
        print("\nLe magicien te propose deux chemins différents :")
        time.sleep(2)
        os.system ("cls")
        print("1. Le chemin de la forêt enchantée")
        print("2. Le chemin des montagnes escarpées\n")
        choix_magicien = input("Choisis ton chemin (1 ou 2) : ")
        
        if choix_magicien == "1":
            os.system ("cls")
            print(f"{nom} décide de suivre le chemin de la forêt enchantée...")
            time.sleep(2)
            print("\nVous entrez dans la forêt et vous sentez une atmosphère magique vous envelopper...")
            time.sleep(3)
            print(f"\n{nom} et le magicien continuent leur quête à travers la forêt.")
            time.sleep(3)
            print("\nMais le Répertoire MD commence à disparaître...")
            time.sleep(3)
            print("Le magicien disparaît également.")
            time.sleep(2)
            os.system ("cls")
            print(f"Tu disparaîs aussi...")
            time.sleep(5)
            
        elif choix_magicien == "2":
            time.sleep(2)
            print(f"{nom} décide de suivre le chemin des montagnes escarpées...")
            time.sleep(2)
            print("\nLa montée est difficile mais vous continuez à grimper courageusement...")
            time.sleep(3)
            print(f"\n{nom} et le magicien progressent dans les montagnes en quête de la reine.")
            time.sleep(3)
            os.system ("cls")
            print("FIN.")
            time.sleep(5)
            
        else:
            os.system ("cls")
            print(f"{nom} n'a pas fait de choix et reste perplexe...")
            time.sleep(2)
            print("\nLe magicien décide de prendre la direction du chemin de la forêt enchantée.")
            time.sleep(3)
            print(f"\n{nom} reste immobile et finit par mourir de faim.")
            time.sleep(3)
            os.system ("cls")
            print("FIN. (vraiment nulle...)")
            time.sleep(5)
            
    elif choix == "2":
        os.system ("cls")
        print(f"{nom} choisit de tourner à droite...")
        time.sleep(2)
        print(f"\n{nom} croise une bête très dangereuse !")
        time.sleep(3)
        print("\nC'est Marine Le Pen (elle est de droite tout ça)")
        time.sleep(3)
        os.system ("cls")
        print("Veux-tu fuir ?\n")
        reponse = input("Oui ou Non : ").lower()
        
        if reponse == "oui":
            os.system ("cls")
            print(f"{nom} a décidé de fuir...")
            time.sleep(2)
            print("\nMais Marine est plus rapide !")
            time.sleep(3)
            print("\nElle rattrape {nom}.")
            time.sleep(3)
            os.system ("cls")
            print("FIN. (tu finis en esclavage)")
            time.sleep(5)

        else:
            os.system ("cls")
            print(f"{nom} a décidé de ne pas fuir...")
            time.sleep(3)
            os.system ("cls")
            print("FIN. (Il est mort)")
            time.sleep(5)
    
    else:
        os.system ("cls")
        print(f"{nom} a hésité et n'as pas choisi de direction...")
        time.sleep(2)
        print(f"\n{nom} reste planté dans cette forêt sans même penser à respirer...")
        time.sleep(5)
        os.system ("cls")
        print("FIN... (Il est décédé)")
        time.sleep(5)
    
    os.system ("cls")
    print("WOAW, ton histoire était... pas ouf...")
    time.sleep(3)
    print("\nLe répertoire sera maintenant réinitialisé...")
    time.sleep(3)
    os.system ("cls")
    print("...3")
    time.sleep(1)
    os.system ("cls")
    print("...2")
    time.sleep(1)
    os.system ("cls")
    print("...1")
    time.sleep(1)
    os.system ("cls")
    print("-- Réinitialisation terminée ! --")
    
    time.sleep(3)
    sys.exit("FERMETURE FORCEE")