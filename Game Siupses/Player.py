import pygame


class Player:

    def __init__(self, p_width, p_height, screen, resp_height, p_speed=None):
        self.surface = pygame.Surface((p_width, p_height))
        self.surface.fill("Red")
        self.rectangle = self.surface.get_rect(bottomleft=(500, resp_height))
        self.screen = screen
        self.jump_force = 0
        self.resp_y = resp_height
        self.gravity = 0
        self.p_speed = p_speed
        self.onGround = 0
        self.isCrouching = 0
        self.isJumping = 0
        self.direction_force = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.isJumping and not self.isCrouching and self.onGround:
            if keys[pygame.K_d]:
                self.rectangle.centerx += 5
            if keys[pygame.K_a]:
                self.rectangle.centerx -= 5

        # generalnie grav musi być przed jump już nie pamiętam dla czego
        self.grav()
        self.jump(keys)
        print(self.isJumping)
        if not self.onGround:
            self.rectangle.x += self.direction_force
            self.isJumping = True


        self.screen.blit(self.surface, self.rectangle)

    def jump(self, keys):
        # jumpington
        if keys[pygame.K_SPACE] and self.onGround:
            # jeżeli w jest klikniete to sie charguje siła skoka
            self.isJumping = False
            self.isCrouching = True
            self.direction_force = 0
            if self.jump_force <= 25:
                self.jump_force += 0.75
            if keys[pygame.K_a]:
                self.direction_force = -8
            if keys[pygame.K_d]:
                self.direction_force = 8

        elif self.jump_force != 0 and self.onGround:
            self.isCrouching = False
            self.isJumping = True
            self.onGround = False
            # jeżeli jumping force jest fajny to dopiero nakurwia
            self.gravity = -1 * self.jump_force  # zamianka jumping forca na ujemny żeby grawitacja działała odwrotnie łot
            self.jump_force = 0  # niesamowity świat chuja/ zerowanie forca skoka

    def grav(self):
        self.gravity += 1

        if self.rectangle.y + self.rectangle.height >= self.resp_y and self.gravity >= 0:

            self.rectangle.bottom =  self.resp_y
            self.gravity = 0
            # print(self.gravity)  # możesz zobaczyć jak ta grawitacja siupuje
            self.onGround = True
            self.isJumping = False

        # tutaj dokonuje sie spadanie(lub skakanie(srakanie hahaha)) właściwe, po prostu dodaje sie grawitacja do y
        self.rectangle.y += self.gravity
