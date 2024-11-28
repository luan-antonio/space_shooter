"""Main module"""

import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
player_x = 100
player_y = 150

# importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                  for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw the game
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(source=star_surf, dest=pos)
    player_x += 0.1
    display_surface.blit(source=player_surf, dest=(player_x, player_y))
    pygame.display.update()
pygame.quit()
