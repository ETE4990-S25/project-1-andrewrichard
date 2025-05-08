import random
import time
from dialogues import story
from heroes import Shield, Sword, Spear, Bow
from items_classes import Item, load_items
from Enemies import load_enemies_from_json, Enemy
from menu import main_menu, SAVE_FILE
import json
import os
import sys

SAVE_FILE = "savegame.json"


def game_intro():
    print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")
    dialogue = story()
    dialogue.show_dialogue("game_intr")
    hero_awakening()


def hero_awakening():
    dialogue = story()
    dialogue.show_dialogue("hero_awakenin")
    dialogue.show_dialogue("robed_explanatio")
    selected_hero = choose_hero()
    player_decision(selected_hero)


items = load_items()
all_enemies = load_enemies_from_json()

hero_classes = {
    1: Sword,
    2: Spear,
    3: Bow,
    4: Shield
}


def choose_hero():
    current_choice = 1
    selected_hero =None

    print("You take a deep breath, stepping closer to the weapons befor you.")
    print("Each one hums with a power of its own, waiting for a wielder.")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\nAvailable heros to choose from:\n")
        for index, hero_class in hero_classes.items():
            hero_name = hero_class.__name__
            selection_marker = ">>" if current_choice == index else " "
            print(f"{selection_marker}{index}: {hero_name}{selection_marker}")

        selected_hero = hero_classes[int(current_choice)]()
        selected_hero.display_status()

        user_input = input("\n Use W/S to move up/down, Enter to select: ").strip().lower()

        if user_input == "w" and current_choice > 1:
            current_choice -= 1
        elif user_input == 's' and current_choice < len(hero_classes):
            current_choice += 1
        elif user_input == "":
            print(f"\nYou have selected the legendary {selected_hero.name}!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invailid Input.Please press (L), (R), or (Enter)")
            continue

    print("The moment your hand touches the weapon, the world around you shudders.")
    print(f"As the {selected_hero.name}, you feel the weight of responsibility settle on your shoulders.")
    print("\nThe robed figure nods solemnly and speaks:")
    
    if selected_hero.name == "Sword Hero":
        print("The Sword Hero... A symbol of courage and strength. The path ahead will be perilous, but your blade shall cleave through all who stand in your way.\n")
    elif selected_hero.name == "Spear Hero":
        print("The Spear Hero... Swift and precise, your strikes will pierce through even the toughest of enemies. But remember, your agility is as vital as your strength.\n")
    elif selected_hero.name == "Bow Hero":
        print("The Bow Hero... A master of ranged combat. From a distance, your arrows will strike true, but be wary of getting too close to danger.\n")
    elif selected_hero.name == "Shield Hero":
        print("The Shield Hero... A protector of all. Your resolve is unmatched, but your defense alone will not win this battle.\n")

    dialogue = story()
    dialogue.show_dialogue("beginning")
    return selected_hero


def player_decision(selected_hero):
    print("\nWhat do you do?")
    print("1. Search the area for supplies.")
    print("2. Move forward toward the sound of battle.")
    print("3. Take a defensive stance and observe your surroundings.")

    choice = input("Enter your choice (1,2, or 3): ")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "1":
            print("You carefully scan the area, searching through the wreckage for anything useful.")
            print("among the debris, you find a **health Potion\n")
            health_potion = items.get("Potion")
            if health_potion:
                selected_hero.add_item_to_inventory(health_potion)

            print("\nThese may be useful later")

            if random.random() > 0.7:
                print("Lucky find! you discover anoter **health Potion** nestled under boken stone.\n")
                if health_potion:
                    selected_hero.add_item_to_inventory(health_potion)

            print("\nBecause you took time to search , monsters noticed your presence")
            print("You're ambushed and forced into a battle with multiple enemies!")
            enemy_count = 3
            break
        elif choice == "2":
            print("You steel yourself and press foward. The sounds of battle grows louder.")
            print(
                "As you approach the ruined streets, a dark silhouette emerges form the swirling smoke its eyes glowing ominously.")
            print("More figures appear monsters, eye gleaming, surrounding you!")
            print("\nBecause of your bold approach, you are caught off guard and ambushed!")
            enemy_count = 2
            break

        elif choice == "3":
            print("You hold your ground, watchcing for movement.")
            print("Your insticts scream that your're not alone. A shadow flits behind the broken stone too fast to fully see.")
            print("You stay low, watching the shifting debris, waiting for the right moment to react.")
            print("Your cautious stance pays off. You're less likely to get ambushed in upcoming encounters.")
            selected_hero.alert = True
            enemy_count = 1
        else:
            choice = input("please enter a vaild option (1,2,3): ")
            break

    time.sleep(2)
    print("\n...The air grows heavy. You hear the snarls of beast closing in.")
    time.sleep(1.5)
    print("Weapons ready....")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    battle(selected_hero, enemy_count)


def display_enemies(enemies):
    """Prints the list of current enemies and their HP."""
    print("\n--- Enemies ---")
    for i, enemy in enumerate(enemies):
        print(f"{i + 1}. {enemy.name} (HP: {enemy.health}/{enemy.max_health})")
    print("---------------")

