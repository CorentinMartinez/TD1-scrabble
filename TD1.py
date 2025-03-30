## Exercice 1+2

#On charge le dictionnaire, on crée une fonction qui renvoie un bouléen pour savoir si un mot est faisable ou pas avec notre tirage puis on crée une fonction qui utilise la fonction précédente pour construire le liste des mots possibles puis extrait le mot le plus long que contient cette liste.

f = open('frenchssaccent.dic','r')
liste=[]
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()

def motpossible(tirage,mot):
    t=0
    r=[]
    l=tirage.copy() #on crée une copie qu'on peut modifier sans problème (si on touche à tirage ça posera problème dans le programme plus grand mot
    for c in mot:
        if c not in l:
            return False
        l.remove(c) #comme ça on ne réutilise pas 2 fois la même lettre du tirage
    return True

def plusgrandmot(tirage):
    mot_possible=[]
    plusgrand=0
    for mot in liste:
        if motpossible(tirage,mot)==True:
            mot_possible.append(mot) #on crée notre liste des mots possibles
    if len(mot_possible)==0:
        return None, 0
    m=len(mot_possible[0])
    for mot in mot_possible:
        if len(mot)>=m:
            m=len(mot)
            plusgrand=mot
            if m==len(tirage): #on s'arrête car on sait qu'on ne pas avoir de mot plus long que notre tirage ce qui permet de ne pas parcourir tous le dictionnaire
                return plusgrand
    return plusgrand

## Exercice 3

#On peut prendre comme base de données un dictionnaire avec les lettres comme clé et les scores des lettres comme valeur

scrabble_points = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 10, 'l': 1, 'm': 2, 'n': 1, 'o': 1, 'p': 3, 'q': 8, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 10, 'x': 10, 'y': 10, 'z': 10
}

def score(mot):
    score=0
    for cle in mot:
        score=score+scrabble_points[cle]
    return score

def meilleurmot(tirage):
    mot_possible=[]
    plusgrand=0
    for mot in liste:
        if motpossible(tirage,mot)==True:
            mot_possible.append(mot)
    if len(mot_possible)==0:
        return None, 0
    max_score=score(mot_possible[0])
    for mot in mot_possible:
        if score(mot)>=max_score:
            max_score=score(mot)
            plusgrand=mot
    return (plusgrand,max_score)

## Exercice 4

def motpossiblejoker(tirage,mot):
    t=0
    joker=1
    l=tirage.copy()
    if '?' in tirage:
        for c in mot:
            if c not in l and joker==0: #joker utilisé
                return False
            if c not in l and joker==1: #joker pas encore utilisé
                joker=joker-1
            if c in l: #pour ne pas utiliser 2 fois la même lettre du tirage
                l.remove(c)
        return True
    else: #cas ou on a pas de joker dans notre tirage donc on peut réutiliser le programme précédent
        return motpossible(tirage,mot)

def meilleurmotjoker(tirage):
    mot_possible=[]
    plusgrand=0
    l=tirage.copy()
    for mot in liste:
        if motpossiblejoker(tirage,mot)==True:
            mot_possible.append(mot)
    if len(mot_possible)==0:
        return None, 0
    score_max=0
    meilleur_mot=''
    for mot in mot_possible:
        s=score(mot)
        for c in mot:
            if c not in l: #ça veut dire qu'on a utilisé un joker pour mettre cette lettre
                s=s-score(c) #permet de compter les '?' comme valant 0
            if c in l:
                l.remove(c)
        if s>=score_max: #on a bien le bon score pour tous les mots donc on peut les comparer pour trouver celui qui a les meilleurs scores
            score_max=s
            meilleur_mot=mot
        l=tirage.copy() #on réinitialise notre copy qui a été modifié
    return (meilleur_mot,score_max)






