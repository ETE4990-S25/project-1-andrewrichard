import json 

class Item:
    def __init__(self, name, item_type, effect =None, amount= None, credit = None):
        self. name= name
        self.type = item_type
        self.effect = effect
        self.amount = amount 
        self.credit = credit
    
    def __repr__(self):
        return f"Item(name={self.name}, type={self.type}, effect ={self.effect}, amount = {self.amount}, credit= {self.credit})"
    
    def clone(self):
        return self.__class__(self.name, self.effect, self.amount, self.credit)

class consumable(Item):
    def __init__(self, name, effect, amount, credit):
        super().__init__(name,"consumable", effect,amount, credit)

    def use(self, hero):
        if self.effect == "restore_hp":
            old_hp = hero.health
            hero.health = min(hero.health + self.amount, hero.max_health)
            healed=hero.health - old_hp
            print(f"{hero.name} restored {self.amount} hp ({hero.health}/{hero.max_health})")

        if self.effect == "restore_mana":
            hero.mana = min(hero.mana + self.amount, hero.max_mana)
            print(f"{hero.name} restored {self.amount} Mana! ({hero.mana}/{hero.max_mana})")
   
class useable(Item):
    def __init__(self, name, effect, amount,  credit):
        super().__init__(name, "useable", effect, amount, credit)

    def use(self):
        print(f"{self.name} used. Effect: {self.effect}")
    
   


def load_items():
     with open("items.json") as f:
         data = json.load(f)
         
     items = {}
     
     for item_key, item_data in data.items():
         if item_data["type"] == "consumable":
             items[item_key] = consumable(
                name=item_data["name"],
                effect=item_data["effect"],
                amount=item_data["amount"],
                credit=item_data["credit"]
            )
         elif item_data["type"] == "useable":
            items[item_key] = useable(
                name=item_data["name"],
                effect=item_data["effect"],
                amount=item_data["amount"],
                credit=item_data["credit"]
            )
         else:
            items[item_key] = Item(
                name=item_data["name"],
                item_type=item_data["type"],
                effect=item_data.get("effect", ""),
                amount=item_data.get("amount", 0),
                credit=item_data.get("credit", 0)
            )

     return items
                     
                            
           
