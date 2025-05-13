import json
import random


class Skill:
    def __init__(self, name, description, damage, effects=None, crit_multiplier=1.0):
        self.name = name
        self.description = description
        self.damage = damage
        self.effects = effects if effects else []
        self.crit_multiplier = crit_multiplier

    def __repr__(self):
        return f"{self.name} (Damage: {self.damage})"

class Enemy:
    def __init__(self, name, health, defense, speed, loot, skills):
        self.name = name
        self.health = health
        self.max_health = health
        self.defense = defense
        self.speed = speed
        self.loot = loot
        self.skills = skills
        self.status_effects = {}
        self.evasion_boost = 0
        self.evasion_duration = 0

    def take_damage(self, amount):
        if self.evasion_duration > 0 and random.random() < self.evasion_boost:
            print(f"{self.name} dodged the attack!")
            return False

        damage_taken = max(0, amount - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. HP: {self.health}/{self.max_health}\n")

        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")

        return True

    def apply_status_effect(self, effect, target):
        if random.random() > effect.get("chance", 1.0):
            print(f"{effect['type'].capitalize()} failed to apply.")
            return

        effect_type = effect.get("type")
        duration = effect.get("duration", 1)

        if effect_type == "poison":
            target.status_effects["poison"] = {
                "duration": duration,
                "damage_per_turn": effect.get("damage_per_turn", 0)
            }
            print(f"{target.name} is poisoned!")

        elif effect_type == "slow":
            target.status_effects["slow"] = {
                "duration": duration,
                "speed_reduction": effect.get("speed_reduction", 0)
            }
            print(f"{target.name} is slowed!")

        elif effect_type == "attack debuff":
            target.status_effects["attack debuff"] = {
                "duration": duration,
                "reduction_amount": effect.get("reduction_amount", 0)
            }
            print(f"{target.name}'s attack is weakened!")

        elif effect_type == "evasion_boost":
            self.evasion_boost = effect.get("evade_chance_bonus", 0)
            self.evasion_duration = duration
            print(f"{self.name} gains an evasion boost!")

    def use_skill(self, target):
        if not self.skills:
            print(f"{self.name} has no skills!")
            return

        skill = random.choice(self.skills)
        print(f"{self.name} uses {skill.name} on {target.name}!")

        is_crit = random.random() < 0.1
        damage = int(skill.damage * skill.crit_multiplier) if is_crit else skill.damage

        if "evade" in target.status_effects:
            print(f"{target.name} evades the attack due to an active effect!")
            del target.status_effects["evade"] # Remove the evade effect after it's used
            return

        if is_crit:
            print("Critical hit!")

        target.take_damage(damage)

        for effect in skill.effects:
            self.apply_status_effect(effect, target)

    def process_status_effects(self):

        if self.evasion_duration > 0:
            self.evasion_duration -= 1
            if self.evasion_duration == 0:
                print(f"{self.name}'s evasion boost wore off.")
                self.evasion_boost = 0

def load_enemies_from_json():
    enemies = {}
    try:
        with open('enemies.json', 'r') as f:
            data = json.load(f)
        for key, val in data.items():
            name = val.get("name_display", key)
            stats = val["stats"]
            health = stats.get("health", 100)
            defense = stats.get("defense", 0)
            speed = stats.get("speed", 10)
            loot = val.get("loot", [])
            skills = [Skill(**{
                'name': s.get("name"),
                'description': s.get("description", ""),
                'damage': s.get("damage", 0),
                'effects': s.get("effects", []),
                'crit_multiplier': s.get("crit_multiplier", 1.0)
            }) for s in val.get("skills", [])]
            enemies[key] = Enemy(name, health, defense, speed, loot, skills)
    except Exception as e:
        print(f"Failed to load enemies: {e}")
    return enemies

