import time
import pygame
pygame.init()


class Display(object):
    def __init__(self, screen_size, relative_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.current_input = set()
        self.relative_size = relative_size
        self.relative_movement = self.screen_size//self.relative_size
        self.pause = False
    
    def input_check(self):
        self.screen.fill((255,255,255))
        self.current_input.clear()
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.pause:
                        self.pause = False
                    else:
                        self.pause = True
        if pressed[pygame.K_UP]:
            self.current_input.add("w")
        if pressed[pygame.K_DOWN]:
            self.current_input.add("s")
        if pressed[pygame.K_RIGHT]:
            self.current_input.add("d")
        if pressed[pygame.K_LEFT]:
            self.current_input.add("a")
        pygame.event.pump()
    
    def relative_origin(self, location_x, location_y):
        return int(self.relative_movement*location_x), int(self.relative_movement*location_y)
    
    def spawn_entity(self, entity_x, entity_y, color):
        entity_x, entity_y = self.relative_origin(entity_x, entity_y)
        pygame.draw.rect(self.screen, color, [entity_x + (self.screen_size-self.relative_size)//2, -entity_y + (self.screen_size-self.relative_size)//2, self.relative_size, self.relative_size])
        pygame.display.update()
        

class Player(object):
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.size = size

class Enemy(object):
    def __init__(self, spawn_x, spawn_y, size):
        self.x = spawn_x
        self.y = spawn_y
        self.size = size

    def movement(self, x, y):
        if self.x > x:
            self.x -= 0.125
        elif self.x < x:
            self.x += 0.125
        else:
            pass
        if self.y > y:
            self.y -= 0.125
        elif self.y < y:
            self.y += 0.125
        else:
            pass

class Game(object):
    def __init__(self):
        self.display = Display(200, 10)
        self.player = Player(1)
        self.scroll_x = 0
        self.scroll_y = 0
        self.enemies = list()
        self.level_init()
        self.alive = True
    
    def detect_collision(self, object_1, object_2):
        print(object_1.x, object_1.y, object_2.x, object_2.y)
        if object_1.x < object_2.x + object_2.size/2 and object_1.x + object_1.size/2 > object_2.x and object_1.y < object_2.y + object_2.size/2 and object_1.y + object_1.size/2 > object_2.y:
          return True
        else:
          return False
    
    def level_init(self):
        self.enemies.append(Enemy(-10, 2, 1))
    
    def tick(self):
        self.display.input_check()
        if not self.display.pause:
            for player_input in self.display.current_input:
                if player_input == "w":
                    self.player.y += 0.25
                if player_input == "a":
                    self.player.x -= 0.25
                if player_input == "s":
                    self.player.y -= 0.25
                if player_input == "d":
                    self.player.x += 0.25
            self.scroll_x = self.player.x
            self.scroll_y = self.player.y
            for enemy in self.enemies:
                enemy.movement(self.player.x, self.player.y)
                if self.detect_collision(self.player, enemy):
                  self.alive = False
                
    def render(self):
        self.display.spawn_entity(self.player.x-self.scroll_x, self.player.y-self.scroll_y, (0,0,0))
        for enemy in self.enemies:
            self.display.spawn_entity(enemy.x-self.scroll_x, enemy.y-self.scroll_y, (255,0,0))
    
    def start(self):
        while self.alive:
            time.sleep(0.025)
            self.tick()
            self.render()
        print("ded nub lol")

game = Game()
game.start()
