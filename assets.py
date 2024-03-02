import os  # To interact with the operating system
import pygame   # Module for writing video games

sprites = {}

# This function will be responsible for loading sprite images from the specified directory
def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

# This function takes a name parameter, which is expected to be the name of a sprite image file without the file extension.
def  get_sprite(name):
    return sprites[name]
