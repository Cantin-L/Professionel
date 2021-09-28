'''
Auteur : Cantin L.
Site web : https://itliocorp.fr
Version : 0.1
License : MIT 3.0

Sujet : 
1. Demander à l'utilisateur de rentrer un nombre;
2. Mettre ce nombre dans une variable "nbr";
3. Ajouter 5 a "nbr" puis le multiplier par 4;
4. Afficher le résultat final;

Notions : Variable, Importation de valeur, Types de variable, Afficher une variable, Fonction, Commentaires

Fonction à utiliser :
input(...)
print(...)
def ...():
if (): 
'''

def main(nbr) :
    nbr = ( nbr + 5 ) * 4
    print("Le nombre final est",nbr)

if (__name__ == '__main__'):
    main(int(input("Rentrer un nombre : ")))

