import random

# Room class to represent each room in the game
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.objects = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_exit(self, direction):
        return self.exits.get(direction, None)

    def get_objects(self):
        return self.objects

# Object class to represent interactive objects in the game
class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.usable = False

    def use(self):
        if self.usable:
            print("You use the", self.name)
            # Implement object usage logic here
        else:
            print("You can't use the", self.name)

# Game class to manage the game state and logic
class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.player_inventory = []

    def add_room(self, room):
        self.rooms[room.name] = room

    def start(self):
        # Implement game setup logic here

    def print_current_room(self):
        # Implement logic to print the current room's name, description, exits, and objects

    def parse_command(self, command):
        # Implement logic to parse and execute player commands

    def move(self, direction):
        # Implement logic to move the player to another room

    def take(self, object_name):
        # Implement logic to allow the player to take an object from the current room

    def use(self, object_name):
        # Implement logic to allow the player to use an object from their inventory

# Create game objects
game = Game()

# Create rooms
room1 = Room("Room 1", "This is room 1.")
room2 = Room("Room 2", "This is room 2.")
room3 = Room("Room 3", "This is room 3.")

# Set room exits
room1.add_exit("north", room2)
room2.add_exit("south", room1)
room2.add_exit("west", room3)
room3.add_exit("east", room2)

# Add rooms to the game
game.add_room(room1)
game.add_room(room2)
game.add_room(room3)

# Set the starting room
game.current_room = room1

# Start the game
game.start()