from pygame.locals import *
from enum import Enum

import Spikes
import variables
import pygame


class GroundSize(Enum):
    NONE = (0, 0)
    START_GROUND = (1280, 100)
    SMALL_RECT = (50, 20)
    SMALL_CUBE = (50, 50)
    MEDIUM_RECT = (200, 50)
    BIG_RECT = (300, 50)


class MiniGround:

    def __init__(self, x, y, width=0, height=0, size: GroundSize = GroundSize.NONE):
        self.startPosx = x
        self.position_x = x
        self.position_y = y
        w = width
        h = height
        if size != GroundSize.NONE:
            w = size.value[0]
            h = size.value[1]
        self.startRect = Rect(x, y, w, h)
        self.rect: Rect = self.startRect
        self.width = w

    def move(self, deltaTime):
        self.position_x += deltaTime * (variables.gameSpeed * variables.screenSpeed)
        if self.position_x <= -self.width:
            return False
        return True




def getGrounds():
    grounds = list()
    for ground in variables.allGrounds:
        if ground not in variables.generatedGrounds \
                and variables.screenPosition <= ground.startPosx <= variables.screenPosition + variables.screenWidth:

            grounds.append(ground)
            variables.generatedGrounds.append(ground)
            ground.position_x = ground.startPosx - variables.screenPosition
            variables.lastGround = ground

    if len(variables.allGrounds) == len(variables.generatedGrounds) and \
            variables.lastGround.position_x <= variables.screenWidth - variables.lastGround.width:  # next levels

        groundRestart()

    return grounds

def groundRestart():
    variables.screenPosition = -(variables.screenWidth + 100)
    variables.levelUp = True
    variables.generatedGrounds.clear()
    variables.spikeNumber += 1
    Spikes.addSpikeToLevel(variables.spikeNumber)

def generateGround(ground: MiniGround, screen: pygame.Surface):
    pygame.draw.rect(surface=screen,
                     color=(0, 0, 0),
                     rect=(ground.position_x,
                           ground.position_y,
                           ground.startRect.width,
                           ground.startRect.height),
                     width=0)
    return pygame.draw.rect(surface=screen,
                            color=(255, 255, 255),
                            rect=(ground.position_x,
                                  ground.position_y,
                                  ground.startRect.width,
                                  ground.startRect.height),
                            width=1)
