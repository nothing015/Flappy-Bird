import pygame.sprite

import assets
import configs
from layer import Layer


# All about the background of the game and updating it constantly
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):

        # Rendering order of sprites, collision detection, and other game logic that depends on the layering of objects in the game scene
        self._layer = Layer.BACKGROUND
        # Load the background image sprite

        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index,0))
        # Initialize the sprite
        super().__init__(*groups)



    def update(self):
        # Move the background towards the left
        self.rect.x -= 1
        # Reset the position of the background when it moves off the screen
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH