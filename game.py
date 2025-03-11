import time
import json
from heroes import ShieldHero, SwordHero, SpearHero, BowHero

print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")
#delay
def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# insert dialogue   
class Dialogue:
     def __init__(self,dialogues_file =r"C:\Users\Owner\OneDrive\Documents\GitHub\project-1-andrewrichard\dialogues.json"):
        try:
            with open(dialogues_file, "r", encoding="utf-8") as f:
                self.dialogues = json.load(f)
        except FileNotFoundError:
            print('File not found')
            exit()
     
     def show_dialogoue(self, dialogue_id):
         if dialogue_id in self.dialogues:
             for line in self.dialogues[dialogue_id]:
                 print_with_delay(line, 0.03)

def display_dialogues(dialogue_ids):
    dialogue = Dialogue()
    for dialogue_id in dialogue_ids:
        dialogue.show_dialogoue(dialogue_id)
        print("-" * 20 + "\n" )
#menue
def main_Menue():
     print("[1] Start")
     print("[2] Quit")
     
     player_choice = input("\nEnter option: ")
     actions = {
         "1": "\nLoading Game ...",
         "2": "\nExiting the game..."
         }
     print(actions.get(player_choice," Invalid option"))
     if player_choice == "1":
         display_dialogues(["world"])
         time.sleep(1.5)
     elif player_choice == "2":
         exit()
# added differnet paths  
def choosePath():
     path = ""
     while path not in ["1", "2"]:
            path = input(
            "Which path will you choose?\n"
            "[1] Will you rise to greatness?\n"
            "[2] Or will you fall into darkness?\n"
            
            "Enter your choice (1 or 2): "
            )
            return path

#continouse the story
def checkPath(chosenPath):
    if chosenPath == "1": 

        print_with_delay("\nYou have chosen the path as Hero ")
        time.sleep(1)
        print_with_delay("\nstranger:Thank you brave Hero!. For your willingness to help us in this endevor")
        print_with_delay("First, we need you to pick the type of hero you want to be.")

        return hero_selection()
  
    elif chosenPath == "2":
        print_with_delay("\nYou have chosen to fall. Darkness consumes the land...\n")
        print_with_delay("\nReturing to menue....")
        return main_Menue()


### added choose hero 
def hero_selection():
    dialogue = Dialogue()
    hero_map = {
        "1": (ShieldHero, "Shield Hero"),
        "2": (SwordHero, "Sword Hero"),
        "3": (SpearHero, "Spear Hero"),
        "4": (BowHero, "Bow Hero")
    }
    
    print_with_delay("\nChoose your Hero: ")
    # Display hero options using list comprehension
    [print_with_delay(f"[{key}] {hero_type} Hero") for key, (_, hero_type) in hero_map.items()]
    
    while True:
        choice_input = input("\nEnter the number of the hero you want to preview: ").strip()
        selected = hero_map.get(choice_input)
        if not selected:
            print_with_delay("\nInvalid choice. Please try again.")
            continue
        
        chosen_class, hero_type = selected
        print_with_delay(f"\nYou chose {chosen_class.__name__}!\n")
        [print_with_delay(line) for line in dialogue.dialogues.get(hero_type, ["No description found."])]
        
        # Display the temporary hero's stats
        temp_hero = chosen_class("preview")
        temp_hero.show_stats()
        
        if input("\nDo you want to choose this hero? (yes/no): ").strip().lower() != "yes":
            print_with_delay("\nReturning to hero selection...\n")
            continue
        
 
        return chosen_class("Default")  # Return the hero instance without asking for a name
# the combat of the game 
def battle_waved(hero):
    number = 1

    if not hasattr(hero, "coin"):
        hero.coins = 0
    while True:
        print_with_delay({f"wave {number}: Monsters apper!"})
        print_with_delay("You engage in battle and defaeat the monsters!")
        

def main_game():
    main_Menue()
    chosen_path = choosePath()
    checkPath(chosen_path)
 #it should  be displaying dialogue for the stranger but it is not 
    display_dialogues(["Stranger"])

    print_with_delay("\nThe ground trembels... A wav of enemies approches!")
    print_with_delay("You are instantly transported to the battelfield.\n")


def main():
    main_game()

if __name__ == "__main__":
    main()
    
