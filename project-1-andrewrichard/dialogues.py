import json
import os
import time 


class story:
     def __init__(self,dialogues_file ="dialogues.json"):
        dialogues_path=os.path.join(os.path.dirname(__file__),dialogues_file)
        if not os.path.exists(dialogues_path):
            print(f"Error:'{dialogues_file}'")
            exit()
        try:
            with open(dialogues_path, "r", encoding="utf-8") as f:
                self.dialogues = json.load(f)
        except FileNotFoundError:
            print('File not found')
            exit()

     def print_with_delay(self,text, delay=0.03):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()

     def wait_and_clear(self):
         input("\npress Enter to continue...")
         os.system('cls' if os.name ==
         'nt' else 'clear')
     
     def show_dialogue(self, dialogue_id):
         if dialogue_id in self.dialogues:
            for line in self.dialogues[dialogue_id]:
                self.print_with_delay(line, 0.03)
            self.wait_and_clear()