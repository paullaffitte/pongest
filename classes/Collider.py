#coding: utf8

from Coord import *

class Collider:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def collide_1d(self, a, size_a, b, size_b):
        return a + size_a >= b and a <= b + size_b

    def collide(self, collider):
        return self.collide_1d(self.position.x, self.size.x, collider.position.x, collider.size.x) and self.collide_1d(self.position.y, self.size.y, collider.position.y, collider.size.y)

    def get_top(self):
        return self.position.y

    def get_bot(self):
        return self.position.y + self.size.y

    def get_left(self):
        return self.position.x

    def get_right(self):
        return self.position.x + self.size.x

    def get_center(self):
        return Coord(self.position.x + self.size.x / 2, self.position.y + self.size.y / 2)

    def set_top(self, position):
        self.position.y = position

    def set_bot(self, position):
        self.position.y = position - self.size.y

    def set_left(self, position):
        self.position.x = position

    def set_right(self, position):
        self.position.x = position - self.size.x
