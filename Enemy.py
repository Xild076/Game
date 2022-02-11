from Entity import Entity
from Utility import AITYPE

class Enemy(Entity):
    def __init__(self, x, y, health, speed, length, width, ai):
        super().__init__(x, y, health, speed, length, width)
        self.ai = ai
    
    def ai_movement(self, x, y):
        if self.ai == AITYPE.MELEE:
            if self.x > x:
                self.x -= self.speed
            elif self.x < x:
                self.x += self.speed
            else:
                pass
            if self.y > y:
                self.y -= self.speed
            elif self.y < y:
                self.y += self.speed
            else:
                pass