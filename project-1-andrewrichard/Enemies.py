import json
import random
import time 

class Enemy:
    def __init__(self, name, health, attack, defense, speed, traits,level, loot_table =None):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.traits = traits
        self.level = level  
        self.status_effects = {}  
        self.low_health_threshold = 0.3 
        self.loot_table = loot_table or []
    
    def take_damage(self, damage):
        if damage is None:
            return 0 
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return damage

    def attack_target(self,target):
        damage = self.attack
        damage = self.apply_status_effects(target,damage)
        if damage is None:
            damage = self.attack
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        time.sleep(1)
        target.take_damage(damage)
        time.sleep(0.5)
  
    def calulate_xp(self, player_level):
        base_xp=50
        level_diff = self.level/player_level
        random_multiplier = random.uniform(0.8,1.2)
        xp = int(base_xp * level_diff * random_multiplier)
        return max(10,xp)
    
    def drop_loot(self):
        dropped = []
        for loot in self.loot_table:
            if random.random() < loot["chance"]:
                dropped.append(loot["item"])
        return dropped
    
    def apply_status_effects(self,target,damage):
        
        if "Venomous" in self.traits:
            venom = self.traits["Venomous"]
            if random.random() < 0.5: 
                print(f">>> {self.name} poisons {target.name}!")
                if "Poison" not in target.status_effects:
                    target.status_effects["Poison"] = {
                        "damage_per_turn": venom["damage_per_turn"],
                        "duration": venom["duration"]
                    }
                damage += venom["damage_per_turn"]
                time.sleep(1)

        # Check if Rage should trigger
        if "Rage" in self.traits and self.traits ["Rage"] is not None:
            if self.health / self.max_health<= self.low_health_threshold:
                rage =self.traits["Rage"]
                print(f">>> {self.name} enters a rage! Attack increased by {rage['boost']['attack']}.")
                self.attack += rage["boost"]["attack"]
                self.traits["Rage"] = None
                time.sleep(1)
                print()

        if "Stealth" in self.traits:
            stealth = self.traits["Stealth"]
            if stealth and random.random() < stealth["chance_to_evade"]:
                print(f">>> {self.name} evades the attack due to Stealth!")
                time.sleep(1)
                print()
                return 0  

def load_enemy():
    with open("enemies.json", 'r') as f:
        data = json.load(f)
        
        enemies = {}

    for item_name, item_data in data.items():
        traits = item_data.get('traits', {})
        loot_table = item_data.get('loot_table', [])
        enemies[item_name] = Enemy(
            name=item_name,
            health=item_data["health"],
            attack=item_data["attack"],
            defense=item_data["defense"],
            speed=item_data["speed"],
            level=item_data["level"],
            traits=traits,
            loot_table=loot_table
        )
    
    return enemies