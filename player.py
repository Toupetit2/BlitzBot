import pygame
import math
from map import *

class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 0
        self.upOrientation = 180
        self.speed = 0.4
        self.sensi = 0.5

        self.fov = 70
        self.nb_rays = 70

    def move(self, keypressed):
        #pygame.key.get_pressed()
        if keypressed not in [pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d]:
            return
        
        orient = self.orientation
        if keypressed == pygame.K_d:
            orient += 90
        if keypressed == pygame.K_q:
            orient += -90
        if keypressed == pygame.K_s:
            orient += -180
        
        self.x += math.cos(math.radians(orient)) * self.speed
        self.y += math.sin(math.radians(orient)) * self.speed
        

    def move_cam(self):
        dx, dy = pygame.mouse.get_rel()
        self.orientation += dx * self.sensi
        self.orientation = self.orientation%360
    

    def orientation_line(self, point):
        orientation_radians = math.radians(point)
        delta_x = math.cos(orientation_radians)
        delta_y = math.sin(orientation_radians)

        return (self.x + delta_x)*65, (self.y + delta_y)*65


    def ray_get_end(self, coordonnees, rotation):
        coordonnees_check = coordonnees
        xstep = math.cos(math.radians(rotation)) * 0.1
        ystep = math.sin(math.radians(rotation)) * 0.1
        while existe_mur(coordonnees_check) != True:
            coordonnees_check = (coordonnees_check[0] + xstep, coordonnees_check[1] + ystep)
        return coordonnees_check


    def ray_casting(self, screen):
        distance_to_wall = []
        start = self.orientation - self.fov//2
        delta_angle = self.fov / self.nb_rays
        for i in range(self.nb_rays):
            ray_end = self.ray_get_end((self.x, self.y), i * delta_angle + start)
            pygame.draw.line(screen, (255, 255, 0), (self.x * 65, self.y * 65), (ray_end[0] * 65, ray_end[1] * 65))

            distance_to_wall.append(sqrt((self.x - ray_end[0])**2 + (self.y - ray_end[1])**2))
        return distance_to_wall
    
    def ray_casting3D(self, screen, minimap):
        height = screen.get_height()
        width = screen.get_width()

        ray_length = self.ray_casting(screen)
        width_rect = width/self.nb_rays
        screen.fill((0, 0, 0))

        for i in range(self.nb_rays):
            height_rect = height//ray_length[i]
            pygame.draw.rect(screen, (0, 255, 0), (width_rect*i, (height - height_rect)//2, width_rect+1, height_rect))
    
