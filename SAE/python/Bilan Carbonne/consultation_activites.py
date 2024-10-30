import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions

#liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Quitter"]
#liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "retour"]

def charger_csv(message):
    fichierchargé = False
    liste_fichier = []
    while fichierchargé == False:
        try: 
            liste_fichier = bc.charger_activites(input("Entrez le nom du " + message + " csv que vous voulez charger (n'oubliez pas de mettre le .csv)" + "\n"))
        except:
            print("Fichier introuvable, veuillez réessayer")
        else:
            fichierchargé = True
            print("Fichier chargé")
    return liste_fichier

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
        print("Erreur lors de la sauvegarde !")

def fusion(fichier1, fichier2):
    try:
        fichier_fusionné = bc.fusionner_activites(fichier1, fichier2)
        return fichier_fusionné
    except:
        print("Erreur lors de la fusion !")

def sauver_fusion(fichier_fusionné):
    try:
        Nomfichier = input("Donnez un nom au fichier fusionné (sans oublier le .csv): ")
        print("sauvegarde en cours...")
        bc.sauver_activites(Nomfichier, fichier_fusionné)
        print("Liste sauvegardée avec succès (le fichier ce trouve dans le dossier courant)")
    except:
        print("Erreur lors de la sauvegarde !")
        


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
    
def rechercher_une_personne(csv_to_list):
    Prenomexist = False
    while Prenomexist == False:
        try:
            Prenom = input("Entrez le prénom de la personne que vous recherchez : ")
            if Prenom in bc.liste_des_personnes(csv_to_list):
                Prenomexist = True
                return Prenom
            elif Prenom == "None":
                Prenomexist = True
                return None
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


def rechercher_date(csv_to_list):
    Dateexist = False
    Liste_act_date = []
    while Dateexist == False:
        try:
            date = input("Entrez la date que vous recherchez (format AAAA-MM-JJ) : ")
            if date != "None":
                Liste_act_date = bc.filtre(csv_to_list, 1, date)
            if Liste_act_date != []:
                Dateexist = True
                return date
            elif date == "None":
                Dateexist = True
                return None
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
    print("Que c'est t-il passé le " + date + " ?|")
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
        print("---------------------------------------")
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

def duree_moyenne(Prenom, prenom_csv_to_list):
    temp_moyen = bc.cumul_temps_activite(prenom_csv_to_list, bc.co2_minute)/len(prenom_csv_to_list)
    temp_moyen = temp_moyen/60
    print("-----------------------------------")
    print(Prenom + " a consacré en moyenne " + str(temp_moyen) + " heures à ces activités")
    print("-----------------------------------")

def rechercher_type(type_csv_to_list):
    typeexist = False
    Liste_act_date = []
    while typeexist == False:
        try:
            type = input("Entrez le type que vous recherchez : ")
            if type != "None":
                Liste_act_date = bc.filtre(type_csv_to_list, 3, type)
            if Liste_act_date != []:
                typeexist = True
                return type
            elif type == "None":
                typeexist = True
                return None
            else:
                print("je ne trouve pas le type que vous cherchez, veuillez réessayer")
        except:
            print("je ne trouve pas le type que vous cherchez, veuillez réessayer")

def affichage_menu_type(type, menu_type):
    print("----------------------------------------------------+")
    print("Que voulez vous savoir sur les activités de " + type + " ? |")
    print("----------------------------------------------------+")
    choix_options(menu_type)

def bilan_carbonne_type(type, type_csv_to_list):
    print("-----------------------------")
    print("Les activités de " + type + " on émise au total " + str(bc.cumul_emmissions(type_csv_to_list)) + " grammes de Co2")
    print("-----------------------------")

def plus_polluante_type(type, type_csv_to_list):
    plus_polluante = bc.max_emmission(type_csv_to_list)
    print("-----------------------------")
    print("L'activité la plus polluante de " + type + " a émise " + str(plus_polluante[2]) + " grammes de Co2")
    print("-----------------------------")

def pourcentage_type(type, type_csv_to_list, csv_to_list):
    try:
        pourcentage = (len(type_csv_to_list)/len(csv_to_list))*100
        print("-----------------------------")
        print("Il y a " + str(pourcentage) + " % " + " de personne pratiquant des activités de " + type)
        print("-----------------------------")
    except:
        print("Erreur lors du calcul de pourcentage")

