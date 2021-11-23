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


def getSpikes():
    spikes = list()
    for spi in variables.levelSpikes:
        if variables.screenPosition <= spi.startPosx <= variables.screenPosition + variables.screenWidth:
            spikes.append(spi)
            spi.position_x = spi.startPosx - variables.screenPosition
            variables.generatedSpikes.append(spi)

    if len(variables.levelSpikes) == len(variables.generatedSpikes) != 0and \
            variables.generatedSpikes[len(variables.generatedSpikes)-1].position_x <= 0:

        variables.generatedSpikes.clear()

    return spikes

def addSpikeToLevel(amount: int):
    variables.levelSpikes.clear()
    for i in range(0, amount):
        if len(variables.allSpikes) > i:
            s: Spike = variables.allSpikes[i]
            variables.levelSpikes.append(s)

