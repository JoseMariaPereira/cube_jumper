from pygame.locals import *

import Spikes
import variables
import pygame


class MiniGround:

    def __init__(self, x, y, width, height):
        self.startPosx = x
        self.position_x = x
        self.position_y = y
        self.startRect = Rect(x, y, width, height)
        self.rect: Rect = self.startRect
        self.width = width

    def move(self, deltaTime):
        self.position_x += deltaTime * (variables.gameSpeed + 50)
        if self.position_x <= -self.width:
            return False
        return True

allGrounds = list((
        MiniGround(x=0, y=620, width=1100, height=100),
        MiniGround(x=1250, y=500, width=350, height=50),
        MiniGround(x=1750, y=400, width=300, height=50),
        MiniGround(x=2150, y=600, width=200, height=50),
        MiniGround(x=2500, y=500, width=300, height=50),
        MiniGround(x=3000, y=500, width=50, height=50),
        MiniGround(x=3200, y=500, width=50, height=50),
        MiniGround(x=3400, y=500, width=50, height=50),
        MiniGround(x=3500, y=550, width=50, height=50),
        MiniGround(x=3600, y=600, width=50, height=50),
        MiniGround(x=3750, y=450, width=50, height=50),
        MiniGround(x=3900, y=300, width=50, height=50),
        MiniGround(x=4050, y=450, width=50, height=50),
        MiniGround(x=4250, y=400, width=50, height=50),
        MiniGround(x=4390, y=350, width=50, height=50)
    ))

generatedGrounds = list()

lastGround: MiniGround


def getGrounds():
    grounds = list()
    for ground in allGrounds:
        if ground.startPosx >= variables.screenPosition:
            if ground.startPosx <= variables.screenPosition + variables.screenWidth:
                grounds.append(ground)
                ground.position_x = ground.startPosx
            else:
                break
    for ground in grounds:
        ground.position_x -= variables.screenPosition
        allGrounds.remove(ground)
        generatedGrounds.append(ground)

    if len(allGrounds) == 0 and generatedGrounds[len(generatedGrounds)-1].position_x <= variables.screenWidth - generatedGrounds[len(generatedGrounds)-1].width:  # next levels
        for ground in generatedGrounds:
            allGrounds.append(ground)

        variables.screenPosition = -(variables.screenWidth + 100)
        variables.levelUp = True

        generatedGrounds.clear()
    return grounds


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
