from outils import lecture_csv
from apps.rep_md.main import f_rep
from apps.gdt_md.main import tps_tache
import datetime
import logging

def str_mois (mois):
    dico_mois = {
        "01": "Janvier",
        "02": "Février",
        "03": "Mars",
        "04": "Avril",
        "05": "Mai",
        "06": "Juin",
        "07": "Juillet",
        "08": "Août",
        "09": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Décembre"
    }
    
    for str_mois, lettres_mois in dico_mois.items ():
        if str_mois == mois:
            return lettres_mois

def afficher ():
    liste = lecture_csv (f_rep)
    logging.info (f"    AFFICHER ANNIVERSAIRES\n")
    
    print ("   · Afficher les Anniversaires ·")
    
    if len (liste) >= 1:
        
        for i in range (len (liste)):
            if liste[i]["date"] != "":
                nom = liste[i]["nom"]
                prenom = liste[i]["prenom"]
                date_naissance = liste[i]["date"]
                jour, mois, annee = date_naissance.split(".")
                mois_str = str (mois)
                mois_lettres = str_mois (mois_str)
                date_anniv_str = f"{annee}-{mois}-{jour}"
                date_anniv = datetime.datetime(datetime.datetime.now().year, int(mois), int(jour)).date()
                aujourdhui = datetime.date.today()
                if aujourdhui > date_anniv: date_anniv = datetime.datetime(datetime.datetime.now().year + 1, int(mois), int(jour)).date()
                tps_restant = date_anniv - aujourdhui
                
                print (f"\n |   {nom} {prenom}")
                print (f" |   Date: {jour} {mois_lettres}")
                if tps_restant.days == 0: print (" |   C'est son Anniversaire !")
                else: print (f" |   Anniversaire dans {tps_restant.days} jours")
                
        print ()
        return
    
    print ("Aucun contact ayant une date de naissance trouvé !\n")
    return