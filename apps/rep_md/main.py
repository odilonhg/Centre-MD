import os

F_rep = "data_rep.csv" # NE PAS MODIFIER LE NOM DE LA VARIABLE (liée à ttes les autres fonctions)

def rep_md ():
    while True:
        print (_("-Rep MD-"))
        
        print (_("Retour"))
        print (_("Ajouter"))
        print (_("Rechercher"))
        print (_("Afficher"))
        print (_("Modifier"))
        print (_("Supprimer"))
        
        choix_rep_md= input (_("Choix")).lower ()
        os.system ("cls")
        
        if choix_rep_md== "0": break
        
        elif choix_rep_md== "1":
            while True:
                print (_("Retour"))
                print (_("Contacts"))
                print (_("Groupes"))
                
                choix_ajouter= input (_("Choix")).lower ()
                
                if choix_ajouter== "0":
                    os.system ("cls")
                    break
                
                elif choix_ajouter== "1":
                    from apps.rep_md.ajouter import ajouter
                    os.system ("cls")
                    ajouter ("contacts")
                    break
                
                elif choix_ajouter== "2":
                    from apps.rep_md.ajouter import ajouter
                    os.system ("cls")
                    ajouter ("groupes")
                    break
                
                else:
                    os.system ("cls")
                    print (_("Choix impossible"))
        
        elif choix_rep_md== "2":
            while True:
                print (_("Retour"))
                print (_("Contacts"))
                print (_("Groupes"))
                
                choix_rechercher= input (_("Choix")).lower ()
                
                if choix_rechercher== "0":
                    os.system ("cls")
                    break
                
                elif choix_rechercher== "1":
                    from apps.rep_md.rechercher import rechercher
                    os.system ("cls")
                    rechercher ("contacts")
                    break
                
                elif choix_rechercher== "2":
                    from apps.rep_md.rechercher import rechercher
                    os.system ("cls")
                    rechercher ("groupes")
                    break
                
                else:
                    os.system ("cls")
                    print (_("Choix impossible"))
        
        elif choix_rep_md== "3":
            while True:
                print (_("Retour"))
                print (_("Contacts"))
                print (_("Groupes"))
                
                choix_afficher= input (_("Choix")).lower ()
                
                if choix_afficher== "0":
                    os.system ("cls")
                    break
                
                elif choix_afficher== "1":
                    from apps.rep_md.afficher import afficher
                    os.system ("cls")
                    afficher ("contacts")
                    break
                
                elif choix_afficher== "2":
                    from apps.rep_md.afficher import afficher
                    os.system ("cls")
                    afficher ("groupes")
                    break
                
                else:
                    os.system ("cls")
                    print (_("Choix impossible"))
        
        elif choix_rep_md== "4":
            while True:
                print (_("Retour"))
                print (_("Contacts"))
                print (_("Groupes"))
                
                choix_modifier= input (_("Choix")).lower ()
                
                if choix_modifier== "0":
                    os.system ("cls")
                    break
                
                elif choix_modifier== "1":
                    from apps.rep_md.modifier import modifier
                    os.system ("cls")
                    modifier ("contacts")
                    break
                
                elif choix_modifier== "2":
                    from apps.rep_md.modifier import modifier
                    os.system ("cls")
                    modifier ("groupes")
                    break
                
                else:
                    os.system ("cls")
                    print (_("Choix impossible"))
        
        elif choix_rep_md== "5":
            while True:
                print (_("Retour"))
                print (_("Contacts"))
                print (_("Groupes"))
                
                choix_supprimer= input (_("Choix")).lower ()
                
                if choix_supprimer== "0":
                    os.system ("cls")
                    break
                
                elif choix_supprimer== "1":
                    from apps.rep_md.supprimer import supprimer
                    os.system ("cls")
                    supprimer ("contacts")
                    break
                
                elif choix_supprimer== "2":
                    from apps.rep_md.supprimer import supprimer
                    os.system ("cls")
                    supprimer ("groupes")
                    break
                
                else:
                    os.system ("cls")
                    print (_("Choix impossible"))
        
        elif choix_rep_md== _("aide"):
            os.system ("cls")
            print (_("aide_rep_md"))
        
        else:
            os.system ("cls")
            print (_("Choix impossible"))