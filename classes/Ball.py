#coding: utf8

from math import sqrt, pow
from Collider import *
from Timer import *
from Coord import *
import config

class Ball(Collider):
    def __init__(self, size):
        Collider.__init__(self, Coord(0, 0), size)
        self.timer = Timer()
        self.speed = Coord(2, 2)

    def launch_ball(self, position, speed):
        self.position = position
        self.speed = speed

    def move(self):
        elapsed = self.timer.get_elapsed()
        self.position.x += self.speed.x * elapsed
        self.position.y += self.speed.y * elapsed

    def get_norm_speed(self):
        return sqrt(pow(self.speed.x, 2) + pow(self.speed.y, 2))

    def collidePaddle(self, paddle):
        if self.collide(paddle):
            center_paddle = paddle.get_center()
            center_ball = self.get_center()
            collide_vector = Coord(center_ball.x - center_paddle.x, center_ball.y - center_paddle.y);
            collide_vector.y /= 2
            self.set_direction(collide_vector)
            self.set_norm_speed(self.get_norm_speed() + config.ACCELERATION)
            return (True)
        return (False)

    def set_norm_speed(self, norm_speed):
        old_norm_speed = self.get_norm_speed()
        self.speed.x = self.speed.x / old_norm_speed * norm_speed
        self.speed.y = self.speed.y / old_norm_speed * norm_speed

    def set_direction(self, direction):
        norm_direction = sqrt(pow(direction.x, 2) + pow(direction.y, 2))
        norm_speed = self.get_norm_speed()
        self.speed.x = direction.x / norm_direction * norm_speed
        self.speed.y = direction.y / norm_direction * norm_speed

    def position(self):
        return self.position
