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
        print(f"{self.name} attacks {target.name} for {damage} damage!.")
        target.take_damage(damage)
        time.sleep(1)

    def take_damage(self, damage):
        if damage is None:
            damage = 0

        damage = self.apply_status_effects(damage)      
        
        self.health -= damage
        if self.health < 0:
            self.health = 0

    
    def apply_status_effects(self, damage):
        if damage is None:
            return 0
        to_remove = []
        
        for effect, details in self.status_effects.items():
            if details["duration"] > 0:
               
                if effect == "Poison":
                    poison_damage = details['damage_per_turn']
                    print(f"{self.name} suffers {poison_damage} poison damage!")
                    damage += poison_damage
        
                elif effect == "defense_boost":
                    reduction = damage * (details["reduction_percent"] / 100)
                    damage -= reduction 
                    print(f"{self.name}'s defense boosts damage reduction by {reduction}%.")
                    print(f"{self.name} takes {damage} damage! ({self.health}/{self.max_health} HP left)")

                details["duration"] -= 1
                if details["duration"] <= 0:
                    print(f"{self.name} is no longer affected by {effect}.")
            else:
                to_remove.append(effect)

        for effect in to_remove:
            del self.status_effects[effect]
        return damage
    
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
            print(f"- Removed {item.name} from your inventory.")
        else:
            print(f"- {item.name} is not in your inventory.")

    def view_inventory(self):
        print("\n---- INVENTORY ----")
        if not self.inventory:
            print("[EMPTY]")
        else:
            for i, item in enumerate(self.inventory, 1):
                desc = item.effect["description"] if hasattr(item, "effect") and isinstance(item.effect, dict) and "description" in item.effect else ""
                print(f"{i}. {item.name} {f'- {desc}' if desc else ''}")
        print("-------------------")

    def level_up(self):
        self.level += 1
        self.xp -= self.level * 100
        self.health += 120
        self.attack += 2
        self.defense += 2
        self.speed += 1
        print(f"{self.name} leveled up! New stats — Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}")

    def use_skill(self, skill_name, target=None, enemies=None):
        if enemies:
            self.weapon.use_skill(skill_name, user=self, target=enemies)
        else:
            self.weapon.use_skill(skill_name, user=self, target=target)


# Hero Classes
class Shield(Player):
    def __init__(self, name="Shield Hero"):
        super().__init__(name, 160, 40, 200, 50, "Tanker - High defense, low attack", weapon=weapons["Small Shield"])

class Sword(Player):
    def __init__(self, name="Sword Hero"):
        super().__init__(name, 120, 100, 100, 75, "Balanced - High offense, moderate defense", weapon=weapons["Long Sword"])

class Spear(Player):
    def __init__(self, name="Spear Hero"):
        super().__init__(name, 130, 75, 120, 70, "Agile - Moderate offense, high speed", weapon=weapons["Pike"])

class Bow(Player):
    def __init__(self, name="Bow Hero"):
        super().__init__(name, 120, 80, 50, 100, "Ranged - High critical chance, low defense", weapon=weapons["Hunter Bow"])
