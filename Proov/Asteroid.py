import pygame as pg, random, time

## Teeme Asteroidi klassi ja ütleme, et see on Sprite.
class Asteroid(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Ütleme, et originaal pilt on suvaline valik Asteroidid piltide listist.
        self.image_orig = random.choice(ASTEROID_IMG)
        # Ütleme, et originaal pilt on sama, mis self.image_orig.
            # Sellist vahet on vaja, sest objekti keerates ei muutu sellega kaasa selle
            # rect, seega keeramine toimub üle nurga, mitte keskelt. Kuidas seda täpselt
            # Tegin näev all "def rotate(self)" kirjelduses.
        self.image = self.image_orig
        # Leiame asteroidi pildi pikslite kaudu klassi Asteroid suuruse ekraanil.
        self.rect = self.image.get_rect()
        # Ütleme, et Asteroidi raadius on selle rect laius korda 0.8 (0.8 leitud proovimisega)
        # ja jagatud kahega. 
            #Tegin nii, sest asteroide on erinevaid suurusi ja nii on nende "hitbox"
            # olenemata suurusest õige.
        self.radius = int(self.rect.width * 0.8 / 2)
        # Paneme selle tekkima suvalisel laiusel ekraani sees.
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Paneme selle tekkima ekraanist väljas (üleval).
        self.rect.y = -100
        # Suvalisusele lisab Asteroididele antud suvaline kiirus.
        # Numbrid suvalised/tuunitud ise mängides.
            # y kiirus 2 kuni 10, sest nii liigub see kindlasti mängia poole.
        self.speedy = random.randrange(2, 10)
            # x kiirus -3 kuni 3
        self.speedx = random.randrange(-3, 3)
        # Paneme mängu alguses asteroidi keeramise ning aja viimasest uuenduset nulliks.
        # Aja mõõtmiseks valisin tick'id. 1 tick = 1/10 000 000 sec.
        self.rot = 0
        self.last_update = pg.time.get_ticks()
        # Paneme keeramis kiiruse suvaliseks arvuks suvaliselt valitud vahemikus.
        self.rot_speed = random.randrange(-10, 10)
        
    # Defineerime keeramise.
    def rotate(self):
        # Ütleme, et hetkel on sama hetk, kui palju on tick'e läinud mööda koodi algusest.
        hetkel = pg.time.get_ticks()
        # Kui hetke tick'id - viimase uuenduse ajal olnud tick'id on suurem kui 50, siis
            # Seega ootame 50 tick'i enne, kui Asteroidid keeramist uuendame.
        if hetkel - self.last_update > 50:
            # Ütleme, et viimati uuendati nüüd
            self.last_update = hetkel
            # Ütleme, et Asteroidi keeramine = self.rot'i ja enne pandid keeramise kiiruse
            # jääk jagades 360 on Asteroidid keeramine.
                # "% 360" kasutan, et arvuti peaks väiksemate numbritega tegelema.
                # Nt 361 % 360 = 1 nii, et suurim number, millega ta tegeleb on 360.
            self.rot = (self.rot + self.rot_speed) % 360
            # Ütleme, et uus pilt (nüüd keeramisega) on self.image_orig keeratud self.rot võrra.
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            
            ## Sellega siin teeme nii, et asteroid keerleks ümber oma keskme.
            
            # Saane vana keskme pärast pööret oleva rect keskmest.
            old_center = self.rect.center
            # Ütleme, et self.image on "pg.transform.rotate(self.image_orig, self.rot)" asemel uus new_image
            self.image = new_image
            # Saame uue rect'i pildi enda suurusest.
            self.rect = self.image.get_rect()
            # Ütleme, et uue pildi kesk punkt on sama, mis vanal pildil pärast keeramist.
            self.rect.center = old_center
    
    # Defineerime klassi põhitsüklis oleva funktsiooni.
    def update(self):
        # Keerame "rotate(self)" järgi.
        self.rotate()
        # Liigutame Laev'a vastavale kiirusele.
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        # Kui Asteroidid rect ülal osa on ekraanist välja lennanud, siis 
        if self.rect.top > HEIGHT + 10 or self.rect.left < -30 or self.rect.right > WIDTH + 30:
            # telepordime selle tagasi üles ja anname suvaliselt uued atribuudid.
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = -100
            self.speedy = random.randrange(2, 10)