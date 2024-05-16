from math import *
import pygame

# def creer_map(n) :
#     """crée une map qui servira à définir la map """
#     t = []
#     for i  in range(n) :
#         t.append([0]*n)
#     return t

# def creer_mur(m,i,j) :
#     """int,int -> None
#     crée un mur aux coordonnées données"""
#     m[i][j] = 1

def draw_map(screen, player, position_minimap, minimap_size, colors):
    
    screen_height = screen.get_height()
    screen_width = screen.get_width()
    
    #Afficher Map
    for i in range(10):
        for j in range(10):
            if 0 <= round(player.x) - 5 + i < len(m[0])-1 and 0 <= round(player.y) - 5 + j < len(m)-1:
                if m[round(player.x) - 5 + i][round(player.y) - 5 + j] == 1:
                    pygame.draw.rect(screen, colors["wall"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
                else:
                    pygame.draw.rect(screen, colors["ground"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
            else:
                pygame.draw.rect(screen, colors["out_of_map"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
    
    #Outline
    pygame.draw.line(screen, (255, 255, 0), position_minimap, (position_minimap[0], position_minimap[1] + minimap_size[1]), 5)
    pygame.draw.line(screen, (255, 255, 0), (position_minimap[0], position_minimap[1] + minimap_size[1]), (position_minimap[0] + minimap_size[0], position_minimap[1] + minimap_size[1]), 5)

    #Afficher joueur
    pygame.draw.circle(screen, (255, 0, 0), (position_minimap[0] + (0.5*minimap_size[0]) + ((player.x - round(player.x))*minimap_size[0]/10), position_minimap[1] + (0.5*minimap_size[1]) + ((player.y - round(player.y))*minimap_size[0]/10)), 5)


def dessine_mur(screen, coordonnees):
    pygame.draw.rect(screen,(0,0,0),(65 * coordonnees[0], 65 * coordonnees[1],65,65))

def dessine_map(screen):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                dessine_mur(screen, (i, j))
          
               

def existe_mur(coordonnees):
    if coordonnees[0] > len(m[0]) - 1 or coordonnees[1] > len(m) - 1:
         return True
    if m[floor(coordonnees[0])][floor(coordonnees[1])] == 1:
        return True
    return False

m = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]