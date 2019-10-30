import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec

class Mario(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mario,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.index=0
        self.acc= vec(0,0)

        # Load the mario image, and get its rect.
        self.image = pygame.image.load('mario/Little_Mario_Jump_Right/6.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
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
        self.was_moving_right = False
        self.was_moving_left = False
        self.jump= False
        self.down = False

    def update(self):
        """Update the mario's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        self.acc =vec (0,.1)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.mario_speed_factor
            #self.acc.x = -.5
            self.walking_right_animation()
        if self.was_moving_right:
            self.image = pygame.image.load('mario/Little_Mario_Running_Right/220.png')
            self.image = pygame.transform.scale(self.image, (40, 40))

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.mario_speed_factor
            self.walking_left_animation()
        if self.was_moving_left:
            self.image = pygame.image.load('mario/Little_Mario_Running_Left/221.png')
            self.image = pygame.transform.scale(self.image, (40, 40))
        if self.jump and self.was_moving_right:
            self.centery -= self.ai_settings.mario_jump_height
            self.jumping_right_animation()
        if self.jump and self.was_moving_left:
            self.centery -= self.ai_settings.mario_jump_height

        if self.rect.bottom != self.ai_settings.screen_height:
            self.centery += self.ai_settings.mario_jump_height

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery=self.centery

    def blitme(self):
        """Draw the mario at its current location."""
        self.screen.blit(self.image, self.rect)

    #def jump(self):

    def jumping_right_animation(self):
        jump_frames = [pygame.image.load('mario/Little_Mario_Jump_Right/6.png'),
                  pygame.image.load('mario/Little_Mario_Jump_Right/7.png'),
                  pygame.image.load('mario/Little_Mario_Jump_Right/8.png'),
                  pygame.image.load('mario/Little_Mario_Jump_Right/9.png'),
                  pygame.image.load('mario/Little_Mario_Jump_Right/10.png')]
                  #pygame.image.load('mario/Little_Mario_Jump_Right/6.png')
        self.index +=1
        if self.index >= len(jump_frames):
            self.index = 0

        self.image = jump_frames[self.index]
        self.image = pygame.transform.scale(self.image, (40, 40))

    def walking_left_animation(self):
        walk_frames = [pygame.image.load('mario/Little_Mario_Running_Left/221.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/222.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/223.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/224.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/225.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/226.png'),
                       pygame.image.load('mario/Little_Mario_Running_Left/228.png')]
        self.index += 1
        if self.index >= len(walk_frames):
            self.index = 0

        self.image = walk_frames[self.index]
        self.image = pygame.transform.scale(self.image, (40, 40))

    def walking_right_animation(self):
        walk_frames = [pygame.image.load('mario/Little_Mario_Running_Right/215.png'),
                       pygame.image.load('mario/Little_Mario_Running_Right/216.png'),
                       pygame.image.load('mario/Little_Mario_Running_Right/217.png'),
                       pygame.image.load('mario/Little_Mario_Running_Right/218.png'),
                       pygame.image.load('mario/Little_Mario_Running_Right/219.png'),
                       pygame.image.load('mario/Little_Mario_Running_Right/220.png')]
        self.index += 1
        if self.index >= len(walk_frames):
            self.index = 0

        self.image = walk_frames[self.index]
        self.image = pygame.transform.scale(self.image, (40, 40))


