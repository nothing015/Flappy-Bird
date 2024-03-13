from enum import IntEnum, auto


# Rendering order of sprites, collision detection, and other game logic that depends on the layering of objects in
# the game scene
class Layer(IntEnum):
    BACKGROUND = auto()
    OBSTACLE = auto()
    FLOOR = auto()
    PLAYER = auto()
    UI = auto()
