import time, pygame
from Utility import KEY

class Display(object):
    def __init__(self, name, screen_size, relative_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption(name)
        self.current_input = set()
        self.relative_size = relative_size
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
            self.current_input.add(KEY.UP)
        if pressed[pygame.K_DOWN]:
            self.current_input.add(KEY.DOWN)
        if pressed[pygame.K_RIGHT]:
            self.current_input.add(KEY.RIGHT)
        if pressed[pygame.K_LEFT]:
            self.current_input.add(KEY.LEFT)
        pygame.event.pump()
    
    def spawn_entity(self, scroll_x, scroll_y, entity, color):
        pygame.draw.rect(self.screen, color, [(entity.x - scroll_x - entity.width/2)*self.relative_size + self.screen_size/2, ( - (entity.y - scroll_y) - entity.length/2)*self.relative_size + self.screen_size/2, self.relative_size*entity.length, self.relative_size*entity.width])
        pygame.display.update()