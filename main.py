# remake of the game Flappy Bird (originally created by Dong Nguyen)
# Currently in progress, by Nuaiman


import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

# For the background to run constantly, 0 and 1(the gap)
Background( 0, sprites)
Background( 1, sprites)

Floor(0, sprites)
Floor(1, sprites)
# First pipe
bird = Bird(sprites)

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            # Generating the pipes
            Column(sprites)
        bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen)
    if not gameover:
        sprites.update()

    if bird.check_collision(sprites):
        gameover = True

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
