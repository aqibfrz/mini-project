import random
import pygame

from player import Player


class Ball:
    def __init__(self, xPosition: int, yPosition: int, speed: float, screen: pygame.Surface) -> None:
        self.x = xPosition  # self.x is the top left corner's x position of the image
        self.y = yPosition  # self.y is the top left corner's y position of the image
        self.speed = speed
        self.screen = screen
        self.image = pygame.image.load('ping-pong.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        list1 = [1, 2, 3]
        r1 = random.choice(list1)
        if r1 == 1:
            self.moveDirection = 'UP'
        elif r1 == 2:
            self.moveDirection = 'UP-LEFT'
        elif r1 == 3:
            self.moveDirection = 'UP-RIGHT'
        self.isMoving = False

    def moveLeft(self):
        self.x = self.x - self.speed
        # Detect collision with screen left
        if self.x < 0:
            self.x = 0
            if (self.moveDirection == 'UP-LEFT'):
                self.moveDirection = 'UP-RIGHT'
            elif (self.moveDirection == 'DOWN-LEFT'):
                self.moveDirection = 'DOWN-RIGHT'

    def moveRight(self):
        self.x = self.x + self.speed
        # Detect collision with screen right
        if self.x > (self.screen.get_width() - self.image.get_width()):
            self.x = self.screen.get_width() - self.image.get_width()
            if(self.moveDirection == 'UP-RIGHT'):
                self.moveDirection = 'UP-LEFT'
            elif (self.moveDirection == 'DOWN-RIGHT'):
                self.moveDirection = 'DOWN-LEFT'

    def moveUp(self):
        self.y = self.y - self.speed
        # Detect collision with screen up
        if self.y < 0:
            self.y = 0
            # Player 1 won
            self.moveDirection = 'DOWN'

    def moveDown(self):
        self.y = self.y + self.speed
        # Detect collision with screen down
        if self.y > (self.screen.get_height() - self.image.get_height()):
            # Player 2 won
            self.y = self.screen.get_height() - self.image.get_height()
            self.moveDirection = 'UP'

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def update(self, player1: Player, player2: Player):
        if self.isMoving:
            if self.moveDirection == 'UP':
                self.moveUp()
            elif self.moveDirection == 'DOWN':
                self.moveDown()
            elif self.moveDirection == 'UP-RIGHT':
                self.moveUp()
                self.moveRight()
            elif self.moveDirection == 'DOWN-RIGHT':
                self.moveDown()
                self.moveRight()
            elif self.moveDirection == 'UP-LEFT':
                self.moveUp()
                self.moveLeft()
            elif self.moveDirection == 'DOWN-LEFT':
                self.moveDown()
                self.moveLeft()
        else:
            self.x = player1.x + ((player1.image.get_width()/2) - (self.image.get_width()/2))
            self.y = player1.y
        
        self.draw()