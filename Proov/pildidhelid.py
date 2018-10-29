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
