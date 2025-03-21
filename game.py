import time
import json
import os
import random
from heroes import ShieldHero, SwordHero, SpearHero, BowHero
from Enemies import DarkSpider
from items import healing_potion

print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")


def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# insert dialogue  
class Dialogue:
     def __init__(self,dialogues_file ="dialogues.json"):
        dialogues_path=os.path.join(os.path.dirname(__file__),dialogues_file)
        if not os.path.exists(dialogues_path):
            print(f"Error:'{dialogues_file}'")
            exit()
        try:
            with open(dialogues_path, "r", encoding="utf-8") as f:
                self.dialogues = json.load(f)
        except FileNotFoundError:
            print('File not found')
            exit()
     
     def show_dialogue(self, dialogue_id):
         if dialogue_id in self.dialogues:
             for line in self.dialogues[dialogue_id]:
                 print_with_delay(line, 0.03)

   
def game_intro():
    dialogue = Dialogue()
    dialogue.show_dialogue("game_intro")
    hero_awakening()

def hero_awakening():
    dialogue = Dialogue()
    dialogue.show_dialogue("hero_awakening")
    print_with_delay("you grip the weapon tighter, felling its weight-heavy.")
    print("\n")
    dialogue.show_dialogue("robed_explanation")
   
    choose_hero()

def choose_hero():
    #print("\n1. Shield Hero - The unbreakableGuardia, protector of the realm")
    print("\n1. Sword Hero - The fearless warrior, cutting dowmn enemies with raw strength.")
    print("2. Spear Hero - The swift sticker, delivering precise amnd devastating blows.")
    print("3. Bow Hero - The unseen hunter, eleimenting threats from afar.")
   
    hero_classes = {


        #"1": (ShieldHero, "Shield Hero"),
        "1": (SwordHero, "Sword Hero"),
        "2": (SpearHero, "Spear Hero"),
        "3": (BowHero, "Bow Hero")
        }
    hero_lore ={
        #"1": (
           # "** The Shield hero **\n"
            #"A bastioon  of unyiedling resolve, the Shield Hero stand as the last line of defense."
            #"when all others fall,, they remain, shieldin the reaml form annihilation"
        #),
        "1": (
            " ** The Swoar Hero**\n"
            "A warrior of unparalleded skill, the Sword eor craves through the darkness with each swing."
            "feared by enemies, revered by allies, they are the embbodiement of raw strength and unrelenting will"
        ),
        "2": (
            "** The Spear Hero** \n"
            "A MAster of speed and precsion, the Spear Hero brak threough enemy line s with lightning-fast strikes"
        ),
        "3":  (
            "** The Bow Hero **\n"
            "A phantom in the shadoe the Bow hero eliminates threats befor they even realiz thier doom."
            "Silent, deadly, and alwasy unseen, they are unseen force that turn the tide of war"
            )
           
    }
    print("\n Previewing heroes...\n")
    for num, (HeroClass, Hero_title) in hero_classes.items():
        print_with_delay(hero_lore[num])
        temp_hero = HeroClass("Preview")
        temp_hero.show_stats()
        print("-" * 40)
    while True:
        choice = input("\nWhich hero do you choose? (enter 1-4): ")
        if choice in hero_classes:
            HeroClass, Hero_title = hero_classes[choice]  
            print_with_delay(f"\nYou have chosen: **{Hero_title}!**")
            hero_name = input("\nWhat is your name, hero? ")

            hero =HeroClass(hero_name)
           
            print_with_delay(f"\nYou have aquired the **{hero.weapon.name}!**")

            while True:
                command = input("Press 'I' to opnen yur inventoery or 'C' to continue: ").strip().lower()
                if command == "i":
                    hero.open_inventory()
                elif command == 'c':
                    print("Continuing the game...")
                    break
                else:
                    print("Invalid input, Press 'I' fro inventory or 'c' to continue.")
            begin_journey(hero.hero_class,hero)
            return hero
 
        else:
            print_with_delay("\nInvalid choice. Pelase enter a number 1-3")


