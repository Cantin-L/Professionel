'''
Auteur : Cantin L.
Site web : https://itliocorp.fr
Version : 0.1
License : MIT 3.0

Sujet : Création d'une fonction
1. Créer une fonction étoile mettre un paramétres "n";
2. Faire une boucle conditionnel qui permet faire le nombre de ligne que tu veux;
3. Afficher a chaque nouvelle ligne une étoile en plus.

Résultat final à faire:

*
**
***
****
*****
******
*******
********
*********
**********

Notions : Afficher une variable, Création d'une fonction, Boucle conditionnel, Commentaires

Fonction à utiliser :
def(...)
print(...)
for():

'''

def étoile(n):
    for n in range (0,n+1):
        print(n*"*")

        
étoile(10)