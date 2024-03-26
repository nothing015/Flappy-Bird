import pygame

import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):

        # Rendering order of sprites, collision detection ...
        # ... and other game logic that depends on the layering of objects in the game scene
        self._layer = Layer.PLAYER
        # List containing images for bird animation
        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap"),
        ]

        # Load the floor image sprite
        self.image = assets.get_sprite("redbird-midflap")
        # Get the rectangle of the bird image
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.flap = 0
        # Initialize the sprite
        super().__init__(*groups)

    def update(self):
        # Update method for Bird class.
        # Animates the bird by cycling through its images.
        # Rotate the images to create the flapping animation
        self.images.insert(0, self.images.pop())
        # Set the current image of the bird to the first image in the list
        self.image = self.images[0]
        # Apply gravity to the bird's flap velocity
        self.flap -= configs.GRAVITY
        self.rect.y -= self.flap
        # Create a mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.image)

        # Starts with throwing the bird like a projectile
        if self.rect.x < 50:
            self.rect.x += 3.25

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Flap the bird when spacebar is pressed (KEYDOWN event)
            self.flap = 0
            self.flap += 5

    def check_collision(self, sprites):
        for sprite in sprites:
            # If bird collides with pipe, floor or goes out of screen, collision becomes true
            if ((type(sprite) == Column or type(sprite) == Floor) and sprite.mask.overlap(self.mask,(
                    self.rect.x - sprite.rect.x,self.rect.y - sprite.rect.y)) or self.rect.bottom < 0):
                return True
        return False
