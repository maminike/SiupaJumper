import pygame
import Block


class Platform:
    def __init__(self, x, y, width, height, block_side, screen):
        self.screen = screen
        self.blocks = []
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.block_side = block_side
        self.horizontal_blocks_amount = width / block_side
        self.vertical_blocks_amount = height / block_side
        self.blocks_amount = self.vertical_blocks_amount * self.horizontal_blocks_amount
        self.rectangle = pygame.Rect((x, y), (width, height))
        for i in range(0, int(self.vertical_blocks_amount)):
            for j in range(0, int(self.horizontal_blocks_amount)):
                self.blocks.append(Block.Block(self.x + j * block_side, self.y + i * block_side, block_side))
        # if nie dzieli sie ładnie wypierdol sie

    def platform_blit(self):
        for i in self.blocks:
            self.screen.blit(i.surface, i.rectangle)

    def colide(self, player):

        rect_x = pygame.Rect(player.rectangle.x + player.direction_force, player.rectangle.y-1, player.surface.get_width(), player.surface.get_height())
        rect_y = pygame.Rect(player.rectangle.x, player.rectangle.y + player.gravity, player.surface.get_width(), player.surface.get_height())
        #pygame.draw.rect(self.screen, "Yellow", rect_y)

        if self.rectangle.colliderect(rect_x):
            #if player.rectangle.bottom > self.rectangle.top or player.top <= self.rectangle.bottom:
                #if abs(player.rectangle.left - self.rectangle.right) < 10:
            if player.direction_force < 0:
                print("LEWA SIUPA")
                player.direction_force = -abs(player.rectangle.left - self.rectangle.right)
                if player.rectangle.left == self.rectangle.right:
                    player.direction_force = 3

            if player.rectangle.bottom > self.rectangle.top or player.top <= self.rectangle.bottom:
                if abs(player.rectangle.right - self.rectangle.left) < 10:
                    print("PRAWA SIUPA")
                    player.rectangle.right = self.rectangle.left
                    player.direction_force = -3
        if self.rectangle.colliderect(rect_y):
            i = 0
            #if rect_y.top <= self.rectangle.bottom and self.rectangle.bottom + 10 < player.rectangle.bottom:
            if player.gravity < 0:
                #print(player.rectangle.top)
                #print(abs(player.rectangle.top - self.rectangle.bottom))
                #if abs(player.rectangle.top - self.rectangle.bottom) < 40:
                #player.rectangle.top = self.rectangle.botto
                print("DOL TEPA")
                player.gravity = -abs(player.rectangle.top - self.rectangle.bottom)
                #player.rectangle.top = -1000
            #if rect_y.bottom >= self.rectangle.top > rect_y.top:
            if player.gravity >= 0:
                player.gravity = -abs(player.rectangle.bottom - self.rectangle.top)
                print("GORA TEPA")
                player.onGround = True
                player.isJumping = False





            ''''
            if player.rectangle.bottom > self.rectangle.top:

                if abs(player.rectangle.left - self.rectangle.right) < 20:
                    player.rectangle.left = self.rectangle.right
                    player.direction_force = 3
                    player.isJumping = True
                    player.onGround = False

                if abs(player.rectangle.right - self.rectangle.left) < 20:
                    player.rectangle.right = self.rectangle.left
                    player.direction_force = -3
                    player.isJumping = True
                    player.onGround = False

                if abs(player.rectangle.top - self.rectangle.bottom) < 20:
                    player.rectangle.top = self.rectangle.bottom
                    player.gravity = 0
                    player.isJumping = True
                    player.onGround = False
                # todo gracz jak spada to jakby nie jest w skoku i przez to może się poruszać normalnie w locie
                if abs(player.rectangle.bottom - self.rectangle.top) < 10:
                    player.rectangle.bottom = self.rectangle.top
                    player.gravity = 0
                    player.onGround = True
                    player.isJumping = False
                '''