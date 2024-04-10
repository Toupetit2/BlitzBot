import pygame
import math

class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 0
        self.upOrientation = 180
        self.speed = 0.2
        self.sensi = 0.5

    def move(self, keypressed):
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
    
