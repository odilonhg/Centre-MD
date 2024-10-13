import outils
import os

def main(L_rep, usr):
    print("   · Supprimer ·\n")
    contact = input("Saisissez une information sur le contact / groupe à supprimer : ")
    os.system("cls")
    if contact == "":
        print(" Action annulée...\n")
        return
    L_rep_recherche = outils.recherche(L_rep, usr, contact)
    for contact in L_rep_recherche:
        test = False
        if contact["nom"]:
            while True:
                print(f" Voulez-vous supprimer {contact['nom']} {contact['prenom']} ?\n",
                      "\n 1. Oui",
                      "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                if choix == "1":
                    test = True
                    for groupe in L_rep:
                        if groupe["id"] in contact["groupes"]:
                            groupe["nbr_groupe"] = str(int(groupe["nbr_groupe"]) - 1)
                    print(f" Le contact {contact['nom']} {contact['prenom']} a été supprimé avec succès...\n")
                    break
                elif choix == "2":
                    break
                else:
                    print(" Choix impossible...\n")
        else:
            while True:
                print(f" Voulez-vous supprimer {contact['nom_groupe']} ?\n",
                      "\n 1. Oui",
                      "\n 2. Non")
                choix = input("\nChoix : ")
                os.system("cls")
                if choix == "1":
                    test = True
                    for groupe in L_rep:
                        if contact["id"] in groupe["groupes"]:
                            new_id = ""
                            for id_groupe in groupe["groupes"]:
                                if id_groupe != contact["id"]:
                                    new_id += id_groupe
                            groupe["groupes"] = new_id
                    print(f" Le groupe \"{contact['nom_groupe']}\" a été supprimé avec succès...\n")
                    break
                elif choix == "2":
                    break
                else:
                    print(" Choix impossible...\n")
        if test:
            L_rep.remove(contact)
            outils.ecriture_rep(L_rep)
            break