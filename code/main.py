"""Main module"""

import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw the game
    display_surface.fill('blue')
    pygame.display.update()
pygame.quit()
