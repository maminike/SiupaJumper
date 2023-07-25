import pygame

class Block:
    def __init__(self, x, y, side):
        self.surface = pygame.Surface((side, side))
        self.surface.fill("Blue")
        self.rectangle = self.surface.get_rect(topleft=(x, y))
