from items import FirstItems

class Heroes:
    def __init__(self,name,hero_class,health,attack,defense):
        self.name = name
        self.hero_class =hero_class
        self.health=health
        self.attack=attack
        self.defense=defense
        self.inventory=FirstItems.get(hero_class,[])

    def show_stats(self):
        print(f"{self.name} the {self.hero_class}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.description}")

    
class ShieldHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Shield Hero",health=150,attack=5,defense=20)

class SwordHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Sword Hero",health=120,attack=15,defense=10)


class SpearHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Spear Hero",health=110,attack=20,defense=5)

class BowHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Bow Hero",health=100,attack=13,defense=5)


class Monster:
    def __init__(self, name, health, attack,defense, reward):
        self.name=name
        self.health=health
        self.attack=attack
        self.defense=defense
        self.reward=reward

class Goblin(Monster):
    def __init__(self):
        super().__init__(name=Goblin, health=30, attack=10,defense=5,reward=3)

class Wolf(Monster):
    def __init__(self):
        super().__init__(name=Wolf, health=40, attack=15,defense=10,reward=5)

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name=Skeleton, health=45, attack=20,defense=5,reward=5)

class Spider(Monster):
    def __init__(self):
        super().__init__(name=Spider, health=25, attack=10,defense=5,reward=2)

class Ogre(Monster):
    def __init__(self):
        super().__init__(name=Ogre, health=50, attack=30,defense=15,reward=6)








        