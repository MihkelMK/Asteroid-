# Asteroids laadne mäng
# Mihkel, Janek, Rihard
# 2018

from sys import *
import pygame

pygame.init()
screen = pygame.display.set_mode([1280,720])  # Teeme 720p akna
laev = pygame.image.load("Spraidid/laev.jpg") # Laeme muutujale laev pildi kosmoselaevast.
kiirus = 10                                   # Määrame kosmoselaeva liikumiskiiruse.
x = 640                                       # Kosmoselaeva tekkimis kordinaadid, silma järgi ekraani all keskel.
y = 600

mäng_käib = True
while mäng_käib:                              # Põhiline programmi tsükkel
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_käib = False
    keys = pygame.key.get_pressed()           # Otsib, kas vajutatakase noolenuppe. Liigutab laeva nuppudele vastavas suunas.
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_LEFT]:
        x -= 1

    screen.fill([255,255,255])                # Paneme tausta valgeks.
    screen.blit(laev, [x, y])                 # Joonistame kosmoselaeva x ja y kordinaatidele.
    pygame.display.flip()                     # Kuvame joonistatut monitoril.

    pygame.time.delay(16)                     # Ootame veidi. Nii on alati ühtlaselt ühes sekundis 60 kaadrit (60fps)
                                              # Sekundis on 1000ms, 1000ms/60 = 16.(6)ms
quit()