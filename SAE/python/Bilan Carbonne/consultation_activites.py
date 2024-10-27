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

def affichage_menu_principal(titre):
    print("+-----------------------------------------+")
    print("|Bienvenu sur l'application " + titre + "|")
    print("+-----------------------------------------+")

def affichage2_menu_principal(liste_option):
    print("\n")
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
        return "Le nombre dépasse le maximum !"
    
def rechercher_une_personne(csv_to_list, liste_options_menu_Personne):
    Prenomexist = False
    while Prenomexist == False:
        try:
            Prenom = input("Entrez le prénom de la personne que vous recherchez" + "\n")
            if Prenom in bc.liste_des_personnes(csv_to_list):
                Prenomexist = True
                return Prenom
            else: 
                print("je ne connais pas la personne que vous cherchez, veuillez réessayer")
        except:
            print("je ne connais pas la personne que vous cherchez, veuillez réessayer")

def affichage_menu_recherche_personne(Prenom2, liste_options):  
    print("Que voulez vous savoir sur " + Prenom2 + " ?")
    choix_options(liste_options)

# ici votre programme principal

def programme_principal():
    appli_running = True
    liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Quitter"]
    liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "Chercher une autre personne", "retour"]
    affichage_menu_principal("Bilan Carbonne")
    csv_to_list = charger_csv()
    affichage2_menu_principal(liste_options_menu)
    rep_menu_principal = demander_nombre("Entrez un nombre [1-", len(liste_options_menu))
    while appli_running:
        if rep_menu_principal == '':
            affichage_menu_principal("Bilan Carbonne")
            affichage2_menu_principal(liste_options_menu)
            rep_menu_principal = demander_nombre("Entrez un nombre [1-", len(liste_options_menu))
                
        if rep_menu_principal == 1:
            recherche_personne_en_cours = True
            Prenom = rechercher_une_personne(csv_to_list, liste_options_menu_Personne)
            while recherche_personne_en_cours == True:
                affichage_menu_recherche_personne(Prenom, liste_options_menu_Personne)
                rep_recherhe_personne = demander_nombre("Entrez un nombre [1-", len(liste_options_menu_Personne))
                try:
                    if rep_recherhe_personne == 1:
                        print("\n")
                        print("-------------------------------------")
                        print(Prenom + " a émit " + str(bc.cumul_emmissions(bc.filtre_par_prenom(csv_to_list, Prenom))) + " grammes de Co2" )
                        print("-------------------------------------")
                        print("\n")

                 
                    elif rep_recherhe_personne == 2:
                        print("rien")

                    elif rep_recherhe_personne == 3:
                        print("")

                    elif rep_recherhe_personne == 4:
                        recherche_personne_en_cours = False
                        
                    elif rep_recherhe_personne == 5:
                        recherche_personne_en_cours = False
                        rep_menu_principal = ''
                
                    else:
                        print("cette option n'existe pas")
                except:
                    print("cette option n'existe pas")

        elif rep_menu_principal == 2:
            print("bleh2")
        
        elif rep_menu_principal == 3:
            print("bleh3")

        elif rep_menu_principal == 4:
            print("bleh4")
        
        elif rep_menu_principal == 5:
            appli_running = False
        
        else:
            appli_running = False

programme_principal()


