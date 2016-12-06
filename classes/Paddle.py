#coding: utf8

import config
from Collider import *
from Timer import *

class Paddle(Collider):
    def __init__(self, position, speed, size):
        Collider.__init__(self, position, size)
        self.timer = Timer()
        self.speed = speed
        self.mv_up = 0
        self.mv_down = 0
        self.spd_up = 1
        self.spd_down = 1

    def move(self):
        self.position.y += self.speed * (self.mv_up + self.mv_down) * self.spd_up * self.spd_down * self.timer.get_elapsed()
        if (self.get_top() < 0):
            self.set_top(0)
        elif (self.get_bot() > config.HEIGHT_SCREEN):
            self.set_bot(config.HEIGHT_SCREEN)

    def move_up(self, move):
        self.mv_up = -1 if move else 0
        self.timer.set_timer()

    def move_down(self, move):
        self.mv_down = 1 if move else 0
        self.timer.set_timer()

    def speed_up(self, speed):
        self.spd_up = config.SPEED_UP if speed else 1

    def speed_down(self, speed):
        self.spd_down = config.SPEED_DOWN if speed else 1

    def speed(self, speed):
        self.speed += speed
