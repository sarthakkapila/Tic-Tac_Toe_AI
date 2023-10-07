import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw game elements here

    # Update the display
    pygame.display.flip()

    # Control frame rate (optional)
    pygame.time.Clock().tick(60)  # 60 FPS (adjust as needed)
