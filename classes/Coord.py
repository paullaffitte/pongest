class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, comparaison):
        result = False
        if self.x == comparaison.x and self.y == comparaison.y:
            result = True
        return result

    def add(self, vector):
        if isinstance(vector, Coord):
            self.x += vector.x
            self.y += vector.y
        return self

    def sub(self, vector):
        if isinstance(vector, Coord):
            self.x -= vector.x
            self.y -= vector.y
        return self
