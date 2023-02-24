# Projet : Générateur de mots de passe aléatoires 

Ce code est une fonction Python qui génère un nombre spécifié de mots de passe aléatoires d'une longueur spécifiée. La fonction prend deux arguments : longueur (longueur du mot de passe) et nb_mdp (nombre de mots de passe à générer).

La fonction crée d'abord des listes de lettres minuscules, de lettres majuscules et de chiffres en utilisant le module string. Elle combine ensuite ces listes en une seule liste appelée caractere, la mélange et génère un mot de passe de la longueur spécifiée en sélectionnant des caractères dans la liste mélangée. Ce processus est répété pour le nombre spécifié de mots de passe, et une liste des mots de passe générés est renvoyée.

Pour utiliser cette fonction, vous pouvez l'importer dans votre script Python ou votre environnement interactif et l'appeler avec les arguments souhaités.

## Examples :

```python
from gen_mdp import gen_mdp
passwords = gen_mdp(10, 5)
print(passwords)
```
Cela générera 5 mots de passe aléatoires de longueur 10 et les affichera dans la console.