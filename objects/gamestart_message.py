import pygame.sprite

import assets
import configs
from layer import Layer


class GameStartMessage(pygame.sprite.Sprite):
    # Rendering order of sprites, collision detection, and other game logic that depends on the layering of objects
    # in the game scene
    def __init__(self, *groups):
        self._layer = Layer.UI
        # Load the floor image sprite
        self.image = assets.get_sprite("message")
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH/2, configs.SCREEN_HEIGHT/2))
        self.mask = pygame.mask.from_surface(self.image)

        # Initialize the sprite
        super().__init__(*groups)