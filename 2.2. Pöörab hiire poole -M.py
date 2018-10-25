# Asteroids laadne mäng
# Mihkel, Janek, Rihard
# 2018

import pygame as pg, random, sys, math
from pygame.math import Vector2

WIDTH = 1280
HEIGHT = 720
FPS = 60
LAEV_IMG = pg.image.load("Spraidid/laev2.png") # Laeme muutujale laev pildi kosmoselaevast.

WHITE = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Asteroids")
clock = pg.time.Clock()
        
class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = LAEV_IMG
        self.rect = self.image.get_rect(center=pos)
        self.orig_img = self.image
        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)
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

        self.rotate()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y


##    def rotate(self):
##        mouse_pos = pg.mouse.get_pos()
##        # Calculate the vector to the mouse position by subtracting
##        # the self.pos vector from the mouse_pos.
##        rel_x, rel_y = mouse_pos - self.pos
##        # Use math.atan2 to get the angle in radians and convert it to degrees.
##        angle = -math.degrees(math.atan2(rel_y, rel_x))
##        # Rotate the image.
##        self.image = pg.transform.rotozoom(self.orig_img, angle, 1)
##        # Update the rect and keep the center at the old position.
##        self.rect = self.image.get_rect(center=self.rect.center)
        
    def rotate(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pg.transform.rotate(self.orig_img, int(angle))
        self.rect = self.image.get_rect(center=self.pos)




##all_sprites = pg.sprite.Group()
##player = Player()
##all_sprites.add(player)
##
### Game loop
##running = True
##while running:
##    # keep loop running at the right speed
##    clock.tick(FPS)
##    # Process input (events)
##    for event in pg.event.get():
##        # check for closing window
##        if event.type == pg.QUIT:
##            running = False
##
##    # Update
##    all_sprites.update()
##
##    # Draw / render
##    screen.fill(WHITE)
##    all_sprites.draw(screen)
##    # *after* drawing everything, flip the display
##    pg.display.flip()
##
##pg.quit()
        
def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    sprite_group = pg.sprite.Group()
    player = Player((300, 200))
    sprite_group.add(player)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        sprite_group.update()
        screen.fill((30, 30, 30))
        sprite_group.draw(screen)

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()