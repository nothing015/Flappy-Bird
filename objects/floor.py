import pygame.sprite

import assets
import configs

# Define a class for creating the floor in the game
class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Initialize the sprite
        super().__init__(*groups)
        # Load the floor image sprite
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index,configs.SCREEN_HEIGHT))

    def update(self):
        # Move the floor towards the left
        self.rect.x -= 1
        # Reset the position of the floor when it moves off the screen
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
