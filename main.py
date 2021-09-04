import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
body_img = pygame.image.load("snake_game/snake_body.png")
playerX = 0
playerY = 0
body_positions = []
body_nums = 0
changeX = 0
changeY = 0
apples_eaten = 0

apple_img = pygame.image.load("snake_game/apple.png")


class Player:
    def __init__(self, x, y):
        global body_nums
        screen.blit(body_img, (x, y))
        body_nums += 1

    @staticmethod
    def display():
        global playerX
        global playerY
        screen.blit(body_img, (playerX, playerY))

    @staticmethod
    def movement():
        global playerX
        global playerY
        global body_positions
        if playerX < 0:
            playerX = 781
        if playerX > 781:
            playerX = 1
        if playerY < 0:
            playerY = 781
        if playerY > 781:
            playerY = 1
        if body_nums > (len(body_positions)):
            body_positions.append((playerX, playerY))
        else:
            body_positions.pop(0)
            body_positions.append((playerX, playerY))
        playerX += changeX
        playerY += changeY
        time.sleep(0.1)


class Apple:
    def __init__(self):
        self.chord = random_chords()

    def eat_apple(self):
        global apples_eaten, body_nums
        if body_positions[-1] == self.chord:
            apples_eaten += 1
            self.chord = random_chords()
            body_nums += 1
            return True

    def display(self):
        screen.blit(apple_img, self.chord)


def random_chords():
    global playerX, playerY, random_spawns
    random_spawns = []
    for x in range(800):
        for y in range(800):
            if x % 20 == 0 and y % 20 == 0:
                random_spawns.append((x + 1, y + 1))
    return random.choice(random_spawns)


apple = Apple()
(X := random_chords())
(Y := random_chords())
playerX = X[0]
playerY = Y[1]
body_start = Player(playerX, playerY)


def main():
    global changeY, changeX, playerX, playerY
    running = True
    movement = False
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX = -20
                    changeY = 0
                elif event.key == pygame.K_RIGHT:
                    changeX = 20
                    changeY = 0
                elif event.key == pygame.K_UP:
                    changeY = -20
                    changeX = 0
                elif event.key == pygame.K_DOWN:
                    changeY = 20
                    changeX = 0
                movement = True
        apple.display()
        body_start.display()
        if movement:
            body_start.movement()
            apple.eat_apple()
            if (playerX, playerY) in body_positions:
                running = False
            for i in range(apples_eaten + 1):
                screen.blit(body_img, (body_positions[-i]))

        pygame.display.update()


main()
