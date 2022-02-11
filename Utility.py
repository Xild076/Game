from enum import Enum

class AITYPE(Enum):
    MELEE = 0,
    RANGED = 1

class KEY(Enum):
    UP = 0,
    W = 0,
    DOWN = 1,
    S = 1,
    LEFT = 2
    A = 2
    RIGHT = 3,
    D = 3

def collision_detection(entity_1, entity_2, relative_width, relative_length):
    if entity_1.x < entity_2.x + entity_2.width*relative_width and entity_1.x + entity_1.width*relative_width > entity_2.x and entity_1.y < entity_2.y + entity_2.length*relative_length and entity_1.y + entity_2.length*relative_length > entity_2.y:
        return True
    else:
        return False
    