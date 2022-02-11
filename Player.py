from turtle import speed
from Entity import Entity
from Utility import KEY

class Player(Entity):
    def __init__(self, x, y, health, speed, length, width):
        super().__init__(x, y, health, speed, length, width)
    
    def movement(self, direction):
        if direction == KEY.UP:
            self.y += self.speed
        if direction == KEY.DOWN:
            self.y -= self.speed
        if direction == KEY.RIGHT:
            self.x += self.speed
        if direction == KEY.LEFT:
            self.x -= self.speed