import outils
import os
import datetime

def main(L_fonds, usr):
    test = False
    usr_id = usr["id"]
    date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    print("   · Retirer ·\n")
    while True:
        argent = input("Saisissez l'argent à retirer : ")
        os.system("cls")
        argent_restant, historique = outils.affiche_fonds(L_fonds, usr)
        if argent.isdigit() and int(argent) != 0:
            argent = int(argent)
            if argent > 0:
                argent = -argent
            argent = str(argent)
            break
        print(" Format incorrect !\n")
    if -int(argent) > argent_restant:
        print(f" Action impossible, il ne vous reste que {argent_restant}€\n")
    else:
        nom = input("Saisissez le nom donné à cette opération : ")
        os.system("cls")
        operation = [usr_id, nom, argent, date]
        L_fonds.append(operation)
        outils.ecriture_fonds(L_fonds)
        outils.ecriture_log(f"    RETIRER : {argent}\n")
        print(" Compte mis à jour !\n")