import pygame, sys, random

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption('Pygame Pong')

windowSize = (1280, 720)

screen = pygame.display.set_mode(windowSize)

playerPaddle = pygame.Rect(110, windowSize[1]/2 - 50, 10, 100)
opponentPaddle = pygame.Rect(windowSize[0] - 110, windowSize[1]/2 - 50, 10, 100)
playerScore, opponentScore = 0, 0

font = pygame.font.SysFont("Consolas", int(windowSize[0]/20))

ball = pygame.Rect(windowSize[0] / 2, windowSize[1] / 2, 20, 20)
speedX, speedY = 1, 1

def resetBall():
    ball.center = (windowSize[0] / 2, windowSize[1] / 2)
    speedX, speedY = random.choice([1, -1]), random.choice([1, -1])

while True: # game loop

    screen.fill((0, 0, 0))

    keyPressed = pygame.key.get_pressed()

    ball.x += speedX * 8
    ball.y += speedY * 8

    pygame.draw.rect(screen, "white", playerPaddle)
    pygame.draw.rect(screen, "white", opponentPaddle)
    pygame.draw.circle(screen, "white", ball.center, 10)

    playerScoreText = font.render(str(playerScore), True, "white")
    opponentScoreText = font.render(str(opponentScore), True, "white")

    screen.blit(playerScoreText, (windowSize[0] / 2 + 50, 50))
    screen.blit(opponentScoreText, (windowSize[0] / 2 - 50, 50))

    if ball.y >= windowSize[1]:
        speedY = -1
    if ball.y <= 0:
        speedY = 1
    if ball.x <= 0:
        opponentScore += 1
        resetBall()
    if ball.x >= windowSize[0]:
        playerScore += 1
        resetBall()
    
    if pygame.Rect.colliderect(playerPaddle, ball):
        speedX = 1
    
    if pygame.Rect.colliderect(opponentPaddle, ball):
        speedX = -1

    if playerScore == 5 or opponentScore == 5:
        resetBall()
        speedX, speedY = 0, 0
        screen.fill((0, 0, 0))
        gameOverText = font.render("Game Over!", True, "white")
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = (windowSize[0] // 2, windowSize[1] // 2)
        screen.blit(gameOverText, gameOverRect)

    if keyPressed[pygame.K_UP]:
        if opponentPaddle.top > 0:
            opponentPaddle.top -= 10

    if keyPressed[pygame.K_DOWN]: 
        if opponentPaddle.bottom < windowSize[1]:
            opponentPaddle.bottom += 10
    
    if keyPressed[pygame.K_w]:
        if playerPaddle.top > 0:
            playerPaddle.top -= 10

    if keyPressed[pygame.K_s]: 
        if playerPaddle.bottom < windowSize[1]:
            playerPaddle.bottom += 10

    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
        
  