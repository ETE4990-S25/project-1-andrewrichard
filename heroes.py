from items import default_weapons


class Heroes:
    def __init__(self, name, hero_class, health, attack, defense, speed,trait, skills):
        self.name = name
        self.hero_class = hero_class
        self.health = health
        self.attack = attack 
        self.defense = defense
        self.speed = speed
        self.level =1
        self.xp =0
        self.trait = trait
        self.inventory  =[]
        self.skills = skills
        self.coins = 0

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins! Total coins: {self.coins}")

   
         
    def show_stats(self):
        stats_display = f"""
        -----------------------------------
                    HERO STATUS
        -----------------------------------
            Class: {self.hero_class:<15}
        -----------------------------------
        Health: {self.health:<5}    Attack: {self.attack:<5}
        Defense: {self.defense:<5}  Speed: {self.speed:<5}
        Level: {self.level:<5}      XP: {self.xp:<5}
        -----------------------------------
        Trait: {self.trait}
        Skills: {','.join(self.skills)}
        """
        print(stats_display)

    def open_inventory(self):
        total_slots = 5

        item_counts ={}
        for item in self.inventory:
            item_counts[item] = item_counts.get(item, 0) +1

           
        inventory_list = []
        for item, count in item_counts.items():
            item_details = f"{item.name} x{count}" if count > 1 else str(item)
            inventory_list.append(item_details)

           
            while len(inventory_list) < total_slots:
                inventory_list.append("[Empty]")

            print("\n" + "-" * 38)
            print("" * 5 + "INVENTORY")
            print("-" * 38)
            for i in inventory_list:
                print(f"[{i:<30} ]")
            print("-"* 35)  
   
    def add_item(self,item):
        self.inventory.append(item)

    def check_level_up(self):
        xp_threshold = self.level * 100  
        if self.xp >= xp_threshold:
            self.level += 1
            print(f"\n{self.name} leveled up to Level {self.level}!")


class ShieldHero(Heroes):
    def __init__(self, name):
        super().__init__(name, "Shield Hero", 150, 5, 20, 4, "Iron Wall: Reduces damage by 20%", ["Block", "Fortify", "Reflecct"])
        self.weapon = default_weapons["Shield Hero"]
        self.inventory.append(self.weapon.name)
class SwordHero(Heroes):
    def __init__(self, name):
        super().__init__(name, "Sword Hero", 120, 15, 10, 10, "Blade Master: +10% critical hit chance", ["Slash", "Power Strike"])
        self.weapon = default_weapons["Sword Hero"]
        self.inventory.append(self.weapon.name)

class SpearHero(Heroes):
    def __init__(self, name):
        super().__init__(name, "Spear Hero", 110, 20, 5, 12, "Piercing Thrust: Ignores 8% defense", ["Pierce", "Whirlwind"])
        self.weapon = default_weapons["Spear Hero"]
        self.inventory.append(self.weapon.name)

class BowHero(Heroes):
    def __init__(self, name):
        super().__init__(name, "Bow Hero", 100, 13, 5, 14, "Deadeye: +12% accuracy", ["Quick Shot", "Snipe"])
        self.weapon = default_weapons["Bow Hero"]
        self.inventory.append(self.weapon.name)
       
#