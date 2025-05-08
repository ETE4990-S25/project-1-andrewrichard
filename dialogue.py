import time

username =input("Enter hero name: ")
dialogues = {
        
"world_intro": [

        "\n─── The Beginning ───\n",
        "No one remembers the first crack in the sky. Some say it was a sign.",
        "Others, a warning. But when the heavens split open, the world below followed.",
        "",
        "Cities crumbled overnight. From the fractures, they came—",
        "monsters unlike anything we had ever known.",
        "",
        "Now, the old world is gone. What remains is ruin, chaos...",
        "and the fight to survive.",
        "",
        "And you? You have been chosen to stand against the endless waves.",
        "",
        "The question is... will you rise, or will you fall?",
        "\n───────────────────\n"
    ],
    
"stranger_intro": [
    f"Stranger: You have finally arrived sir {username}",

    "Stranger: The world is in danger. A great darkness is spreading.",

    "Stranger: The Waves bring destruction, and only a true hero can stop them.",

    "Stranger: Will you stand and fight, or turn away?",
    ],


}
      
def show_dialogue(key):
    if key in dialogues:
        for line in dialogues[key]:
            print(line)
            time.sleep(1.5)
    else:
        print("Dialogue Not Found")


    
    





