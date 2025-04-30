
import json
import random


class Enemy:
    def __init__(self, name, health, attack, defense, speed, traits, level, loot_table=None):
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
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! ({self.health}/{self.max_health} HP left)")

    def attack_target(self, target):
        damage =  self.attack
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)
        self.apply_traits(target,damage)
        return damage

    def apply_traits(self, target, damage):
        for trait_name, trait_data in self.traits.items():
            if trait_name == "Venomous":
                # Apply poison effect with a 50% chance
                if random.random() < 0.5:
                    target.status_effects["poison"] = {
                        "duration": trait_data["duration"],
                        "damage_per_turn": trait_data["damage_per_turn"]
                    }
                    print(f"{self.name}'s venom poisons {target.name}!")
                    print(f"{target.name} takes {damage} damage per {trait_data['duration']} turns!")
        

            elif trait_name == "Rage":
                # Apply attack boost if health is low
                if self.health <= 0.3 * self.max_health:
                    boost = trait_data.get("boost", {})
                    attack_boost = boost.get("attack", 0)
                    self.attack += attack_boost
                    print(f"{self.name} enters a rage and gains +{attack_boost} attack!")

            elif trait_name == "Stealth":
                # Chance to evade
                if random.random() < trait_data.get("chance_to_evade", 0):
                    self.status_effects["evade"] = {
                        "duration": trait_data.get("duration", 1)
                    }
                    print(f"{self.name} uses stealth and becomes harder to hit!")
                else:
                    print(f"{self.name} failed to use stealth.")

    def apply_status_effects(self,damage):
        if "poison" in self.status_effects:
            poison_effect = self.status_effects["poison"]
            poison_damage = poison_effect["damage_per_turn"]
            print(f"{self.name} suffers {poison_damage} poison damage!")
            self.health -= poison_damage
            if self.health < 0:
                self.health = 0


            # Reduce poison duration each turn
            poison_effect["duration"] -= 1
            if poison_effect["duration"] <= 0:
                print(f"{self.name} is no longer poisoned.")
                del self.status_effects["poison"]  
                

        if "evade" in self.status_effects:
            evade_effect = self.status_effects["evade"]
            print(f"{self.name} is harder to hit due to stealth! (Duration: {evade_effect['duration']})")

            # Reduce evade duration each turn
            evade_effect["duration"] -= 1
            if evade_effect["duration"] <= 0:
                del self.status_effects["evade"]  
                print(f"{self.name}'s stealth effect has worn off.")

    
    def drop_loot(self):
        dropped = []
        for loot in self.loot_table:
            if random.random() < loot["chance"]:
                dropped.append(loot["item"])
        return dropped
    
    def calculate_xp(self, player_level):
        base_xp = 50
        level_diff = self.level / player_level
        random_multiplier = random.uniform(0.8, 1.2)
        xp = int(base_xp * level_diff * random_multiplier)
        return max(10, xp)

def load_enemy():
    with open("enemies.json", 'r') as f:
        data = json.load(f)

    enemies = {}
    for name, stats in data.items():
        enemies[name] = Enemy(
            name=name,
            health=stats["health"],
            attack=stats["attack"],
            defense=stats["defense"],
            speed=stats["speed"],
            level=stats["level"],
            traits=stats.get("traits", {}),
            loot_table=stats.get("loot_table", [])
        )
    return enemies
