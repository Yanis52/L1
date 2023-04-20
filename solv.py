# -*- coding: utf-8 -*-

from grille import Grille
from player import Joueur


class Signal:
    def __init__(self):
        self.signal = False


class Node:
    """ création des noeuds """
    def __init__(self, caisses, pos, h, parent=None):
        self.box = caisses  # liste des coordonnées des caisses
        self.pos = pos  # position du joueur
        self.h = h  # entier (heuristic ou le hammig ici)
        self.parent = parent  # pointeur sur Node (le parent cad où le caisse est déjà passé)


def niveauToState(fichier, monde):
    g = Grille(fichier, monde)
    niveau = g.niveau
    """ ici la fonction sauvegarde les coordonnées des objectifs, murs et objectifs"""
    objectifs = []
    murs = []
    caisses = []
    perso = (0, 0)
    for x in range(len(niveau)):
        for y in range(len(niveau[x])):
            if niveau[x][y] == 3:
                perso = (x, y)
            if niveau[x][y] == 4:
                caisses.append((x, y))
            elif niveau[x][y] == 1:
                murs.append((x, y))
            if niveau[x][y] == 2:
                objectifs.append((x, y))
    return objectifs, Node(caisses, perso, petit_chemin(caisses, perso, objectifs), None), murs
# retourn respectivement la liste des objectifs, etat, et murs


def verification(etat, Objectifs):
    for caisse in etat.box:    # ici la variable box va parcourir toutes les coordonnées
        if caisse not in Objectifs:    # si ces coordonnées correspondent aux coordonnées des objectifs le jeu est fini
            return False
    return True


def distance(start, end):
    """ la fonction calcule la distance entre start et end """
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def petit_chemin(caisses, pos, S):

    """ la fonction ici va choisir l'objectif le plus proche de la caisse """
    DSTtot = []   # liste qui va contenir la distance totale (perso vers caisse puis vers objectif)
    for c in caisses:   # on parcours la liste des coordonnées des caisses
        Dcaisse_objectif = []
        # une liste qui va contenir les differentes distances entre une caisse et les autres objectifs

        for st in S:    # on parcours la liste des coordonnées des objectifs
            Dcaisse_objectif.append(distance(c, st))     # on retiens la distance entre la caisse et objectif
        DSTtot.append(min(Dcaisse_objectif) + distance(pos, c))   # on ajoute la distance la plus petite
        # ici on prend la distance la plus petite entre
        # la caisse et l'objectif et puis on ajoute la distance entre le joueur et la caisse
    return min(DSTtot)    # ici on renvoie le chemin le plus court du perso vers la caisse puis vers objectif


def fils(etat, S, M, openList, closedList):
    # état ça sera un noeud (liste caisses, tuple pos du Joueur, heuristic, parent)
        """ Fonction qui vérifie les prochains mouvements de l'IA """
        lsState = []    # notre parcours ou chemin
        cutClosed = [(node.box, node.pos) for node in closedList]
    # liste des noeuds étant dans la close list (endroits déjà passés)

        cutOpen = [(node.box, node.pos) for node in openList]
    # liste des noeuds qui sont dans l'openlist

        for dire in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # on détermine les directions vers lesquels il peut se diriger
            posX, posY = etat.pos[0] + dire[0], etat.pos[1] + dire[1]
        # changement de coordonnées du personnage
            if (posX, posY) in etat.box and ((posX + dire[0], posY + dire[1]) not in etat.box) and (
                    (posX + dire[0], posY + dire[1]) not in M):
            # si les coordonnées du joueur sont dans la liste des caisses
            # et les coordonnées des alentours n'est pas un mur ou une box
                caisses = []
                for c in etat.box:  # change la coodonnée de la caisse qui sera déplacé par le mouvement
                # plus précisèment pour c dans les coordonnées des caisses
                # si c est égal au coordonnées du personnage alors on modifie les coordonnées de la caisse vers
                # la direction
                    if c == (posX, posY):
                        caisses.append((posX + dire[0], posY + dire[1])) # on ajoute la nouvelle coordonnées de la caisse
                    else:
                        caisses.append(c)   # sinon on ajoute les coordonnées des caisses

                newState = Node(caisses, (posX, posY), petit_chemin(caisses, (posX, posY), S), etat)
            # le nouvelle état et le node etat là où on était devient un parent
                if (newState.box, newState.pos) not in cutClosed:   # on vérifie si le nouveau noeud n'est pas déja présent
                # dans la closelist et si non on l'ajoute à notre chemin (path)
                    lsState.append(newState)

            elif ((posX, posY) not in etat.box) and ((posX, posY) not in M):
            # quand l' IA bouge si les coordonnées nouvelles ne sont pas dans celles des caisses ou des murs
                newState = Node(etat.box, (posX, posY), petit_chemin(etat.box, (posX, posY), S), etat)   # nouveau état
            # si les coordonnées ne sont pas dans les noeuds ou état de la closelist
                if (newState.box, newState.pos) not in cutClosed:
                    lsState.append(newState)    # on ajoute le nouveau état dans notre chemin

    # print('lsState '+str(lsState))
        for state in lsState:   # on parcourt tout le chemin qu'a fait l'IA
        # si un noeud ou état dans le chemin n'est pas dans l'openlist
            if (state.box, state.pos) not in cutOpen:
                openList.append(state)  # on ajoute cet état à l'openlist
            else:
            # si la distance entre le perso et l'objectif dans notre nouvelle état (ou noeud du chemin) est plus petite que celle de l'ancien
            # on change l'élément par le nouveau qui est meilleur puisque la distance est plus petite
                if state.h < openList[cutOpen.index((state.box, state.pos))].h:
                    openList[cutOpen.index((state.box, state.pos))] = state

