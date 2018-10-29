# Asteroids laadne mäng
# Janek - Asteroidid; Rihard - Laev ja kuulid; Mihkel - Helid(Tehtud kasutades bfxr.net, Muusika - opengameart.org),
# Pildid, Skoor, Põhitsükkel, Kommentaarid.
# 2018

# Impordime vajalikud asjad
import pygame as pg, random, time, Laev, Kuul, Asteroid, pildidhelid

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
