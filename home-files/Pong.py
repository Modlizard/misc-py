import pygame
from pygame.locals import *
from sys import exit #We use sys.exit to prevent the program from hanging and leaving windows behind.
import random

SCREEN_WIDTH = 600 #Constants
SCREEN_HEIGHT = 500
BLACK = (0,0,0)
GREEN = (72,158,51)
WHITE = (255,255,255)

class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Century Gothic', 100)
        self.update()

    def update(self):
        if self.score < 10:
            scoreText = '0'+str(self.score)
        else:
            scoreText = str(self.score)
        self.blitText = self.font.render(scoreText, True, WHITE) #Render creates a surface with the score on it
        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #Manually running the init of pygame.sprite.Sprite

        self.image = pygame.Surface((8,8)) #Making the surface
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE) #Making it white but transparent

        pygame.draw.rect(self.image, GREEN, [0,0,8,8]) #All my favourite balls are rectangular
        self.rect = self.image.get_rect()

        self._restart() #Runs initial ball placement function
        
    def _restart(self):
        self.rect.x = 296 #Starts in the middle of the screen (ball is 8x8 and these are the coordinates of the top left of it)
        self.rect.y = 236
        
        self.velocityX = random.choice([random.randint(4,8),random.randint(-8,-4)]) #Random initial velocity, to the right/to the left respectively
        self.velocityY = random.randint(-8,8)
    
    def update(self):
        if self.rect.x >= 592: #If it touches the left side of the screen add one to the score of the other player
            theGame.scoreL.score += 1
            theGame.scoreL.update() #Redraws surface with score on it
            self._restart() #Resets the ball to the centre of the screen with a random velocity
        elif self.rect.x <= 0: #We reference the top left corner of the ball so bouncing off the top and left wall don't need toaccount for ball size.
            theGame.scoreR.score += 1
            theGame.scoreR.update()
            self._restart()
        else:
            pass
        
        if self.rect.y >= 492 or self.rect.y <= 0: #Bouncing off the top and bottom of the screen
            self.velocityY = -self.velocityY
        else:
            pass
        
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY
        
    def _batBounce(self):
        self.velocityX = -self.velocityX

        #self.velocityY = random.randint(-8,8) #Use this instead for sudden changes
        self.velocityY = random.randint(self.velocityY-3,self.velocityY+3) #Bounces are more gradual rather than sudden direction changes
        if self.velocityY < -8: #Capping vertical velocity between -8 and 8
            self.velocityY = -8
        elif self.velocityY > 8:
            self.velocityY = 8
        else:
            pass
    
class Bat(pygame.sprite.Sprite):
    def __init__(self,upKey, downKey, bat_x):
        super().__init__() #Manually running the init of pygame.sprite.Sprite
        
        self.image = pygame.Surface((8, 64))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        pygame.draw.rect(self.image,GREEN,[0,0,8,64])
        self.rect = self.image.get_rect()
        
        self.rect.x = bat_x
        self.rect.y = 150
        self.upKey = upKey
        self.downKey = downKey

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.upKey] and self.rect.y >= 5: #Moving up
            self.rect.y -= 5
        elif pressed[self.downKey] and self.rect.y <= 435: #Moving down
            self.rect.y += 5
        else:
            pass
        
class Game():
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Le Pong")
        self.__clock = pygame.time.Clock()
        
        #Instantiate screen components
        self.scoreL = Score()
        self.scoreR = Score()
        
        self.batR = Bat(K_UP,K_DOWN, 575)
        self.batL = Bat(K_w,K_s, 15)
        self.ball = Ball()

        #Group all sprites
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.batR)
        self.sprites.add(self.batL)
        self.sprites.add(self.ball)
        
    def update(self, running):
        #Updating sprite positions
        self.batL.move()
        self.batR.move()
        self.ball.update()

        if pygame.sprite.collide_mask(self.ball, self.batL) or pygame.sprite.collide_mask(self.ball, self.batR):
            self.ball._batBounce()
        else:
            pass
        
        #Redrawing all sprites
        self.__screen.fill(BLACK) #Clear screen

        self.__screen.blit(self.scoreL.blitText,(150,20)) #Scores
        self.__screen.blit(self.scoreR.blitText,(340,20))
        
        for x in range(-5,500,40): #Inclusive: from -5 to 475; step 40
            pygame.draw.line(self.__screen,WHITE,[300,x],[300,x+30],5) #Drawing dotted line in the middle
            
        self.sprites.draw(self.__screen) #Drawing all the sprites (paddles & ball)
        pygame.display.flip() #Update display

        #Clock
        self.__clock.tick(30)

        return running

#Code for running everything
theGame = Game()

running = True
while running:

    running = theGame.update(running)

    if running:
        # check if user clicked close window etc
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                print("Bye")
                running = False
