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
        if self.rectangle.colliderect(player.rectangle):
            if player.rectangle.bottom > self.rectangle.top:

                if abs(player.rectangle.left - self.rectangle.right) < 20:
                    player.rectangle.left = self.rectangle.right
                    player.direction_force = 3

                if abs(player.rectangle.right - self.rectangle.left) < 20:
                    player.rectangle.right = self.rectangle.left
                    player.direction_force = -3

                if abs(player.rectangle.top - self.rectangle.bottom) < 20:
                    player.rectangle.top = self.rectangle.bottom
                    player.gravity = 0

                # todo gracz jak spada to jakby nie jest w skoku i przez to może się poruszać normalnie w locie
                if abs(player.rectangle.bottom - self.rectangle.top) < 10:
                    player.rectangle.bottom = self.rectangle.top
                    player.gravity = 0
                    player.onGround = True
                    player.isJumping = False
