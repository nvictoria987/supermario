import sys
from timer import Timer
import pygame


def check_keydown_events(event, ai_settings, screen, mario):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
    elif event.key == pygame.K_SPACE:
        mario.jump = True

        #need to add timer to make jump false
    # Timer(frames= mario.image ,wait=100, looponce=True)
    # mario.jump=False
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, mario):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    elif event.key == pygame.K_SPACE:
        mario.jump = False



def check_events(ai_settings, screen, mario, start_button, sc):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(ai_settings,screen, start_button, mouse_x, mouse_y)

def update_screen(ai_settings, screen, mario, sc, bg):
    """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    bg.blitme()
    mario.blitme()
    mario.update()
    bg.update(mario)


    if not ai_settings.game_active:
        sc.start()





        # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_start_button(ai_setting,screen,start_button, mouse_x, mouse_y):
    button_clicked = start_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not ai_setting.game_active:
        ai_setting.game_active = True
