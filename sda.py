# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 7
# Video link: https://www.youtube.com/watch?v=U8yyrpuplwc
# Adding score (and drawing text)
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 480
HEIGHT = 600
FPS = 60

shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'Lask.wav'))


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            
    nupud = pg.key.get_pressed()
    if nupud[pg.K_LEFT]:
        shoot_sound.play()
pygame.quit()
