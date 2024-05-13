import pygame.sprite

import assets
import configs
from layer import Layer


# Define a class for creating the floor in the game
class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):

        # Rendering order of sprites, collision detection, and other game logic that depends on the layering of objects in the game scene
        self._layer = Layer.FLOOR
        # Load the floor image sprite
        self.image = assets.get_sprite("floor")
        # Getting the rectangle of the floor image and positioning it at the bottom left corner of the screen.
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index,configs.SCREEN_HEIGHT))
        # Creating a collision mask for the floor sprite based on its image.
        self.mask = pygame.mask.from_surface(self.image)

        # Initialize the sprite
        super().__init__(*groups)

    def update(self):
        # Move the floor towards the left
        self.rect.x -= 2
        # Reset the position of the floor when it moves off the screen
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH