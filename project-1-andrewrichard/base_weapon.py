import json
import random
import time

# Define the Skill class
class Skill:
    def __init__(self, name, effect, effect_type, base_damage, hits=1, stun_duration=0, 
                 buff_type=None, duration=0, reduction_percent=0, crit_multiplier=1.0):
        self.name = name
        self.effect = effect
        self.effect_type = effect_type
        self.base_damage = base_damage
        self.hits = hits
        self.stun_duration = stun_duration
        self.buff_type = buff_type
        self.duration = duration
        self.reduction_percent = reduction_percent
        self.crit_multiplier = crit_multiplier

    def __repr__(self):
        return f"{self.name}:{self.effect}- Damge:{self.base_damage}"

# Define the Weapon class with Overheat Mechanism
class Weapon:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills  
        self.overheat = 0 
        self.max_overheat = 100  
        self.overheating = False  # 

    def __repr__(self):
        return f"Weapon(name={self.name}, skills={self.skills}, overheat={self.overheat}%)"

    # Method to increase overheat with each skill usage
    def increase_overheat(self):
        self.overheat += 20  
        if self.overheat >= self.max_overheat:
            self.overheat = self.max_overheat
            self.overheating = True
            print(f"{self.name} is overheating! Please wait...\n")
            time.sleep(1)

        self.display_overheat_bar()

    # Method to display the overheat bar
    def display_overheat_bar(self):
        bar_length = 20  # Length of the overheat bar
        filled_length = int(self.overheat / self.max_overheat * bar_length)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"Weapon Overheat: [{bar}] {self.overheat}%\n")
        time.sleep(0.5)

    # Reset the overheat state after cooldown
    def reset_overheat(self):
        self.overheat = 0
        self.overheating = False
        print(f"{self.name} has cooled down.\n")
        time.sleep(1)

    # Method to handle weapon skill use
    def use_skill(self, skill_name, user, target=None, enemies=None):
        if self.overheating:
            print(f"Weapon is overheating! Cannot use skills until it cools down.")
            time.sleep(1)
            return

        if skill_name not in [skill.name for skill in self.skills]:
            print(f"Skill '{skill_name}' not found in {self.name}.\n")
            time.sleep(1)
            return

        skill = next(skill for skill in self.skills if skill.name == skill_name)
        effect_type = skill.effect_type
        print(f"\n{user.name} uses {skill_name}: {skill.effect}\n")
        time.sleep(1)

        # Handle based on effect_type
        if effect_type == "single_target":
            self.handle_single_target(skill, user, target)
        elif effect_type == "multi_hit":
            self.handle_multi_hit(skill, user, target)
        elif effect_type == "aoe":
            self.handle_aoe(skill, user, enemies, target)
        elif effect_type == "self_buff":
            self.apply_self_buff(skill, user)
        else:
            print(f"No handler for effect type: {effect_type}\n")
            time.sleep(1)

        # Increase overheat after using a skill
        self.increase_overheat()
        
        if self.overheating:
            self.start_cooldown()

    def handle_single_target(self, skill,user, target):
        damage = skill.base_damage
        total_damage = damage

        print(f"\n{user.name} uses {skill.name} on {target.name}")
        time.sleep(0.5)

        # Check for critical hit
        crit_multiplier = skill.crit_multiplier
        if crit_multiplier and random.random() < 0.3:
            total_damage = int(damage * crit_multiplier)
            print(">> Critical hit!\n")
            time.sleep(0.5)

        # Apply damage
        target.health -= total_damage
        print(f">> {target.name} takes {total_damage} damage.\n")
        time.sleep(0.5)

        # Check for stun
        if skill.stun_duration and random.random() < 0.5:
            print(f">> {target.name} is stunned for {skill.stun_duration} turn(s)!\n")
            target.status_effects["stun"] = {"duration": skill.stun_duration}
            time.sleep(0.5)

    def handle_multi_hit(self, skill,user, target):
        for i in range(skill.hits):
            print(f">> {user.name} target Hit {target.name} for {i+1}: {target.name} takes {skill.base_damage} damage.\n")
            target.health -= skill.base_damage
            time.sleep(0.5)

    def handle_aoe(self, skill, enemies):
        for enemy in enemies:
            print(f">> {enemy.name} takes {skill.base_damage} damage.\n")
            enemy.health -= skill.base_damage
            time.sleep(1)

    def apply_self_buff(self, skill, user):
        if skill.buff_type == "defense_boost":
            print(f">> {user.name}'s defense increased by {skill.reduction_percent}% for {skill.duration} turns.\n")
            user.status_effects["defense_boost"] = {
                "duration": skill.duration,
                "reduction_percent": skill.reduction_percent
            }
            time.sleep(1)

    def start_cooldown(self):
        self.cooldown_turn = 3
        print(f"{self.name} is cooling down for {self.cooldown_turn} turns...\n")
        time.sleep(1)
    
    def update_cooldown(self):
        if self.cooldown_turn > 0:
            self.cooldown_turn -= 1
            print(f"{self.name} has {self.cooldown_turn} turns left in cooldown.\n")
            if self.cooldown_turn == 0:
                self.reset_overheat()

# Function to load weapons and skills from a JSON file
def load_weapon():
    with open("weapons.json", 'r') as f:
        data = json.load(f)
    
    weapons = {}
    for weapon_name, weapon_data in data.items():
        skills = []
        for skill_data in weapon_data["skills"]:
            skill = Skill(
                name=skill_data["name"],
                effect=skill_data["effect"],
                effect_type=skill_data["effect_type"],
                base_damage=skill_data.get("base_damage", 0),
                hits=skill_data.get("hits", 1),
                stun_duration=skill_data.get("stun_duration", 0),
                buff_type=skill_data.get("buff_type", None),
                duration=skill_data.get("duration", 0),
                reduction_percent=skill_data.get("reduction_percent", 0),
                crit_multiplier=skill_data.get("crit_multiplier", 1.0)
            )
            skills.append(skill)
        
        weapon = Weapon(
            name=weapon_name,
            skills=skills
        )
        weapons[weapon_name] = weapon

    return weapons
