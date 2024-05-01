from math import *

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

def existe_mur(coordonnees) :
     if map[floor(coordonnees[0])][floor(coordonnees[1])] == 0:
         return True
     return False

map = [[0, 1, 0, 0, 0],
       [0, 1, 1, 0, 0], 
       [0, 0, 0, 0, 1], 
       [0, 0, 0, 0, 0], 
       [0, 0, 1, 1, 0]]

print(existe_mur(map, (3.8, 4.5)))