import pygame
import sys
from pygame.sprite import Sprite

class Goomba(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.ai_settings = ai_game.settings

        self.image1 = pygame.image.load('Goomba/0.png')
        self.image2 = pygame.image.load('Goomba/14.png')

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.dead = False

        self.x = float(self.rect.x)

    def check_collision_with_items(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, deltaTime):
        if not self.dead:
            self.currState.execute(self, deltaTime)

    def blitime(self):
        self.x += (self.ai_settings.goomba_speed * self.ai_settings.goomba_direction)
        self.rect.x = self.x






