import pygame
from mario import Mario
from settings import Settings
from button import Button
from startscreen import Startscreen
from background import Background

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Super Mario")

    #make button and start screen
    start_button=Button(ai_settings, screen)
    sc = Startscreen(ai_settings,screen, start_button)
    # make background
    bg = Background(ai_settings, screen)
    bg.scale_bg()
    #make mario
    mario=Mario(ai_settings,screen)

    while True:
        #mario.blitme()
        gf.check_events(ai_settings=ai_settings, screen=screen, mario=mario, start_button=start_button, sc=sc)
        gf.update_screen(ai_settings=ai_settings, screen=screen, mario=mario, sc=sc,bg=bg)

        if ai_settings.game_active:
        #     mario.update()
            gf.update_screen(ai_settings=ai_settings, screen=screen, mario=mario, sc=sc, bg=bg)







run_game()