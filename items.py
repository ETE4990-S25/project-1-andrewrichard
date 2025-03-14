from items import FirstItems

class Heroes:
    def __init__(self,name,hero_class,health,attack,defense,):
        self.name = name
        self.hero_class =hero_class
        self.health=health
        self.attack=attack
        self.defense=defense
        self.inventory=FirstItems.get(hero_class,[])
    

    def show_stats(self):
        print("\n" + "=" *30)
        print(f"{self.name} the {self.hero_class}")
        print("-" *30)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print("=" * 40)

        print(" Inventorty:".center(40))

        total_slots = 5
        items_list = [f"[{item.name}]" for item in self.inventory]
        inventory_slots = " ".join(items_list + ["[Empty]"] * (total_slots - len(items_list)))
        print(inventory_slots)

class ShieldHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Shield Hero",health=150,attack=5,defense=20,)

class SwordHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Sword Hero",health=120,attack=15,defense=10)


class SpearHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Spear Hero",health=110,attack=20,defense=5)

class BowHero(Heroes):
    def __init__(self,name):
        super().__init__(name, "Bow Hero",health=100,attack=13,defense=5)

