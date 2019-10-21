import pygame
from mario import Mario
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Super Mario")

    #make mario
    mario=Mario(ai_settings,screen)
    screen.fill(ai_settings.bg_color)
    while True:
        gf.check_events(ai_settings=ai_settings, screen=screen, mario=mario)
        screen.fill(ai_settings.bg_color)
        if ai_settings.game_active:
            mario.update()






run_game()