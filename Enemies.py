class Enemy:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
   
    def show_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}")

# Define the DarkSpider as a subclass of Enemy (you can add more enemies like this)
class DarkSpider(Enemy):
    def __init__(self):
        super().__init__(name="Dark Spider", health=50, attack=8, defense=4, speed=6)