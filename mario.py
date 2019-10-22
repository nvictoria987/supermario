import pygame
from pygame.sprite import Sprite

class Mario(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mario,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the mario image, and get its rect.
        self.image = pygame.image.load('resources/graphics/mainship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new mario at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.jump= False
        self.down = False

    def update(self):
        """Update the mario's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.mario_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.mario_speed_factor
        if self.jump:
            self.centery -= self.ai_settings.mario_jump_height
        if self.rect.bottom != self.ai_settings.screen_height:
            self.centery += self.ai_settings.mario_jump_height

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery=self.centery

    def blitme(self):
        """Draw the mario at its current location."""
        self.screen.blit(self.image, self.rect)