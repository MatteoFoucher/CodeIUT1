#Exo1
liste = [1,2,3,4,5,6,7,8,9]
def trouver_dans_liste(liste, cible):
    ind = 0
    trouve = False
    while ind < len(liste) and not trouve:
        if liste[ind] == cible:
            trouve = True
        ind += 1
    return trouve

#print(trouver_dans_liste(liste, 16))

dico = {'a':10, 'b':6 ,'c':2}

def cumuler_jusqu_a_seuil(dico, seuil):
    total = 0
    ind_dico = 0
    liste_cles = []
    for elem in dico.keys():
        liste_cles.append(elem)
    while total <= seuil and ind_dico < len(liste_cles):
        total += dico[liste_cles[ind_dico]]
        ind_dico += 1
    return total
#print(cumuler_jusqu_a_seuil(dico, 20))

#Exo2


