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
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0, 0))
        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0, 0))
        # Create an image surface for the column
        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap))
        self.image.fill("red")
        # Get the rectangle of the image surface
        #17:24!!!!!!!!!!!!!
        self.rect = self.image.get_rect(topleft=(0, 0))

    # def update(self):
    #   self.rect.x -= 1
