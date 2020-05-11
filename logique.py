import random 
import itertools 

# nom
def nom ():
    with open('liste_projet/names.txt','r') as file:
        fichier_nom = file.read()
        liste_nom = fichier_nom.split("\n") 
        liste = list(liste_nom)
    alea = random.choices(liste,k=10)
    
    list_nom = list()
    
    for i in alea: 
        list_nom.append(i)
    
    return list_nom

# fonction pour age

def age():
    age = list(range(18,55))
    random.shuffle(age)
    l_age = random.choices(age,k=10)
    list_age = list()

    for i_a in l_age:
        list_age.append(i_a) 
    return list_age

# fonction pour le Sexe

def sexe():
    sexe = ['M','F']
    rand_sexe = random.choices(sexe,k=10)
    liste_sexe = list()

    for s in rand_sexe:
        liste_sexe.append(s)
    return liste_sexe

# def dictionnaire_personne():
cles=["nom"]
sexe =sexe()
age =age()
nom =nom()  
liste_p = dict()
for (n,a,s) in itertools.zip_longest(nom, age, sexe): 
    liste_p.update({"nom":n, "age":a, "sexe":s}) 

print(liste_p)