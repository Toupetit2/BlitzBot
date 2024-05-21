import pygame
import math

from map import *

fov = 70
nb_rays = 70
size_step = 0.01

def ray_get_end(coordonnees, rotation):
    coordonnees_check = coordonnees
    xstep = math.cos(math.radians(rotation)) * size_step
    ystep = math.sin(math.radians(rotation)) * size_step
    while existe_mur(coordonnees_check) != True:
        coordonnees_check = (coordonnees_check[0] + xstep, coordonnees_check[1] + ystep)
    return coordonnees_check


def wall_side(coord):
    """
    renvoie 1 si le mur est vertical, 0 si c'est horizontal
    """
    if abs(coord[0] - round(coord[0])) < abs(coord[1] - round(coord[1])):
        return 1
    return 0

def ray_casting(orientation, coord):
    """
    renvoie la distance aux murs selon différents angles dans une liste
    """
    distance_to_wall = []
    rays_end = []
    start = orientation - fov//2
    delta_angle = fov / nb_rays

    wall_side_tab = []

    for i in range(nb_rays):
        ray_end = ray_get_end((coord[0], coord[1]), i * delta_angle + start)
        
        
        wall_side_tab.append(wall_side(ray_end)) # Détecter le coté du mur
        
        rays_end.append(rays_end) #Pour l'affichage
        distance_to_wall.append(sqrt((coord[0] - ray_end[0])**2 + (coord[1] - ray_end[1])**2))
    return distance_to_wall, rays_end, wall_side_tab
    
def draw_rays2D(self, rays, screen):
    for i in range(self.nb_rays):
        pygame.draw.line(screen, (255, 255, 0), (self.x * 65, self.y * 65), (rays[1][0] * 65, rays[1][1] * 65))


def ray_casting3D(screen, colors, orientation, coord):
    """
    Pour afficher en '3D' la vue du joueur
    """
    height = screen.get_height()
    width = screen.get_width()
    ray_cast = ray_casting(orientation, coord)
    ray_color = ray_cast[2]
    ray_length = ray_cast[0]
    width_rect = width/nb_rays
    screen.fill((0, 0, 0))

    for i in range(nb_rays):
        if ray_length[i] > 0.1:
            height_rect = (height*0.9)//ray_length[i]
        else:
            height_rect = height
        
        if ray_color[i] == 0:
            pygame.draw.rect(screen, colors["wall1"], (width_rect*i, (height - height_rect)//2, width_rect+1, height_rect))
        else:
            pygame.draw.rect(screen, colors["wall2"], (width_rect*i, (height - height_rect)//2, width_rect+1, height_rect))

