import pygame
from sys import exit
import Player

#inintitate pygame siupses
pygame.init()
w_WIDTH = 1000
w_HEIGHT = 500
screen = pygame.display.set_mode((w_WIDTH, w_HEIGHT))
clock = pygame.time.Clock()
ground = pygame.Surface((w_WIDTH, w_HEIGHT/5))
ground.fill("Green")
ground_rect = ground.get_rect(topleft=(0, 350))
# huj
player = Player.Player(20, 40, screen, ground_rect.y)


while True:
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    screen.blit(ground, ground_rect)
    player.update()
    clock.tick(60)
    pygame.display.update()
