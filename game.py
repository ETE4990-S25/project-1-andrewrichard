import  menu
import dialogue
import time
 
print("welcome to Richard and Anderw RPG Game!. Hope you enjoy!\n")


menu.main_Menue()

dialogue.show_dialogue("world_intro")

dialogue.show_dialogue("stranger_intro")


def choosePath():
    path = ""
    while path not in [ "1", "2"]:
        path = input("which path will you chooses, will you rise(1) or fall(2): ")
    return path 

def checkPath(chosenPath):
    if chosenPath == "1":
        print("You have to chosen to rise. Your Jouerny begins now. hero!\n")
        time.sleep(1)
        print("\nstranger:Thank you brave Hero!. For your willingness to help us in this endevor")
        print("First, we need you to pick the type of hero u want to be. Please follow me")
        time.sleep(2)
        hero=hero_selection()
  
    elif chosenPath == "2":
        print("\nYou have chosen to fall. Darkness consumes the land...\n")
        print("\nReturing to menue....")
        time.sleep(2)
        return menu.main_Menue()




    
### added choose hero from old structure file 
def hero_selection():
        print("Choose the type of hero you want to be.")
        heroes = {
            "1": "Shield Hero",
            "2":"Sword Hero", 
            "3":"Spear Hero",
            "4":"Bow Hero", 
            "5": "Magic Hero"

        }
        for key, value in heroes.items():
            print(f"[{key}]{value}")
        while True:

            choice = input ("Enter the number for the Hero you want to be (1-5):").strip()

            if choice in heroes:
                selected_hero = heroes[choice].split(" - ")[0]
                print(f"you have chosen {selected_hero}. Goodluck on your journey to save us from the Waves")
                return selected_hero

            else:
                print("invalid selection. Choose (1-5)")

    


chosen_path = choosePath()
checkPath(chosen_path)
