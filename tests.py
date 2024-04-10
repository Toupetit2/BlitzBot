import pygame
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_color = (255, 255, 255)  # Couleur du joueur (blanc dans cet exemple)
player_radius = 20  # Rayon du joueur
sensitivity = 0.1  # Sensibilité de la rotation

player_angle = 0  # Angle initial du joueur

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Obtenir le mouvement de la souris
    dx, _ = pygame.mouse.get_rel()
    
    # Calculer la rotation du joueur en fonction du mouvement de la souris
    player_angle += dx * sensitivity
    
    # Effacer l'écran
    screen.fill((0, 0, 0))
    
    # Dessiner le joueur (cercle)
    player_x = 400 + math.cos(math.radians(player_angle)) * 150  # 150 est la distance du joueur à l'origine (400, 300)
    player_y = 300 + math.sin(math.radians(player_angle)) * 150
    pygame.draw.circle(screen, player_color, (int(player_x), int(player_y)), player_radius)
    
    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
