import sys
import math


n = int(input())  # nombre de température à analyser 
j = 0  # car la première valeur n'a aucune autre valeur pour se comparer car c'est la 1ere
temperature_plus_proche_de_zero = 0

for i in input().split(): # chaine qui va devenir une liste
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    #si c'est la première température qui nous est donné
    if j == 0:
        temperature_plus_proche_de_zero = t

    if abs(t) < abs(temperature_plus_proche_de_zero): #si la temperature qui nous est donné est plus petite que celle qui est enregistré jusque la qui est la plus proche de 0 
        temperature_plus_proche_de_zero = t # alors la temperature la plus proche de 0 devient t

    if abs(t) == abs(temperature_plus_proche_de_zero) and t > temperature_plus_proche_de_zero: # si on a deux valeurs qui sont égal (comme 1 et -1) alors on garde celle qui est positive
        temperature_plus_proche_de_zero = t

    j = j + 1 # boucle


print(temperature_plus_proche_de_zero)
