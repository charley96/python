# Building a game based on an escape room theme

# Need 3 objects:
# Game Object
# Room - escape code and list of game objects found within the room
# Game - whole new instance of game - needs to keep track of 1 room and number of attempts to escape

# Text based so will run entirely within the terminal

# name = input("What is your name?\n")
# print("Ah!", name.capitalize(), "is your name!")

class GameObject:           # use camel case to separate names in classes, rather than underscores
    name = ""
    appearance = ""
    feel = ""           # These are fields: variables relating to the object
    smell = ""

    def __init__(self, name, appearance, feel, smell):     
# this is the initialiser function. This syntax is specific to the initialiser.  
# needs to be indented within the class
# used to setup the initial values of the given variables
# don't need to do the above part, can just initialise and setup the variables here
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

# Method is a function that belongs to a class
# We now want to add some methods to the game object class - so it can do more than just contain properties
# Methods will be look, touch and sniff - to print out other properties
    
    def look(self):         # these are methods relating to the game object, so need to include "self"
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch at the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You smell the {self.name}. {self.smell}\n"

# Now need to create a game object, to make use of the class

# game_object = GameObject("Knife", "Some appearance", "Some feel", "Some smell")

# print(game_object.name)
# print(game_object.sniff())

class Room:
    # Our Room class has an escape code and a list of game objects as attributes/fields
    escape_code = 0
    game_objects = []

    # Initializer
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # Returns whether the escape code of the room matches the code entered by the player
    def check_code(self, code):
        return self.escape_code == code

    # Returns a list with all the names of the objects we have in our room
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

# Now need to implement the game class
    
class Game:
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(732, objects)       # Uses the room class previously initialised

    def create_objects(self):       # will return a list of objects
        return [
            GameObject(
                "Jumper",
                "It's a blue jumper that had the number 27 stitched on it.",
                "Someone has unstitched the second number, leaving only the 2.",
                "The jumper smells of washing powder."
            ),
            GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.",
            "Someone had deliberately snapped off one of the legs.",
            "It smells like old wood."),
          GameObject(
            "Journal",
            "The final entry states that time should be hours then minutes then seconds (H-M-S).",
            "The cover is worn and several pages are missing.",
            "It smells like musty leather."),
          GameObject(
            "Bowl of soup", 
            "It appears to be tomato soup.",
            "It has cooled down to room temperature.",
            "You detect 7 different herbs and spices."),
          GameObject(
            "Clock", 
            "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
            "The battery compartment is open and empty.",
            "It smells of plastic."),
        ]
    
# Now going to create our take-turn method
# Will introduce the game loop and taking turns
    
    # For each turn, we want to present the prompt to the player
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if selection >=1 and selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        else:
            if self.guess_code(selection) == True:
                print("Congratulations! You have won the game!")
                return
            else:
                if self.attempts < 3:
                    print(f"Incorrect! Please try again. You have {3 - self.attempts} attempt(s) remaining.\n")
                    self.take_turn()
                else:
                    print("Game Over! You are out of lives and have lost the game.")
                    quit()

    # Shows the option to enter the code or interact further with the objects in the room
    def get_room_prompt(self):
        prompt = "Enter the 3-digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"      # += will add onto the previous string
            index += 1                          # create an index to number the options
        return prompt
    
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
    
    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"
    
    def interact_with_object(self, object, interaction):
        # which interaction? 1, 2 or 3? which one are we going to select
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
    
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1          # Don't need self.game.attempts as we're still in the same class
            return False

# game = Game()
# game.take_turn()

# Unit tests - functions that test small parts of code
# Unit tests should target individual functions or blocks of code
# Unit tests should cover all input and output scenarios
# Difficult to unit test if user input required, as you want unit testing to be automated
# Functions with lots of input and output aren't great candidates for unit testing

# Integration tests - ensure entire blocks of code function together as expected
# Target procedures or overarching functionality
# Tests the results of multiple functions running together

class RoomTests:

    def __init__(self):
        self.room1 = Room(111, [
            GameObject(
                "Jumper",
                "It's a blue jumper that had the number 27 stitched on it.",
                "Someone has unstitched the second number, leaving only the 2.",
                "The jumper smells of washing powder."
            ),
            GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.",
            "Someone had deliberately snapped off one of the legs.",
            "It smells like old wood.")
            ])
        self.room2 = Room(111, [])
        
    def test_check_code(self):
        print(self.room1.check_code(111) == True)
        print(self.room1.check_code(112) == True)
        print(self.room1.check_code(222) == False)

    def test_get_game_object_names(self):
        print(self.room1.get_game_object_names() == ['Jumper', 'Chair'])
        print(self.room2.get_game_object_names() == [])

tests = RoomTests()
tests.test_check_code()
tests.test_get_game_object_names()

# Generally tend to have unit test procedures/templates
        