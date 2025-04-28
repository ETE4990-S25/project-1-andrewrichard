import os
import time
import random
import sys
from dialogues import story
from heroes import Shield, Sword,Spear, Bow
from items_classes import Item, load_items
from Enemies import load_enemy, Enemy
from menu import main_menu,SAVE_FILE
import json
SAVE_FILE = "savegame.json"



def game_intro():
    print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")
    dialogue = story()
    dialogue.show_dialogue("game_intro")
    hero_awakening()

def hero_awakening():
    dialogue = story()
    dialogue.show_dialogue("hero_awakening")
    dialogue.show_dialogue("robed_explanation")
    selected_hero = choose_hero()
    player_decision(selected_hero)

game_items = load_items()
all_enemies = load_enemy()

hero_classes = {
    1: Sword,
    2: Spear,
    3: Bow,
    4: Shield
    }

def choose_hero():
    
    current_choice = 1

    print("You take a deep breath, stepping closer to the weapons befor you.")
    print("Each one hums with a power of its own, waiting for a wielder.")

    while True:

        os.system('cls' if os.name =='nt' else 'clear')

        print("\nAvailable heros to choose from:\n")
        for index, hero_class in hero_classes.items():
            hero_name = hero_class.__name__
            selection_marker = ">>" if current_choice == index else " "
            print(f"{selection_marker}{index}: {hero_name}{selection_marker}")

        selected_hero = hero_classes[int(current_choice)]()
        selected_hero.display_status()

        user_input= input("\n Use W/S to move up/down, Enter to select: ").strip().lower()

        if user_input == "w" and current_choice > 1:
            current_choice -=1
        elif user_input == 's' and current_choice < len(hero_classes):
            current_choice += 1
        elif user_input == "":
            print(f"\nYou have selected the legendary {selected_hero.hero_class}!")
            os.system('cls' if os.name =='nt' else 'clear')
            break
        else:
            print("Invailid Input.Please press (L), (R), or (Enter)")
            continue 

    print("The moment your hand touches the weapon, the world around you shudders.")
    print(f"As the {selected_hero.hero_class}, you feel the weight of responsibility settle on your shoulders.")
    print("\nThe robed figure nods solemnly and speaks:")
    
    if selected_hero.hero_class == "Sword":
        print("'The Sword Hero... A symbol of courage and strength. The path ahead will be perilous, but your blade shall cleave through all who stand in your way.'")
    elif selected_hero.hero_class == "Spear":
        print("'The Spear Hero... Swift and precise, your strikes will pierce through even the toughest of enemies. But remember, your agility is as vital as your strength.'")
    elif selected_hero.hero_class == "Bow":
        print("'The Bow Hero... A master of ranged combat. From a distance, your arrows will strike true, but be wary of getting too close to danger.'")
    elif selected_hero.hero_class == "Shield":
        print("'The Shield Hero... A protector of all. Your resolve is unmatched, but your defense alone will not win this battle. You must rely on your allies.'")    
   
    dialogue = story()
    dialogue.show_dialogue("beginning")
    return selected_hero

def player_decision(selected_hero):
    selected_hero.alert=False

    print("\nWhat do you do?")
    print("1. Search the area for supplies.")
    print("2. Move forward toward the sound of battle.")
    print("3. Take a defensive stance and observe your surroundings.")

    selected_hero.alert =False
    choice = input("Enter your choice (1,2, or 3): ")
    while True:
        os.system('cls' if os.name =='nt' else 'clear')
        if choice =="1":
            print("You carefully scan the area, searching through the wreckage for anything useful.")
            print("among the debris, you find a **health Potion\n")
            selected_hero.add_item_to_inventory(game_items["Health_Potion"])
      
            print("\nThese may be useful later")

            if random.random() > 0.7:
                print("Lucky find! you discover a shimmering **Mana Flask** nestled under boken stone.")
                selected_hero.add_item_to_inventory(game_items["Mana_Flask"])
            print("\nBecause you took time to search , monsters noticed your presence")
            print("You're ambushed and forced into a battle with multiple enemies!")
            enemy_count = 3
            break
        elif choice =="2":
            print("You steel yourself and press foward. The sounds of battle grows louder.")
            print("As you approach the ruined streets, a dark silhouette emerges form the swirling smoke its eyes glowing ominously.")
            print("More figures appear monsters, eye gleaming, surrounding you!")
            print("\nBecause of your bold approach, you are caught off guard and ambushed!")
            enemy_count = 2
            break
          

        elif choice =="3":
            print("You hold your ground, watchcing for movement.")
            print("Your insticts scream that your're not alone. A shadow flits behind the broken stone too fast to fully see.")
            print("You stay low, watching the shifting debris, waiting for the right moment to react.")
            print("Your cautious stance pays off. You're less likely to get ambushed in upcoming encounters.")
            selected_hero.alert = True
            enemy_count = 1
    
            break
        else:
            choice = input("please enter a vaild option (1,2,3): ")
    
    time.sleep(2)
    print("\n...The air grows heavy. You hear the snarls of beast closing in.")
    time.sleep(1.5)
    print("Weapons ready....")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    battle(selected_hero, enemy_count, all_enemies)

