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


FirstItems={
    "Shield Hero": [

        Item("Wood Shield", "Shield made from the Grand Oak Tree", "Weakhand",0,0,10,0,0),
        Item("Wood Armor", "Armor made from the grand", "Body", 0,0,5,0,0)
    ],

    "Sword Hero":[ 
        Item("Stone Sword", "Sword made from swordsmith from local village", "StrongHand",5,2,1,0,0),
        Item("Leather Armor","Light Armor for better agility","body",0,0,2,0,0)
    ],

    "Bow Hero": [
        Item("Hunter's Bow","Bow used from the village's most skilled hunters","Stronghand",5,2,0,0,0),
        Item("Arrows","set of arrows for long range attacks","accessory",0,1,0,0,0, )

    ],

    "Spear hero": [
        Item("Long stone spear","Long spear made midrange attacks", "Stronghand",4,2,0,0,0),
        Item("Wood Armor", "Armor made from the grand", "Body", 0,0,5,0,0)

    ]
}

