import time

def main_menu():
    while True:
        print("\n=====MAIN MENU=====")


        print("[1] Start")
        print("[2]Instructions")
        print("[3] Quit")

        player_choice = input("\nEnter option: ")
        actions = {
            "1": "\nLoading Game ...",
            "2": "\nOpening Instructions...",
            "3": "\nExiting the game..."

         }

        print(actions.get(player_choice," Invalid option"))

        time.sleep(1)
        if player_choice in ["1","2","3"]:
            return player_choice
        else: 
            print("\n Invalid Option. Enter 1,2,or 3")

def show_instructions():
    print("\n=====INSTRUCTIONS=====")
    print("You will be randomly assigned be a Hero ")
    print("Your choices will shape your journey in this world")
    print("Fight waves of enemies and uncover the mysteries of this world.")
    print("Make wise decisions or the kingdom will fall.")
    input("Press Enter to return to the main menu...")
    
    