import pygame

from Grounds import MiniGround, GroundSize
from Spikes import Spike

title = "El mejor de los juegos!"

gravity = 15
gameSpeed = 1

screenSpeed = 100

screenPosition = 0
score = 0

screenWidth = 1280
screenHeight = 720

levelUp = False
level = 1
spikeNumber: int = 0

#grounds

allGrounds = list((
        MiniGround(x=0, y=620, width=1100, height=100),
        MiniGround(x=1250, y=500, width=350, height=50),
        MiniGround(x=1750, y=400, size=GroundSize.BIG_RECT),
        MiniGround(x=2150, y=600, width=200, height=50),
        MiniGround(x=2500, y=500, width=300, height=50),
        MiniGround(x=3000, y=500, width=50, height=50),
        MiniGround(x=3200, y=500, width=50, height=50),
        MiniGround(x=3400, y=500, width=50, height=50),
        MiniGround(x=3500, y=550, width=50, height=50),
        MiniGround(x=3600, y=600, width=50, height=50),
        MiniGround(x=3750, y=500, width=50, height=50),
        MiniGround(x=3900, y=400, width=50, height=50),
        MiniGround(x=4050, y=450, width=50, height=50),
        MiniGround(x=4250, y=400, width=50, height=50),
        MiniGround(x=4390, y=400, width=50, height=50)
    ))

generatedGrounds = list()

lastGround: MiniGround

# spikes

spike_img = pygame.image.load("img/bg/spike.png")
spike = pygame.transform.scale(spike_img, (50, 50))

allSpikes = list((
        Spike(x=2600, y=500, surface=spike),
        Spike(x=300, y=620, surface=spike),
        Spike(x=1350, y=500, surface=spike),
        Spike(x=4390, y=400, surface=spike),
        Spike(x=1850, y=400, surface=spike)
    ))
levelSpikes = list()

generatedSpikes = list()
