class Item:
    def __init__(self,name,description,slot,damage,bonus_attack,bonus_defense, max_hp,bonus_magic):
        self.name=name
        self.description = description
        self.slot=slot
        self.damage = damage
        self.bonus_attack=bonus_attack
        self.bonus_defense=bonus_defense
        self.bonus_magic=bonus_magic
        self.max_hp=max_hp

def __str__(self):
    return(f"{self.name}({self.slot})\n"
           f"{self.description}\n"
           f"Damage:{self.damage}, Defense:{self.bonus_defense}, Magic:{self.bonus_magic}, HP:{self.max_hp}") 
