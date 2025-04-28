from base_weapon import load_weapon
import time

weapons = load_weapon()


class Player:
    def __init__(self, name, health, attack, defense, speed, trait, weapon):
        self.name = name
        self.hero_class = name 
        self.trait = trait
        self.weapon = weapon
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.status_effects = {}
        self.xp = 0
        self.level = 1
        self.inventory = []
        self.alert = False
        self.mana = 0
        self.max_mana = 100
    
    def attack_target(self, target):
        damage = self.attack
        damage = self.apply_status_effects(target, damage)  # Fix applied here
        if damage is None:
            damage = self.attack
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        time.sleep(1)
        target.take_damage(damage)
        time.sleep(0.5)

    def take_damage(self, damage):
        if damage is None:
            return 0 
        
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")
        return damage
    
    def apply_status_effects(self, target, damage):
        to_remove = []
        # Modify damage based on the player's status effects
        for effect, details in self.status_effects.items():
            if details["duration"] > 0:
                if "damage_boost" in details:
                    print(f"{self.name} boosts damage due to {effect}.")
                    damage += details["damage_boost"]
                elif "damage_reduction" in details:
                    print(f"{self.name} reduces damage due to {effect}.")
                    damage -= details["damage_reduction"]
                details["duration"] -= 1
            else:
                to_remove.append(effect)
        
        # Remove expired effects
        for effect in to_remove:
            print(f"{effect} wore off.")
            del self.status_effects[effect]
        
        # Return modified damage
        return max(damage, 0)

    def display_status(self):
        skill_names = [skill.name for skill in self.weapon.skills]
        print(f"""
        -----------------------------------
                {self.hero_class} - LV. {self.level}
        -----------------------------------
        Health: {self.health:<5}    
        Attack: {self.attack:<5}
        Defense: {self.defense:<5}  
        Speed: {self.speed:<5}
        Level: {self.level:<5}      
        XP: {self.xp:<5}
        -----------------------------------
        Trait: {self.trait}
        Skills: {', '.join(skill_names)}
        -----------------------------------
        """)

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"- Added {item.name} to your inventory.")
    
    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Removed {item} from your inventory.")
        else:
            print(f"{item} is not in your inventory.")
    
    def view_inventory(self):
        if not self.inventory:
            print("[EMPTY]")
        else:
            print("\n----INVENTORY----")
            for i, item in enumerate(self.inventory, start=1):
                if hasattr(item, "effect") and isinstance(item.effect, dict) and "description" in item.effect:
                    print(f"{i}. {item.name} - {item.effect['description']}")
                else:
                    print(f"{i}. {item.name}")
            print("----------------------")
    
    def level_up(self):
        self.level += 1
        self.xp -= self.level * 100
        self.health += 10  
        self.attack += 2
        self.defense += 2
        self.speed += 1
        print(f"{self.name} leveled up! New stats: Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}")
    
    def use_skill(self,skill_name, target=None, enemies=None):
        self.weapon.use_skill(skill_name,user=self, target=target, enemies=enemies)
        
    

class Shield(Player):
    def __init__(self, name ="Shield Hero"):
        weapon =weapons ["Small Shield"]
        super().__init__(name, 160, 40, 200, 50,"Tanker - High defense, low attack", weapon=weapon)

class Sword(Player):
    def __init__(self, name="Sword Hero"):
        weapon = weapons["Long Sword"]
        super().__init__(name, 120, 100, 100, 75, "Balanced - High offense, moderate defense", weapon = weapon)

class Spear(Player):
    def __init__(self, name="Spear Hero"):
        weapon=weapons ["Pike"]
        super().__init__(name, 130, 75, 120, 70, "Agile - Moderate offense, high speed", weapon =weapon)

class Bow(Player):
    def __init__(self, name="Bow Hero"):
        weapon = weapons ["Hunter Bow"]
        super().__init__(name, 100, 80, 50, 100, "Ranged - High critical chance, low defense", weapon = weapon)
