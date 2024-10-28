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

def bilan_carbonne(Prenom, Prenom_csv_to_list):
    print("\n")
    print("-------------------------------------")
    print(Prenom + " a émit au total " + str(bc.cumul_emmissions(Prenom_csv_to_list)) + " grammes de Co2" )
    print("-------------------------------------")
    print("\n")

def plus_polluante(Prenom, Prenom_csv_to_list):
    act_plus_polluante = bc.max_emmission(Prenom_csv_to_list)
    print("-------------------------------------")
    print("l'acivité la plus polluante de " + Prenom + " a émise " + str(act_plus_polluante[2]) + " grammes de Co2 le " + act_plus_polluante[1] + ", c'était une activité de " + act_plus_polluante[3] + "-------------------------------------" + "\n")

def afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom):
    print("Voici la liste d'activité de " + Prenom + " :")
    print(Prenom_csv_to_list)    



# ici votre programme principal

def programme_principal():
    appli_running = True
    liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Quitter"]
    liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "Chercher une autre personne", "retour"]
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
                while recherche_personne_en_cours == True:
                    affichage_menu_recherche_personne(Prenom, liste_options_menu_Personne)
                    rep_recherhe_personne = demander_nombre("Entrez un nombre [1-", len(liste_options_menu_Personne))
                    try:
                        if rep_recherhe_personne == 1:
                            bilan_carbonne(Prenom, Prenom_csv_to_list)
                    
                        elif rep_recherhe_personne == 2:
                            afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom)
                                                                             
                        elif rep_recherhe_personne == 3:
                            plus_polluante(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 4:
                                Prenom = rechercher_une_personne(csv_to_list, liste_options_menu_Personne)
                            
                        elif rep_recherhe_personne == 5:
                                recherche_personne_en_cours = False
                        
                        else:
                                print("cette option n'existe pas")
                    except:
                        print("erreur")
                    input("Appuyer sur Entrée pour continuer")

            elif rep_menu_principal == 2:
                print("bleh2")
            
            elif rep_menu_principal == 3:
                print("bleh3")

            elif rep_menu_principal == 4:
                print("bleh4")
            
            elif rep_menu_principal == 5:
                appli_running = False
        except:
            print("cette option n'existe pas !")
        input("Appuyer sur Entrée pour continuer")
    print("Au revoir !")
programme_principal()


