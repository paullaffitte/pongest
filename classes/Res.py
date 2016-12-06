#coding: utf8

import sys
import pygame
import config
sys.path.append('themes/' + config.THEME)
import theme
from Ball import *
from Paddle import *
from Coord import *

def get_path(file):
    return "themes/" + config.THEME + "/" + file

class Res:

    pygame.init()
    window = pygame.display.set_mode((config.WIDTH_SCREEN, config.HEIGHT_SCREEN))

    font = pygame.font.Font(get_path(theme.FONT), theme.SIZE_SCORE)
    pygame.mixer.music.load(get_path("music.ogg"))

    images = {Ball.__name__: pygame.image.load(get_path("ball.png")).convert_alpha(),
    Paddle.__name__: pygame.image.load(get_path("paddle.png")).convert()}

    sounds = {"paddle": pygame.mixer.Sound(get_path("paddle.ogg")),
    "wall": pygame.mixer.Sound(get_path("wall.ogg")),
    "score": pygame.mixer.Sound(get_path("score.ogg"))}
