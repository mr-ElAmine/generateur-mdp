# By moi
import string
from re import sub
from random import *

# liste des lettres miniscules 
list_lettres_mini = list(string.ascii_lowercase)

# liste des lettres majuscules 
list_lettres_maju = list(string.ascii_uppercase)

# lists des chiffre 
list_chiffre = list(string.digits)

caractere = []
caractere.append(list_lettres_mini)
caractere.append(list_lettres_maju)
caractere.append(list_chiffre)

caractere = list(sub("\ |\'|\,|\]|\[", "", str(caractere)))

#def gen-mdp
def gen_mdp(longueur, nb_mdp):
    mdp=str()
    list_mdp=[]
    for j in range(nb_mdp):
        shuffle(caractere)
        for x in range(longueur):
            mdp+=caractere[x]
        list_mdp.append(mdp)
        mdp = str()
    return list_mdp