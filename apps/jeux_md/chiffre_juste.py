import outils
import os
import random

def main(nom):
    nbr = random.randint(0, 100)
    tentatives = 0
    while True:
        print("   · Le Chiffre Juste ·\n")
        mon_nbr = input(f"{nom}, saisissez un nombre entre 0 et 100 : ")
        os.system("cls")
        if mon_nbr.isdigit():
            mon_nbr = int(mon_nbr)
            break
        print(" Format incorrect !\n")
    
    while mon_nbr != nbr:
        if mon_nbr < nbr:
            print(" C'EST PLUS !\n")
        elif mon_nbr > nbr:
            print(" C'EST MOINS !\n")
        
        tentatives += 1
        
        while True:
            mon_nbr = input("Saisissez un autre nombre : ")
            os.system("cls")
            if mon_nbr.isdigit():
                mon_nbr = int(mon_nbr)
                break
            print(" Format incorrect !\n")
    
    print(f" Félicitations {nom} !\n\n Tu as trouvé le nombre {str(nbr)} en {tentatives} tentatives !\n")
    outils.ecriture_log(f"    LE CHIFFRE JUSTE : {nom} a trouvé \"{str(nbr)}\" en {tentatives} tentatives !\n")
    return