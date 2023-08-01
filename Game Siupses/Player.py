import pygame as p


class Player:

    def __init__(self, p_width, p_height, screen, resp_height, p_speed=None):
        self.surface = p.Surface((p_width, p_height))
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
        self.Falling = 0
        self.direction_force = 0

    def update(self, plats):
        keys = p.key.get_pressed()
        for plat in plats:
            if not self.isJumping and self.onGround and not self.isCrouching:
                if keys[p.K_d]:
                    if abs(self.rectangle.right - plat.rectangle.left) < 6 and (self.rectangle.bottom <= plat.rectangle.top or self.rectangle.top <= plat.rectangle.bottom):
                        print("SIUPA")
                        self.rectangle.right = plat.rectangle.left - 5
                        if self.rectangle.right == plat.rectangle.left:
                            self.rectangle.centerx += 0
                if keys[p.K_a]:
                    if abs(self.rectangle.left - plat.rectangle.right) < 6 and (self.rectangle.bottom <= plat.rectangle.top or self.rectangle.top <= plat.rectangle.bottom):
                        self.rectangle.left = plat.rectangle.right + 5
                        if self.rectangle.right == plat.rectangle.left:
                            self.rectangle.centerx += 0

            self.collision(plat)

            # generalnie grav musi być przed jump już nie pamiętam dla czego    (zajebisty komentarz)
            #print(self.gravity)
            #print(self.isJumping)
        self.grav()
        self.jump(keys)
        if not self.onGround:
            self.rectangle.x += self.direction_force
                #self.isJumping = True
        if not self.isJumping and self.onGround and not self.isCrouching:
            if keys[p.K_d]:
                self.rectangle.centerx += 5

            if keys[p.K_a]:
                self.rectangle.centerx -= 5
                #print(self.direction_force)
        self.screen.blit(self.surface, self.rectangle)

    def jump(self, keys):
        # jumpington
        if keys[p.K_SPACE] and self.onGround:
            # jeżeli w jest klikniete to sie charguje siła skoka
            self.isJumping = False
            self.isCrouching = True
            self.direction_force = 0
            if self.jump_force <= 25:
                self.jump_force += 0.75
            if keys[p.K_a]:
                self.direction_force = -8
            if keys[p.K_d]:
                self.direction_force = 8

        elif self.jump_force != 0 and self.onGround:
            self.isCrouching = False
            self.isJumping = True
            self.onGround = False
            # jeżeli jumping force jest fajny to dopiero nakurwia
            self.gravity = -1 * self.jump_force  # zamianka jumping forca na ujemny żeby grawitacja działała odwrotnie łot
            self.jump_force = 0  # niesamowity świat chuja/ zerowanie forca skoka


    def collision(self, plat):
        rect_x = p.Rect(self.rectangle.x + self.direction_force, self.rectangle.y, self.surface.get_width(), self.surface.get_height())
        rect_y = p.Rect(self.rectangle.x, self.rectangle.y + self.gravity, self.rectangle.width, self.rectangle.height)
        #p.draw.rect(self.screen, "Yellow", rect_y)
        if self.isJumping and abs(self.rectangle.bottom - plat.rectangle.top) > 2:
            if self.rectangle.bottom > plat.rectangle.top:
                if self.direction_force < 0:
                    if rect_x.colliderect(plat.rectangle):
                        print("PRAWY BOK NIEWIDZIALNY RECT")
                        self.direction_force = -abs(self.rectangle.left - plat.rectangle.right)
                        if self.rectangle.left == plat.rectangle.right:
                            print("PRAWY BOK WIDZIALNY RECT")
                            self.direction_force = 3
                elif self.direction_force > 0:
                    if rect_x.colliderect(plat.rectangle):
                        print("LEWY BOK NIEWIDZIALNY")
                        self.direction_force = abs(self.rectangle.right - plat.rectangle.left)
                        if self.rectangle.right == plat.rectangle.left:
                            print("LEWY BOK WIDZIALNY")
                            self.direction_force = -3

                if self.direction_force < 0 and self.gravity < 0:
                    if rect_x.colliderect(plat.rectangle) and rect_y.colliderect(plat.rectangle):
                        print("WARUNEK ROGU PRAWEGO")
                        self.rectangle.left = plat.rectangle.right
                        self.direction_force = 3
                        #self.gravity = 1
                elif self.direction_force > 0 and self.gravity < 0:
                    if rect_x.colliderect(plat.rectangle) and rect_y.colliderect(plat.rectangle):
                        print("WARUNEK ROGU LEWEGO")
                        self.rectangle.right = plat.rectangle.left
                        self.direction_force = -3
                        #self.gravity = 1

        if self.gravity < 0 and self.isJumping:
            if rect_y.colliderect(plat.rectangle):
                self.gravity = -abs(self.rectangle.top - plat.rectangle.bottom)
                print("DOL WIDZIALNY")
                self.rectangle.top = plat.rectangle.bottom
                self.gravity = 1
        elif self.gravity >= 0:
            if rect_y.colliderect(plat.rectangle):
                #if abs(self.rectangle.bottom - plat.rectangle.top) < 2:
                print("GORA")
                self.rectangle.bottom = plat.rectangle.top
                if self.isJumping:
                    self.direction_force = 0
                self.gravity = 0
                self.isJumping = False
                self.onGround = True


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
