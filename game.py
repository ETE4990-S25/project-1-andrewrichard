import time
import json
 
print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
         start_game()
     elif player_choice == "2":
         return main_Menue()

def start_game():
    display_dialogues(["world"])

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
        print("-" * 5 + "\n")

       
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


def checkPath(chosenPath):
    if chosenPath == "1": 

        print_with_delay("\nYou have chosen the path as Hero ")
        print_with_delay("\nstranger:Thank you brave Hero!. For your willingness to help us in this endevor")
        print_with_delay("First, we need you to pick the type of hero u want to be.\n")

        return hero_selection()
        
  
    elif chosenPath == "2":
        print_with_delay("\nYou have chosen to fall. Darkness consumes the land...\n")
        print_with_delay("\nReturing to menue....")
        return main_Menue()


### added choose hero from old structure file 
def hero_selection():
        print_with_delay("\nChoose the type of hero you want to be\n.")
        heroes = {
         
            "1":"Shield Hero",
            "2":"Sword Hero", 
            "3":"Spear Hero",
            "4":"Bow Hero", 
            

        }
        for key, value in heroes.items():
            print_with_delay(f"[{key}]{value}")

        while True:

            choice = input ("\nEnter the number for the Hero you want to be (1-4):").strip()

            if choice in heroes:
                selected_hero = heroes[choice]
                print_with_delay(f"\nyou have chosen {selected_hero}.")
            
            

            else:
                print_with_delay("invalid selection. Choose (1-4)")
        


main_Menue()
chosen_path = choosePath()
checkPath(chosen_path)
