import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions

#liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Quitter"]
#liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "retour"]

def charger_csv():
    fichierchargé = False
    liste_fichier = []
    while fichierchargé == False:
        try: 
            liste_fichier = bc.charger_activites(input("Entrez le nom du fichier csv que vous voulez charger (n'oubliez pas de mettre le .csv)" + "\n"))
        except:
            print("Fichier introuvable, veuillez réessayer")
        else:
            fichierchargé = True
            print("Fichier chargé")
    return liste_fichier

def menu(titre, liste_options):
    try:
        affichage_menu_principal(titre, liste_options)
        rep = demander_nombre("Entrez votre choix [1-", len(liste_options))
        return rep
    except:
        return None

def affichage_menu_principal(titre, liste_option):
    print("+-----------------------------------------+")
    print("|Bienvenu sur l'application " + titre + "|")
    print("+-----------------------------------------+" + "\n")
    print("-----------------------+")
    print("Que voulez vous faire ?|")
    print("-----------------------+")
    choix_options(liste_option)
    


def choix_options(liste_options):
    cpt = 1
    for i in range(len(liste_options)):
        print(cpt, " -> ", liste_options[cpt-1])
        cpt+=1


def demander_nombre(message, borne_max):
    try:
        rep = int(input(message + str(borne_max) + "]" + "\n"))

        if rep <= borne_max:
            return rep
    except:
        return None

def demander_oui_non(message):
    try:
        rep = input((message))
        return rep
    except:
        return None
    
def rechercher_une_personne(csv_to_list, liste_options_menu_Personne):
    Prenomexist = False
    while Prenomexist == False:
        try:
            Prenom = input("Entrez le prénom de la personne que vous recherchez : ")
            if Prenom in bc.liste_des_personnes(csv_to_list):
                Prenomexist = True
                return Prenom
            else: 
                print("je ne connais pas la personne que vous cherchez, veuillez réessayer")
        except:
            print("je ne connais pas la personne que vous cherchez, veuillez réessayer")

def affichage_menu_recherche_personne(Prenom2, liste_options): 
    print("---------------------------------------+") 
    print("Que voulez vous savoir sur " + Prenom2 + " ?    |")
    print("---------------------------------------+")
    choix_options(liste_options)

def bilan_carbonne_personne(Prenom, Prenom_csv_to_list):
    print("-------------------------------------")
    print(Prenom + " a émit au total " + str(bc.cumul_emmissions(Prenom_csv_to_list)) + " grammes de Co2" )
    print("-------------------------------------")

def plus_polluante_personne(Prenom, Prenom_csv_to_list):
    act_plus_polluante = bc.max_emmission(Prenom_csv_to_list)
    print("-------------------------------------")
    print("l'acivité la plus polluante de " + Prenom + " a émise " + str(act_plus_polluante[2]) + " grammes de Co2 le " + act_plus_polluante[1] + ", c'était une activité de " + act_plus_polluante[3]) 
    print("-------------------------------------")

def afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom):
    try:
        liste_types = bc.liste_des_types(Prenom_csv_to_list)
        print("------------------------------------------")
        print(Prenom + " pratique les activités de type :" + str(liste_types))
        print("------------------------------------------")
    except:
        print("Erreur lors de l'affichage des activités")

def sauver_liste(rep, list):
    repOn = True
    try:
        while repOn:
            if rep == 'o':
                Nomfichier = input("Donnez un nom à votre fichier (sans oublier le .csv): ")
                print("sauvegarde en cours...")
                bc.sauver_activites(Nomfichier, list)
                print("Liste sauvegardée avec succès (le fichier ce trouve dans le dossier courant)")
                repOn = False
            if rep == 'n':
                print("")
                repOn = False
    except:
        print("Erreur lors de la sauvegarde")

def rechercher_date(csv_to_list):
    Dateexist = False
    while Dateexist == False:
        try:
            date = input("Entrez la date que vous recherchez (format AAAA-MM-JJ) : ")
            Liste_act_date = bc.filtre(csv_to_list, 1, date)
            if Liste_act_date != []:
                Dateexist = True
                return date
            else:
                print("je ne trouve pas la date que vous cherchez, veuillez réessayer")
        except:
            print("je ne trouve pas la date que vous cherchez, veuillez réessayer")

def affichage_liste_personne(csv_to_list):
    try:
        print("Voici la liste des personnes :")
        liste_personne = bc.liste_des_personnes(csv_to_list)
        print(liste_personne)
        return liste_personne
    except:
        print("Erreur lors de l'affichage des personnes")

def moyenne_act_personne(Prenom, Prenom_csv_to_list):
    print("----------------------------------------")
    print(Prenom + " a émis quotidiennement en moyenne " + str(bc.cumul_emmissions(Prenom_csv_to_list)/len(Prenom_csv_to_list)+1) + " grammes de Co2 en septembre")
    print("----------------------------------------")

def affichage_menu_date(date, list_opt_date):
    print("----------------------------------+")
    print("Que c'est il passé le " + date + " ?|")
    print("----------------------------------+")
    choix_options(list_opt_date)

