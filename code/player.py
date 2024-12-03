import pygame
from os.path import join
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from sprite_groups import all_sprites, laser_sprites
from laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300
        self.laser_surf = pygame.image.load(
            join('images', 'laser.png')).convert_alpha()
        self.laser_sound = pygame.mixer.Sound(join('audio', 'laser.wav'))

        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        self.move(dt)
        self.shoot()
        self.laser_timer()

    def move(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize(
        ) if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

    def shoot(self):
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(self.laser_sound, self.laser_surf, self.rect.midtop,
                  (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
