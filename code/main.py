"""Main module"""

import pygame
from player import Player
from star import Star
from meteor import Meteor
from animated_explosion import AnimatedExplosion
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


def get_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(f'{current_time}', True, (240, 240, 240))
    text_rect = text_surf.get_frect(
        midbottom=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
    pygame.draw.rect(display_surface, (240, 240, 240),
                     text_rect.inflate(20, 10).move(0, -8), 5, 10)
    return (text_surf, text_rect)


# imports
star_surf = pygame.image.load(
    join('images', 'star.png')).convert_alpha()
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 40)
explosion_frames = [pygame.image.load(
    join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]


# custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


def collisions():
    global running
    if pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask):
        running = False
    for laser in laser_sprites:
        if pygame.sprite.spritecollide(laser, meteor_sprites, True, pygame.sprite.collide_mask):
            laser.kill()
            AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)


[Star(all_sprites, star_surf) for i in range(45)]
player = Player(all_sprites)

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
    display_surface.fill('#3a2e3f')
    all_sprites.draw(display_surface)

    (text_surf, text_rect) = get_score()
    display_surface.blit(text_surf, text_rect)

    pygame.display.update()
pygame.quit()
