class Weapon:
    def __init__(self,name,skills, upgrade_path=None):
        self.name =name
        self.skills =skills
        self.upgrade_path =upgrade_path or []
   
    def show_skills(self):
        skills_text = ",".join(self.skills) if self.skills else "None"
        print(f"\n{self.name} skills: {skills_text}")

   
    def upgrade(self):
        if self.upgrade_path:
            new_weapon = self.upgrade_path.pop(0)
            print(f"\nUpgraded to {new_weapon.name}!")
            return new_weapon

standard_shield = Weapon("legendary Shield", ["block","Shiled Bash"], [])
standard_sword = Weapon("legendary Sword", ["block","Shiled Bash"], [])
standard_spear = Weapon("legendary spear", ["block","Shiled Bash"], [])
standard_bow = Weapon("legendary Bow", ["block","Shiled Bash"], [])



class Heroes:
    def __init__(self, name, hero_class, health, attack, defense, speed):
        self.name = name
        self.hero_class = hero_class
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory  =[]
        self.weapon = None
        self.xp=0
        self.level=1
        self.coins=0

    def gain_xp(self, amount):
        self.xp += amount
        print_with_delay(f"\n You gained {amount} XP! (Total XP: {self.xp})")

        if self.xp >= self.level * 10:
            self.level_up()


    def level_up(self):
        self.level_up()
        self.xp=0
        self.attack+=5
        self.defense +=1
        self.health=self.max_health
        print_with_delay(f"\n LEVELED UP! You are now Level {self.level}!")
        print_with_delay(f" Atack increased: {self.attack}")
        print_with_delay(f" Defense Increased: {self.defense}")

    def get_coins (self, amount):
        self.coins += amount 
        print("f\n you earned {amount} coins! (Total: {self.coins})")


    def show_stats(self):
        print("\n" + "=" * 30)
        print(f"{self.name} the {self.hero_class}")
        print("-"*30)
        print(f"health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print("="* 40)
        if self.weapon:
            self.weapon.show_skills()
        self.show_inventory()
   
    def show_inventory(self):
        print("Incentory".center(40))
        total_slots = 5
        items_list = [f"[{item.name}]" for item in self.inventory]
        inventory_slots =" ".join(items_list+ ["[Empty]"] *(total_slots - len(items_list)))
        print(inventory_slots)
        print("=" * 40)


class ShieldHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Shield Hero", health=150, attack= 5, defense=20, speed=4)
        self.trait = "Iron Wall: Reduce damage  taken by 20%"
        self.weapon = standard_shield

class SwordHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Sword Hero", health=120, attack= 15, defense=10, speed=10)
        self.trait = "Blade Master: +10% critical hit chance."
        self.weapon = standard_sword


class SpearHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Spear Hero", health=110, attack= 20, defense=5, speed=12)
        self.trait = "Piercing Thrust: Attacks ignore 8% defense"
        self.weapon = standard_spear


class BowHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Bow Hero", health=100, attack= 13, defense=5, speed=14)
        self.trait = "Deadeye: Accuracy with ranged attacjs increasedd by 12%"
        self.weapon = standard_bow


class Enemy:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


    def show_stats(self):
        print("\n" + "=" * 30)
        print(f"enemy:{self.name}")
        print(f"health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print("="* 30)
        
        
        
        
        
class DarkSpider(Enemy):
    def __init__(self):
        super().__init__(name="DarkSpider", health=20, attack=5, defense=2, speed=8)
