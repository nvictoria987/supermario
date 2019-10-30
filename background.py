import pygame
from pygame.locals import *
import os
import sys
import math
from mario import Mario
from settings import Settings

class Background:
    def __init__(self, ai_settings, screen):
        self.bg = pygame.image.load(os.path.join('levels', 'level_1.png')).convert()
        self.screen_rect = screen.get_rect()
        self.middle = self.screen_rect.right/2
        self.scrolling_speed = ai_settings.mario_speed_factor
        self.bg_x = 0

    def update(self, mario):
        if mario.moving_right and mario.rect.right >= self.middle:
            self.bg_x -= self.scrolling_speed

    def scale_bg(self):
        self.bg = pygame.transform.scale(self.bg, (int(self.bg.get_width()*2.69), int(self.bg.get_height() * 2.69)))

    def blitme(self):
        self.bg.blit(self.bg, (self.bg_x, 0))