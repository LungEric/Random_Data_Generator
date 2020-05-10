import random 

with open('liste_projet/names.txt','r') as file:
    fichier_nom = file.read()
    liste_nom = fichier_nom.split("\n") 
    liste = list(liste_nom)

alea = random.choices(liste,k=10)

# for i in alea: 
#     print({"Nom":i})
    
# age
age = list(range(18,55))
random.shuffle(age)
l_age = random.choices(age,k=10)
for i_a in l_age: 
    for i in alea:
        print({"Nom":i,"Age":i_a})
        

