# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)
def construireCoordonnee(li: int, co: int) -> tuple:
    coord = (li, co)
    if isinstance(li,int) == False or isinstance(co,int) == False:
        if isinstance(li,int) == False:
            raise TypeError(f"contruireCoordonnee: le numero de ligne {type(li)} n'est pas un entier")
        elif isinstance(co,int) == False:
            raise TypeError(f"contruireCoordonnee: le numero de colonne {type(co)} n'est pas un entier")
    elif li<0 or co<0:
        if li<0:
            raise ValueError(f"contruireCoordonnee: le numero de ligne {li} n'est pas positif")
        elif co<0:
            raise ValueError(f"contruireCoordonnee: le numero de colonne {co} n'est pas positif")
    return coord

def getLigneCoordonnee(coord: tuple) -> int:
    ligne = coord[0]
    if isinstance(coord,tuple) == False:
        raise TypeError("getLigneCoordonne : le parametre n'est pas une coordonnee")
    return ligne

def getColonneCoordonnee(coord: tuple) -> int:
    colonne = coord[1]
    if isinstance(coord,tuple) == False:
        raise TypeError("getColonneCoordonne : le parametre n'est pas une coordonnee")
    return colonne

def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


