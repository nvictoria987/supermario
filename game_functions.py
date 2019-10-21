import sys

import pygame


def check_keydown_events(event, ai_settings, screen, mario):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
   # elif event.key == pygame.K_SPACE:
        #jump
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, mario):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False


def check_events(ai_settings, screen, mario):
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
