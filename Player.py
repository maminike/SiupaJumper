import pygame


class Player:

    def __init__(self, p_width, p_height, screen, resp_height, p_speed=None):
        self.surface = pygame.Surface((p_width, p_height))
        self.surface.fill("Red")
        self.rectangle = self.surface.get_rect(bottomleft=(500, resp_height))
        self.screen = screen
        self.jump = 0
        self.resp_y = resp_height
        self.gravity = 0
        self.p_speed = p_speed




    def jump1(self, keys):
        if keys[pygame.K_w]:
            self.jump += 1
        else:
            self.gravity = -1 * self.jump
            self.jump = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rectangle.centerx += 10
        if keys[pygame.K_a]:
            self.rectangle.centerx -= 10

        self.jump1(keys)
        self.grav()

        self.screen.blit(self.surface, self.rectangle)

    def grav(self):
        if self.rectangle.y + self.rectangle.height >= self.resp_y:
            self.gravity = 0
            self.rectangle.y = self.resp_y - self.rectangle.height

        self.gravity += 1
        self.rectangle.y += self.gravity
        if self.gravity > 10:
            self.gravity = 10
        if self.gravity < -1000000:
            self.gravity = -10
