import pygame as pg, random, time

## Teeme mängia klassi, (kosmose)laev, mis on Sprite.
class Laev(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Anname LAEV_IMG muutujalt klassile Laev välimuse. (laev.png)
        self.image = LAEV_IMG
        # Kustutan valge tausta
        self.image.set_colorkey(VALGE)
        # Leiame laev.png pikslite kaudu klassi Laev suuruse ekraanil.
        self.rect = self.image.get_rect()
        # Ütleme, et selle klassi raadius on 20. See on tehtud, et kokkupõrkamine
        # asteroididega oleks täpsem. Arv leitud proovimisega.
        self.radius = 20
        # Ütleme, kuhu Laev peaks tekkima mängu alguses.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        # Paneme mängu alguses Laev'a kiiruse x-teljel nulliks.
        self.speedx = 0

    # Defineerime laskmise.
    def lask(self):
        # Ütleme, et "kuul" on klass "Kuul" Laev'a keskel üleval kordinaatidel.
        kuul = Kuul(self.rect.centerx, self.rect.top)
        # Lisame kuuli spraitide gruppi koik_spraidid, selles grupis on kõik spraidi.
        koik_spraidid.add(kuul)
        # Lisame kuuli spraitide gruppi kuulid, selles grupis on kõik ekraanil olevad kuulid.
        kuulid.add(kuul)
        # Valime laskmise helide listist suvaliselt ühe ja mängime seda.
        random.choice(lask_SND).play()

    # Defineerime klassi põhitsüklis oleva funktsiooni.
    def update(self):
        # Paneme kiiruse nulliks.
        self.speedx = 0
        # Vaatame, kas vajutakse nuppu, ja selle järgi paneme kiiruse.
        nupud = pg.key.get_pressed()
        if nupud[pg.K_LEFT]:
            self.speedx = -8
        if nupud[pg.K_RIGHT]:
            self.speedx = +8
        # Liigutame Laev'a vastavale kiirusele.
        self.rect.x += self.speedx
        # See rida hoiab ära Laev'a lahkumist ekraanilt.
        self.rect.clamp_ip(screen.get_rect())