import pygame
import variables
import sys
from pygame.locals import *

import Grounds
import Spikes
from Player import Cube


def main():
    pygame.init()
    pygame.display.set_caption(variables.title)
    screen = pygame.display.set_mode((variables.screenWidth, variables.screenHeight), pygame.NOFRAME)
    fondo = pygame.image.load('img/bg/bg.jpg')
    fondo = pygame.transform.scale(fondo, (1280, 720))
    player = pygame.image.load('img/player/player.png')
    player = pygame.transform.scale(player, (50, 50))

    cube = Cube()

    cube.playerHeight = player.get_width()
    cube.position_y = cube.startposition_y
    cube.position_x = cube.startposition_x
    clock = pygame.time.Clock()

    miniGrounds = Grounds.getGrounds()
    spikes = Spikes.getSpikes()

    pygame.font.init();
    myFont = pygame.font.SysFont('Comic Sans MS', 30)

    while True:
        if variables.levelUp and variables.screenPosition > 0:
            levelUp()

        # instantiate
        dt = variables.gameSpeed/clock.tick(60)
        screen.blit(fondo, (0, 0))
        player_rect = screen.blit(player, (cube.position_x, cube.position_y))
        deathpit_rect = generateDeathPit(screen)
        for i in range(0, len(miniGrounds)):
            miniGrounds[i].rect = Grounds.generateGround(miniGrounds[i], screen)
        for i in range(0, len(spikes)):
            spike: Spikes.Spike = spikes[i]
            spike.rect = screen.blit(spike.surface, (spike.position_x, spike.position_y - spike.surface.get_height()))

        textsurface = myFont.render('Score: ' + str(int(variables.score)), False, (255, 255, 255))
        screen.blit(textsurface,(0,0))

        # Key imputs
        if not cube.jumping:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[K_w]:
                cube.jumping = cube.startJumping()

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        # apply gravity
        cube.applyGravity(dt)

        # delete grounds and move
        removeList = list()
        for i in range(0, len(miniGrounds)):
            if not miniGrounds[i].move(-dt):
                removeList.append(miniGrounds[i])
        for minig in removeList:
            miniGrounds.remove(minig)

        removeSpike = list()
        for i in range(0, len(spikes)):
            if not spikes[i].move(-dt):
                removeSpike.append(spikes[i])
        for spi in removeSpike:
            spikes.remove(spi)

        # move world
        variables.screenPosition += dt * (variables.gameSpeed * variables.screenSpeed)
        variables.score += dt * variables.gameSpeed * variables.level / 5

        # check collision
        for mg in miniGrounds:
            miniGround_rect = mg.rect
            if player_rect.colliderect(miniGround_rect) and cube.jumpSpeed > 0:
                cube.jumping = not cube.stopJumping(miniGround_rect, player_rect)

        for s in spikes:
            if player_rect.colliderect(s.rect):
                return

        # check death
        if player_rect.colliderect(deathpit_rect):
            return

        # controll jumpstate
        cube.jumping = cube.jumpSpeed != 0

        # generate grounds
        for ground in Grounds.getGrounds():
            if ground not in miniGrounds:
                miniGrounds.append(ground)

        for spike in Spikes.getSpikes():
            if spike not in spikes:
                spikes.append(spike)

        # update
        pygame.display.update()


def generateDeathPit(screen: pygame.Surface):
    return pygame.draw.rect(surface=screen,
                            color=(0, 0, 0),
                            rect=(0,
                                  variables.screenHeight - 30,
                                  variables.screenWidth,
                                  variables.screenWidth))

def gameStartUp():
    variables.screenPosition = 0
    variables.score = 0
    variables.gameSpeed = 1
    variables.generatedGrounds.clear()
    variables.levelUp = False
    variables.levelSpikes.clear()
    variables.level = 1
    variables.spikeNumber = 0

def levelUp():
    variables.level += 1
    variables.gameSpeed += 0.05
    variables.levelUp = False

if __name__ == '__main__':
    while True:
        main()
        gameStartUp()