def choose_enemy(enemies):
    """Lets the player choose an enemy from the list."""
    while True:
        display_enemies(enemies)
        choice = input("Choose an enemy by number: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(enemies):
                return enemies[idx]
        print("Invalid choice. Try again.")

def handle_victory(player, enemies, wave, enemy_count):
    print("\n--- Victory! ---")
    xp = 20 * len(enemies)
    player.gain_xp(xp)
    print(f"{player.name} gained {xp} XP!")

    for enemy in enemies:
        for loot in enemy.loot:
            if random.random() < loot["drop_chance"]:
                print(f"Found loot: {loot['item']}")
                item = load_items().get(loot["item"])
                if item:
                    player.add_item_to_inventory(item)

    player.display_status()
    if input("Continue to next wave? (yes/no): ").lower() == "yes":
        battle(player, enemy_count + 1, wave + 1)
    else:
        print("Thanks for playing!")

def get_player_action():
    print("Choose your action:")
    print("1. Use Skill")
    print("2. Use Item")
    print("3. Run Away")
    while True:
        choice = input("Enter action number: ")
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid input. Please enter 1, 2, or 3.")

def use_skill(player, enemies):
    print("\nAvailable Skills:")
    for i, skill in enumerate(player.weapon.skills):
        print(f"{i + 1}. {skill.name} - {skill.description} (Damage: {skill.damage})")

    choice = input("Choose skill number: ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(player.weapon.skills):
            target = choose_enemy(enemies)
            player.weapon.use_skill(player.weapon.skills[idx].name, player, enemy=target, enemies=enemies)
            return True
    print("Invalid skill selection.")
    return False

def use_item(player):
    player.view_inventory()
    choice = input("Choose item number: ")
    if choice.isdigit():
        idx = int(choice) - 1
        return player.use_item(idx)
    print("Invalid item selection.")
    return False

def run_away():
    print("\nYou try to run away...")
    time.sleep(1)
    if random.random() < 0.5:
        print("You escaped!")
        return True
    print("You failed to escape!")
    return False

def enemies_turn(enemies, player):
    for enemy in enemies:
        if enemy.health <= 0:
            continue
        print(f"\n-- {enemy.name}'s Turn --")
        enemy.process_status_effects()
        if enemy.health > 0:
            enemy.use_skill(player)

def battle(player, enemy_count=1, wave=1):
    enemy_data = load_enemies_from_json()
    chosen_keys = random.choices(list(enemy_data.keys()), k=enemy_count)
    enemies = [enemy_data[key] for key in chosen_keys]

    print(f"\n--- Wave {wave} Begins! ---")
    display_enemies(enemies)

    while player.health > 0 and any(e.health > 0 for e in enemies):
        print(f"\n-- {player.name}'s Turn --")
        player.handle_status_effects()
        if player.health <= 0:
            break

        action = get_player_action()
        if action == "1" and not use_skill(player, enemies):
            continue
        elif action == "2" and not use_item(player):
            continue
        elif action == "3" and run_away():
            return

        enemies = [e for e in enemies if e.health > 0]
        if not enemies:
            handle_victory(player, enemies, wave, enemy_count)
            return

        enemies_turn(enemies, player)

    if player.health <= 0:
        print("You were defeated. Game Over.")
        handle_hero_defeat(player)

def handle_hero_defeat(selected_hero):
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
    print(f"\nYou lose {xp_loss} XP due to your defeat. Current XP: {selected_hero.xp}")
    time.sleep(1)

    stat_penalty = 10
    selected_hero.health = max(1, int(selected_hero.health * (1 - stat_penalty / 100)))
    selected_hero.attack = max(1, int(selected_hero.attack * 0.95))
    print(f"\nYour health reduced to {selected_hero.health}. Attack power is reduced to {selected_hero.attack}.")
    time.sleep(2)

    selected_hero.status_effects["Fatigued"] = {"duration": 3, "reduction_percent": 0.2}
    print("\nYou have become fatigued. Your attack will be weaker for the next few battles.")
    time.sleep(1)

    retry_choice = input("\nDo you want to try again? (yes/no): ")
    if retry_choice.lower() == "yes":
        print("\nYou gather your strength and prepare to face the enemies again.")
        return battle(selected_hero, enemy_count=2)  # Removed all_enemies
    else:
        print("\nYou have been defeated. The journey ends here.")
        time.sleep(2)
        sys.exit()


def handle_victory(selected_hero, enemies, wave, enemy_count):
    xp_gained = sum(enemy.calculate_xp(selected_hero.level) for enemy in enemies)
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
            print(f"- {item}")
            selected_hero.inventory.append(Item(name=item, item_type="loot"))

    while True:
        print("\nWhat will you do next?")
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
                health_potion = items.get("Potion")
                if health_potion:
                    selected_hero.add_item_to_inventory(health_potion)

                print("You found a Health Potion.")
            else:
                print("Sorry, there's nothing here.")
            continue

        elif next_choice == "2":
            if wave < 2:
                print("\nYou ready yourself and prepare for another wave of enemies to defeat…")
                time.sleep(1)
                return battle(selected_hero, enemy_count, wave + 1)  # Removed all_enemies
            else:
                dialogue = story()
                dialogue.show_dialogue("Game_ending")
                sys.exit()

        elif next_choice == "3":
            print("\n---- YOUR INVENTORY ----")
            selected_hero.view_inventory()
            input("\nPress Enter to go back…")
            continue

        elif next_choice == "4":
            inv_names = [item.name if hasattr(item, "name") else str(item) for item in selected_hero.inventory]
            print("Saving your game...")
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
            print("\nGame saved. COME BACK SOON!")
            sys.exit()

        else:
            print("Invalid choice. Please enter 1–4.")
            continue


if __name__ == "__main__":
    choice = main_menu()
    if choice == "new":
        game_intro()

    elif choice == "continue":

        print("Loading your saved game...)")
        time.sleep(1)
        game_intro()