def bilan_caronne_date(date, date_csv_to_list):
    print("\n")
    print("-------------------------------------")
    print(str(bc.cumul_emmissions(date_csv_to_list)) + " grammes de Co2 ont été émis le " + date)
    print("-------------------------------------")
    print("\n")

def liste_des_personne_date(date, date_csv_to_list):
    try:
        print("voici la liste des personnes ayant émi du Co2 le " + date)
        print("-----------------------------------------------")
        liste_pers_date = bc.liste_des_personnes(date_csv_to_list)
        print(liste_pers_date)
        return liste_pers_date
    except:
        print("Erreur lors de l'affichage des personnes")

def plus_polluante_date(date, date_csv_to_list):
    try:
        plus_polluante = bc.max_emmission(date_csv_to_list)
        print("---------------------------------")
        print("L'activité la plus polluante le " + date + " a émise " + str(plus_polluante[2]) + " grammes de Co2, c'était une activité de " + str(plus_polluante[3]))
        print("---------------------------------")
    except:
        print("Erreur lors de l'affichage")

def moyenne_act_date(date, date_csv_to_list):
    print("----------------------------------------")
    print("Il y a eu en moyenne " + str(bc.cumul_emmissions(date_csv_to_list)/len(date_csv_to_list)) + " grammes de Co2 émis le " + date)
    print("----------------------------------------")


    




# ici votre programme principal

def programme_principal():
    appli_running = True
    liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Affichier la liste des personnes", "Quitter"]
    liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "La moyenne de ses émissions", "Le temps moyen consacré à ses activités", "Chercher une autre personne", "Retour"]
    Liste_options_menu_date = ["Bilan Carbonne de cette date", "Liste des Personnes à cette date", "Activité la plus polluante à cette date", "Moyenne des émissions", "Chercher une autre date", "Retour"]
    csv_to_list = charger_csv()
    while appli_running:
        rep_menu_principal = menu("Bilan carbonne", liste_options_menu)
        try:
            if rep_menu_principal is None:
                print("cette option n'existe pas !")
                    
            elif rep_menu_principal == 1:
                recherche_personne_en_cours = True
                Prenom = rechercher_une_personne(csv_to_list, liste_options_menu_Personne)
                Prenom_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom)
                while recherche_personne_en_cours:
                    affichage_menu_recherche_personne(Prenom, liste_options_menu_Personne)
                    rep_recherhe_personne = demander_nombre("Entrez un nombre [1-", len(liste_options_menu_Personne))
                    try:
                        if rep_recherhe_personne == 1:
                            bilan_carbonne_personne(Prenom, Prenom_csv_to_list)
                    
                        elif rep_recherhe_personne == 2:
                            afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom)
                            rep_sauver = demander_oui_non("Voulez vous sauvegarder la liste des activités de " + Prenom +  " dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 3:
                            plus_polluante_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 4:
                            moyenne_act_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 5:
                            print("")
                        elif rep_recherhe_personne == 6:
                                Prenom = rechercher_une_personne(csv_to_list, liste_options_menu_Personne)
                                Prenom_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom)
                            
                        elif rep_recherhe_personne == 7:
                                recherche_personne_en_cours = False
                        
                        else:
                                print("cette option n'existe pas")
                    except:
                        print("erreur")
                    input("Appuyer sur Entrée pour continuer")

            elif rep_menu_principal == 2:
                recherche_date_en_cours = True
                date = rechercher_date(csv_to_list)
                date_csv_to_list = bc.filtre(csv_to_list, 1, date)
                while recherche_date_en_cours:
                    affichage_menu_date(date, Liste_options_menu_date)
                    rep_date = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_date))
                    try:
                        if rep_date == 1:
                            bilan_caronne_date(date, date_csv_to_list)
                        
                        elif rep_date == 2:
                            liste_des_personne_date(date, date_csv_to_list)
                            rep_sauver_date = demander_oui_non("Voulez vous sauvegarder ces données dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_date, date_csv_to_list)
                        
                        elif rep_date == 3:
                            plus_polluante_date(date, date_csv_to_list)

                        elif rep_date == 4:
                            moyenne_act_date(date, date_csv_to_list)                            
                    
                        elif rep_date == 5:
                            date = rechercher_date(csv_to_list)
                            date_csv_to_list = bc.filtre(csv_to_list, 1, date)

                        elif rep_date == 6:
                            recherche_date_en_cours = False
                        
                        else:
                            print("cette option n'existe pas")
                    except:
                        print("erreur")
                    input("Appuyer sur Entrée pour continuer")


                
                
                
            
            elif rep_menu_principal == 3:
                print("bleh3")

            elif rep_menu_principal == 4:
                print("bleh4")

            elif rep_menu_principal == 5:
                affichage_liste_personne(csv_to_list)          
            elif rep_menu_principal == 6:
                appli_running = False
        except:
            print("cette option n'existe pas !")
        input("Appuyer sur Entrée pour continuer")
    print("Au revoir !")
programme_principal()


