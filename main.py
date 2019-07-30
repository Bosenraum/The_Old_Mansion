################################
# Title    -- The Old Mansion
# Author   -- Austin Rosenbaum
# Started  -- July 5, 2018
# Modified -- July 29, 2019
# Finished -- ??/??/????
################################

# Imports
# pygame?
import time, random

# Custom imports
from entity.player import Player
from map.spot import Spot

# Create map

# create a default spot to test
default_spot = Spot(0, 0)

# Create player object
name = input("What is your name? ")
player = Player(name, default_spot)

print(f"Welcome to The Old Mansion {player.name}!")

print(f"You are currently at ({player.location.x}, {player.location.y})")

# Create enemies
# Create items
