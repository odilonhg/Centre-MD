import outils
import os
import datetime

def main(L_fonds, usr):
    test = False
    usr_id = usr["id"]
    date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    print("   · Ajouter ·\n")
    while True:
        argent = input("Saisissez l'argent à ajouter : ")
        os.system("cls")
        if argent.isdigit() and int(argent) != 0:
            argent = int(argent)
            if argent < 0:
                argent = -argent
            argent = str(argent)
            break
        print(" Format incorrect !\n")
    print("   · Ajouter ·\n")
    nom = input("Saisissez le nom donné à cette opération : ")
    os.system("cls")
    operation = [usr_id, nom, argent, date]
    L_fonds.append(operation)
    outils.ecriture_fonds(L_fonds)
    outils.ecriture_log(f"    AJOUTER : {argent}\n")
    print(" Compte mis à jour !\n")