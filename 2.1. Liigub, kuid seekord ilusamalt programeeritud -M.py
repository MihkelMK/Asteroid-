# Asteroids laadne mäng
# Mihkel, Janek, Rihard
# 2018

import pygame as pg, random, sys

WIDTH = 720
HEIGHT = 800
FPS = 60
LAEV_IMG = pg.image.load("Spraidid/laev.png") # Laeme muutujale laev pildi kosmoselaevast.
KUUL_IMG = pg.image.load("Spraidid/kuul.png")

WHITE = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Asteroids")
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = LAEV_IMG
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        nupud = pg.key.get_pressed()
        if nupud[pg.K_a]:
            self.speedx = -8
        if nupud[pg.K_d]:
            self.speedx = +8
        if nupud[pg.K_w]:
            self.speedy = -8
        if nupud[pg.K_s]:
            self.speedy = +8
        self.rect.x += self.speedx
        self.rect.y += self.speedy

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()