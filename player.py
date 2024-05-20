import pygame
import math
from map import *
from ray_casting import *

class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 0
        self.upOrientation = 180
        self.speed = 0.05
        self.sensi = 0.01

        

    def move(self):
        keys = pygame.key.get_pressed()
        collisions = self.collision_detect(ray_casting(self.orientation, (self.x, self.y)))
        
        if collisions[0] and keys[pygame.K_q]:
            return
        if collisions[1] and keys[pygame.K_z]:
            return
        if collisions[2] and keys[pygame.K_d]:
            return

        orient = self.orientation
        if keys[pygame.K_d]:
            orient += 90
        if keys[pygame.K_q]:
            orient += -90
        if keys[pygame.K_s]:
            orient += -180
        if keys[pygame.K_d] or keys[pygame.K_q] or keys[pygame.K_s] or keys[pygame.K_z]:
            self.x += math.cos(math.radians(orient)) * self.speed
            self.y += math.sin(math.radians(orient)) * self.speed
        

    def move_cam(self):
        dx, dy = pygame.mouse.get_rel()
        self.orientation += dx * self.sensi
        self.orientation = self.orientation%360
    
    def collision_detect(self, rays):
        tab = [False, False, False]
        if rays[0][0] < 0.2:
            tab[0] = True
        if rays[0][nb_rays//2] < 0.2:
            tab[1] = True
        if rays[0][nb_rays-1] < 0.2:
            tab[2] = True
        return tab

