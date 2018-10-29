import pygame as pg, random, time

""" Teeme kuuli klassi ja ütleme, et see on Sprite.
Muutujad: (x, y) ehk tekkimis kordinaadid.
"""
class Kuul(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # Anname KUUL_IMG muutujalt klassile Kuul välimuse. (kuul.png)
        self.image = KUUL_IMG
        # Leiame kuul.png pikslite kaudu klassi Kuul suuruse ekraanil.
        self.rect = self.image.get_rect()
        # Paneme tekkimis kordinaadid laskja kordinaatideks.
        self.rect.bottom = y
        self.rect.centerx = x
        # Paneme Kuul'i kiiruse y'teljel -10'neks. Nii liigub see üles.
        self.speedy = -10
   
    # Defineerime klassi põhitsüklis oleva funktsiooni.
    def update(self):
        # Liigutame Kuul'a vastavale kiirusele.
        self.rect.y += self.speedy
        # Vaatame, kas Kuul on lennanud ekraanist välja.
        if self.rect.bottom < 0:
            # Kui on, siis kustutame Kuul'i ära.
            self.kill()
