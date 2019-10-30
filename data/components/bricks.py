import pygame as pg
from .. import setup
from .. import constants as c


class Brick(pg.sprite.Sprite):
    """Bricks that can be destroyed"""
    def __init__(self, x, y, contents=None, name='brick'):
        """Initialize the object"""
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']

        self.frames = []
        self.frame_index = 0
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.bumped_up = False
        self.rest_height = y
        self.state = c.RESTING
        self.y_vel = 0
        self.gravity = 1.2
        self.name = name
        self.coin_total = 0


    def get_image(self, x, y, width, height):
        """Extracts the image from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):
        """Set the frames to a list"""
        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))


    def update(self):
        """Updates the brick"""
        self.handle_states()

    def resting(self):
        """State when not moving"""
        if self.coin_total == 0:
            self.state == c.OPENED

    def handle_states(self):
        """Determines brick behavior based on state"""
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()

    def bumped(self):
        """Action during a BUMPED state"""
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y >= (self.rest_height + 5):
            self.rect.y = self.rest_height


    def start_bump(self, score_group):
        """Transitions brick into BUMPED state"""
        self.y_vel = -6

        self.state = c.BUMPED


class BrickPiece(pg.sprite.Sprite):
    """Pieces that appear when bricks are broken"""
    def __init__(self, x, y, xvel, yvel):
        super(BrickPiece, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = xvel
        self.y_vel = yvel
        self.gravity = .8


    def setup_frames(self):
        """create the frame list"""
        self.frames = []

        image = self.get_image(68, 20, 8, 8)
        reversed_image = pg.transform.flip(image, True, False)

        self.frames.append(image)
        self.frames.append(reversed_image)


    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self):
        """Update brick piece"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        self.check_if_off_screen()

    def check_if_off_screen(self):
        """Remove from sprite groups if off screen"""
        if self.rect.y > c.SCREEN_HEIGHT:
            self.kill()












