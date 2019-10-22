import pygame.font

class Startscreen():
    def __init__(self,ai_settings, screen, start_button):
        self.screen = screen
        self.ai_settings = ai_settings
        self.start_button = start_button
        self.bg_color=(0, 0, 200)




    def start(self):
        self.screen.fill(self.bg_color)
        self.start_button.draw_button()
       # self.screen.blit(self.super_mario_logo, (self.ai_setting.screen_width/3, 140))
