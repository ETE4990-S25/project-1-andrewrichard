# items.py
class Weapon:
    def __init__(self, name, skills,damage, durability, upgrade_level =0):
        self.name = name
        self.skills = skills
        self.damage = damage
        self.durability = durability
        self.upgrade_level = upgrade_level
    
    def __str__(self):
        return f"""
    ------------------------------
    {self.name:<15}
    ------------------------------
    Damage: {self.damage}
    Durability: {self.durability}
    Upgrade Level: {self.upgrade_level}
    Skills: {', '.join(self.skills)}
    ------------------------------
    """

# Default weapons for each hero type
default_weapons = {
    "Shield Hero": Weapon("Guardian Shield", ["Shield Bash", "Fortress Stance"], damage=5, durability=50,),
    "Sword Hero": Weapon("Knight's Blade", ["Swift Slash", "Power Thrust"], damage=10, durability=40, ),
    "Spear Hero": Weapon("Dragon Spear", ["Lance Charge", "Piercing Strike"], damage=12, durability=35,),
    "Bow Hero": Weapon("Hunter's Bow", ["Longshot", "Rapid Fire"], damage=8, durability=30,)
}

class Item: 
    def __init__(self, name, description, stackable =False, max_stack =10):
        self. name =name 
        self.description = description
        self.stackable = stackable 
        self.max_stack =max_stack

    def __str__(self):
        return f"{self.name}: {self.description} (Stackable: {self.stackable}, Max Stack: {self.max_stack})"

healing_potion = Item("Healing Potion", "Restores 20 HP", stackable=True, max_stack =  5)

default_items = {
    "healingPotion": healing_potion 
}

def use(self, hero):
    if self.stackable and hero.inventory.count(self) > 0:
        # Apply effects, e.g., healing for healing potions
        print(f"{self.name} used by {hero.name}.")
        # If it's a healing potion, restore HP
        if self.name == "Healing Potion":
            hero.hp += 20
            hero.inventory.remove(self)
    else:
        print(f"Cannot use {self.name}.")
