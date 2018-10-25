# Asteroids laadne mäng
# Mihkel, Janek, Rihard
# 2018

import pygame as pg, random, sys, time

WIDTH = 720
HEIGHT = 800
FPS = 60

pg.init()
pg.mixer.init()

LAEV_IMG = pg.image.load("Spraidid/laev.png")
KUUL_IMG = pg.image.load("Spraidid/kuul.png")
ASTEROID_IMG = []
Asteroid_list =["Spraidid/asteroid_väike.png", "Spraidid/asteroid_keskmine.png", "Spraidid/asteroid_keskmine2.png", "Spraidid/asteroid_suur.png"]
for img in Asteroid_list:
    ASTEROID_IMG.append(pg.image.load(img))
Taust = pg.image.load("Spraidid/taust.png")
Taust_rect = Taust.get_rect()

WHITE = (255, 255, 255)
RED = (255, 0, 0, 50)
BLACK = (0, 0, 0)

lask_SND = []
for snd in ["Helid/Lask.wav", "Helid/Lask2.wav"]:
    lask_SND.append(pg.mixer.Sound(snd))
plahvatus_SND = []
for sound in ["Helid/Vplahvatus.wav", "Helid/Kplahvatus.wav", "Helid/Splahvatus.wav"]:
    plahvatus_SND.append(pg.mixer.Sound(sound))
algus_SND = pg.mixer.Sound("Helid/Muusika/Intro Jingle.wav")
pg.mixer.music.load("Helid/Muusika/Venus.wav")

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Asteroids")
clock = pg.time.Clock()

font_name = pg.font.match_font("arial")
def prindi_tekst(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Laev(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = LAEV_IMG
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0


    def update(self):
        self.speedx = 0
        nupud = pg.key.get_pressed()
        if nupud[pg.K_LEFT]:
            self.speedx = -8
        if nupud[pg.K_RIGHT]:
            self.speedx = +8
        self.rect.x += self.speedx
        self.rect.clamp_ip(screen.get_rect())
        
    def lask(self):
        kuul = Kuul(self.rect.centerx, self.rect.top)
        all_sprites.add(kuul)
        kuulid.add(kuul)
        random.choice(lask_SND).play()
        
class Asteroid(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(ASTEROID_IMG)
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.8 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Kuul(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = KUUL_IMG
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
   
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pg.sprite.Group()
asteroidid = pg.sprite.Group()
kuulid = pg.sprite.Group()
laev = Laev()
all_sprites.add(laev)


raskustase = 1
for i in range(8 * raskustase):
    a = Asteroid()
    all_sprites.add(a)
    asteroidid.add(a)
skoor = 0

algus_SND.play()
time.sleep(2)
pg.mixer.music.play(loops=-1)

# Põhi tsükkel
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():i
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                laev.lask()
    all_sprites.update()
    
    hits = pg.sprite.groupcollide(asteroidid, kuulid, True, True, pg.sprite.collide_circle)
    
    for hit in hits:
        skoor += 50 - hit.radius
        a = Asteroid()
        all_sprites.add(a)
        asteroidid.add(a)
        random.choice(plahvatus_SND).play()

    hits = pg.sprite.spritecollide(laev, asteroidid, False, pg.sprite.collide_circle)
    if hits:
        running = False
        

    # Joonista/Kuva monitoril
    screen.fill(WHITE)
    screen.blit(Taust, Taust_rect)
    all_sprites.draw(screen)
    prindi_tekst(screen, str(skoor), 18, WIDTH / 2, 10)
    # Pärast kõige "joonistamist" näita monitoril
    pg.display.flip()
    
pg.quit()