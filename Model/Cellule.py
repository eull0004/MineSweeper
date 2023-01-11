# Model/Cellule.py
#

from Model.Constantes import const

#
# Modélisation d'une cellule de la grille d'un démineur
#
def isContenuCorrect(contenu: int) -> bool:
    contient = True
    if isinstance(contenu,int) == False:
        contient = False
    if contient == True:
        if contenu != const.ID_MINE and contenu < 0 or contenu > 8:
            contient = False
    return contient


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


