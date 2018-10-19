class Movie:
    characters = []
    def __init__(self, name="Not yet named!"):
        self.name = name

    def setName(self, name):
        self.name = name
    
    def addCharacter(self, character):
        self.characters.append(character)

    def addCharacters(self, characters):
        self.characters.extend(characters)

    pass

class Character:
    name = "Not yet named!"
    def __init__(self, name):
        self.name = name
    pass