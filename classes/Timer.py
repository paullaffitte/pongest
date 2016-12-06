#coding: utf8

import pygame

class Timer:
    def __init__(self):
        self.time = 0

    def set_timer(self):
        self.time = pygame.time.get_ticks()

    def get_elapsed(self):
        elapsed = pygame.time.get_ticks() - self.time
        self.set_timer()
        return float(elapsed) / 1000