def battle(selected_hero, enemy_count, all_enemies, wave=1):
    enemy_blueprints = load_enemy()
    
    chosen_names = random.choices(list(enemy_blueprints.keys()), k=enemy_count)
    enemies = []
    for nm in chosen_names:
        proto = enemy_blueprints[nm]
        enemies.append(
            Enemy(
                name=proto.name,
                health=proto.max_health,
                attack=proto.attack,
                defense=proto.defense,
                speed=proto.speed,
                traits=dict(proto.traits),    
                level=proto.level,
                loot_table=list(proto.loot_table)  
            )
        )
   
    print(f"\nYou encounter {enemy_count} enemies:")
    
    for enemy in enemies:
        print(f"{enemy.name} appears!")
        print(f"Health: {enemy.health} | Attack: {enemy.attack}| Defense: {enemy.defense} | Speed: {enemy.speed}")
        time.sleep(1)

    combatants = [selected_hero] + enemies
    combatants.sort(key=lambda x: x.speed, reverse=True)

    while selected_hero.health > 0 and any(e.health > 0 for e in enemies):
        for fighter in combatants:
            if fighter.health <= 0:
                continue

            if fighter == selected_hero:
                print(f"\n{fighter.name} turn!")
                time.sleep(1)

                for i, e in enumerate(enemies):
                    if e.health > 0:
                        print(f"{i + 1} {e.name} (HP: {e.health})")

                try:
                    choice = int(input("Choose enemy to attack:")) - 1
                    target = enemies[choice]
                    if target.health <= 0:
                        print("This enemy is already defeated. Choose another one")
                        continue
                except (ValueError, IndexError):
                    print("Invalid choice")
                    continue

                print("\nWhat would you like to do?")
                print("1. Attack")
                print("2. Use Item")
                print("3. Run Away")
                action_choice = input("Choose an action (1, 2, or 3): ")
                time.sleep(1)
                
                if action_choice == "1":
                    print("\nAvailable skills:")
                    for i, skill in enumerate(fighter.weapon.skills, start=1):
                        print(f"{i}. {skill.name} - {skill.effect}")
                        time.sleep(0.5)
                    try:
                        skill_index = int(input("Choose skill: ")) - 1
                        chosen_skill = fighter.weapon.skills[skill_index]
                    except (ValueError, IndexError):
                        print("Invalid skill.")
                        continue

                    damage = selected_hero.attack  # Base damage

                    # Apply status effects (both player and target)
                    damage = selected_hero.apply_status_effects(target, damage)

                    if chosen_skill.effect_type == "aoe":
                        selected_hero.use_skill(
                            chosen_skill.name,
                            enemies=enemies
                        )
                    else:
                        selected_hero.use_skill(
                            chosen_skill.name,
                            target=target
                        )

                elif action_choice == "2":
                    consumables = [item for item in fighter.inventory if item.type == "consumable"]
                    if not consumables:
                        print("You have no usable items!")
                        continue
                    
                    print("\nYour Inventory:")
                    fighter.view_inventory()
                    time.sleep(1)

                    try:
                        item_choice = int(input("Choose an item to use (number): ")) - 1
                        selected_item = consumables[item_choice]
                        selected_item.use(fighter) 
                        fighter.inventory.remove(selected_item)
                        print(f"{selected_item.name} used!")
                    except (ValueError, IndexError):
                        print("Invalid item choice. Turn skipped.")
                        continue
                
                elif action_choice == "3":
                    print("Attempting to run away...")
                    if random.random() < 0.5:
                        print("You successfully ran away from the battle!")
                        return run_away_story(selected_hero, all_enemies)
                    else:
                        print("You failed to escape! The battle continues.")
                        continue
                else: 
                    print("Invalid action. Turn skipped.")
                    continue
            else:
                print(f"\nEnemies's turn")
                time.sleep(1)

                for enemy in enemies:
                    if enemy.health <= 0:
                        continue

                fighter.apply_status_effects(target=selected_hero, damage=fighter.attack)
                fighter.attack_target(selected_hero)

        
                print("\nEnemies turn:")
                time.sleep(1)

                enemy.apply_status_effects(target=selected_hero, damage=enemy.attack)
                enemy.attack_target(selected_hero)

    if all(e.health <= 0 for e in enemies):
        print("\nYou are Victorious")   

        xp_gained = sum(enemy.calulate_xp(selected_hero.level) for enemy in enemies)
        selected_hero.xp += xp_gained
        print(f"You earn {xp_gained} XP!")

        while selected_hero.xp >= selected_hero.level * 100:
            selected_hero.level_up()
        
        loot = []
        for enemy in enemies:
            loot.extend(enemy.drop_loot())
        
        if loot:
            print("\nYou found the following loot:")
            time.sleep(1)
            for item in loot:
                print(f"-{item}")
                selected_hero.inventory.append(Item(name=item, item_type ="loot"))
        
        while True:
            print("\nwhat will you do next?")
            print("1. Search the area for more loot.")
            print("2. Fight the next wave of enemies.")
            print("3. View your inventory.")
            print("4. Save and Exit.")
            next_choice = input("Enter your choice (1,2,3,4): ")
            time.sleep(1)

            if next_choice == "1":
                print("\nYou scour the battlefield for anything useful…")
                time.sleep(1)
                if random.random() < 0.5:
                    selected_hero.add_item_to_inventory(game_items["Health_Potion"])
                
                    print("You found a Health Potion.")
                else:
                    print("Sorry, theres nothing here.")
                continue 

            elif next_choice == "2":
            
                if wave < 3:
                    
                    print("\nYou ready yorself and prepare for another wave enemies to defeat…")
                    time.sleep(1)
                    return battle(selected_hero, enemy_count, all_enemies, wave+1)
                else:
                    dialogue = story()
                    dialogue.show_dialogue("Game_ending")
                    sys.exit()

            elif next_choice == "4":
                inv_names = []
                for entry in selected_hero.inventory:
                    if hasattr(entry,"name"):
                        inv_names.append(entry.name)
                    else:
                        inv_names.append(str(entry))
                print("Saving your game")
                save_data = {
                    "hero": {
                        "class": selected_hero.hero_class,
                        "hp": selected_hero.health,
                        "xp": selected_hero.xp,
                        "inventory": inv_names
                    }
                }
                with open(SAVE_FILE, "w", encoding="utf-8") as f:
                    json.dump(save_data, f, indent=2)
                print("\nGame saved. COME BACK SOON !")
                sys.exit()

            elif next_choice == "3":
                print("\n---- YOUR INVENTORY ----")
                selected_hero.view_inventory()
                input("\nPress Enter to go back…")
                continue
            else:
                print("Invalid choice. Please enter 1–4.")
                continue   
        
    if selected_hero.health <= 0:
        print(f"{selected_hero.name} has been defeated...")
        time.sleep(2)
        print("\nConsequences of your defeat are severe")
        time.sleep(2)

        k = min(2, len(selected_hero.inventory))

        lost_items = random.sample(selected_hero.inventory, k=k)
        for item in lost_items:
            selected_hero.inventory.remove(item)
            print(f"\nLost items: {item.name}")
            time.sleep(1)

        xp_loss = 50
        selected_hero.xp = max(0, selected_hero.xp - xp_loss)
        print(f"\nYou lose {xp_loss} Xp due to your defeat. Current Xp: {selected_hero.xp}")
        time.sleep(1)

        stat_penalty = 10
        selected_hero.health =max(1, int(selected_hero.health * (1-stat_penalty)))
        selected_hero.attack = max(1, int(selected_hero.attack * (1-0.05)))
        print(f"\nYour health reduced to {selected_hero.health} attack power is reduced to  {selected_hero.attack}.")
        time.sleep(2)

        selected_hero.status_effects["Fatigued"] = {"duration": 3, "reduction_percent": 0.2}
        print("\nYou have beocome fatigued. Your attack will be weaker for the next few battles")
        time.sleep(1)

        retry_choice = input("\nDo you want to try again? (yes/no): ")
        if retry_choice =="yes":
            print("\nYou gather your strength and prepare  to face the enemies again.")
            return battle(selected_hero, enemy_count, all_enemies)
        else:
            print("\nYou have been defeated. The journey ends here.")
            time.sleep(2)
            sys.exit()

