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

def construireCellule(contenu=0, visible=False) -> dict:
    cell = { const.CONTENU: contenu, const.VISIBLE: visible }
    if isContenuCorrect(contenu) == False:
        raise ValueError (f"construireCellule : le contenu {contenu} n'est pas correct")
    elif isinstance(visible, bool) == False:
        raise TypeError (f"construireCellule: le second parametre ({type(visible)}) n'est pas un booleen")
    return cell
def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def getContenuCellule(cell: dict) -> int:
    if type_cellule(cell) == False:
        raise TypeError ("getContenuCellule : Le parametre n'est pas une cellule")
    return cell[const.CONTENU]

def isVisibleCellule(cell: dict) -> bool:
    if type_cellule(cell) == False:
        raise TypeError ("getVisibleCellule : Le parametre n'est pas une cellule")
    return cell[const.VISIBLE]

def setContenuCellule(cell: dict, contenu2: int) -> None:
    cell[const.CONTENU] = contenu2
    if isinstance(contenu2, int) == False:
        raise TypeError("setContenuCellule : le second parametre n'est pas un entier")
    elif isContenuCorrect(contenu2) == False:
        raise ValueError (f"setContenuCellule : la valeur du contenu ({contenu2}) n'est pas correcte")
    elif type_cellule(cell) == False:
        raise TypeError ("setContenuCellule : le premier parametre n'est pas une cellule")
    return None

def setVisibleCellule(cell: dict, visible2: int) -> None:
    cell[const.VISIBLE] = visible2
    if type_cellule(cell) == False:
        raise TypeError ("setVisibleCellule : le premier parametre n'est pas une cellule")
    elif isinstance(visible2, bool) == False:
        raise TypeError ("setVisibleCellule : le second parametre n'est pas un booleen")
    return None

def contientMineCellule(cell: dict) -> bool:
    res = False
    if type_cellule(cell) == False:
        raise TypeError ("contientMineCellule : le parametre n'est pas une cellule")
    if const.ID_MINE in cell.values():
        res = True
    return res