def affichage_liste_personnes_type(type, type_csv_to_list):
    try:
        print("Voici la liste des personnes pratiquant des activités de " + type)
        print("---------------------------------------")
        print(str(bc.liste_des_personnes(type_csv_to_list)))
        print("---------------------------------------")
    except:
        print("Erreur lors de l'affichage des personnes")

def affichage_dichotomique(Prenom, date, type, csv_to_list):
    try:
        activite_precise = bc.recherche_activite_dichotomique(Prenom, date, type, csv_to_list)
        print("-------------------------------")
        print(Prenom + " a émis " + str(activite_precise[2]) + " grammes de Co2 le " + date + " c'était une activité de " + type)
        print("-------------------------------")
    except:
        print("Désolé mais cette activité n'existe pas !")

def affichage_recherche_precise(Liste_options_menu_recherche_precise):
    print("---------------------------------------------+")
    print("Que voulez vous savoir sur cette recherche ? |")
    print("---------------------------------------------+")
    choix_options(Liste_options_menu_recherche_precise)

def bilan_carbonne_precis(precis_csv_to_list):
    try:
        print("--------------------------------")
        print("Ces activités ont émise au total " + str(bc.cumul_emmissions(precis_csv_to_list)) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors du bilan carbonne !")

def plus_polluante_precis(precis_csv_to_list):
    try:
        act_plus_polluante = bc.max_emmission(precis_csv_to_list)
        print("--------------------------------")
        print("L'activité la plus polluante de cette liste à émise " + str(act_plus_polluante[2]) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors de l'affichage precis !")

def moyenne_emission_precis(precis_csv_to_list):
    try:
        print("--------------------------------")
        print("Ces activités ont emises en moyenne " + str(bc.cumul_emmissions(precis_csv_to_list)/len(precis_csv_to_list)) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors du calcul de la moyenne des émissions !")

def affichage_liste_act_precis(precis_csv_to_list):
    try:
        print("Voici la liste des activités selon vos critères :")
        print("-------------------------------------------------------")
        print(precis_csv_to_list)
        print("-------------------------------------------------------")
    except:
        print("Erreur lors de l'affichage de la liste !")





# ici votre programme principal

def programme_principal():
    appli_running = True
    liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise","Autres informations", "Afficher la liste des personnes", "Fusionner deux fichiers", "Charger un autre fichier", "Quitter"]
    liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "La moyenne de ses émissions", "Le temps moyen consacré à ses activités", "Chercher une autre personne", "Retour"]
    Liste_options_menu_date = ["Bilan Carbonne de cette date", "Liste des Personnes à cette date", "Activité la plus polluante à cette date", "Moyenne des émissions", "Chercher une autre date", "Retour"]
    Liste_options_menu_type = ["Bilan carbonne de ces activité", "Activité la plus polluante de ce type", "Pourcentage des personnes pratiquant ce type d'activités", "Liste des personnes pratiquant ces activités", "Chercher un autre type", "Retour"]
    Liste_options_menu_recherche_precise = ["Bilan carbonne", "Activité la plus poulluante", "Moyenne des émissions", "Liste des activités", "Retour"]
    Liste_options_menu_autres_informations = ["Plus longue période d'émissions décroissantes", "Evolution"]
    csv_to_list = charger_csv("fichier")
    fichier1 = None
    fichier2 = None
    while appli_running:
        rep_menu_principal = menu("Bilan carbonne", liste_options_menu)
        try:
            if rep_menu_principal is None:
                print("cette option n'existe pas !")
                    
            elif rep_menu_principal == 1:
                recherche_personne_en_cours = True
                Prenom = rechercher_une_personne(csv_to_list)
                Prenom_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom)
                while recherche_personne_en_cours:
                    affichage_menu_recherche_personne(Prenom, liste_options_menu_Personne)
                    rep_recherhe_personne = demander_nombre("Entrez un nombre [1-", len(liste_options_menu_Personne))
                    try:
                        if rep_recherhe_personne == 1:
                            bilan_carbonne_personne(Prenom, Prenom_csv_to_list)
                    
                        elif rep_recherhe_personne == 2:
                            afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom)
                            rep_sauver_personne = demander_oui_non("Voulez vous sauvegarder la liste des activités de " + Prenom +  " dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_personne, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 3:
                            plus_polluante_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 4:
                            moyenne_act_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 5:
                            duree_moyenne(Prenom, Prenom_csv_to_list)

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
                recherche_type_en_cours = True
                type = rechercher_type(csv_to_list)
                type_csv_to_list = bc.filtre(csv_to_list, 3, type)
                while recherche_type_en_cours:
                    affichage_menu_type(type, Liste_options_menu_type)
                    rep_type = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_type))
                    try:
                        if rep_type == 1:
                            bilan_carbonne_type(type, type_csv_to_list)

                        elif rep_type == 2:
                            plus_polluante_type(type, type_csv_to_list)
                       
                        elif rep_type == 3:
                            pourcentage_type(type, type_csv_to_list, csv_to_list)

                        elif rep_type == 4:
                            affichage_liste_personnes_type(type, type_csv_to_list)
                            rep_sauver_type = demander_oui_non("Voulez vous sauvegarder la liste des activités de " + type +  " dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_type, type_csv_to_list)
                        
                        elif rep_type == 5:
                            type = rechercher_type(csv_to_list)
                            type_csv_to_list = bc.filtre(csv_to_list, 3, type)

                        elif rep_type == 6:
                            recherche_type_en_cours = False
                        
                        else:
                            print("Cette option n'existe pas !")
                    except:
                        print("Erreur")
                    input("Appuyer sur Entrée pour continuer")


            elif rep_menu_principal == 4:
                recherche_precise_en_cours = True
                print("Veuillez renseigner au minimum 2 critères. (None si vous ne voulez pas renseigner un critère)")
                print("---------------------------------------------------------------------------------------------")
                Prenom_precis = rechercher_une_personne(csv_to_list)
                date_precise = rechercher_date(csv_to_list)
                type_precis = rechercher_type(csv_to_list)

                if Prenom_precis != None and date_precise != None and type_precis != None:
                    affichage_dichotomique(Prenom_precis, date_precise, type_precis, csv_to_list)
                    recherche_precise_en_cours = False
                
                if Prenom_precis == None:
                    precis_csv_to_list = bc.filtre(csv_to_list, 3, type_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 1, date_precise)                
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                if date_precise == None:
                    precis_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 3, type_precis)
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                if type_precis == None:
                    precis_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 1, date_precise)
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                
                while recherche_precise_en_cours:
                    affichage_recherche_precise(Liste_options_menu_recherche_precise)
                    rep_precis = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_recherche_precise))
                    try:
                        if rep_precis == 1:
                            bilan_carbonne_precis(precis_csv_to_list)

                        elif rep_precis == 2:
                            plus_polluante_precis(precis_csv_to_list)

                        elif rep_precis == 3:
                            moyenne_emission_precis(precis_csv_to_list)

                        elif rep_precis == 4:
                            affichage_liste_act_precis(precis_csv_to_list)
                            rep_sauver_precis = demander_oui_non("Voulez vous sauvegarder cette liste d'activités dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_precis, precis_csv_to_list)

                        elif rep_precis == 5:
                            recherche_precise_en_cours = False
                        
                        else:
                            print("Cette option n'existe pas")
                    except:
                        print("Erreur lors de la recherche précise")
                    input("Appuyer sur Entrée pour continuer")


            elif rep_menu_principal == 5:
                autres_information_en_cours = True
                while autres_information_en_cours:
                    try:

                         
            elif rep_menu_principal == 6:
                affichage_liste_personne(csv_to_list) 

            elif rep_menu_principal == 7:
                fichier1 = charger_csv("premier fichier")
                fichier2 = charger_csv("deuxième fichier")
                sauver_fusion(fusion(fichier1, fichier2))

            elif rep_menu_principal == 8:
                csv_to_list = charger_csv("fichier")
                
            elif rep_menu_principal == 9:
                appli_running = False
            else:
                print("cette option n'existe pas !")
        except:
            print("erreur !")
        input("Appuyer sur Entrée pour continuer")
    print("Au revoir !")
programme_principal()