# .index() va chercher l'élément qui a le même (state.box, state.pos)

# ici on démarre le A* pathfinding:
class IA:
    def __init__(self, fichier, monde):
        self.init = niveauToState(fichier, monde)  # on initialise les listes des caisses, murs objectifs
    # niveauToState renvoie dans l'ordre: S, état, M
        self.objectif = self.init[0]
        self.walls = self.init[2]
        self.start = self.init[1]     # on initialise le noeud de départ

        self.openList = []   # initialise l'openlist
        self.closedList = []     # initialise la closelist

        self.openList.append(self.start)  # on ajoute à l'openlist notre noeud de départ
        self.cpt = 0     # on initiale le nombre de coups ( c'est 'g' )
        self.g = Grille(fichier, monde)
        self.j = Joueur(fichier, monde)
        self.solutionIA = []    # cette liste va contenir le chemin qu'a trouvé notre algorithm

    def astar(self):   # Tant que l'openlist n'est pas vide
        if self.openList != [] or not self.g.endgame(self.g.niveau):
            self.cpt += 1    # on ajoute 1 à un compteur
            path = Node([], (), 1000000000)
            # on initialise un noeud vide sans rien ne possède aucune liste caisses ni la pos du joueur, et un heuristic
            # énorme pour pas que l'algorithme se dise qu'on a le chemin le plus court
            for state in self.openList:
                # on parcourt l'openlist
                if state.h < path.h:
                # si la distance du perso vers l'objectif en passant par la caisse du noeud dans l'openlist
                # est plus petit que celui dont on veut aller vers (le fils, le prochain supposé noeud)
                    path = state   # le nouveau noeud devient celui si

            self.closedList.append(path)    # on l'ajoute à la closelist (parce qu'on est passé dessus)
            self.openList.remove(path)  # on l'enlève de l'openlist

            fils(path, self.objectif, self.walls, self.openList, self.closedList)
        # ensuite on cheque si les coordonnées des caisses sont ou pas égales à celles des objectifs
            if verification(path, self.objectif):
                print("chemin trouvé en ", self.cpt, " iterations")  # donne le nombre de coups au total
                self.solutionIA.append(reconstruction(path))
                return reconstruction(path)



def reconstruction(node):
    """ Cette fonction sert à reconstruire le chemin dans le bon sens """
    dire = []   # liste qui va contenir les directions prises par le robot
    currentNode = node  # notre état actuel
    while currentNode.parent != None:   # si on a des parents
        dire.append((currentNode.pos[0] - currentNode.parent.pos[0], currentNode.pos[1] - currentNode.parent.pos[1]))
        # pour chaque coordonnées du noeud actuel on fait (x,y) - noeud parent (x du parent, y du parent) et on aura de la forme
        # (0,1) ou (0,-1) ... va nous montrer les directions qu'a pris le robot
        currentNode = currentNode.parent
        # puis notre état actuel devient un parent
        # l'algoritme va se faire au fur et à mesure de la résolution

    for x in range(len(dire)):
        if dire[x] == (0, 1):
            dire[x] = 'down'
        if dire[x] == (0, -1):
            dire[x] = 'up'
        if dire[x] == (1, 0):
            dire[x] = 'right'
        if dire[x] == (-1, 0):
            dire[x] = 'left'
    return dire[::-1]   # pour afficher la liste dans le sens inverse



