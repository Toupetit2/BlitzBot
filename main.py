import pygame
import sys

from player import*


LARGEUR, HAUTEUR = 900, 650
pygame.init()

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
FPS = 60

#2D game

def position_devant_joueur(player, distance):
    orientation_radians = math.radians(player.orientation)
    delta_x = math.cos(orientation_radians)
    delta_y = math.sin(orientation_radians)
    print(round(delta_x, 1), round(delta_y, 1), player.orientation)
    return (player.x + delta_x)*65, (player.y + delta_y)*65

# PLAYER
player = Player()


# MAP
def dessine_map() : # Dessine la map sous forme de grille 
    case = 65
    for x in range(0, LARGEUR,case) :
        for y in range(0, HAUTEUR, case) :
            rect =pygame.Rect(x,y, case,case)
            pygame.draw.rect(screen, (255,255,255), rect, 1)

#Mur
def dessine_mur() :
    # Les coordonnées sont comptées de 65 en 65 (pour l'instant)
    #LES LIGNES CI DESSOUS SERVENT DE TEST (les coodonnées équivalante sont indiquées à côté)
    
    pygame.draw.rect(screen,(0,0,0),(65, 0,65,65 )) # = (1,0)
    pygame.draw.rect(screen,(0,0,0),(65, 65,65,65 )) # = (1,1)
    pygame.draw.rect(screen,(0,0,0),(130,65,65,65))# =(1,2)     
    pygame.draw.rect(screen,(0,0,0),(260,130,65,65 ))  # =(4,2)
    pygame.draw.rect(screen,(0,0,0),(130, 260,65,65 )) # = (2,4)
    pygame.draw.rect(screen,(0,0,0),(195, 260,65,65 )) # = (3,4)
    pygame.draw.rect(screen,(0,0,0),(390, 260,65,65 )) # = (6,4)

# TEMPORAIREMENT 65 DE LARGE POUR UNE TUILE



while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Get key press
            print(pygame.KEYDOWN)
            player.move(event.key) #Move player if key pressed
    
    player.move_cam()
    
    # AFFICHAGE TEMPORAIRE background map
    for i in range(15):
        for j in range(15):
            pygame.draw.rect(screen, (i * 5 + 30, j * 5 + 30, 100),(i*65, j*65, 65, 65))
    
    #Afficher joueur
    pygame.draw.circle(screen, (0, 0, 255), (player.x * 65, player.y * 65), 10)
    #Afficher direction
    pygame.draw.line(screen, (255, 255, 0), (player.x * 65, player.y * 65), position_devant_joueur(player, 1))

    dessine_map()
    dessine_mur()
    
    #print(round(player.x, 1), round(player.y, 1), player.orientation)
    pygame.display.update()