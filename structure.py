import time
inventory=[]

def main_Menu():
    while True:
        print("[1] Start")
        print("[2] Quit")
        
        option = input("\nEnter option: ").strip()  # Get user input inside the loop
        
       
        if option == "1":
            print("\nStarting Game.... ")
            time.sleep(1)
            start_Game()
            
            
            break
        elif option == "2":
            print("\nExiting game...")
            exit()
        else:
            print("\nInvalid option. Please enter 1 or 2.")
# Call the function to start the menu loop
def start_Game():
    time.sleep(1)
    username = input("\nEnter Hero name: ").strip()
   
    if not username:
        username = "Hero"
        print(f"Invaild name. using defaulting to {username}")
    display_intro(username)
    player_choice(username)
   

#stroy telling 
def display_intro(username):
    intro = f"""\nStranger:Hello {username}! We welcome you to a Brand-New world and You alone have been chosen as the hero 
of this land, a realm filled with wonder, mystery and untold challenegs. However, a great calamity looms
of the horizon-and impeding castrophe unknwon as the Waves. These relentless forces bring destruction and choas,threatening to consume everythinng in thier path.\n
""" 
    
    for line in intro.splitlines():
        print(line)
        time.sleep(2)

def player_choice(username):
    while True:
        choice = input(f"\nStarnger:Sir {username}, will you help us and fight againt the waves? (yes or no): ").strip().lower()
        if choice == "yes":
            print("\nStranger:Thank you brave Hero!. For your willness to help us in this endevor we will provide the land most sacred treasuer.")
            time.sleep(2)
            hero_type= hero_selection()
            print(f"You are now the {hero_type}.")

            break

        elif choice == "no":
            print(f"\nStranger:We understand, {username}. Not everyone can bare the wight of hero \n")
            time.sleep(2)
            print("You decided to let darkness fell over the land")
            time.sleep(3)
            print("\nGame over. Returing to the menu....\n")
            time.sleep(2)
            main_Menu()
            break
        else:
            print("Invaild option")
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

            choice = input ("Enter the number for the Hero you want to be (1-5)").strip()

            if choice in heroes:
                selected_hero = heroes[choice].split(" - ")[0]
                print(f"you have chosen {selected_hero}. Goodluck on your journey to save us from the Waves")
                return selected_hero

            else:
                print("invalid selection. Choose (1-5)")


if __name__ == "__main__":
    main_Menu()
    



        
        
    







