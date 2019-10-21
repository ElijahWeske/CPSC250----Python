#
# Tom's Pong
# A simple pong game with realistic physics and AI
# http://www.tomchance.uklinux.net/projects/pong.shtml
#
# Released under the GNU General Public License
#
##############################################################
#
# Modified for educational purposes for the
# CNU Department of Physics, Computer Science and Engineering
#
# Spring 2019 Semester
# Mathew Bartgis, David Conner
#

VERSION = "0.4"

import time
import math
import os
import pygame


def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('../img', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image
    except pygame.error:
        print('Cannot load image:', fullname)


def calcnewpos(rect, vector):
    (angle, z) = vector
    (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
    return rect.move(dx, dy)


class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame """

    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
            and its x and y position. """
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('basic_block.png')
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 60
        self.rect.height = 15
        self.__block_health = 300

    def update(self):
        if self.rect.colliderect(ball.rect):
            self.__block_health -= 100
            player.score += 1

        if self.__block_health == 200:
            self.image.fill([0, 0, 205])

        if self.__block_health == 100:
            self.image.fill([255, 0, 0])

        if self.__block_health == 0:
            blocks.remove(self)
            # blocks.update()
            self.image.fill([0, 0, 0])


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)

        self.image = load_png('ball.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.rect.center = [screen_width / 2, (screen_height * .75)]
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
        self.initpos = [screen_width / 2, -(screen_height / 4)]

        self.ball_x = 0
        self.ball_y = 0

    def update(self):
        newpos = calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        self.ball_x = ball.rect[0]
        self.ball_y = ball.rect[1]

        if self.ball_y >= 470:
            angle = angle
            player.lives -= 1
            pygame.time.delay(1000)
            self.rect.center = [screen_width / 2, (screen_height * .75)]

        elif not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if (tr and tl) or (br and bl):
                angle = -angle
            if (tl and bl) or (tr and br):
                angle = math.pi - angle

        else:
            # Deflate the rectangles so you can't catch a ball behind the bat
            player.rect.inflate(3, 3)

            if self.rect.colliderect(player.rect) and not self.hit:
                angle = -angle
                self.hit = not self.hit
            elif self.rect.collidelist(blocks.sprites()) != -1 and not self.hit:
                angle = -angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle, z)


class Paddle(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    X = 0
    Y = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('paddle.png')
        self.image.fill([177, 212, 116])
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 10
        self.state = "still"
        self.reinit()

        self.score = 0
        self.lives = 3

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        self.rect.midbottom = self.area.midbottom

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveleft(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] - self.speed
        self.state = "moveleft"

    def moveright(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] + self.speed
        self.state = "moveright"

    def still(self):
        self.movepos = [0, 0]
        self.state = "still"


def main():
    # Initialize screen

    global screen_height
    global screen_width
    global background

    screen_width = 640
    screen_height = 480

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakout by Elijah and Elijah v' + str(VERSION))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialize players
    global player
    global ball
    global blocks

    # keeps track of the number of blocks
    global blockcount

    player = Paddle()

    # Initialize ball
    speed = 10
    ball = Ball((1.1, speed))

    # Initialize block
    blocks = pygame.sprite.Group()
    # The top of the block (y position)
    top = 50
    # Number of blocks to create
    blockcount = 35
    # --- Create blocks
    # Five rows of blocks
    for row in range(5):
        # 20 columns of blocks
        for column in range(blockcount):
            # Create a block (color,x,y)
            if row == 4:
                block = Block((255, 0, 0), (column * 90) + 20, top)
                blocks.add(block)
            if row == 3:
                block = Block((255, 255, 0), (column * 90) + 20, top)
                blocks.add(block)
            if row == 2:
                block = Block((19, 139, 97), (column * 90) + 20, top)
                blocks.add(block)
            if row == 1:
                block = Block((255, 201, 56), (column * 90) + 20, top)
                blocks.add(block)
            if row == 0:
                block = Block((100, 149, 237), (column * 90) + 20, top)
                blocks.add(block)
        # Move the top of the next row down
        top += 10 + 35

    # Initialize sprites

    global playersprite
    global ballsprite
    global blocksprites

    global pausestate
    global gameover
    playersprite = pygame.sprite.RenderPlain(player)
    ballsprite = pygame.sprite.RenderPlain(ball)
    blocksprites = pygame.sprite.RenderPlain(blocks)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    #create the font
    font = pygame.font.SysFont('OCR A EXTENDED', 23)

    pausestate = False
    gameover = False

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        if player.lives <= 0:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('OCR A EXTENDED', 40)
            text = font.render("GAME OVER", False, (255, 255, 255))
            textpos = text.get_rect(centerx=(background.get_width() / 2))
            textpos.top = 300
            screen.blit(text, textpos)
            pygame.display.flip()
            gameover = True

        # Checks key input to move the paddle
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not pausestate:
                        font = pygame.font.SysFont('OCR A EXTENDED', 40)
                        text = font.render("Paused", False, (255, 255, 255))
                        textpos = text.get_rect(centerx=(background.get_width() / 2))
                        textpos.top = 300
                        screen.blit(text, textpos)
                        pygame.display.flip()
                        pausestate = True
                    elif pausestate:
                        pygame.draw.rect(screen, (0, 0, 0), (((background.get_width() / 2) - 260), 300,
                                         1000, 1000), 100)
                        pausestate = False
                    if gameover:
                        main()
                if event.key == pygame.K_LEFT:
                    player.moveleft()
                if event.key == pygame.K_RIGHT:
                    player.moveright()
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.still()

        if not pausestate and not gameover:
            # Font for scores and lives
            font = pygame.font.SysFont('OCR A EXTENDED', 23)

            screen.blit(background, ball.rect, ball.rect)
            screen.blit(background, player.rect, player.rect)

            pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) + 230, 10, 50, 40), 100)
            pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) + 245, 10, 80, 50), 100)
            pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) + 260, 10, 100, 50), 100)
            text = font.render("lives: {}".format(player.lives), False, (255, 255, 255))
            textpos = text.get_rect(centerx=(background.get_width() / 2) + 245)
            textpos.top = 10
            screen.blit(text, textpos)

            if player.score > 99:
                pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) - 265, 10, 80, 50), 100)
                pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) - 260, 10, 100, 50), 100)
                text = font.render("score: {}".format(player.score), False, (255, 255, 255))
                textpos = text.get_rect(centerx=(background.get_width() / 2) - 240)
                textpos.top = 10
                screen.blit(text, textpos)

            else:
                pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) - 265, 10, 80, 50), 100)
                text = font.render("score: {}".format(player.score), False, (255, 255, 255))
                textpos = text.get_rect(centerx=(background.get_width() / 2) - 250)
                textpos.top = 10
                screen.blit(text, textpos)

            ballsprite.update()
            playersprite.update()
            blocksprites.update()
            playersprite.draw(screen)
            blocksprites.draw(screen)
            ballsprite.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    main()