def begin_journey(hero_class,hero):
    print_with_delay(f"\nAs the {hero_class}, your body surges with newfound power.")
    print_with_delay("\nThe figuers whisper in awe: 'The **Legendary Hero** has arrive.")
    print_with_delay("\nBut there is no time to celebrate.")

    print_with_delay("** In the far distance.. ** A deep rumble shakes the labd. the first **wave** is coming.")
    print_with_delay("\nMonstrous shadows emrge on the horizon; they seem endelss")
    print_with_delay(f"\nThe people cry out: **{hero_class}! Save us!** ")

    print_with_delay("\n**Robed Figure:** Your weapon is one of the most powerful weapons in existance, but remmember, it has it limits.")
    print_with_delay("while you can protect and deal yourself form great damage, the weapons durability is finite. if it overheats,")
    print_with_delay("you'll have to wait for it to cool down")

    print("\nWhat will you do?")
    print("1. Stand and fight")
    print("2. Seek answers about your summoning")
    print("3. Refuse to fight")

    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            stand_and_fight(hero_class, hero)
            break  
        elif choice == "2":
            seek_answers()  
        elif choice == "3":
            abandon_kingdom()  
        else:
            print_with_delay("Invalid choice. Please enter a valid option.")


def abandon_kingdom():
    dialogue = Dialogue()
    dialogue.show_dialogue("abandon_kingdom")

def seek_answers():
    dialogue = Dialogue()
    print_with_delay("\nYou demnad answers from the robed figuers.")
    print_with_delay("Why was I summond? what is the truth of the world?")
    dialogue.show_dialogue("Histroy")

def stand_and_fight(hero_class,hero):
    print_with_delay(f"\nBracing yourself, you prepare for battle as the {hero_class}.")
    print_with_delay("\nThe robed figuer approaches you and hands you a healing potion.")

    hero.add_item(healing_potion)

    print_with_delay(f"\nYou have acquired a Healing Potion and it has been added to your inventory.")
    print_with_delay("\nA sudden surge of light surrounds you, brightening erything in sight.")
    print_with_delay("you fell yoursself being pulled into another dimensio, and before you can react,")
    print_with_delay("You find yoursfel standing on vast , darkness battlefiled.")
   
    print_with_delay("\nTe ground shaes as montrous figuer emrge from the shadows")
    print_with_delay("You have been teleported to the dirst wave of battle!")

    start_combat(hero)

def start_combat(hero):
    print_with_delay("\nThe battle has begun!")
    enemies = [DarkSpider()]  # Now using the defined enemy class
    for enemy in enemies:
        enemy.show_stats()

    combat(hero, enemies)

def combat(hero, enemies):
    actions = {
        "1": lambda: attack_action(hero, enemies),
        "2": lambda: defend_action(hero),
        "3": lambda: run_action(hero, enemies),
        "4": lambda: use_skill_action(hero, enemies)  # New action for using skills
    }

    while any(enemy.health > 0 for enemy in enemies) and hero.health > 0:
        print_with_delay(f"\nYour turn, {hero.name}!")

        # Show available actions
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Run")
        print("[4] Use Skill")  # Show option to use a skill

        action = input("Choose an action: ")

        # Execute the selected action if it's valid
        actions.get(action, lambda: print_with_delay("Invalid action!"))()

        # Enemy attacks after the player's turn
        for enemy in enemies:
            if enemy.health > 0:
                damage = max(1, enemy.attack - hero.defense)
                hero.health -= damage
                print_with_delay(f"\nThe {enemy.name} attacked you for {damage} damage!")

        print_with_delay(f"\n{hero.name}'s Health: {hero.health}")

        if hero.health <= 0:
            print_with_delay("You have been defeated... The world succumbs to the darkness.")
            exit()  # End the game if the hero is defeated

def use_skill_action(hero, enemies):
    # Show available skills
    print_with_delay(f"\nAvailable skills for {hero.name}:")
    for i, skill in enumerate(hero.skills, 1):
        print(f"[{i}] {skill}")
   
    skill_choice = input("Choose a skill: ")
   
    try:
        skill_index = int(skill_choice) - 1
        if 0 <= skill_index < len(hero.skills):
            skill_name = hero.skills[skill_index]
            use_skill(hero, skill_name, enemies)
        else:
            print_with_delay("Invalid skill choice.")
    except ValueError:
        print_with_delay("Invalid input. Please enter a number.")

def use_skill(hero, skill_name, enemies):
    # Skill actions stored in a dictionary to avoid `if`/`else`
    skill_effects = {
       
        "Shield Bash": lambda: shield_bash(hero, enemies),
        "Swift Slash": lambda: swift_slash(hero, enemies),
        "Lance Charge": lambda: lance_charge(hero, enemies),
        "Longshot": lambda: longshot(hero, enemies),
        # Add more skills here if needed
    }

    # Execute the corresponding skill
    skill_effects.get(skill_name, lambda: print_with_delay(f"{hero.name} This skill is unlock. No action taken."))()

