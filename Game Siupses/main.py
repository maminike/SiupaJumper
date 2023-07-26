import pygame
from sys import exit
import Player
import Platform
# inintitate pygame siupses
pygame.init()

# screen stuff
w_WIDTH = 1000
w_HEIGHT = 500
screen = pygame.display.set_mode((w_WIDTH, w_HEIGHT))

clock = pygame.time.Clock()

# ground
ground = pygame.Surface((w_WIDTH, w_HEIGHT/5))
ground.fill("Green")
ground_rect = ground.get_rect(topleft=(0, 350))
# player
player = Player.Player(20, 40, screen, ground_rect.y)

platform = Platform.Platform(360, 100, 100, 100, 20, screen)

platform1 = Platform.Platform(550, 100, 100, 100, 20, screen)



while True:
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    screen.blit(ground, ground_rect)

    platform1.platform_blit()
    platform.platform_blit()
    player.update()
    platform.colide(player)
    platform1.colide(player)
    clock.tick(60)
    pygame.display.update()
