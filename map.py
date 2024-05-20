from math import *
from random import*
import pygame

taille_map = 15
use_map_generator = True

def draw_map(screen, player, position_minimap, minimap_size, colors):
    """
    affiche une minimap en haut de l'écran
    """
    
    screen_height = screen.get_height()
    screen_width = screen.get_width()
    
    #Afficher Map
    for i in range(10):
        for j in range(10):
            if 0 <= round(player.x) - 5 + i < len(m[0])-1 and 0 <= round(player.y) - 5 + j < len(m)-1:
                if m[round(player.x) - 5 + i][round(player.y) - 5 + j] == 1:
                    pygame.draw.rect(screen, colors["wall1"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
                else:
                    pygame.draw.rect(screen, colors["ground"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
            else:
                pygame.draw.rect(screen, colors["out_of_map"], pygame.Rect((position_minimap[0] + (i*(minimap_size[0]/10)), position_minimap[1] + (j*(minimap_size[0]/10))), (minimap_size[0]/10, minimap_size[0]/10)))
    
    #Outline
    pygame.draw.line(screen, (255, 255, 0), position_minimap, (position_minimap[0], position_minimap[1] + minimap_size[1]), 5)
    pygame.draw.line(screen, (255, 255, 0), (position_minimap[0], position_minimap[1] + minimap_size[1]), (position_minimap[0] + minimap_size[0], position_minimap[1] + minimap_size[1]), 5)

    #Afficher joueur
    pos_joueur = (position_minimap[0] + (0.5*minimap_size[0]) + ((player.x - round(player.x))*minimap_size[0]/10), position_minimap[1] + (0.5*minimap_size[1]) + ((player.y - round(player.y))*minimap_size[0]/10))
    pygame.draw.circle(screen, (255, 0, 0), pos_joueur, 5)

    #Afficher direction joueur
    point = (pos_joueur[0] + cos(radians(player.orientation))*10, pos_joueur[1] + sin(radians(player.orientation))*10)
    pygame.draw.line(screen, (255, 255, 0),pos_joueur, point, 2)

def existe_mur(coordonnees):
    """
    renvoie True si aux coordonnees en argument il y a un mur, renvoie False sinon
    """
    if coordonnees[0] > len(m[0]) - 1 or coordonnees[1] > len(m) - 1:
         return True
    if m[floor(coordonnees[0])][floor(coordonnees[1])] == 1:
        return True
    return False

def generation_map(x,y) : 
    """
    Créé un tableau de tableaux représentant une map,
    dans lequel les 1 représentent des murs et des 0 l'absence de ces derniers
    """
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
    
    mp[5][5] = 0
    return mp

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

if use_map_generator:
    m = generation_map(taille_map, taille_map)