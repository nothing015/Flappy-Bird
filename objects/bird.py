import pygame

import assets
from layer import Layer


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):

        # Rendering order of sprites, collision detection, and other game logic that depends on the layering of objects in the game scene
        self._layer = Layer.PLAYER

        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap"),
            ]

        # Load the floor image sprite
        self.image = assets.get_sprite("redbird-midflap")
        self.rect = self.image.get_rect(topleft=(0,0))
        # Initialize the sprite
        super().__init__(*groups)


    def update(self):
        self.images.insert(0, self.images.pop())
        self.image = self.images[0]
