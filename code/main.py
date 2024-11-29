"""Main module"""

import pygame
from player import Player
from star import Star
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from os.path import join

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(
    join('images', 'star.png')).convert_alpha()
[Star(all_sprites, star_surf) for i in range(45)]
player = Player(all_sprites)

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # draw the game
    display_surface.fill('darkgray')
    all_sprites.draw(display_surface)

    pygame.display.update()
pygame.quit()
