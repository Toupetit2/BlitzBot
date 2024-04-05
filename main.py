import pygame
import sys

from player import *

LARGUEUR, HAUTEUR = 900, 650
pygame.init()

screen = pygame.display.set_mode((LARGUEUR, HAUTEUR))
clock = pygame.time.Clock()
FPS = 60

# PLAYER
player = Player()


# MAP




while True:
    clock.tick(FPS)

    # AFFICHAGE TEMPORAIRE
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (i * 15 + 30, j * 15 + 30, 0),(i*65, j*65, 65, 65))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            player.move(event.key)
    
    pygame.display.update()