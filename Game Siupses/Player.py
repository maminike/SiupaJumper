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

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.isJumping:
            if keys[pygame.K_d]:
                self.rectangle.centerx += 10
            if keys[pygame.K_a]:

                self.rectangle.centerx -= 10

        # generalnie grav musi być przed jump już nie pamiętam dla czego
        self.grav()
        self.jump(keys)

        #print("Crouch: "+ str(self.isCrouching))
        #print("Ground: " + str(self.onGround))
        print("Jumping: " + str(self.isJumping))
        self.screen.blit(self.surface, self.rectangle)

    def jump(self, keys):
        # jumpington
        if keys[pygame.K_w]:
            # jeżeli w jest klikniete to sie charguje siła skoka
            self.isJumping = False
            self.isCrouching = True
            self.onGround = True
            if self.jump_force <= 25:
                self.jump_force += 0.75
        elif self.jump_force != 0:
            self.isCrouching = False
            self.isJumping = True
            self.onGround = False
            # jeżeli jumping force jest fajny to dopiero nakurwia
            self.gravity = -1 * self.jump_force  # zamianka jumping forca na ujemny żeby grawitacja działała odwrotnie łot
            self.jump_force = 0  # niesamowity świat chuja/ zerowanie forca skoka

    def grav(self):
        # jak to sie dzieje na świecie przedmioty grawitacyjnie spadaja na dół
        # prędkość z jaką spada zwiększa się cały czas
        self.gravity += 1

        # jeżeli jest pod miejscem na którym sie zrespił no to go wykurwia tam znowu zjeba jebanego
        # grawitacja musi być większa od zera bo jak robi skoka to jest ujemna co nie
        # inaczej by se programik pomyślał że nie powinien spadać w góre i by wyzerował śmieć
        # todo naprawić te grawitacje huja wartą
        if self.rectangle.y + self.rectangle.height >= self.resp_y and self.gravity >= 0:
            self.gravity = 0
        # print(self.gravity)  # możesz zobaczyć jak ta grawitacja siupuje
            self.onGround = True
            self.isJumping = False
        # tutaj dokonuje sie spadanie(lub skakanie(srakanie hahaha)) właściwe, po prostu dodaje sie grawitacja do y
        self.rectangle.y += self.gravity