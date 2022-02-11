from Display import Display
from entities.Player import Player
from entities.Enemy import Enemy
import time
from Utility import collision_detection, AITYPE

class Game(object):
    def __init__(self):
        self.display = Display(1000, 25)
        self.player = Player(0, 0, 10, 0.05, 2, 2)
        self.scroll_x = 0
        self.scroll_y = 0
        self.enemies = list()
        self.level_init()
        self.alive = True
    
    def level_init(self):
        self.enemies.append(Enemy(20, 20, 10, 0.01, 1, 1, AITYPE.MELEE))
        self.enemies.append(Enemy(-20, -20, 10, 0.01, 1, 1, AITYPE.MELEE))
        self.enemies.append(Enemy(20, -20, 10, 0.01, 1, 1, AITYPE.MELEE))
        self.enemies.append(Enemy(-20, 20, 10, 0.01, 1, 1, AITYPE.MELEE))
    
    def tick(self):
        self.display.input_check()
        if not self.display.pause:
            for player_input in self.display.current_input:
                self.player.movement(player_input)
            self.scroll_x = self.player.x
            self.scroll_y = self.player.y
            for enemy in self.enemies:
                enemy.ai_movement(self.player.x, self.player.y)
                if collision_detection(self.player, enemy, 3.625, 3.625):
                    #COLLISION DETECTION INCREASES PER 1.125 every time, 1 -> 2.5, 2 -> 3.625, 3 -> 5, 4 -> 6.25, 5 -> 7.365
                    self.alive = False
                
    def render(self):
        self.display.spawn_entity(self.scroll_x, self.scroll_y, self.player, (0,0,0))
        for enemy in self.enemies:
            self.display.spawn_entity(self.scroll_x, self.scroll_y, enemy, (0,0,255))
    
    def start(self):
        while self.alive:
            time.sleep(0.0025)
            self.tick()
            self.render()
        print("ded nub lol")