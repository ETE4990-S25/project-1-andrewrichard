import time
import os
SAVE_FILE="savegame.json"

def main_menu():
    while True:
        print("\n=====MAIN MENU=====")
        
        if os.path.exists(SAVE_FILE):
            print("[1] Continue")
            print("[2] New Game")
        else:
            print("[1] Start Game")
            print("[2]Instructions")
            print("[3] Quit")
     
    
        player_choice = input("\nEnter option: ")

        if player_choice=="1" and os.path.exists(SAVE_FILE):
            return "continue"
        elif player_choice== "1":
            return "new"
        elif player_choice == "2" and os.path.exists(SAVE_FILE):
            return "new"
        elif player_choice == "3":
            show_instructions()
        elif player_choice == "4":
            print("Exiting the Game...")
            time.sleep(1)
            exit()
        else:
            print("Invalid option. ENter 1,2,3,4")

    


    
def show_instructions():
    print("\n=====INSTRUCTIONS=====")
    print("choose your hero and go on a journey ")
    print("Your choices will shape your journey in this world")
    print("Fight a waves of enemies and uncover the mysteries of this world.")
    print("Make wise decisions or the kingdom will fall.")
    print("You may save and continue progress anytime")
    input("Press Enter to return to the main menu...")
    
    