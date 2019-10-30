import pygame

class Button():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('resources/fonts/Fixedsys500c.ttf', 40)
        self.msg = "start"
        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.ai_settings.screen_width / 2, self.ai_settings.screen_height - 180)

        # The button message only needs to be prepped once.
        self.prep_msg()

        # self.super_mario_logo=pygame.image.load('resources/graphics/logo.png')

    def prep_msg(self):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.ai_settings.screen_width / 2, self.ai_settings.screen_height - 180)

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)