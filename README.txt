Ce jeu a été fait en utilisant un système de "raycasting"
a chaque fois qu'on relance le programme la map est différente

ECHAP pour quitter


--- Paramètres ---

main.py : minimap_width, minimap_height pour changer la taille de la minicarte
          colors pour changer les couleurs des murs

player.py : self.speed pour changer la vitesse du joueur
            self.sensi pour changer la sensibilité de la souris

map.py : taille_map le nombre de cubes en x et y
         use_map_generator mettez ça sur False et modifiez m pour créer votre terrain (1 pour cube et 0 pour air; il faut absolument des murs de chaque coté)

ray_casting.py : size_step plus le nombre est petit plus c'est couteux mais plus le rendu sera clair (le raycasting n'a pas été codé en suivant toutes les formules mathématiques et un peu en bruteforce)