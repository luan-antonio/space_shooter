"""Main module"""

import pygame
from player import Player
from star import Star
from meteor import Meteor
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from os.path import join
from sprite_groups import all_sprites, meteor_sprites, laser_sprites
from random import randint

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

star_surf = pygame.image.load(
    join('images', 'star.png')).convert_alpha()
[Star(all_sprites, star_surf) for i in range(45)]
player = Player(all_sprites)

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()

# custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


def collisions():
    global running
    if pygame.sprite.spritecollide(player, meteor_sprites, True):
        running = False
    for laser in laser_sprites:
        if pygame.sprite.spritecollide(laser, meteor_sprites, True):
            laser.kill()


while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))
    all_sprites.update(dt)

    collisions()

    # draw the game
    display_surface.fill('darkgray')
    all_sprites.draw(display_surface)

    # test collision
    # player.rect.colliderect()

    pygame.display.update()
pygame.quit()
