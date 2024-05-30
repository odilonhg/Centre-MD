from outils import Outils
from apps.rep_md.main import f_rep
from logging import info
from os import system

def supprimer():
    choice = "non"
    liste = Outils.CSV.lecture_csv (f_rep)
    
    print ("   · Supprimer: Contacts ·\n")
    contact = input ("Renseigner une information sur le contact à supprimer : ").lower()
    
    for i in range (len (liste)):
        nom = liste[i]["nom"].lower ()
        prenom = liste[i]["prenom"].lower ()
        date_naissance = liste[i]["date"]
        num = liste[i]["num"]
        email = liste[i]["email"].lower ()
        favori = liste[i]["favori"]
        
        if date_naissance != "":
            jour, mois, annee = date_naissance.split (".")
            if contact == nom or contact == prenom or contact == date_naissance or contact == jour or contact == mois or contact == annee or contact == num or contact == email or contact == favori:
                system ("cls")
                print (f"Supprimer {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice = input ("Choix : ").lower ()
        else:
            if contact == nom or contact == prenom or contact == date_naissance or contact == num or contact == email or contact == favori:
                system ("cls")
                print (f"Supprimer {nom.upper ()} {prenom.capitalize ()} ?\n")
                choice = input ("Choix : ").lower ()
        
        if choice == "oui":
            system ("cls")
            del (liste[i])
            Outils.CSV.ecriture_csv (liste, f_rep)
            print (f"Le contact {nom.upper ()} {prenom.capitalize ()} a été supprimé des contacts !\n")
            info (f"    SUPPRIMER CONTACTS: {nom.upper ()} {prenom.capitalize ()}\n")
            return
    
    system ("cls")
    print ("Aucun contact trouvé !\n")
    return