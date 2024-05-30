from logging import info
from os import system
from sys import exit
from time import sleep

def fonctions_md ():
    print("   · FS MD ·\n")
    
    print (" 0. Retour")
    print (" 1. Fonction Spéciale V1.0")
    print (" 2. Fonction Spéciale V2.0")
    print (" 3. Fonction Spéciale Ultime (BETA)\n")
    
    choice = input ("Choix : ")

    match choice:
        
        case "0": return
        case "1": return fs_v1()
        case "2": return fs_v2()
        case "3": return fs_ultime()
        case _:   return

def confirm_action(cle):
    action = input(f"\nTapez \"{cle}\" pour continuer ou \"non\" pour annuler : ").lower ()
    if action == cle.lower (): return True
    elif action == "non": return False
    else:
        print("\nAction impossible...")
        return confirm_action()

def fs_v1():
    system ("cls")
    info ("    LANCEMENT FONCTION SPECIALE: VERSION 1.0 !\n")
    print ("Ouverture de \"Fonction Spéciale V1.0\"")
    print ("\nATTENTION, cette action est irréversible !!!")

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
                    print("\nBalourd...")
                    return fs_md ()
            else:
                print("\nPourquoi faire tout cela pour annuler ???")
                return fs_md ()
        else:
            print("\nTu écris trop vite je crois... courage !")
            return fs_md ()
    else:
        return fs_md ()

def la_fin_v1():
    system ("cls")

    print("Les Crédits :")
    print("\nLes Créateurs")
    print("\nGORLAS Maxime")
    print("MESNAGE Dylan")
    print("\nLes Cerveaux")
    print("\nLEMERCIER Guénaël")
    print("Mr MOUCHEL")
    print("\nRemerciement Spécial :")
    print("\nMr MOUCHEL")
    print("\nMerci d'avoir essayé notre programme, il va maintenant s'arrêter !")
    sleep (2)
    exit (0)

def fs_v2():
    system ("cls")
    info("    LANCEMENT FONCTION SPECIALE: VERSION 2.0 !\n")
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
    
    soundtrack = "audios/the_end.ogg"
    
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.play()
    
    system ("cls")
    print("Les Crédits :\n")

    sleep (5)
    print("\nLes Créateurs")

    sleep (3)
    print("\nGORLAS Maxime")

    sleep (3)
    print("MESNAGE Dylan\n")

    sleep (5)
    system ("cls")
    print("Les Crédits :\n")
    print("\nLes Cerveaux")

    sleep (3)
    print("\nLEMERCIER Guénaël")

    sleep (3)
    print("Mr MOUCHEL\n")

    sleep (5)
    system ("cls")
    print("Les Crédits :\n")
    print("\nRemerciements Spéciaux")

    sleep (3)
    print("\nMr MOUCHEL")

    sleep (3)
    print("Toi, qui as essayé notre répertoire !")

    sleep (5)
    system ("cls")
    print("Merci d'avoir essayé notre programme, il va maintenant s'arrêter !")

    sleep (10)
    exit (0)

