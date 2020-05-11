import random 
import itertools 
import csv
# nom
def nom ():
    with open('liste_projet/names.txt','r') as file:
        fichier_nom = file.read()
        liste_nom = fichier_nom.split("\n") 
        liste = list(liste_nom)
    alea = random.choices(liste,k=50)
    
    list_nom = list()
    
    for i in alea: 
        list_nom.append(i)
    
    return list_nom

# nom
def pays():
    with open('liste_projet/pays.txt','r') as file:
        fichier_nom = file.read()
        liste_nom = fichier_nom.split("\n") 
        liste = list(liste_nom)
    pays = random.choices(liste,k=50)
    
    list_pays = list()
    
    for i in pays: 
        list_pays.append(i)
    
    return list_pays

# fonction pour age

def age():
    age = list(range(18,55))
    random.shuffle(age)
    l_age = random.choices(age,k=50)
    list_age = list()
    for i_a in l_age:
        list_age.append(i_a) 
    return list_age

# fonction pour le Sexe

def sexe():
    sexe = ['M','F']
    rand_sexe = random.choices(sexe,k=50)
    liste_sexe = list()

    for s in rand_sexe:
        liste_sexe.append(s)
    return liste_sexe

# def dictionnaire_personne():

# les variables contenant la liste pour créer une personne 

cles=["nom"]
sexe =sexe()
age =age()
nom =nom()
pays = pays()  

liste_final = list()
for (n,a,s,p) in itertools.zip_longest(nom, age, sexe,pays): 
    liste_final.append({"nom":n, "age":a, "sexe":s,"pays":p})
    # pour ecrire dans un fichier csv    
    with open('personne.csv','w',newline='') as f_csv:
        nom_col = ["nom","age","sexe","pays"]
        csv_p = csv.DictWriter(f_csv,fieldnames=nom_col)
        csv_p.writeheader()
        for p in liste_final:
            csv_p.writerow(p)

print(liste_final)