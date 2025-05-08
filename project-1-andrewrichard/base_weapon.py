import json
import random

class Skill:
    def __init__(self, name, effect, effect_type, damage, hits=1, status_effects=None, crit_multiplier=1.0):

        self.name = name
        self.effect = effect
        self.effect_type = effect_type
        self.damage = damage
        self.hits = hits
        self.status_effects = status_effects if status_effects else {}
        self.crit_multiplier = crit_multiplier
        self.description = effect  

    def __repr__(self):  
        return f"Skill(name='{self.name}', damage={self.damage}, type='{self.effect_type}')"

class Weapon:
    def __init__(self, name, base_damage=0, overheat_threshold=100):

        self.name = name
        self.skills = []
        self.base_damage = base_damage  # Store base damage
        self.overheat_threshold = overheat_threshold
        self.overheat_level = 0
        self.overheating = False
        self.cooldown_turn = 0

    def add_skill(self, skill):
        self.skills.append(skill)

    def increase_overheat(self, amount):
        self.overheat_level += amount
        if self.overheat_level >= self.overheat_threshold and not self.overheating:
            print(f"{self.name} has reached maximum heat! your wepaon skill cannot be use for the next turn.")
            self.overheating = True
            self.cooldown_turn = 0
            self.max_cooldown_turns = random.randint(1, 3)


    def _display_heat_bar(self) -> None:
        bar_length = 20
        filled = int(bar_length * self.overheat_level / self.overheat_threshold)
        bar = '[' + '█' * filled + '-' * (bar_length - filled) + ']'
        print(f"Heat: {bar} {self.overheat_level}/{self.overheat_threshold}")

    def reset_overheat(self):
        self.overheating = False
        self.overheat_level = 0
        self.cooldown_turn = 0
        self.max_cooldown_turns = 0

    def use_skill(self, skill_name, player, enemy=None, enemies=None):

        if self.overheating and self.overheat_level >= self.overheat_threshold:
            self.cooldown_turn += 1
            print(f"{self.name} is overheated and cannot be used! Cooling down ({self.cooldown_turn}/{self.max_cooldown_turns})...")
            if self.cooldown_turn >= self.max_cooldown_turns:
                self.reset_overheat()
            return

        for skill in self.skills:
            if skill.name == skill_name:
                if skill.effect_type == "single_target":
                    print(f"\n{player.name} uses {skill.name} on {enemy.name}!\n")
                    self._apply_single_target(skill, enemy, player) # Pass player
                elif skill.effect_type == "multi_hit":
                    print(f"\n{player.name} uses {skill.name} on {enemy.name}!\n")
                    self._apply_multi_hit(skill, enemy, player) # Pass player
                elif skill.effect_type == "aoe":
                    print(f"\n{player.name} uses {skill.name} on all enemies!\n")
                    self._apply_aoe(skill, enemies, player) # Pass player
                elif skill.effect_type == "self_buff":
                    print(f"\n{player.name} uses {skill.name} to buff themselves!\n")
                    self._apply_self_buff(skill, player)
                self._display_heat_bar()
                self.increase_overheat(25)
                return  
        print(f"Skill '{skill_name}' not found on weapon '{self.name}'.") # added error message

    def _apply_single_target(self, skill, enemy,):
        """Applies a single-target skill's effects."""
        if enemy:
            damage = skill.damage + self.base_damage # add base damage
            if skill.crit_multiplier > 1 and random.random() < 0.25:
                damage *= skill.crit_multiplier
                print("Critical Hit!")
            enemy.take_damage(int(damage))
            if skill.status_effects:
                enemy.status_effects.update(skill.status_effects)

    def _apply_multi_hit(self, skill, enemy):
        """Applies a multi-hit skill's effects."""
        if enemy:
            for i in range(skill.hits):
                damage = (skill.damage + self.base_damage) // skill.hits # add base damage
                if skill.crit_multiplier > 1 and random.random() < 0.25:
                    damage *= skill.crit_multiplier
                    print("Critical Hit!")
                enemy.take_damage(int(damage))
                print(f"Hit {i+1} for {int(damage)} damage.")

    def _apply_aoe(self, skill, enemies):
        """Applies an AoE skill's effects."""
        if enemies:
            damage = skill.damage + self.base_damage # add base damage
            if skill.crit_multiplier > 1 and random.random() < 0.25:
                damage *= skill.crit_multiplier
                print("Critical Hit!")
            for e in enemies:  # Changed from enemies.take_damage to iterate and apply to each
                e.take_damage(int(damage))
            if skill.status_effects:
                for e in enemies:
                    e.status_effects.update(skill.status_effects)  # apply to each enemy

    def _apply_self_buff(self, skill, player):
        """Applies a self-buff skill's effects."""
        if player:
            if skill.status_effects:
                player.status_effects.update(skill.status_effects)


def load_weapons(file_path="weapons.json"):
    """Loads weapons and their skills from a JSON file."""
    weapons = {}
    try:
        with open(file_path, "r") as f:
            weapon_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Returning empty weapon list.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}. Returning empty weapon list.")
        return {}

    for weapon_name, weapon_info in weapon_data.items():
        # Ensure weapon_info is a dictionary
        if not isinstance(weapon_info, dict):
            print(f"Warning: Skipping malformed weapon data for '{weapon_name}'. Expected a dictionary.")
            continue

        skills = []
        json_skills = weapon_info.get("skills", [])
        if not isinstance(json_skills, list):
            print(f"Warning: Skills data for '{weapon_name}' is malformed. Expected a list.")
            json_skills = [] 

        for skill_data in json_skills:
            if not isinstance(skill_data, dict):
                print(f"Warning: Skipping malformed skill data in '{weapon_name}'. Expected a dictionary.")
                continue
            
            skill = Skill(
                name=skill_data.get("name", "Unnamed Skill"),
                effect=skill_data.get("description", ""), 
                effect_type=skill_data.get("effect_type", "single_target"),
                damage=skill_data.get("damage_value", 0), 
                hits=skill_data.get("hits", 1),
                status_effects=skill_data.get("status_effects"), # Pass directly, Skill constructor will handle if None
                crit_multiplier=skill_data.get("crit_multiplier", 1.0),
            )
            skills.append(skill)

        weapon = Weapon(
            name=weapon_name,
            base_damage=weapon_info.get("damage", 0),
        )
        for skill_in_list in skills: 
            weapon.add_skill(skill_in_list)

        weapons[weapon_name] = weapon
            
    return weapons
