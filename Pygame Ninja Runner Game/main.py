import pygame
from random import randint
from pygame.locals import (
    QUIT
)
from sys import exit

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.player_throw_l_animate = False
        self.player_throw_r_animate = False
        self.player_run_animate = False
        self.player_run_l_animate = False
        self.player_idle_animate = False
        self.player_idle_l_animate = False
        self.right = True
        self.left = False

        # Throw Left Animation

        player_throw_l_1 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__000.png"), (100, 130)).convert_alpha()
        player_throw_l_2 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__001.png"), (100, 130)).convert_alpha()
        player_throw_l_3 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__002.png"), (100, 130)).convert_alpha()
        player_throw_l_4 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__003.png"), (100, 130)).convert_alpha()
        player_throw_l_5 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__004.png"), (100, 130)).convert_alpha()
        player_throw_l_6 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__005.png"), (100, 130)).convert_alpha()
        player_throw_l_7 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__006.png"), (100, 130)).convert_alpha()
        player_throw_l_8 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__007.png"), (100, 130)).convert_alpha()
        player_throw_l_9 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__008.png"), (100, 130)).convert_alpha()
        player_throw_l_10 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Left/Throw__009.png"), (100, 130)).convert_alpha()

        self.player_throw_l = [
            player_throw_l_1,
            player_throw_l_2,
            player_throw_l_3,
            player_throw_l_4,
            player_throw_l_5,
            player_throw_l_6,
            player_throw_l_7,
            player_throw_l_8,
            player_throw_l_9,
            player_throw_l_10
        ]

        # Throw Right Animation

        player_throw_r_1 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__000.png"), (100, 130)).convert_alpha()
        player_throw_r_2 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__001.png"), (100, 130)).convert_alpha()
        player_throw_r_3 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__002.png"), (100, 130)).convert_alpha()
        player_throw_r_4 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__003.png"), (100, 130)).convert_alpha()
        player_throw_r_5 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__004.png"), (100, 130)).convert_alpha()
        player_throw_r_6 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__005.png"), (100, 130)).convert_alpha()
        player_throw_r_7 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__006.png"), (100, 130)).convert_alpha()
        player_throw_r_8 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__007.png"), (100, 130)).convert_alpha()
        player_throw_r_9 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__008.png"), (100, 130)).convert_alpha()
        player_throw_r_10 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Throw Right/Throw__009.png"), (100, 130)).convert_alpha()

        self.player_throw_r = [
            player_throw_r_1,
            player_throw_r_2,
            player_throw_r_3,
            player_throw_r_4,
            player_throw_r_5,
            player_throw_r_6,
            player_throw_r_7,
            player_throw_r_8,
            player_throw_r_9,
            player_throw_r_10,
        ]

        # Idle Left Animation

        player_idle_l_1 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_000.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_2 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_001.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_3 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_002.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_4 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_003.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_5 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_004.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_6 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_005.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_7 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_006.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_8 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_007.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_9 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_008.png"),
                                                 (65, 130)).convert_alpha()
        player_idle_l_10 = pygame.transform.scale(
            pygame.image.load("Assets/Player Animations/Idle Left/Idle_L_009.png"),
            (65, 130)).convert_alpha()

        self.player_idle_l = [
            player_idle_l_1,
            player_idle_l_2,
            player_idle_l_3,
            player_idle_l_4,
            player_idle_l_5,
            player_idle_l_6,
            player_idle_l_7,
            player_idle_l_8,
            player_idle_l_9,
            player_idle_l_10
        ]

        # Idle Right Animation

        player_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__000.png"),
                                               (65, 130)).convert_alpha()
        player_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__001.png"),
                                               (65, 130)).convert_alpha()
        player_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__002.png"),
                                               (65, 130)).convert_alpha()
        player_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__003.png"),
                                               (65, 130)).convert_alpha()
        player_idle_5 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__004.png"),
                                               (65, 130)).convert_alpha()
        player_idle_6 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__005.png"),
                                               (65, 130)).convert_alpha()
        player_idle_7 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__006.png"),
                                               (65, 130)).convert_alpha()
        player_idle_8 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__007.png"),
                                               (65, 130)).convert_alpha()
        player_idle_9 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__008.png"),
                                               (65, 130)).convert_alpha()
        player_idle_10 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Idle Right/Idle__009.png"),
                                                (65, 130)).convert_alpha()

        self.player_idle = [
            player_idle_1,
            player_idle_2,
            player_idle_3,
            player_idle_4,
            player_idle_5,
            player_idle_6,
            player_idle_7,
            player_idle_8,
            player_idle_9,
            player_idle_10
        ]

        # Run Left Animation

        player_run_l_1 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__000.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_2 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__001.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_3 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__002.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_4 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__003.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_5 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__004.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_6 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__005.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_7 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__006.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_8 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__007.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_9 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__008.png"),
                                                (100, 130)).convert_alpha()
        player_run_l_10 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Left/Run_L__009.png"),
                                                 (100, 130)).convert_alpha()

        self.player_run_l = [
            player_run_l_1,
            player_run_l_2,
            player_run_l_3,
            player_run_l_4,
            player_run_l_5,
            player_run_l_6,
            player_run_l_7,
            player_run_l_8,
            player_run_l_9,
            player_run_l_10,
        ]

        # Run Right Animation
        player_run_1 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__000.png"),
                                              (100, 130)).convert_alpha()
        player_run_2 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__001.png"),
                                              (100, 130)).convert_alpha()
        player_run_3 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__002.png"),
                                              (100, 130)).convert_alpha()
        player_run_4 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__003.png"),
                                              (100, 130)).convert_alpha()
        player_run_5 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__004.png"),
                                              (100, 130)).convert_alpha()
        player_run_6 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__005.png"),
                                              (100, 130)).convert_alpha()
        player_run_7 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__006.png"),
                                              (100, 130)).convert_alpha()
        player_run_8 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__007.png"),
                                              (100, 130)).convert_alpha()
        player_run_9 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__008.png"),
                                              (100, 130)).convert_alpha()
        player_run_10 = pygame.transform.scale(pygame.image.load("Assets/Player Animations/Run Right/Run__009.png"),
                                               (100, 130)).convert_alpha()

        self.player_run = [player_run_1,
                           player_run_2,
                           player_run_3,
                           player_run_4,
                           player_run_5,
                           player_run_6,
                           player_run_7,
                           player_run_8,
                           player_run_9,
                           player_run_10]

        # Player Attributes
        self.player_index = 0
        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 455))
        self.gravity = 0
        self.called = False
        self.cycled = False

    def player_input(self):

        if keys[pygame.K_d] and self.rect.x <= 725:
            self.rect.x += 5
            self.player_run_animate = True
            self.player_run_l_animate = False
            self.right = True
            self.left = False

        if keys[pygame.K_a] and self.rect.x >= 10:
            self.rect.x -= 5
            self.image = self.player_run_l[int(self.player_index)]
            self.player_run_l_animate = True
            self.player_run_animate = False
            self.right = False
            self.left = True

        if keys[pygame.K_SPACE] and self.rect.bottom >= 455:
            self.player_run_animate = False
            self.player_run_l_animate = False
            self.player_idle_animate = False
            self.player_idle_l_animate = False
            self.gravity = -20

        if self.called and not self.cycled:
            if self.right:
                self.player_throw_r_animate = True
            if self.left:
                self.player_throw_l_animate = True

    def idle(self):
        if self.right:
            self.player_idle_animate = True
        elif self.left:
            self.player_idle_l_animate = True

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 455:
            self.rect.bottom = 455

    def animate_player(self):
        if self.player_run_animate:
            self.player_index += 0.4
            if self.player_index >= len(self.player_run):
                self.player_index = 0
                self.player_run_animate = False
            else:
                self.image = self.player_run[int(self.player_index)]
        elif self.player_run_l_animate:
            self.player_index += 0.4
            if self.player_index >= len(self.player_run_l):
                self.player_index = 0
                self.player_run_l_animate = False
            else:
                self.image = self.player_run_l[int(self.player_index)]
        elif self.player_idle_animate and self.right and not self.player_throw_r_animate:
            self.player_index += 0.4
            if self.player_index >= len(self.player_idle):
                self.player_index = 0
            else:
                self.image = self.player_idle[int(self.player_index)]
        elif self.player_idle_l_animate and self.left and not self.player_throw_l_animate:
            self.player_index += 0.4
            if self.player_index >= len(self.player_idle_l):
                self.player_index = 0
            else:
                self.image = self.player_idle_l[int(self.player_index)]
        elif self.player_throw_r_animate and self.right:
            self.player_index += 0.4
            if self.player_index >= len(self.player_throw_r):
                self.player_throw_r_animate = False
                self.cycled = True
                self.player_index = 0
            else:
                self.image = self.player_throw_r[int(self.player_index)]
        elif self.player_throw_l_animate and self.left:
            self.player_index += 0.4
            if self.player_index >= len(self.player_throw_l):
                self.player_throw_l_animate = False
                self.cycled = True
                self.player_index = 0
            else:
                self.image = self.player_throw_l[int(self.player_index)]

    # Returns X and Y coordinates from Player Class and assigns them to the Projectile Class
    def create_projectile(self):
        self.called = True
        self.cycled = False
        return Projectile(self.rect.x, self.rect.y, self.right, self.left)

    def update(self):
        self.idle()
        self.player_input()
        self.animate_player()
        self.apply_gravity()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        fly_frame_1 = pygame.image.load("Assets/Enemies/Fly/Fly1.png").convert_alpha()
        fly_frame_2 = pygame.image.load("Assets/Enemies/Fly/Fly2.png").convert_alpha()

        self.fly_frames = [
            fly_frame_1,
            fly_frame_2
        ]

        y_pos = 400
        x_pos = randint(900, 1100)
        self.index = 0
        self.image = self.fly_frames[self.index]
        self.rect = self.image.get_rect(midbottom=(x_pos, y_pos))

    def animation_state(self):
        self.index += 0.1
        if self.index >= len(self.fly_frames):
            self.index = 0
        else:
            self.image = self.fly_frames[int(self.index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 5
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, right, left):
        super().__init__()
        y += 80

        self.right = right
        self.left = left
        self.vel = 10

        if self.right:
            self.image = pygame.image.load("Assets/kunai_r.png")
            self.image = pygame.transform.scale(self.image, (80, 60))
            self.rect = self.image.get_rect(midleft=(x, y))
        elif self.left:
            self.image = pygame.image.load("Assets/kunai_l.png")
            self.image = pygame.transform.scale(self.image, (80, 60))
            self.rect = self.image.get_rect(midleft=(x, y))

    def update(self):
        if self.right:
            self.rect.x += self.vel
        elif self.left:
            self.rect.x -= self.vel

        # Kill Projectile Sprite once it goes off screen
        if self.rect.x >= 800 or self.rect.x <= -100:
            self.kill()


def display_txt():
    ammo_surf = game_font.render(f"Kunais: {ammo}", False, (64, 64, 64))
    ammo_rect = ammo_surf.get_rect(center=(400, 50))
    screen.blit(ammo_surf, ammo_rect)
    if ammo == 0:
        warning_surf = game_font.render("Reload!", False, (237, 59, 62))
        warning_rect = warning_surf.get_rect(center=(400, 100))
        screen.blit(warning_surf, warning_rect)


def sprite_collision():
    global game_running
    if pygame.sprite.spritecollide(player, enemy_group, False):
        print("Collision!")
        enemy_group.empty()
        game_running = False


# fly_frame_1 = pygame.image.load("Assets/Enemies/Fly/Fly1.png")

# Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

# Groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
projectile_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()
enemy = Enemy()

# Important Variables
pygame.display.set_caption("Project Pixel")
clock = pygame.time.Clock()
running = True
ammo = 5
game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_running = False

# Background
background_surf = pygame.image.load("Assets/background.png").convert()
background_surf = pygame.transform.scale(background_surf, (800, 600))

# Platform
platform_surf = pygame.image.load("Assets/Platform.png")
platform_surf = pygame.transform.scale(platform_surf, (800, 200))

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if game_running:
            if keys[pygame.K_r] and ammo == 0:
                ammo = 5
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ammo -= 1
                if ammo >= 0:
                    projectile_group.add(player.create_projectile())
                else:
                    ammo = 0
            if event.type == enemy_timer:
                enemy_group.add(Enemy())

    if game_running:
        screen.blit(background_surf, (0, 0))
        screen.blit(platform_surf, (0, 450))
        # screen.blit(fly_frame_1, (400, 400))

        # Objects on Screen
        projectile_group.draw(screen)
        player_group.draw(screen)
        player_group.update()
        projectile_group.update()
        enemy_group.draw(screen)
        enemy_group.update()

        sprite_collision()
        display_txt()

        pygame.display.update()
        clock.tick(60)

    elif not game_running:
        screen.fill((255, 255, 255))
        if keys[pygame.K_SPACE]:
            game_running = True
