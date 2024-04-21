# @property - definiuje że dana funkcja ma za zadanie zwrócić wartość jako zmienną klasy.

# Globals for the directions
# Change the values as you see fit
EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self._x = x_pos
        self._y = y_pos

    @property
    def coordinates(self):
        return (self._x, self._y)

    def move(self, movements):
        for command in movements:
            if command == "R":
                self.direction = (self.direction + 90) % 360
            elif command == "A":
                if self.direction == NORTH: self._y += 1
                elif self.direction == EAST: self._x += 1
                elif self.direction == WEST: self._x -= 1
                else: self._y -= 1
            elif command == "L":
                self.direction = (self.direction - 90) % 360
