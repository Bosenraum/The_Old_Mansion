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
from entity.entity import Entity
from map.map import GameMap

# Create map

# Create player object
name = input("What is your name? ")
player = Entity(name)

print(f"Welcome to The Old Mansion {player.name}!")

# Create enemies
# Create items