def shield_bash(hero, enemies):
    skill_damage = hero.attack * 1.5  # Example damage multiplier for Shield Bash
    target = enemies[0]  # Targeting the first enemy for simplicity
    target.health -= skill_damage
    print_with_delay(f"{hero.name} used Shield Bash on {target.name} for {skill_damage} damage!")
    check_enemy_status(hero, target, enemies)

def swift_slash(hero, enemies):
    skill_damage = hero.attack * 2  # Example damage multiplier for Swift Slash
    target = enemies[0]
    target.health -= skill_damage
    print_with_delay(f"{hero.name} used Swift Slash on {target.name} for {skill_damage} damage!")
    check_enemy_status(hero, target, enemies)

def lance_charge(hero, enemies):
    skill_damage = hero.attack * 1.8  # Example multiplier for Lance Charge
    target = enemies[0]
    target.health -= skill_damage
    print_with_delay(f"{hero.name} used Lance Charge on {target.name} for {skill_damage} damage!")
    check_enemy_status(hero, target, enemies)

def longshot(hero, enemies):
    skill_damage = hero.attack * 1.3  # Example multiplier for Longshot
    target = enemies[0]
    target.health -= skill_damage
    print_with_delay(f"{hero.name} used Longshot on {target.name} for {skill_damage} damage!")
    check_enemy_status(hero, target, enemies)

def check_enemy_status(hero, target, enemies):
    if target.health <= 0:
        print_with_delay(f"\nThe {target.name} has been defeated!")
        hero.xp += 5  # Adds 5 XP
        hero.check_level_up()  # Check if the hero should level up
        hero.earn_coins(random.randint(5, 10))  # Hero earns random coins between 5 and 10
        enemies.remove(target)  # Remove defeated enemy
    else:
        print_with_delay(f"{target.name}'s Health: {target.health}")

def attack_action(hero, enemies):
    target = enemies[0]  # For simplicity, just attacking the first enemy
    damage = max(1, hero.attack - target.defense)
    target.health -= damage
    print_with_delay(f"You attacked the {target.name} for {damage} damage!")

    if target.health <= 0:
        print_with_delay(f"\nThe {target.name} has been defeated!")
        hero.xp +=(5)
        hero.earn_coins(random.randint(5, 10))
        enemies.remove(target)
    else:
        print_with_delay(f"\n{target.name}'s health: {target.health}")

def defend_action(hero):
    print_with_delay(f"{hero} prepare to block an attack, reducing damage next turn.")

def run_action(hero, enemies,):
    print_with_delay("You attempt to escape...")
    if hero.speed > enemies[0].speed:
        print_with_delay("You successfully escaped!")
        return  # End the combat if escape is successful
    else:
        print_with_delay("The enemies are too fast! You have to fight!")
        first_victory()

def first_victory(hero):
    """
    Handles the event when the player defeats the first monster.
    """
    print_with_delay("\nAs the monster falls, you hear a voice calling out to you.")
    print_with_delay('"Thank you for defending our people!" says Rob Figure, stepping forward.')
    print_with_delay('"Rest up before your next battle, hero."')

    # Give the player a choice to return to the kingdom
    choice = input("\nWould you like to return to the kingdom to rest? (yes/no): ").lower()
    if choice == "yes":
        return_to_kingdom(hero)  # The game saves inside this function

    # Ask if they want to continue the story
    continue_story = input("\nWould you like to continue with the story? (yes/no): ").lower()
    if continue_story == "yes":
        print_with_delay("\nCOMING SOON...\n")

def return_to_kingdom(hero):
    """
    Handles the event when the player returns to the kingdom.
    Rob Figure congratulates them, they rest, the game saves, and their health is restored.
    """
    print_with_delay("\nYou return to the kingdom, greeted by the cheers of the people.")
    print_with_delay('"Congratulations, hero!" says Rob Figure. "Please, rest and recover your strength."')

    # Restore hero's health (assuming `hero.health` exists)
    hero.health = hero.max_health
    print_with_delay("\nYou feel refreshed as your health is fully restored!")

    # Save the game (only saves if the player chooses to rest)
    save_game(hero)
    print_with_delay("\nYour progress has been saved.")

def save_game(hero):
    """Simulates saving the game."""
    print_with_delay(f"\nGame saved for {hero.name}.")
    


if __name__ == "__main__":
    game_intro()