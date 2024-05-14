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

# Initializing Pygame
pygame.init()
# Creating the game window
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
# Creating a clock object to control the frame rate of the game
clock = pygame.time.Clock()
# Defining a custom event for creating columns
column_create_event = pygame.USEREVENT
score = 0
running = True
Gameover = False
gamestarted = False

assets.load_sprites()
# Creating a LayeredUpdates sprite group to manage all sprites in the game
sprites = pygame.sprite.LayeredUpdates()
# Function to create initial game sprites
def create_sprites():
    # For the background to run constantly, 0 and 1(the gap)
    Background( 0, sprites)
    Background( 1, sprites)

    Floor(0, sprites)
    Floor(1, sprites)
    # First pipe
    return Bird(sprites), GameStartMessage(sprites)

# Creating initial game sprites (bird and game start message)
bird, game_start_message = create_sprites()

#game_start_message = GameStartMessage(sprites)
#game_over_message = GameOverMessage(sprites)
# Setting up the column creation timer event to occur every 1.5 seconds
pygame.time.set_timer(column_create_event, 1500)
# Main game loop
while running:
    # Handling events
    for event in pygame.event.get():
        # Quit event: close the game
        if event.type == pygame.QUIT:
            running = False

        # Column creation event: create new columns
        if event.type == column_create_event:
            Column(sprites)

        # Keydown event handling for bird flapping and game control
        if event.type == pygame.KEYDOWN:
            # Start game on spacebar press if not already started and not game over
            if event.key == pygame.K_SPACE and not gamestarted and not Gameover:
                gamestarted = True
                game_start_message.kill()

            # Restart game on spacebar press after game over
            if event.key == pygame.K_SPACE and Gameover:
                Gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_message = create_sprites()
            # Bird flaps
        bird.handle_event(event)

    # Clearing the screen by filling it with black color
    screen.fill(0)

    # Drawing all sprites on the screen
    sprites.draw(screen)

    # Updating sprites if game is started and not over
    if gamestarted and not Gameover:
        sprites.update()

    # Checking for collision between bird and other sprites
    if bird.check_collision(sprites):
        Gameover = True
        gamestarted = False
        GameOverMessage(sprites)

    # Scoring - incomplete
    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score += 1

    # Updating the display to show changes
    pygame.display.flip()

    # Controlling the frame rate of the game
    clock.tick(configs.FPS)


pygame.quit()
