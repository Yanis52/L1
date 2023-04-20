# -*- coding: utf-8 -*-
import pygame
from grille import *


class Joueur:
    def __init__(self, fichier, monde):

        self.g = Grille(fichier, monde)
        self.file = fichier
        self.Taille = self.g.Taille

        self.up = self.g.up
        self.down = self.g.down
        self.right = self.g.right
        self.left = self.g.left

        self.Vide = self.g.Vide
        self.obstacle = self.g.obstacle
        self.objectif = self.g.objectif
        self.caisse = self.g.caisse
        self.point = self.g.point

        self.sprite = self.left

        self.compteur = 0
        self.go = False

    def position_joueur(self, niveau):
        """ fonction qui permet de sauvegarder la position du personnage """
        pos = []
        for lin in range(len(niveau)):
            for col in range(len(niveau[lin])):
                imgs = niveau[lin][col]
                if imgs == 3:
                    pos.append(lin)
                    pos.append(col)
        return pos

    def move(self, niveau, screen, pos):
        """ fonction se charge des déplacements du personnage dans la grille selon de la touche appuyée """
        x = self.position_joueur(niveau)[0]
        y = self.position_joueur(niveau)[1]

        screen.blit(self.sprite, (x * self.Taille, y * self.Taille))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or pos == self.up:
            self.go = True
            self.compteur += 1
            self.sprite = self.up  # vers le haut
            if self.possible(niveau, x, y, self.sprite, screen) == False:  # test collision ou pas
                if niveau[x - 1][y] == 0:  # s'il ya du vide devant
                    if (x, y) in self.g.objectifs():
                        x -= 1
                        niveau[x][y] = 3
                        niveau[x + 1][y] = 2
                    else:
                        x -= 1  # changement de coordonnées
                        niveau[x][y] = 3  # la position devant nous prend la valeur 3
                        niveau[x + 1][y] = 0  # la position là où on était prend la valeur 0
        else:
            self.go = False

        if keys[pygame.K_RIGHT] or pos == self.down:
            self.go = True
            self.compteur += 1
            self.sprite = self.down  # vers le bas
            if self.possible(niveau, x, y, self.sprite, screen) == False:  # test collision ou pas
                if niveau[x + 1][y] == 0:
                    if (x, y) in self.g.objectifs():
                        x += 1
                        niveau[x][y] = 3
                        niveau[x - 1][y] = 2
                    else:
                        x += 1  # changement de coordonnées
                        niveau[x][y] = 3  # la position devant nous prend la valeur 3
                        niveau[x - 1][y] = 0  # la position là où on était prend la valeur 0
        else:
            self.go = False

        if keys[pygame.K_UP] or pos == self.left:
            self.go = True
            self.compteur += 1
            self.sprite = self.left  # vers la gauche
            if self.possible(niveau, x, y, self.sprite, screen) == False:  # test collision ou pas
                if niveau[x][y - 1] == 0:  # s'il y a un vide à gauche
                    if (x, y) in self.g.objectifs():
                        y -= 1
                        niveau[x][y] = 3
                        niveau[x][y + 1] = 2
                    else:
                        y -= 1  # changement de coordonnées
                        niveau[x][y] = 3  # la position devant nous prend la valeur 3
                        niveau[x][y + 1] = 0  # la position là où on était prend la valeur 0
        else:
            self.go = False

        if keys[pygame.K_DOWN] or pos == self.right:
            self.go = True
            self.compteur += 1
            self.sprite = self.right  # vers la droite
            if self.possible(niveau, x, y, self.sprite, screen) == False:  # test collision ou pas
                if niveau[x][y + 1] == 0:  # s'il y a un Vide à droite
                    if (x, y) in self.g.objectifs():
                        y += 1
                        niveau[x][y] = 3
                        niveau[x][y - 1] = 2
                    else:
                        y += 1  # changement de coordonnées
                        niveau[x][y] = 3  # la position devant nous prend la valeur 3
                        niveau[x][y - 1] = 0  # la position là où on était prend la valeur 0
        else:
            self.go = False

        if keys[pygame.K_r]:
            self.g.player_path = []    # réinititialisation de l'historique du personnage
            self.g.box_path = []  # réinitialisation de l'historique des caisses
            return False

    def possible(self, niveau, lin, col, sprite, screen):
        """ fonction qui gère les différentes possibilités de déplacement """

        if sprite == self.up:  # on part vers le haut
            if niveau[lin - 1][col] == 4 or niveau[lin - 1][col] == 6 or niveau[lin - 1][col] == 1 or niveau[lin - 1][
                col] == 2:  # s'il ya une collision
                if niveau[lin - 1][col] == 4 or niveau[lin - 1][col] == 6:  # si au-dessus on a une caisse ou un point
                    if self.g.deplacementdecaisse(niveau, lin, col, sprite):  # s'il y'a mouvement de caisses
                        lin -= 1  # on modifie les coordonnees
                    return True
                if niveau[lin - 1][col] == 2:
                    if (lin, col) in self.g.objectifs():
                        niveau[lin][col] = 2
                        screen.blit(self.objectif, (lin * self.Taille, col * self.Taille))
                    else:
                        niveau[lin][col] = 0
                    lin -= 1
                    niveau[lin][col] = 3
                    return True
                if niveau[lin - 1][col] == 1:  # si on a un mur
                    return True  # rien ne se passe
            else:
                return False  # sinon pas d'obstacle devant nous

        if sprite == self.down:  # on part vers le bas
            if niveau[lin + 1][col] == 4 or niveau[lin + 1][col] == 6 or niveau[lin + 1][col] == 1 or niveau[lin + 1][
                col] == 2:
                if niveau[lin + 1][col] == 4 or niveau[lin + 1][col] == 6:  # si au-dessus on a une caisse ou un point
                    if self.g.deplacementdecaisse(niveau, lin, col, sprite):  # s'il y'a mouvement de caisses
                        lin += 1
                    return True
                if niveau[lin + 1][col] == 2:
                    if (lin, col) in self.g.objectifs():
                        niveau[lin][col] = 2
                        screen.blit(self.objectif, (lin * self.Taille, col * self.Taille))
                    else:
                        niveau[lin][col] = 0

                    lin += 1

                    niveau[lin][col] = 3
                    return True
                if niveau[lin + 1][col] == 1:  # si on a un mur
                    return True  # rien ne se passe
            else:
                return False  # sinon pas d'obstacle devant nous

        if sprite == self.left:  # on part vers la gauche
            if niveau[lin][col - 1] == 4 or niveau[lin][col - 1] == 6 or niveau[lin][col - 1] == 1 or niveau[lin][
                col - 1] == 2:  # s'il ya une collision
                if niveau[lin][col - 1] == 4 or niveau[lin][col - 1] == 6:  # si au-dessus on a une caisse ou un point
                    if self.g.deplacementdecaisse(niveau, lin, col, sprite):  # s'il y'a mouvement de caisses
                        col -= 1  # on modifie les coordonnees
                    return True
                if niveau[lin][col - 1] == 2:
                    if (lin, col) in self.g.objectifs():
                        niveau[lin][col] = 2
                        screen.blit(self.objectif, (lin * self.Taille, col * self.Taille))

                    else:
                        niveau[lin][col] = 0

                    col -= 1

                    niveau[lin][col] = 3
                    return True

                if niveau[lin][col - 1] == 1:  # si on a un mur
                    return True  # rien ne se passe
            else:
                return False  # sinon pas d'obstacle devant nous

        if sprite == self.right:  # on part vers la droite
            if niveau[lin][col + 1] == 4 or niveau[lin][col + 1] == 6 or niveau[lin][col + 1] == 1 or niveau[lin][
                col + 1] == 2:  # s'il ya une collision
                if niveau[lin][col + 1] == 4 or niveau[lin][col + 1] == 6:  # si au-dessus on a une caisse ou un point
                    if self.g.deplacementdecaisse(niveau, lin, col, sprite):  # s'il y'a mouvement de caisses
                        col += 1  # on modifie les coordonnees
                    return True
                if niveau[lin][col + 1] == 2:
                    if (lin, col) in self.g.objectifs():
                        niveau[lin][col] = 2
                        screen.blit(self.objectif, (lin * self.Taille, col * self.Taille))

                    else:
                        niveau[lin][col] = 0

                    col += 1
                    niveau[lin][col] = 3
                    return True
                if niveau[lin][col + 1] == 1:  # si on a un mur
                    return True  # rien ne se passe
            else:
                return False  # sinon pas d'obstacle devant nous

    def base(self):
        with open(self.file, 'r') as fichier:
            niveau = [[int(l) for l in ligne.strip()] for ligne in fichier]
        objectifs = []
        murs = []
        caisses = []
        perso = []
        sol = []
        for x in range(len(niveau)):
            for y in range(len(niveau[x])):
                if niveau[x][y] == 4:
                    caisses.append((x, y))
                if niveau[x][y] == 1:
                    murs.append((x, y))
                if niveau[x][y] == 2:
                    objectifs.append((x, y))
                if niveau[x][y] == 3:
                    perso.append((x, y))
                if niveau[x][y] == 0:
                    sol.append((x, y))
        return caisses, murs, objectifs, perso, sol

    def recommencer(self, niveau):
        """ fonction pour restart le niveau """
        base = self.base()
        restart = pygame.display.set_mode((1080, 720))
        background = pygame.image.load('PNG/fond.png').convert()
        restart.blit(background, (0, 0))
        for (x, y) in base[0]:
            niveau[x][y] = 4
            restart.blit(self.caisse, (x * self.Taille, y * self.Taille))
        for (x, y) in base[1]:
            niveau[x][y] = 1
            restart.blit(self.obstacle, (x * self.Taille, y * self.Taille))
        for (x, y) in base[2]:
            niveau[x][y] = 2
            restart.blit(self.objectif, (x * self.Taille, y * self.Taille))
        for (x, y) in base[3]:
            niveau[x][y] = 3
            restart.blit(self.sprite, (x * self.Taille, y * self.Taille))
        for (x, y) in base[4]:
            niveau[x][y] = 0
            restart.blit(self.Vide, (x * self.Taille, y * self.Taille))
