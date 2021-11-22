import variables
from pygame.locals import *


class Cube:
    def __init__(self):
        self.jumping = False
        self.playerHeight = 0
        self.startposition_x = 150
        self.startposition_y = 550
        self.position_x = 0
        self.position_y = 0
        self.jumpSpeed = 0
        self.jumpForce = 15

    def startJumping(self):
        self.jumpSpeed = -self.jumpForce
        return True

    def applyGravity(self, deltaTime):
        speed = variables.gravity * float(deltaTime)
        self.position_y += self.jumpSpeed * speed
        self.jumpSpeed += speed

    def stopJumping(self, rect: Rect, playerRect: Rect):
        if rect.midtop[1] >= playerRect.midbottom[1] - 30:
            self.position_y = rect.y - 49
            self.jumpSpeed = 0
            return True
        return False
