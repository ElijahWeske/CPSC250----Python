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
#
VERSION = "0.4"

import struct
import math
import os
import pygame
import random

global block_num
block_num = 35


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


def make_blocks():
    # The top of the block (y position)
    top = 50
    # Number of blocks to create
    block_count = 35
    for row in range(5):
        for column in range(block_count):
            # Create a block (color,x,y)
            if row == 4:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 3:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 2:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 1:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 0:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
        # Move the top of the next row down
        top += 10 + 35


def make_blocks_bonus():
    # The top of the block (y position)
    top = 50
    # Number of blocks to create
    block_count = 35
    for row in range(5):
        for column in range(block_count):
            # Create a block (color,x,y)
            if row == 4:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 3:
                block = Block((255, 255, 255), (column * 90) + 20, top)
                block.bonus = True
                blocks.add(block)
            if row == 2:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 1:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
            if row == 0:
                block = Block((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (column * 90) + 20, top)
                blocks.add(block)
        # Move the top of the next row down
        top += 10 + 35


class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame"""
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position."""
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('basic_block.png')
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 60
        self.rect.height = 15
        self.block_health = 300
        self.color = color

        self.destroyed = False
        self.bonus = False

        self.x = x
        self.y = y

    def update(self):
        if self.rect.colliderect(ball.rect) and self.block_health > 0:
            center = self.rect.center
            self.image = pygame.transform.scale(self.image, (65, 20))
            self.rect = self.image.get_rect()
            self.rect.center = center
            effect = pygame.mixer.Sound('hit1.wav')
            effect.play()
            self.block_health -= 100
            player.score += 1

        if self.block_health == 200:
            self.image.fill([0, 0, 205])

        if self.block_health == 100:
            self.image.fill([255, 0, 0])

        if self.block_health == 0 and not self.destroyed and self.bonus:
            player.lives += 1
            effect = pygame.mixer.Sound('blockexplode1.wav')
            effect.play()
            blocks.remove(self)
            self.image.fill([0, 0, 0])
            global block_num
            block_num -= 1
            print("Health Block Destroyed! +1 Life! Blocks Remaining: {}".format(block_num))
            self.destroyed = True

        if self.block_health == 0 and not self.destroyed and not self.bonus:
            effect = pygame.mixer.Sound('blockexplode1.wav')
            effect.play()
            blocks.remove(self)
            self.image.fill([0, 0, 0])
            block_num -= 1
            print("Block Destroyed! Blocks Remaining: {}".format(block_num))
            self.destroyed = True


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
                effect = pygame.mixer.Sound('hitpaddle.wav')
                effect.play()
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

    def __init__(self, score, lives, level, paddle_x, paddle_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('paddle.png')
        self.image.fill([177, 212, 116])
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 10
        self.state = "still"
        self.reinit()

        self.score = score
        self.lives = lives
        self.level = level
        self.paddle_x = paddle_x
        self.paddle_y = paddle_y

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
    global screen_height
    global screen_width
    global background

    global pause
    global game_over
    global difficulty
    difficulty = 1

    # Create screen dimensions
    screen_width = 640
    screen_height = 480

    # Initialize pygame, create screen
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakout by Elijah and Elijah v' + str(VERSION))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Set states of game
    pause = False
    game_over = False
    new_game = True

    # Initialize players
    global player
    global ball
    global blocks
    global block_count
    global block_num

    # Initialize block
    blocks = pygame.sprite.Group()

    # Check to see if any saved data exists; if there is saved data, set the new game state to false
    if os.path.getsize('save_data.dat') > 0:
        new_game = False

    # If this is not a new game, unpack saved data
    if not new_game:
        # Unpack saved data for player and ball attributes
        binary_save = []
        with open('save_data.dat', 'rb') as bin:
            ba = bytearray(bin.read())
        chunk_size = struct.calcsize('>fiiiiiii')
        for i in range(len(ba) // chunk_size):
            chunk = ba[i * chunk_size: (i + 1) * chunk_size]
            item = struct.unpack('>fiiiiiii', chunk)
            binary_save.append(item)

        print("Unpacking saved data for player and ball data: ", binary_save)

        angle = binary_save[0][0]
        speed = binary_save[0][1]
        lives = binary_save[0][2]
        level = binary_save[0][3]
        score = binary_save[0][4]
        paddle_x = binary_save[0][5]
        paddle_y = binary_save[0][6]
        block_num = binary_save[0][7]

        # Unpack saved data for block positions / coordinates
        binary_block = []
        with open('block_data.dat', 'rb') as bin:
            b_a = bytearray(bin.read())
        chunk_size = struct.calcsize('>ii')
        for i in range(len(b_a) // chunk_size):
            chunk = b_a[i * chunk_size: (i + 1) * chunk_size]
            item = struct.unpack('>ii', chunk)
            binary_block.append(item)

        print("Unpacking saved x and y coordinates: ", binary_block)

        # Unpack saved data for block colors
        block_colors = []
        with open('block_data_2.dat', 'rb') as bin:
            b_a = bytearray(bin.read())
        chunk_size = struct.calcsize('>iii')
        for i in range(len(b_a) // chunk_size):
            chunk = b_a[i * chunk_size: (i + 1) * chunk_size]
            item = struct.unpack('>iii', chunk)
            block_colors.append(item)

        print("Unpacking saved block colors: ", block_colors)

        for i in range(len(block_colors)):
            temp_color = [0, 0, 0]
            for j in range(3):
                temp_color[j] = block_colors[i][j]
            block = Block((tuple(temp_color)), binary_block[i][0], binary_block[i][1])
            if tuple(temp_color) == (255, 255, 255):
                block.bonus = True
            if tuple(temp_color) == (0, 0, 255):
                block.block_health = 200
            if tuple(temp_color) == (255, 0, 0):
                block.block_health = 100
            blocks.add(block)

        print("List of blocks: ", blocks)

    else:
        angle = 1.1
        speed = 10
        lives = 3
        level = 1
        score = 0
        paddle_x = 0
        paddle_y = 0
        block_num = 35

        # Create a new arrangement of blocks
        # The top of the block (y position)
        top = 50
        # Number of blocks to create
        block_count = 7
        # Five rows of blocks
        for row in range(5):
            for column in range(block_count):
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

    player = Paddle(score, lives, level, paddle_x, paddle_y)
    ball = Ball((angle, speed))

    # Initialize sprites
    global playersprite
    global ballsprite
    global blocksprites

    playersprite = pygame.sprite.RenderPlain(player)
    ballsprite = pygame.sprite.RenderPlain(ball)
    blocksprites = pygame.sprite.RenderPlain(blocks)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        if player.lives <= 0:
            screen.fill((0, 0, 0))

            font = pygame.font.SysFont('OCR A EXTENDED', 40)
            text = font.render("GAME OVER", False, (255, 255, 255))
            textpos = text.get_rect(centerx=(background.get_width() / 2))
            textpos.top = 200
            screen.blit(text, textpos)
            pygame.display.flip()

            game_over = True

        if block_num == 0:
            effect = pygame.mixer.Sound('new_level_sound.wav')
            effect.play()

            player.level += 1
            num = random.randint(1, 2)
            if num == 1:
                make_blocks()
            else:
                make_blocks_bonus()

            block_num = 35
            blocksprites = pygame.sprite.RenderPlain(blocks)
            pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) + 5, 10, 50, 40), 100)
            text = font.render("level: {}".format(player.level), False, (255, 255, 255))
            textpos = text.get_rect(centerx=(background.get_width() / 2) + 5)
            textpos.top = 10
            screen.blit(text, textpos)

        # Checks key input to move the paddle
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Store data of block positions in binary
                    blocks_x = []
                    blocks_y = []
                    for item in blocks:
                        blocks_x.append(item.x)
                        blocks_y.append(item.y)
                    byte_array = bytearray()
                    for i in range(len(blocks_x)):
                        byte_array.extend(struct.pack('>ii', blocks_x[i], blocks_y[i]))
                    with open("block_data.dat", "wb") as bin_out:
                        bin_out.write(byte_array)

                    print("Saved X coordinates of blocks: ", blocks_x)
                    print("Saved Y coordinates of blocks: ", blocks_y)

                    # Store data of ball angle and speed, player lives, level, and x and y coordinates of paddle
                    ba = bytearray()
                    ba.extend(struct.pack('>fiiiiiii', angle, speed, player.lives, player.level, player.score,
                                    player.paddle_x, player.paddle_y, block_num))
                    with open("save_data.dat", "wb") as bin_out:
                        bin_out.write(ba)

                    # Store data of block colors in binary
                    block_colors = []
                    for item in blocks:
                        block_colors.append(item.color)
                    byte_array = bytearray()
                    for i in range(len(blocks_x)):
                        byte_array.extend(struct.pack('>iii', block_colors[i][0], block_colors[i][1], block_colors[i][2]))
                    with open("block_data_2.dat", "wb") as bin_out:
                        bin_out.write(byte_array)

                    print("BLOCK COLORSSSSSSSSSSSSSSSSSS: ", block_colors)

                    # Ends the run game loop
                    return False

                if event.key == pygame.K_SPACE:
                    if not pause and not game_over:
                        effect = pygame.mixer.Sound('pause_sound.wav')
                        effect.play()
                        font = pygame.font.SysFont('OCR A EXTENDED', 40)
                        text = font.render("Paused", False, (255, 255, 255))
                        textpos = text.get_rect(centerx=(background.get_width() / 2))
                        textpos.top = 300
                        screen.blit(text, textpos)
                        pygame.display.flip()
                        pause = True

                    elif pause:
                        pygame.draw.rect(screen, (0, 0, 0), (((background.get_width() / 2) - 260), 300,
                                                             1000, 1000), 100)
                        pause = False

                    if game_over:
                        print("GAME OVERRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                        f = open("save_data.dat", "w")
                        f.close()
                        main()

                if event.key == pygame.K_LEFT:
                    player.moveleft()

                if event.key == pygame.K_RIGHT:
                    player.moveright()

                if event.key == pygame.K_1:
                    if pause:
                        difficulty = 1

                if event.key == pygame.K_2:
                    if pause:
                        difficulty = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.still()

        if not pause and not game_over:
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

            pygame.draw.rect(screen, (0, 0, 0), ((background.get_width() / 2) + 5, 10, 50, 40), 100)
            text = font.render("level: {}".format(player.level), False, (255, 255, 255))
            textpos = text.get_rect(centerx=(background.get_width() / 2) + 5)
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
