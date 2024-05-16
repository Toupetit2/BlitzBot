import pygame
import sys

from player import *
from map import *
from ray_casting import *

WIDTH, HEIGHT = 900, 650

minimap_width, minimap_height = 250, 250

colors = {
    "wall": (20, 54, 255),
    "ground": (0, 0, 0),
    "out_of_map": (140, 140, 140)
}

minimap_position = (WIDTH - minimap_width, 0)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
#2D game

def position_devant_joueur(player, distance):
    orientation_radians = math.radians(player.orientation)
    delta_x = math.cos(orientation_radians)
    delta_y = math.sin(orientation_radians)
    #print(round(delta_x, 1), round(delta_y, 1), player.orientation)
    return (player.x + delta_x)*65, (player.y + delta_y)*65

# PLAYER
player = Player()



# TEMPORAIREMENT 65 DE LARGE POUR UNE TUILE



while True:
    pygame.mouse.set_pos = (WIDTH//2, HEIGHT//2)
    clock.tick(FPS)
    pygame.display.set_caption(f"Projet NSI - {round(clock.get_fps(), 1)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Get key press
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    player.move() #Move player if key pressed
    
    player.move_cam()
    # Dessin map
    dessine_map(screen)
    
    #Afficher les rays
    #player.ray_casting(screen)

    ray_casting3D(screen, (minimap_width, minimap_height), colors, player.orientation, (player.x, player.y))

    draw_map(screen, player, minimap_position, (minimap_width, minimap_height), colors)
    
    #print(round(player.x, 1), round(player.y, 1), player.orientation)
    pygame.display.update()