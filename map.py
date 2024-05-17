from math import *
from random import*
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

def draw_map(screen, player, position_minimap, minimap_size):
    
    screen_height = screen.get_height()
    screen_width = screen.get_width()

    #Outline
    pygame.draw.line(screen, (255, 255, 0), position_minimap, (position_minimap[0], position_minimap[1] + minimap_size[1]), 5)
    pygame.draw.line(screen, (255, 255, 0), (position_minimap[0], position_minimap[1] + minimap_size[1]), (position_minimap[0] + minimap_size[0], position_minimap[1] + minimap_size[1]), 5)

    #Afficher joueur
    pygame.draw.circle(screen, (255, 0, 0), (position_minimap[0] + (0.5*minimap_size[0]) + (player.x - round(player.x)), position_minimap[1] + (0.5*minimap_size[1]) + (player.y - round(player.y))), 5)
    
    #Afficher Map
    #TODO : afficher la map autour du joueur

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

def generation_map(x,y) : 
    """Créé un tableau de tableaux représentant une map,
    dans lequel les 1 représentent des murs et des 0 l'absence de ces derniers"""
    mp = []
    for i in range(y) :
        mp.append([]) 
        for j in range(x) :
            mp[i].append(randint(0,1))
    for k in range(len(mp)) :
            mp[j-k][0] =1
            mp[0][k] = 1
            mp[j][k] = 1
            mp[k][-1] = 1
    return mp 