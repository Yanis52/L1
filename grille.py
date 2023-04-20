# -*- coding: utf-8 -*-

from menuSelection import Texture


class Grille:
    def __init__(self, file, monde):
        self.file = file
        with open(self.file, 'r') as fichier:
            self.niveau = [[int(l) for l in ligne.strip()] for ligne in fichier]

        self.Vide = Texture().choix(monde)[0]
        self.obstacle = Texture().choix(monde)[1]
        self.objectif = Texture().choix(monde)[2]
        self.caisse = Texture().choix(monde)[3]
        self.point = Texture().choix(monde)[4]
        self.decor8 = Texture().choix(monde)[5]
        self.left = Texture().choix(monde)[6]
        self.right = Texture().choix(monde)[7]
        self.down = Texture().choix(monde)[8]
        self.up = Texture().choix(monde)[9]

        self.historique = []    # liste va contenir les coordonnées des caisses pour la sauvegarde
        self.Taille = 64

    def affichage(self, niveau, screen):
        """ fonction qui se charge de l'interface graphique """
        for n in range(1, 6):
            if self.file == 'sauvegarde/sauvegarde' + str(n) + '/partie' + str(n) + '.txt':
                for lin in range(len(niveau)):
                    for col in range(len(niveau[lin])):
                        imgs = niveau[lin][col]

                        if imgs == 8:
                            screen.blit(self.decor8, ((lin * self.Taille), (col * self.Taille)))

                        if imgs == 0:
                            screen.blit(self.Vide, ((lin * self.Taille), (col * self.Taille)))
                        if imgs == 1:
                            screen.blit(self.obstacle, ((lin * self.Taille), (col * self.Taille)))
                        if imgs == 4:
                            screen.blit(self.caisse, ((lin * self.Taille), (col * self.Taille)))
                        if imgs == 6:
                            screen.blit(self.point, ((lin * self.Taille), (col * self.Taille)))

                for (x, y) in self.objectifs():
                    screen.blit(self.objectif, (x * self.Taille, y * self.Taille))
                    if niveau[x][y] == 6:
                        screen.blit(self.point, (x * self.Taille, y * self.Taille))

        else:
            for lin in range(len(niveau)):
                for col in range(len(niveau[lin])):
                    imgs = niveau[lin][col]

                    if imgs == 8:
                        screen.blit(self.decor8, ((lin * self.Taille), (col * self.Taille)))

                    if imgs == 0:
                        screen.blit(self.Vide, ((lin * self.Taille), (col * self.Taille)))
                    if imgs == 1:
                        screen.blit(self.obstacle, ((lin * self.Taille), (col * self.Taille)))
                    if imgs == 4:
                        screen.blit(self.caisse, ((lin * self.Taille), (col * self.Taille)))
                    if imgs == 6:
                        screen.blit(self.point, ((lin * self.Taille), (col * self.Taille)))

            for (x, y) in self.objectifs():
                screen.blit(self.objectif, (x * self.Taille, y * self.Taille))
                if niveau[x][y] == 6:
                    screen.blit(self.point, (x * self.Taille, y * self.Taille))

    def deplacementdecaisse(self, niveau, lin, col, sprite):
        """ fonction qui se charge du déplacement des caisses """
        if sprite == self.up:
            if (niveau[lin - 2][col] != 1) and (niveau[lin - 2][col] != 4) and (niveau[lin - 2][col] != 6):
                if niveau[lin - 1][col] == 4 or niveau[lin - 1][col] == 6:  # s'il y a une caisse devant nous

                    if niveau[lin - 1][col] == 4:  # s'il ya une caisse devant
                        pass
                    
                    if niveau[lin - 2][col] == 2:  # s'il y'a un objectif après la caisse
                        niveau[lin - 1][col] = 3  # le personnage prend l'ancienne position de la caisse
                        niveau[lin - 2][col] = 6  # on a un objectif atteint si on pousse la caisse
                        self.historique.append(((lin - 2), col))
                        if (lin, col) in self.objectifs():    # quand devant la caisse on a encore un objectif
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

                    if niveau[lin - 2][col] == 0:  # s'il y'a un vide après la caisse
                        niveau[lin - 1][col] = 3  # la position où était la caisse le personnage l'a prend
                        niveau[lin - 2][col] = 4  # ça devient une caisse
                        self.historique.append(((lin - 2), col))

                        if (lin, col) in self.objectifs():  # on teste ici si le personnage était sur un objectif ou pas
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

        # on repete pour les differentes directions

        if sprite == self.down:
            if (niveau[lin + 2][col] != 1) and (niveau[lin + 2][col] != 4) and (niveau[lin + 2][col] != 6):
                if niveau[lin + 1][col] == 4 or niveau[lin + 1][col] == 6:  # s'il y a une caisse devant nous

                    if niveau[lin + 1][col] == 4:  # s'il ya une caisse devant
                        pass

                    if niveau[lin + 2][col] == 2:  # s'il y'a un objectif après la caisse
                        niveau[lin + 1][col] = 3  # le personnage prend l'ancienne position de la caisse
                        niveau[lin + 2][col] = 6  # on a un objectif atteint si on pousse la caisse
                        self.historique.append(((lin + 2), col))
                        if (lin, col) in self.objectifs():    # quand devant la caisse on a encore un objectif
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

                    if niveau[lin + 2][col] == 0:  # s'il y'a un vide après la caisse
                        niveau[lin + 1][col] = 3
                        niveau[lin + 2][col] = 4  # ça devient une caisse
                        self.historique.append(((lin + 2), col))

                        if (lin, col) in self.objectifs():  # on teste ici si le personnage était sur un objectif ou pas
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

        if sprite == self.left:
            if (niveau[lin][col - 2] != 1) and (niveau[lin][col - 2] != 4) and (niveau[lin][col - 2] != 6):
                if niveau[lin][col - 1] == 4 or niveau[lin][col - 1] == 6:  # s'il y a une caisse devant nous

                    if niveau[lin][col - 1] == 4:  # s'il ya une caisse devant
                        pass

                    if niveau[lin][col - 2] == 2:  # s'il y'a un objectif après la caisse
                        niveau[lin][col - 1] = 3
                        niveau[lin][col - 2] = 6  # on a un objectif atteint si on pousse la caisse
                        self.historique.append((lin, (col - 2)))
                        if (lin, col) in self.objectifs():    # quand devant la caisse on a encore un objectif
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

                    if niveau[lin][col - 2] == 0:  # s'il y'a un vide après la caisse
                        niveau[lin][col - 1] = 3  # le personnage juste derrière
                        niveau[lin][col - 2] = 4  # ça devient une caisse
                        self.historique.append((lin, (col - 2)))
                        if (lin, col) in self.objectifs():
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

        if sprite == self.right:
            if (niveau[lin][col + 2] != 1) and (niveau[lin][col + 2] != 4) and (niveau[lin][col + 2] != 6):
                if niveau[lin][col + 1] == 4 or niveau[lin][col + 1] == 6:  # s'il y a une caisse devant nous

                    if niveau[lin][col + 1] == 4:  # s'il ya une caisse devant
                        pass

                    if niveau[lin][col + 2] == 2:  # s'il y'a un objectif après la caisse
                        niveau[lin][col + 1] = 3
                        niveau[lin][col + 2] = 6  # on a un objectif atteint si on pousse la caisse

                        if (lin, col) in self.objectifs():  # quand devant la caisse on a encore un objectif
                            niveau[lin][col] = 2

                        else:
                            niveau[lin][col] = 0

                    if niveau[lin][col + 2] == 0:  # s'il y'a un vide après la caisse
                        niveau[lin][col + 1] = 3
                        niveau[lin][col + 2] = 4  # ça devient une caisse

                        if (lin, col) in self.objectifs():
                            niveau[lin][col] = 2
                        else:
                            niveau[lin][col] = 0

    def caisses_pos(self, niveau):
        caisses_pos = []
        for lin in range(len(niveau)):
            for col in range(len(niveau[lin])):
                if niveau[lin][col] == 4 or niveau[lin][col] == 6:
                    caisses_pos.append((lin, col))
        return caisses_pos

    def objectifs(self):
        """ Cette fonction sauvegarde dans une liste les coordonnées des objectifs """
        for i in range(1, 6):
            if self.file == 'sauvegarde/sauvegarde'+ str(i) +'/partie'+ str(i) +'.txt':
                with open('sauvegarde/sauvegarde' + str(i) + '/coordonnees_objectifs.txt', 'r') as fichier:
                    lire = [l for l in fichier]

                    coordonnees_objectif = []
                    for i in range(0, len(lire)):
                        if lire[i][0] == '\n' or lire[i][1] == '\n':
                            pass
                        else:
                            x = int(lire[i][0])
                            y = int(lire[i][1])
                            coordonnees_objectif.append((x, y))
                    return coordonnees_objectif
        else:
            with open(self.file, 'r') as fichier:
                 niveau = [[int(l) for l in ligne.strip()] for ligne in fichier]
            coordonnees_but = []
            for lin in range(len(niveau)):
                for col in range(len(niveau[lin])):
                    if niveau[lin][col] == 2 or niveau[lin][col] == 6:
                        coordonnees_but.append((lin, col))
            return coordonnees_but

    def endgame(self, niveau):
        if self.objectifs() == self.caisses_pos(niveau):  # si il y'a autant de points que de nombre d'objectifs
            return True  # renvoie True le Jeu est fini
        else:
            return False  # pas encore fini
