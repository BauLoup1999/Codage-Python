

# 1ere boucle : for = pour une valeure de départ 1, jusqu'a une valeur finale 5 

for num_client in range (1, 6): # si on veut de 1 a 5 il faut mettre une valeure au dessus du max que l'on veut, donc 6 ici
    print("Vous êtes le client N°", num_client)


# deuxieme boucle : for each : pour chaque valeur d'une liste données

emails = ['test@gmail.com', 'test2@gmail.com', 'test3@gmail.com']

blacklist = ['test3@gmail.com']

for email in emails: # pour chaqu'une des valeurs, j'affiche "email envoyé à "l'email en question"
    
    if email in blacklist : # ici on créé une "blacklist", c'est a dire une condition dans laquelle on n'enverra le mail si il est dans la variable blacklist
        print("Email {} interdit ! envoi impossible...".format(email))
        continue # il existe aussi la fonction break, qui arrête completement la boucle si, dans notre cas, on tombe sur une variable venant de blacklist
    print("Email envoyé à ", email)


# 3eme boucle : While = tant qu'une condition est vrai, avc un exemple d'un salarié gagnant 1500€/mois

Salary = 1500

while Salary < 2000:
    Salary += 120 # va rajouter 120 tant que le salaire est < a 2000 (1620, 1740 etc)
    print("votre salaire actuel est de ",Salary, "€")


