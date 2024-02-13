import pygame.sprite

import assets
import configs


# All about the background of the game and updating it constantly
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        super().__init__(*groups)
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index,0))

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH