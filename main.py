import pygame
import sys

from player import *
from map import *
from ray_casting import *

WIDTH, HEIGHT = 900, 650

minimap_width, minimap_height = 250, 250

colors = {
    "wall1": (20, 54, 255),
    "wall2": (10, 34, 205),
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

# PLAYER
player = Player()

while True:
    pygame.mouse.set_pos = (WIDTH//2, HEIGHT//2)
    clock.tick(FPS)
    pygame.display.set_caption(f"Projet NSI - {round(clock.get_fps(), 1)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    player.move()
    
    player.move_cam()

    ray_casting3D(screen, (minimap_width, minimap_height), colors, player.orientation, (player.x, player.y))

    draw_map(screen, player, minimap_position, (minimap_width, minimap_height), colors)
    
    pygame.display.update()