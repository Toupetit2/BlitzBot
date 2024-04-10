import pygame
import sys

from player import *

LARGUEUR, HAUTEUR = 900, 650
pygame.init()

screen = pygame.display.set_mode((LARGUEUR, HAUTEUR))
clock = pygame.time.Clock()
FPS = 60

#2D game

def position_devant_joueur(player, distance):
    orientation_radians = math.radians(player.orientation)
    delta_x = math.cos(orientation_radians)
    delta_y = math.sin(orientation_radians)
    print(round(delta_x, 1), round(delta_y, 1), player.orientation)
    return (player.x + delta_x)*65, (player.y + delta_y)*65

# PLAYER
player = Player()


# MAP

# TEMPORAIREMENT 65 DE LARGE POUR UNE TUILE



while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Get key press
            print(pygame.KEYDOWN)
            player.move(event.key) #Move player if key pressed
    
    player.move_cam()
    
    # AFFICHAGE TEMPORAIRE background map
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (i * 5 + 30, j * 5 + 30, 100),(i*65, j*65, 65, 65))
    
    #Afficher joueur
    pygame.draw.circle(screen, (0, 0, 255), (player.x * 65, player.y * 65), 10)
    #Afficher direction
    pygame.draw.line(screen, (255, 255, 0), (player.x * 65, player.y * 65), position_devant_joueur(player, 1))


    
    #print(round(player.x, 1), round(player.y, 1), player.orientation)
    pygame.display.update()