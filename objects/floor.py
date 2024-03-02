import pygame.sprite

import assets
import configs


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        super().__init__(*groups)
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index,configs.SCREEN_HEIGHT))

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH