# Asteroids laadne mäng
# Janek - Asteroidid; Rihard - Laev ja kuulid; Mihkel - Helid(Tehtud kasutades bfxr.net, Muusika - opengameart.org),
# Pildid, Skoor, Põhitsükkel, Kommentaarid.
# 2018

# Impordime vajalikud asjad
import pygame as pg, random, time, importlib, Laev, Kuul, Asteroid

pg.init()
pg.mixer.init()
clock = pg.time.Clock()

# Paneme skoori nulli.
skoor = 0

# Defineerime ekraani suuruse ja programmi kiiruse(FPS).
WIDTH = 700
HEIGHT = 800
FPS = 60

# Defineerime värvi, et hiljem oleks neid seda kasutada.
VALGE = (255, 255, 255)

# Teeme akna enne defineeritud suurustega ja paneme selle nimeks "Asteroids".
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Asteroids")


## Kanname vastavetele muutjutale kõik vajalikud pildid.
##
LAEV_IMG = pg.image.load("Spraidid/laev.png")
KUUL_IMG = pg.image.load("Spraidid/kuul.png")

# Teeme tühja asteroidid jaoks listi.
ASTEROID_IMG = []
# Teeme teise listi kõikidest asteroidid piltide nimedest ja asukohast.
Asteroid_list =["Spraidid/asteroid_väike.png", "Spraidid/asteroid_keskmine.png", "Spraidid/asteroid_keskmine2.png", "Spraidid/asteroid_suur.png"]
# Lisame iga pildi esimesse listi.
for img in Asteroid_list:
    ASTEROID_IMG.append(pg.image.load(img))

# Laeme sisse ka tasuta ning leiame selle suuruse.
Taust = pg.image.load("Spraidid/taust.png")
Taust_rect = Taust.get_rect()


## Kanname vastavetele muutjutale kõik vajalikud helid.
##
# Kuna heli faile on mõlemas kategoorias mitu, siis käitume sarnaselt, nagu asteroidide piltidega.
lask_SND = []
for snd in ["Helid/Lask.wav", "Helid/Lask2.wav"]:
    lask_SND.append(pg.mixer.Sound(snd))

plahvatus_SND = []
for sound in ["Helid/Vplahvatus.wav", "Helid/Kplahvatus.wav", "Helid/Splahvatus.wav"]:
    plahvatus_SND.append(pg.mixer.Sound(sound))
algus_SND = pg.mixer.Sound("Helid/Muusika/Intro Jingle.wav")
# Anname pygame'ile teada, milline on muusika fail.
pg.mixer.music.load("Helid/Muusika/Venus.wav")

""" Teeme funktsiooni, mis kuvab ekraanile teksti.
Muutujad: pind, kuhu kuvada, teksti sisu, suurus ja x, y kordinaadid.
"""
# Defineerime fondi.
font_name = pg.font.match_font("arial")
def prindi_tekst(surf, text, size, x, y):
    # Määrame teksti fondiks enne defineeritud fondi.
    font = pg.font.Font(font_name, size)
    # "Joonistame" teksti, valgena. True parameeter lülitab sisse anti-aliasing'u.
    text_surface = font.render(text, True, VALGE)
    # Saame teksti suurse ekraanil.
    text_rect = text_surface.get_rect()
    # Ütleme, et teksi ülemine keskosa peaks olema x, y kordinaatidel.
    text_rect.midtop = (x, y)
    # Kuvame "joonistatud" teksti ekraanil.
    surf.blit(text_surface, text_rect)

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

# Defineerime koik_spraidid spraitide grupina.
koik_spraidid = pg.sprite.Group()

# Defineerime asteroidid spraitide grupina.
asteroidid = pg.sprite.Group()

# Defineerime kuulid spraitide grupina.
kuulid = pg.sprite.Group()

# Ütleme, et laev on klass "Laev".
laev = Laev()
# Lisame spraitide gruppi koik_sparidi muutuja "laev".
koik_spraidid.add(laev)

# Tekitame asteroidi Asteroid klassi järgi ja paneme selle
# spraidi gruppidesse koik_sparidid ja asteroid. Kordame 8 korda.
for i in range(8):
    a = Asteroid()
    koik_spraidid.add(a)
    asteroidid.add(a)

# Mängime alguse heli.
algus_SND.play()
# Ootme alguse heli pikkuse.
time.sleep(2)
# Paneme mängima laulu lõpmatult.
pg.mixer.music.play(loops=-1)

## Põhi tsükkel
# Ütleme, et mäng jookseb.
jookseb = True
# Tsükel kestab, kuni mäng jookseb
while jookseb:
    # Uuenda kella tickides mutuja "FPS" väärtuse võrra.
    clock.tick(FPS)
    # Jälgmine toimuvaid sündmusi.
    for event in pg.event.get():
        # Kui mäng pannakse mingit viisi kinni, siis lõpeta põhi tsükkel.
        if event.type == pg.QUIT:
            jookseb = False
        # Või siis kui vajutataekse nuppu,
        elif event.type == pg.KEYDOWN:
            # vaatame, kas see on tühik. Kui on,
            if event.key == pg.K_SPACE:
                # siis kasutame Laeva klassiga laskmise funktsiooni.
                laev.lask()
    
    # Kasutame kõikidel spraitidel update funktsiooni.
    koik_spraidid.update()
    
    # Ütleme, et "puuted" on kahe spraidi grupi kokkupuude (asteroidid ja kuulid),
    # et mõlemad kokkupuutel kustutada ning et kokkupuute tüüp on "cicle". Selle jaoks oli vaja classide raadiuseid.
    puuted = pg.sprite.groupcollide(asteroidid, kuulid, True, True, pg.sprite.collide_circle)
    # Iga puude
    for puude in puuted:
        # Lisa skoorile 50 - maha lastud asteroidi raadius.
        skoor += 50 - puude.radius
        # Kui lastakse asteroid maha, siis tekitame uue ning
        a = Asteroid()
        koik_spraidid.add(a)
        asteroidid.add(a)
        # mängime heli plahvatuse helide listist.
        random.choice(plahvatus_SND).play()
    
    # Ütleme, et "puuted" on ühe spraidi ja ühe spraidi grupi kokkupuude (laev ja asteroidide grupp),
    # et kumbagi ei kustutataks ja et kokkupuute tüüp on "cicle". Selle jaoks oli vaja classide raadiuseid.
    puuted = pg.sprite.spritecollide(laev, asteroidid, False, pg.sprite.collide_circle)
    # Kui on puude, siis
    if puuted:
        # Lõpetame põhitsükkel
        jookseb = False
        

    # Joonista/Kuva monitoril
    
    # "Joonistame" Tauseta.
    screen.blit(Taust, Taust_rect)
    # "Joonistame" kõik spraidid.
    koik_spraidid.draw(screen)
    # Kasutame funktsiooni "prindi_tekst", et "joonistada" muutuja "skoor",
    # fondi suurusega 25, ekraani üles keskele.
    prindi_tekst(screen, str(skoor), 25, WIDTH / 2, 12)
    
    # Pärast kõige "joonistamist" näita monitoril
    pg.display.flip()
    
# Väljume pygame'ist.
pg.quit()
