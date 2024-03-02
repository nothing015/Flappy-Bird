import pygame.sprite

import assets
import configs


# All about the background of the game and updating it constantly
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Initialize the sprite
        super().__init__(*groups)
        # Load the background image sprite
        """   29:44   """
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index,0))

    def update(self):
        # Move the background towards the left
        self.rect.x -= 1
        # Reset the position of the background when it moves off the screen
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
