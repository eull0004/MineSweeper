# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste

def construireGrilleDemineur(nl: int, nc: int) -> list:
    grille = []
    if nl <= 0 or nc <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes ({nl}) ou de colonnes ({nc}) est négatif ou nul")
    elif isinstance(nl, int) == False or isinstance(nc, int) == False:
        raise TypeError(f"construireGrilleDemineur : le nombre de lignes ({nl}) ou de colonnes ({nc}) n'est pas un entier")
    for i in range(nl):
        ligne = []
        for j in range(nc):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille

def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True
def getNbLignesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbLignesGrilleDemineur: le parametre n'est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbColonnesGrilleDemineur: le parametre n'est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    contient = True
    if (coord[0]<0 or coord[0]>(getNbLignesGrilleDemineur(grille)-1)) or (coord[1]<0 or coord[1]>(getNbColonnesGrilleDemineur(grille)-1)):
        contient = False
    if isinstance(grille,list) == False or isinstance(coord,tuple) == False:
        raise TypeError("isCoordonneeCorrecte : un des parametres n'est pas du bon type")
    return contient


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnee non contenue dans la grille")
    if isinstance(grille,list) == False or isinstance(coord,tuple) == False:
        raise TypeError("isCoordonneeCorrecte : un des parametres n'est pas du bon type")
    return grille[coord[0]] [coord[1]]

def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    cell = getCelluleGrilleDemineur(grille, coord)
    return getContenuCellule(cell)

def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    cell = getCelluleGrilleDemineur(grille, coord)
    setContenuCellule(cell, contenu)
    return None

def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    cell = getCelluleGrilleDemineur(grille, coord)
    return isVisibleCellule(cell)

def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    cell = getCelluleGrilleDemineur(grille, coord)
    setVisibleCellule(cell, visible)
    return None

def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    cell = getCelluleGrilleDemineur(grille, coord)
    return contientMineCellule(cell)
