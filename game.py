import time
import json
import random
import os
import menu
from heroes import ShieldHero, SwordHero, SpearHero, BowHero, DarkSpider


print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")
#delay

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
     
     def show_dialogue(self, dialogue_id,**kwargs):
         if dialogue_id in self.dialogues:
             for line in self.dialogues[dialogue_id]:
                formatted_line=line.format(**kwargs)
                print_with_delay(formatted_line, 0.03)

def game_intro():
    dialogue = Dialogue()
    dialogue.show_dialogue("game_intro")
    assign_random_hero()

def assign_random_hero():
    hero_classes = {

        "Shield Hero":ShieldHero,
        "Sword Hero": SwordHero,
        "Spear Hero":SpearHero,
        "Bow Hero": BowHero,

    }
    chosen_hero = random.choice(list(hero_classes.keys()))
    print_with_delay(f"\n A suddenly light start glowing beneath you... fate has chosen ou as the **{chosen_hero}! ")
    hero_instance = hero_classes[chosen_hero]("player")
    hero_awakening(chosen_hero, hero_instance)

def combat(hero, enemies):
    print_with_delay("\n The battle has begun!")
    for enemy in enemies:
        enemy.show_stats()

    while any(enemy.health> 0 for enemy in enemies) and hero.health >0:
        print("your turn!")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Run")

        action=input("choose an action:")

        if action =="1":
            target=enemies[0]
            damage=max(1,hero.attack-target.defense)
            target.health -= damage
            print(f"you attacked the {target.name} for {damage}damage!")
            
            if target.health <=0:
                print(f"\n the {target.name} has been defeated!")
                hero.gain_xp(5)
                hero.earn_coins(random.randint(5,10))
                enemies.remove(target)
            else:
                print(f"\n{target.name}'s health: {target.health}")

        elif action=="2":
            print("You blocked an attack, reducing damage.")

        elif action=="3":
            print("you attempt to escape...")
            if hero.speed> enemies[0].speed:
                print("You successfully escaped!")
                return
            else: 
                print("the enemies are too fast YOU HAVE TO FIGHT!!!")  

        for enemy in enemies:
            if enemy.health>0:
                damage=max(1, enemy.attack-hero.defense)
                hero.health -= damage
                print(f"\nTHe {enemy.name} attacked you for {damage} damage!")

        print(f"\n{hero.__class__.__name__}'s Health: {hero.health}")

        if hero.health<=0:
            print("You have been defeated..... The World succumbs to the darkness") 
            exit()

    print("\nYou have survived the battle!")   
def next_action(hero):
    while True:
        print("\n[1] Perpare to fight the Wave immediateiatly")
        print("\n[2] denmand answer from the robed figuer")
        print("\n[3] refused to fight the battle")
    
        choice = input("\nWhat will you do? (1,2,3): ")
        dialogue = Dialogue()
     
        if choice == "1":
            print_with_delay(" you build your resolve and prepare for battle ")
            print_with_delay("The battle begins!!! The wave of Giant DarkSpiders charge at You!")

            enemies =[DarkSpider() for _ in range (5)]
            combat(hero,enemies)

            print_with_delay("Congratulations you have survived the battle")
            print_with_delay("The first wave is over, but prepare yourself for the upcoming 2nd wave in days to come.")
            break
     

        elif choice == "2":
            print_with_delay("\nYou turn to the robed figuer, demanding the truth\n")
            dialogue.show_dialogue ("robed_figure_truth")

         
        elif choice == "3":
            dialogue.show_dialogue("refuse_to_fight")
            print_with_delay("Through your decision, the kingdom falls into ruin...")
            print_with_delay("The world fades to datkness. ** tou have failed as a hero.**\n")
            exit()

def begin_journey(hero_type,hero):
    print_with_delay(f"As the {hero_type}, your body surges with newfound power")
    print_with_delay("The robed figures whisper in awe: 'The **Legendary hero ** has arrived ")
    print_with_delay("\n But there is no time to celebrate.")

    print_with_delay("\na A deep ruble shakes the land. The first **wave** is coming")
    print_with_delay("Monstrouseshadows emrrge on th ehorizo, thie seems to be endless")
    print_with_delay(f"te people cry out: '**{hero_type}! save us!**'")
 
    print_with_delay("\nwill you stand and fight, seek answers to why you were summond? or let the kingdom fall to the waves.")

    next_action(hero)

def hero_awakening(hero_type,hero):
    dialogue = Dialogue()
    dialogue.show_dialogue("hero_awakening",hero_type=hero_type)
    dialogue.show_dialogue("robed_figure_explanation")
    begin_journey(hero_type, hero)
while True:
    choice=menu.main_menu()
    if choice == "1":
        game_intro()
        break
    elif choice =="2":
        menu.show_instructions()
    elif choice == "3":
        print("GOODBYE")
        time.sleep(1)
        exit()
def choose_weapon(hero):
    print_with_delay("\nThe robed figuer gestures toead foure weapon")
    print_with_delay("Choose wisel, hero. Your eapon detetmines your path")

    weapon_choices = {

        "1": hero.weapon,
        "2": hero.weapon,
        "3": hero.weapon,
        "4": hero.weapon,

    }

    print("\n[1] Shield")
    print("[2] Sword")
    print("[3] spear ")
    print("[4] Bow")

    choice = input("\nWhich eeapon will you choose? (1,2,3,4): ")

    if choice in weapon_choices:
        hero.weapon = weapon_choices[choice]
        print_with_delay(f"You have chosen the {hero.weapon.name}!")
    else:
        print_with_delay("\nInvalid choice! You hesiated and fate chose for you.")
        hero.weapon =random.choice(list(weapon_choices.vales()))
        print_with_delay(f"you have been given the {hero.weapon.name}.")


def shop(hero):
    print_with_delay("Welcome to the Potion and Repair Shop!")
    print_with_delay("You have {hero.coins} coins.")

    while True:
        print()








    
