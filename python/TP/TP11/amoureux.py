ATM={'Armand':'Beatrice', 'Beatrice':'Cesar', 'Cesar':'Dalida', 'Dalida':'Cesar', 'Etienne':'Beatrice', 'Firmin':'Henri', 'Gaston':'Beatrice','Henri':'Firmin'}

def couples(amoureux):
    liste_couples = []
    couple = ()
    for personne, amoureu in amoureux.items():
        if personne == amoureux[amoureu]:
            
