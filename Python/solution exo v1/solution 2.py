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

Notions : Afficher une variable, Importation de valeur, Commentaires

Fonction à utiliser :
input(...)
print(...)
'''

nbr = int(input("Rentrer un nombre : "))
nbr = ( nbr + 5 ) * 4
print("Le nombre final est",nbr)