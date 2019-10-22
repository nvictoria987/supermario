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

    while True:
        mario.blitme()
        gf.check_events(ai_settings=ai_settings, screen=screen, mario=mario)
        gf.update_screen(ai_settings=ai_settings, screen=screen, mario=mario)

        # if ai_settings.game_active:
        #     mario.update()
        # gf.update_screen(ai_settings=ai_settings, screen=screen)







run_game()