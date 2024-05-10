print("#####--------37. Pokedex--------#####")

class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, level, region, height, weakness):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.level = level
        self.region = region
        self.height = height
        self.weakness = weakness

    def speak(self):
        print(f"{self.name * 2} ")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        print(f"Caught?: {self.is_caught}")
        print(f"Level: {self.level}")
        print(f"Region: {self.region}")
        print(f"Height: {self.height}")
        print(f"Weakness: {self.weakness}")


Charmander = Pokemon('0004', '🦎 Charmander 🦎 ', '🔥', 'The flame on its tail shows the strength of its life-force.', 'Has already been caught!', 15 , 'Johto 🗾', 2.4, '💧-🪨')
Squirtle = Pokemon('0007', '🐢 Squirtle 🐢 ', '💧', 'After birth, its back swells and hardens into a shell.', 'Has not already been caught!', 13 , 'Johto 🗾', 1, '⚡-🌿')
Bulbasaur = Pokemon('0001', '🦕 Bulbasaur 🦕 ', '🌿 - ☠️', 'It carries a seed on its back right from birth.', 'Has not already been caught!', 18 , 'Johto 🗾', 2.8, '🔥-❄️')

Charmander.speak()
Charmander.display_details()
