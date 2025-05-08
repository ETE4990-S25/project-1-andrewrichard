from base_weapon import load_weapons,Weapon

class Player:
    def __init__(self, name, health, speed, weapon_name, defense=0):  
   
        self.name = name
        self.health = health
        self.max_health = health
        self.speed = speed
        self.status_effects = {}
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.defense = defense  
        self._defense_boost = 0
        self._defense_boost_duration = 0
        self.alert = False

        self.weapon = load_weapons().get(weapon_name)  # Load weapons and get the specific one
        if self.weapon is None:  # Handle the case where the weapon_name is invalid
            print(f"Warning: Weapon '{weapon_name}' not found!  Defaulting to no weapon.")
            self.weapon = Weapon(name="Unarmed", damage=0)  # Ensure it's a Weapon object
            self.attack = 0
        else:
            self.attack = self.weapon.base_damage  # Initialize attack based on the weapon's damage

    def take_damage(self, damage):
        incoming_damage = damage
        if self._defense_boost_duration > 0:
            incoming_damage = int(damage * (1 - self._defense_boost / 100))
            print(f"{self.name} reduces incoming damage by {self._defense_boost}%!")

        total_damage = max(0, incoming_damage - self.defense)  # Apply defense here
        self.health -= total_damage

        print(f"{self.name} takes {total_damage} damage. Remaining HP: {self.health}/{self.max_health}")

        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def use_weapon_skill(self, skill_name, enemy=None, enemies=None):
        """Uses a weapon skill."""
        self.weapon.use_skill(skill_name, player=self, enemy=enemy, enemies=enemies)

    def handle_status_effects(self):
        """Processes status effects like poison and defense boosts."""

        # Track if any effects printed, to insert spacing after
        printed_effects = False

        # Handle poison
        if "poison" in self.status_effects:
            poison = self.status_effects["poison"]
            damage = poison["damage_per_turn"]
            print(f"{self.name} is suffering from poison.")
            self.health-=(damage)
            poison["duration"] -= 1
            if poison["duration"] <= 0:
                print(f"{self.name} has recovered from the poison.")
                del self.status_effects["poison"]
            printed_effects = True

        # Handle defense boost
        if "defense_boost" in self.status_effects:
            buff = self.status_effects["defense_boost"]
            percent = buff.get("reduction_percent", 0)
            turns_left = buff.get("duration", 0)

            if turns_left > 0:
                self._defense_boost = percent
                self._defense_boost_duration = turns_left
                self.status_effects["defense_boost"]["duration"] -= 1
                print(f"{self.name}'s defense is boosted by {percent}% for {turns_left} more turn.")
            else:
                self._defense_boost = 0
                self._defense_boost_duration = 0
                del self.status_effects["defense_boost"]
                print(f"{self.name}'s defense boost has wore off.")
            printed_effects = True

        if printed_effects:
            print()  # Add an empty line before the action menu


    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        """Levels up the player."""
        self.level += 1
        self.xp = 0  # Reset XP
        self.max_health += 10  # Example stat increase
        self.health = self.max_health  # heal on level up
        self.speed += 5  # Example stat increase
        self.defense += 2  # Example defense increase
        print(f"{self.name} leveled up! Now at level {self.level}.")

    def display_status(self):
        if self.weapon:
            skill_names = [skill.name for skill in self.weapon.skills]
            weapon_name = self.weapon.name
        else:
            skill_names = []
            weapon_name = "None"
        print(f"""
        -----------------------------------
              {self.name} - LV. {self.level}
        -----------------------------------
        Health: {self.health:<5}/{self.max_health:<5}
        Speed: {self.speed:<5}
        Level: {self.level:<5}
        XP: {self.xp:<5}
        Defense: {self.defense:<5}
        -----------------------------------
        Weapon: {weapon_name}
        Skills: {', '.join(skill_names)}
        -----------------------------------
        """)

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"- Added {item.name} to your inventory.")

    def view_inventory(self):

        print("\n---- INVENTORY ----")
        if not self.inventory:
            print("[EMPTY]")
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item.name} - {item.effect['description']}")
        print("-------------------")

    def use_item(self, index):
        """Uses an item from the inventory."""
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            if hasattr(item, 'use') and callable(getattr(item, 'use')):  # generic check
                if item.use(self):
                    item.amount -= 1
                    if item.amount <= 0:
                        self.inventory.pop(index)
                    return True
            print(f"{item.name} can't be used.")
        else:
            print("Invalid item selection.")
        return False


# Hero Classes
class Shield(Player):
    def __init__(self, weapon_name="Small Shield"):
        super().__init__("Shield Hero", 160, 50, weapon_name, defense=20)  # High defense

class Sword(Player):
    def __init__(self, weapon_name="Long Sword"):
        super().__init__("Sword Hero", 120, 75, weapon_name, defense=10)  # Balanced defense

class Spear(Player):
    def __init__(self, weapon_name="Pike"):
        super().__init__("Spear Hero", 130, 60, weapon_name, defense=15)  # Medium defense

class Bow(Player):
    def __init__(self, weapon_name="Hunter Bow"):
        super().__init__("Bow Hero", 100, 100, weapon_name, defense=5)  # Low defense