def run_away_story(selected_hero):
    selected_hero.health = min(selected_hero.max_health, selected_hero.health +20)
    print(f"\n{selected_hero.name} health is now{selected_hero.health}/{selected_hero.max_health}.\n")
    time.sleep(1)

    print("\nYou look around the cave, wondering what to do next.")
    print("1. Rest and recover more before returning to the battlefield.")
    print("2. Head back to the battlefield now, determined to face the next wave.")
    
    choice = input("What will you do next? (1 or 2): ")
    
    if choice == "1":
        print("\nYou decide to take some extra time to rest, gathering your strength before facing the next wave.")
        selected_hero.health = min(selected_hero.max_health, selected_hero.health + 30) 
        print(f"\n{selected_hero.name}'s health is now {selected_hero.health}/{selected_hero.max_health}.")
        return "resting" 
    
    elif choice == "2":
        print("\nYou steel yourself and decide it's time to face the next wave of enemies.")
        time.sleep(2)
        print("\nYou gather your weapons and exit the cave, stepping back onto the battlefield with renewed determination.")
        return battle(selected_hero, enemy_count=3, all_enemies=all_enemies)  

    else:
        print("Invalid choice. You decide to rest a little longer, allowing your body to recover further.")
        time.sleep(1)
        return "resting"

if __name__ == "__main__":
    choice = main_menu()
    if choice == "new":
        game_intro()
        
    elif choice == "continue":

        print("Loading your saved game...)")
        time.sleep(1)
        game_intro()
