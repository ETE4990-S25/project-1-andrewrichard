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
        print("\nstranger:Thank you brave Hero!. For your willness to help us in this endevor")
        print("we will provide the land most sacred treasuer. Please follow me")
        time.sleep(2)
  
  
    elif chosenPath == "2":
        print("\nYou have chosen to fall. Darkness consumes the land...\n")
        print("\nReturing to menue....")
        time.sleep(2)
        return menu.main_Menue()




    
### having the user pick the weapons

    


chosen_path = choosePath()
checkPath(chosen_path)
