# Importing Class Movie and Character from "movie.py"  file
from movie import Movie
from movie import Character

# Initiating object of class Movie with a empty constructor
movie1 = Movie()
print(movie1)

# Checking the attribute
print(movie1.name)

# Calling a method of the class
movie1.setName("Prometheus")

# Verifying the attribute
print(movie1.name)

# Initiating object of class Movie with a parameterized constructor
movie2 = Movie("Avengers")
print(movie2.name)

# Initiating object of class Character with a parameterized constructor
ironMan = Character("Iron Man")
# adding the object to the movie object
movie2.addCharacter(ironMan)

# Verifying
for character in movie2.characters:
    print(character.name)

# Adding another
pinkPanther = Character("Pink Panther")
movie2.addCharacter(pinkPanther)
#Verifying
for character in movie2.characters:
    print(character.name)

# Adding Some more with a another method
characters = [Character("Captain America"), 
        Character("Spider Man"), 
        Character("Hulk"), 
        Character("Black Widow")]
movie2.addCharacters(characters)
#Verifying
for character in movie2.characters:
    print(character.name)