import random
import pygame.sprite
import assets
import configs

# Define a class for creating columns in the game
class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        # Set the gap between top and bottom pipes
        self.gap = 100
        # Load the sprite for the pipe
        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()
        # Set up the bottom pipe & top pipe by flipping the bottom pipe vertically
        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0, self.sprite_rect.height + self.gap))

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0, 0))
        # Create an image surface for the column and fill in the black rectangle area around the pipe
        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)
        # Get the rectangle of the image surface
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)   # Top ring of pipe
        self.image.blit(self.pipe_top, self.pipe_top_rect)    # Bottom ring of pipe

        sprite_floor_height = assets.get_sprite("floor").get_rect().height
        min_y = 100
        max_y = configs.SCREEN_HEIGHT - sprite_floor_height - 100
        # Generate a pipe with a gap at a random height
        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))

    def update(self):
        self.rect.x -= 1
        if self.rect.right <= 0:
            self.kill()
