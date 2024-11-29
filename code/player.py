import pygame
from os.path import join
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300

    def update(self, dt):
        self.move(dt)
        self.shoot()

    def move(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize(
        ) if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

    def shoot(self):
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')
