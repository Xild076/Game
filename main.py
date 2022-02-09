import time
import pygame
pygame.init()


class Display(object):
    def __init__(self, screen_size, relative_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.current_input = list()
        self.relative_size = relative_size
    
    def input_check(self):
        self.screen.fill((255,255,255))
        self.current_input.clear()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_input.append("w")
                if event.key == pygame.K_DOWN:
                    self.current_input.append("s")
                if event.key == pygame.K_RIGHT:
                    self.current_input.append("d")
                if event.key == pygame.K_LEFT:
                    self.current_input.append("a")
    
    def relative_origin(self, location_x, location_y):
        return int(location_x*self.relative_size-((self.screen_size)/2)), int(location_y*self.relative_size-((self.screen_size)/2))
    
    def spawn_entity(self, entity_x, entity_y, color):
        entity_x, entity_y = self.relative_origin(entity_x, entity_y)
        pygame.draw.rect(self.screen, color, (self.relative_size, self.relative_size, entity_x + (self.screen_size-self.relative_size)/2, entity_y + (self.screen_size-self.relative_size)/2))
        print(entity_x, entity_y)
        pygame.display.update()
        

class Player(object):
    def __init__(self):
        self.player_x = 0
        self.player_y = 0

class Enemy(object):
    def __init__(self, spawn_x, spawn_y):
        self.enemy_x = spawn_x
        self.enemy_y = spawn_y

    def movement(self, player_x, player_y):
        if abs(self.enemy_x - player_x) > abs(self.enemy_y - player_y):
            if self.enemy_x > player_x:
                self.enemy_x -= 0.5
            elif self.enemy_x < player_x:
                self.enemy_x += 0.5
            else:
                pass
        else:
            if self.enemy_y > player_y:
                self.enemy_y -= 0.5
            elif self.enemy_y < player_y:
                self.enemy_y += 0.5
            else:
                pass

"""class RenderMap(object):
    def __init__(self, map_size):
        self.map_size = map_size
        self.map = [[" " for i in range(self.map_size)] for j in range(self.map_size)]
    
    def update_map(self, player, enemies, scroll_x, scroll_y):
        print(player.player_x-scroll_x, player.player_y-scroll_y, "!")
        self.set_reference(player.player_x-scroll_x, player.player_y-scroll_y, "!")
        for enemy in enemies:
            self.set_reference(enemy.enemy_x-scroll_x, enemy.enemy_y-scroll_y, "@")
    
    def reset_map(self):
        self.map = [[" " for i in range(self.map_size)] for j in range(self.map_size)]
    
    def print_map(self):
        self.map
        for y in range(self.map_size):
            line = ""
            for x in range(self.map_size):
                line += self.map[x][y] + " "
            print(line)
        self.reset_map()
    
    def set_reference(self, location_x, location_y, entity_sign):
        try:
            self.map[int(location_x+((self.map_size-1)/2))][int(-1*location_y+((self.map_size-1)/2))] = entity_sign
        except:
            pass"""

class Game(object):
    def __init__(self):
        #self.visible_map = RenderMap(20)
        self.display = Display(1000, 50)
        self.player = Player()
        self.scroll_x = 0
        self.scroll_y = 0
        self.enemies = list()
        self.level_init()
        self.alive = True
    
    def level_init(self):
        self.enemies.append(Enemy(-10, 2))
        self.enemies.append(Enemy(-10, 10))
        self.enemies.append(Enemy(6, 10))
        self.enemies.append(Enemy(1, -10))
        self.enemies.append(Enemy(-10, 10))
    
    def tick(self):
        self.display.input_check()
        print(self.display.current_input)
        for player_input in self.display.current_input:
            if player_input == "w":
                self.player.player_y += 1
            if player_input == "a":
                self.player.player_x -= 1
            if player_input == "s":
                self.player.player_y -= 1
            if player_input == "d":
                self.player.player_x += 1
        self.scroll_x = self.player.player_x
        self.scroll_y = self.player.player_y
        for enemy in self.enemies:
            enemy.movement(self.player.player_x, self.player.player_y)
            if enemy.enemy_x == self.player.player_x and enemy.enemy_y == self.player.player_y:
                self.alive = False
                
    def render(self):
        self.display.spawn_entity(self.player.player_x-self.scroll_x, self.player.player_y-self.scroll_y, (0,0,0))
        for enemy in self.enemies:
            self.display.spawn_entity(enemy.enemy_x-self.scroll_x, enemy.enemy_y-self.scroll_y, (255,0,0))
        #print(f"Player X: {self.player.player_x}")
        #print(f"Player Y: {self.player.player_y}")
        #print(f"Player Location on Visible Map: {self.player.player_x-self.scroll_x}, {self.player.player_y-self.scroll_y}")
        #self.visible_map.update_map(self.player, self.enemies, self.scroll_x, self.scroll_y)
        #self.visible_map.print_map()
    
    def start(self):
        while self.alive:
            time.sleep(1)
            self.tick()
            self.render()
        print("ded nub lol")

game = Game()
game.start()
