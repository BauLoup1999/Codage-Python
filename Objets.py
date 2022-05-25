class Player:

    def __init__(self, pseudo, health, attack): #Constructeur, et Self se mets automatiquements, qui donne le contexte
        self.pseudo = pseudo # on créé un nv attribut et on affecte la valeur qui recupere du constructeur
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur test", pseudo, "/Points de vie: ", health, "/ Attaque", attack)

    def get_pseudo(self): # pr recuperer le pseudo
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        damage = self.attack

        
        if self.has_weapon(): # # si le joueur a une arme
            
            damage += self.weapon.get_damage_amount() # # ajoute les dégats de l'arme au point d'attaque du joueur

        target_player.damage(damage)

    
    def set_weapon(self, weapon): # méthode pour changer l'arme du joueur
        self.weapon = weapon

    # méthode pour verifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None 