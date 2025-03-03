import time

def main_Menue():
     print("[1] start")
     print("[2] Quit")
     
     player = input("\nEnter option: ")
     actions = {
         "1": "\nLoading Game ...",
         "2": "\nExiting the game..."     
         }
     print(actions.get(player," Invalid option"))
     time.sleep(1)
     if player == "2":
        time.sleep(1)
        exit()






        
        
    







