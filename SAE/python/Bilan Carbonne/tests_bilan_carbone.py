# fichier de tests de la SAE 1.01 partie 1
# bilan carbone d'activités mystères en septembre 2024

# on importe toutes les fonctions et données définies dans le fichier bilan_carbone
# l'appel de ces fonctions et données doit être préfixé par bc. 
import bilan_carbone as bc  

# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_avant():
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Erika', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('Erika', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-10', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-10', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant((), ('Lucas', '2024-09-01', 67.2, 'type4')) == None
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ()) == None
    assert bc.est_avant((),()) == None


def test_annee():
    assert bc.annee(('Lucas', '2024-09-01', 67.2, 'type3')) == '2024'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'
    assert bc.annee(()) == None
    assert bc.annee(('Lucas', '', 70.08, 'type3')) == None


def test_annee_mois():
    assert bc.annee_mois(('Lucas', '2024-10-01', 67.2, 'type3')) == '2024-10'
    assert bc.annee_mois(('Lucas', '2023-09-01', 67.2, 'type3')) == '2023-09'
    assert bc.annee_mois(()) == None
    assert bc.annee_mois(('Lucas', '', 70.08, 'type3')) == None


def test_max_emmission():
    assert bc.max_emmission([]) == None
    assert bc.max_emmission(bc.liste1) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste2) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste3) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste4) == ('David', '2024-09-27', 21, 'type2')
    assert bc.max_emmission(bc.liste5) == ('Erika', '2024-09-28', 240.5, 'type2')
    assert bc.max_emmission(bc.liste6) == ('Erika', '2024-09-28', 76.56, 'type1')
    assert bc.max_emmission([('Erika', '2024-09-28', 76.56, 'type1'), ('Erika', '2024-09-28', 76.56, 'type1')]) == ('Erika', '2024-09-28', 76.56, 'type1')
    assert bc.max_emmission([('Erika', '2024-09-28', 76.56, 'type1')]) == ('Erika', '2024-09-28', 76.56, 'type1')
 
    
def test_filtre_par_prenom():
    assert bc.filtre_par_prenom([], 'Lucas') == []
    assert bc.filtre_par_prenom(bc.liste5, "Alix") == []
    assert bc.filtre_par_prenom([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')], 'Lucas') == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.filtre_par_prenom(bc.liste1, 'David') == [('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 21, 'type2'), ('David', '2024-09-28', 17, 'type3'), ('David', '2024-09-29', 23, 'type4')]
    assert bc.filtre_par_prenom(bc.liste5, 'Matéo') == [('Matéo', '2024-09-01', 22.62, 'type1'), ('Matéo', '2024-09-02', 6.09, 'type1'), ('Matéo', '2024-09-03', 30.45, 'type1'), ('Matéo', '2024-09-04', 12.18, 'type1'), ('Matéo', '2024-09-05', 22.62, 'type1'), ('Matéo', '2024-09-06', 20.01, 'type1'), ('Matéo', '2024-09-07', 42.63, 'type1'), ('Matéo', '2024-09-08', 18.27, 'type1'), ('Matéo', '2024-09-09', 54.81, 'type1'), ('Matéo', '2024-09-10', 24.36, 'type1'), ('Matéo', '2024-09-11', 9.57, 'type1'), ('Matéo', '2024-09-12', 22.62, 'type1'), ('Matéo', '2024-09-13', 15.66, 'type1'), ('Matéo', '2024-09-14', 26.1, 'type1'), ('Matéo', '2024-09-15', 11.31, 'type1'), ('Matéo', '2024-09-16', 20.88, 'type1'), ('Matéo', '2024-09-17', 25.23, 'type1'), ('Matéo', '2024-09-18', 11.31, 'type1'), ('Matéo', '2024-09-19', 13.05, 'type1'), ('Matéo', '2024-09-20', 13.92, 'type1'), ('Matéo', '2024-09-21', 22.62, 'type1'), ('Matéo', '2024-09-22', 0.87, 'type1'), ('Matéo', '2024-09-23', 21.75, 'type1'), ('Matéo', '2024-09-24', 6.09, 'type1'), ('Matéo', '2024-09-25', 49.59, 'type1'), ('Matéo', '2024-09-26', 13.92, 'type1'), ('Matéo', '2024-09-27', 28.71, 'type1'), ('Matéo', '2024-09-28', 15.66, 'type1'), ('Matéo', '2024-09-29', 33.93, 'type1'), ('Matéo', '2024-09-30', 19.14, 'type1'), ('Matéo', '2024-09-01', 70.08, 'type3'), ('Matéo', '2024-09-02', 18.24, 'type3'), ('Matéo', '2024-09-03', 93.12, 'type3'), ('Matéo', '2024-09-04', 37.44, 'type3'), ('Matéo', '2024-09-05', 70.08, 'type3'), ('Matéo', '2024-09-06', 60.48, 'type3'), ('Matéo', '2024-09-07', 129.6, 'type3'), ('Matéo', '2024-09-08', 55.68, 'type3'), ('Matéo', '2024-09-09', 167.04, 'type3'), ('Matéo', '2024-09-10', 74.88, 'type3'), ('Matéo', '2024-09-11', 30.72, 'type3'), ('Matéo', '2024-09-12', 69.12, 'type3'), ('Matéo', '2024-09-13', 48.0, 'type3'), ('Matéo', '2024-09-14', 81.6, 'type3'), ('Matéo', '2024-09-15', 35.52, 'type3'), ('Matéo', '2024-09-16', 63.36, 'type3'), ('Matéo', '2024-09-17', 77.76, 'type3'), ('Matéo', '2024-09-18', 35.52, 'type3'), ('Matéo', '2024-09-19', 41.28, 'type3'), ('Matéo', '2024-09-20', 43.2, 'type3'), ('Matéo', '2024-09-21', 69.12, 'type3'), ('Matéo', '2024-09-22', 2.88, 'type3'), ('Matéo', '2024-09-23', 68.16, 'type3'), ('Matéo', '2024-09-24', 20.16, 'type3'), ('Matéo', '2024-09-25', 150.72, 'type3'), ('Matéo', '2024-09-26', 43.2, 'type3'), ('Matéo', '2024-09-27', 86.4, 'type3'), ('Matéo', '2024-09-28', 48.0, 'type3'), ('Matéo', '2024-09-29', 103.68, 'type3'), ('Matéo', '2024-09-30', 59.52, 'type3')]
    assert bc.filtre_par_prenom(bc.liste2, "Christophe") == [('Christophe', '2024-09-26', 15, 'type1'), ('Christophe', '2024-09-27', 19, 'type2'), ('Christophe', '2024-09-28', 14, 'type3'), ('Christophe', '2024-09-29', 20, 'type4')]

def test_filtre():
    assert bc.filtre([], 3, 'type1') == []
    assert bc.filtre(bc.liste3, 1, '2024-09-29') == [('David', '2024-09-29', 23, 'type4'), ('Guillaume', '2024-09-29', 22, 'type4')]
    
def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78

def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    
def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False


def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']


def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']


def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2


def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'


def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')

def test_charger_sauver():
    ...

def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None

def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96

# ---------------------------------------------------------------------------------------------
# Ajoutez ici les tests manquants (vos propres fonctions le cas échéant)
# ---------------------------------------------------------------------------------------------

