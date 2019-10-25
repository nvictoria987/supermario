import pygame
import sys
import time

pygame.init()

def timer():
    count_down = 400
    while count_down > 0:
        print(count_down)
        time.sleep(1)
        count_down -= 1
        if count_down == 0:
            print("Game Over!")
timer()
