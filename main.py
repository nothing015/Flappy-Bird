# remake of the game Flappy Bird (originally created by Dong Nguyen)
# Currently in progress, by Nuaiman


import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
score = 0
running = True
Gameover = False
gamestarted = False

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()
def create_sprites():
    # For the background to run constantly, 0 and 1(the gap)
    Background( 0, sprites)
    Background( 1, sprites)

    Floor(0, sprites)
    Floor(1, sprites)
    # First pipe
    return Bird(sprites), GameStartMessage(sprites)

bird, game_start_message = create_sprites()

#game_start_message = GameStartMessage(sprites)
#game_over_message = GameOverMessage(sprites)


pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            # Generating the pipes
            Column(sprites)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not Gameover:
                gamestarted = True
                game_start_message.kill()
                """  1 hour 01 min  """

            if event.key == pygame.K_ESCAPE and Gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_message = create_sprites()

        bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen)
    if gamestarted and not Gameover:
        sprites.update()

    if bird.check_collision(sprites):
        Gameover = True
        gamestarted = False
        GameOverMessage(sprites)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score =+ 1

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()