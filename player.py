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

        self.fov = 70
        self.nb_rays = 70

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
    

    def orientation_line(self, point):
        orientation_radians = math.radians(point)
        delta_x = math.cos(orientation_radians)
        delta_y = math.sin(orientation_radians)

        return (self.x + delta_x)*65, (self.y + delta_y)*65

    def draw_rays(self, screen):
        start = self.orientation - self.fov//2
        delta_angle = self.fov / self.nb_rays
        for i in range(self.nb_rays):
            pygame.draw.line(screen, (255, 255, 0), (self.x * 65, self.y * 65), (self.orientation_line(start + i * delta_angle)))