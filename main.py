import pygame

import assets
import configs
from objects.background import Background
from objects.floor import Floor

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
on = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

# For the background to run constantly, 0 and 1(the gap)
Background( 0, sprites)
Background( 1, sprites)

Floor(0, sprites)
Floor(1, sprites)


while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = false

    screen.fill("pink")

    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()