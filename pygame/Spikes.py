from pygame.locals import *

import variables
import pygame


class Spike:

    def __init__(self, x, y, surface: pygame.Surface):
        self.startPosx = x
        self.position_x = x
        self.position_y = y
        self.surface = surface
        self.rect: Rect = surface.get_rect()
        self.width = surface.get_width()

    def move(self, deltatime):
        self.position_x += deltatime * (variables.gameSpeed * variables.screenSpeed)
        if self.position_x <= -self.width:
            return False
        return True

spike_img = pygame.image.load("img/bg/spike.png")
spike = pygame.transform.scale(spike_img, (50, 50))

allSpikes = list((
        #  Spike(x=300, y=620, surface=spike),
        Spike(x=1350, y=500, surface=spike),
        Spike(x=1850, y=400, surface=spike),
        Spike(x=2600, y=500, surface=spike),
        Spike(x=4390, y=350, surface=spike)
        # Spike(x=3300, y=620, surface=spike)
    ))

levelSpikes = list()

generatedSpikes = list()


def getSpikes():
    spikes = list()
    for spi in allSpikes:
        if spi.startPosx >= variables.screenPosition:
            if spi.startPosx <= variables.screenPosition + variables.screenWidth:
                spikes.append(spi)
                spi.position_x = spi.startPosx
            else:
                break
    for spi in spikes:
        spi.position_x -= variables.screenPosition
        allSpikes.remove(spi)
        generatedSpikes.append(spi)

    if len(allSpikes) == 0 and len(generatedSpikes) != 0 and generatedSpikes[len(generatedSpikes)-1].position_x <= 0:  # next levels
        for ground in generatedSpikes:
            allSpikes.append(ground)
        generatedSpikes.clear()
    return spikes

def addSpikeToLevel():
    if len(allSpikes) > 0:
        s: Spike = allSpikes[0]
        levelSpikes.append(s)
        allSpikes.remove(s)