def fs_ultime():
    system ("cls")
    info ("    LANCEMENT FONCTION SPECIALE: VERSION ULTIME 0.1 !\n")

    print("-- Une Fin Spéciale --\n")
    sleep (2)
    print("-- Félicitations ! --\n\n Tu as parcouru tout le répertoire de contacts.")
    sleep (3)
    print("\nMais ce n'est pas la fin de l'aventure...")
    print("Du moins pas encore...")
    sleep (2)
    print("\nPrépare-toi pour une histoire interactive !")
    sleep (4)
    
    system ("cls")
    print("Quel est ton nom jeune héros ?\n")
    nom = input ("Ton nom : ")
    system ("cls")
    print("Bienvenue sur la planète Globul !\n")
    sleep (2)
    print(f"Le grand et fort héros {nom} décida de partir à la découverte de cette planète !")
    sleep (3)
    print("Il courut dans une grande forêt à proximité de son lieu d'atterrissage.")
    sleep (2)
    print("Mais où doit-il aller exactement ?")
    sleep (4)
    system ("cls")
    print("Choisis une direction pour continuer :\n")
    print("1. Gauche")
    print("2. Droite\n")
    choix = input("Choix : ")
    
    if choix == "1":
        system ("cls")
        print("Il choisit de tourner à gauche...")
        sleep (2)
        print(f"\n{nom} rencontre un magicien !")
        sleep (2)
        print("\nMagicien: \"Bonjour jeune héros, je cherche Modyle, reine de Globul...")
        sleep (3)
        print(f"\nMais {nom} ne sait pas où elle pourrait se situer.")
        sleep (3)
        print("\nMagicien: Je sais ! Suis-moi et on pourra peut-être la retrouver !")
        sleep (3)
        print("\nLe magicien te propose deux chemins différents :")
        sleep (2)
        system ("cls")
        print("1. Le chemin de la forêt enchantée")
        print("2. Le chemin des montagnes escarpées\n")
        choix_magicien = input("Choisis ton chemin (1 ou 2) : ")
        
        if choix_magicien == "1":
            system ("cls")
            print(f"{nom} décide de suivre le chemin de la forêt enchantée...")
            sleep (2)
            print("\nVous entrez dans la forêt et vous sentez une atmosphère magique vous envelopper...")
            sleep (3)
            print(f"\n{nom} et le magicien continuent leur quête à travers la forêt.")
            sleep (3)
            print("\nMais le Répertoire MD commence à disparaître...")
            sleep (3)
            print("Le magicien disparaît également.")
            sleep (2)
            system ("cls")
            print(f"Tu disparaîs aussi...")
            sleep (5)
            
        elif choix_magicien == "2":
            sleep (2)
            print(f"{nom} décide de suivre le chemin des montagnes escarpées...")
            sleep (2)
            print("\nLa montée est difficile mais vous continuez à grimper courageusement...")
            sleep (3)
            print(f"\n{nom} et le magicien progressent dans les montagnes en quête de la reine.")
            sleep (3)
            system ("cls")
            print("FIN.")
            sleep (5)
            
        else:
            system ("cls")
            print(f"{nom} n'a pas fait de choix et reste perplexe...")
            sleep (2)
            print("\nLe magicien décide de prendre la direction du chemin de la forêt enchantée.")
            sleep (3)
            print(f"\n{nom} reste immobile et finit par mourir de faim.")
            sleep (3)
            system ("cls")
            print("FIN. (vraiment nulle...)")
            sleep (5)
            
    elif choix == "2":
        system ("cls")
        print(f"{nom} choisit de tourner à droite...")
        sleep (2)
        print(f"\n{nom} croise une bête très dangereuse !")
        sleep (3)
        print("\nC'est Marine Le Pen (elle est de droite tout ça)")
        sleep (3)
        system ("cls")
        print("Veux-tu fuir ?\n")
        reponse = input("Oui ou Non : ").lower()
        
        if reponse == "oui":
            system ("cls")
            print(f"{nom} a décidé de fuir...")
            sleep (2)
            print("\nMais Marine est plus rapide !")
            sleep (3)
            print("\nElle rattrape {nom}.")
            sleep (3)
            system ("cls")
            print("FIN. (tu finis en esclavage)")
            sleep (5)

        else:
            system ("cls")
            print(f"{nom} a décidé de ne pas fuir...")
            sleep (3)
            system ("cls")
            print("FIN. (Il est mort)")
            sleep (5)
    
    else:
        system ("cls")
        print(f"{nom} a hésité et n'as pas choisi de direction...")
        sleep (2)
        print(f"\n{nom} reste planté dans cette forêt sans même penser à respirer...")
        sleep (5)
        system ("cls")
        print("FIN... (Il est décédé)")
        sleep (5)
    
    system ("cls")
    print("WOAW, ton histoire était... pas ouf...")
    sleep (3)
    print("\nLe répertoire sera maintenant réinitialisé...")
    sleep (3)
    system ("cls")
    print("...3")
    sleep (1)
    system ("cls")
    print("...2")
    sleep (1)
    system ("cls")
    print("...1")
    sleep (1)
    system ("cls")
    print("   -- C'était une blague ! --\n")
    print (" Si tu veux réinitialiser le Centre MD, tu peux le faire depuis les options !\n Je t'y dépose directement !\n")
    
    sleep (5)
    return