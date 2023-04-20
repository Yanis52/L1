import pygame
import math
import sys

import launcher
import menuSelection as ms
import menuSelectionSaves as mss
from player import Joueur

pygame.init()


#Yanis ajout texte pour guider le joueur pour revenir au menu
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Felicitation:
    def __init__(self, file, solutionIA, pas, monde):
        self.j = Joueur(file, monde)
        self.niv = file
        self.chemin = []
        self.chemin.append(solutionIA)  # la liste chemin va contenir le chemin trouvé par le robot
        self.coups = 0  # cette variable va contenir le nombre de coups de l'IA (s'il a trouvé un chemin)
        self.cpt = pas  # cette variable représente le nombre de pas

    def lvlcompleted(self, screen, monde):
        """ Cette fonction permet l'affichage du score à la fin de la partie """
        niv = self.niv
        compteur = self.cpt

        # Ajout et positonnement du boutton
        image7 = pygame.image.load('PNG/fleche.png')
        image7 = pygame.transform.scale(image7, (100, 80))
        image7_rect = image7.get_rect()
        image7_rect.x = math.ceil(screen.get_width() / 1.1)
        image7_rect.y = math.ceil(screen.get_height() / 5.36)
        next_button = pygame.image.load('PNG/buttonNext.png')
        next_button = pygame.transform.scale(next_button, (200, 300))
        next_button_rect = next_button.get_rect()
        next_button_rect.x = math.ceil(screen.get_width() / 2.5)
        next_button_rect.y = math.ceil(screen.get_height() / 1.55)

        font = pygame.font.Font('8-BIT WONDER.TTF', 15)  # ajout du font
        color = (0, 0, 0)

        fond = pygame.image.load("PNG/fond.png")
        screen.blit(fond, (0, 0))

        fond = pygame.image.load("PNG/fond.png")
        screen.blit(fond, (0, 0))

        # pour détecter la touche
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # capteur d'événement du click
                if image7_rect.collidepoint(event.pos):
                    launcher.lancement()
                elif next_button_rect.collidepoint(event.pos):
                    for i in range(1, 6):
                        if niv == 'sauvegarde/sauvegarde' + str(i) + '/partie' + str(i) + '.txt':
                            mss.savespartie(screen, monde)
                        if niv == 'levels/map' + str(i) + '.txt':
                            ms.levels(screen, monde)

            # pour quitter le jeu
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            launcher.main(screen, niv, monde)

        if keys[pygame.K_e]:
            launcher.lancement()

        if keys[pygame.K_w]:
            ms.levels(screen, monde)

        if niv == 'levels/map1.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))
            else:
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png")
                    screen.blit(image, (-50, 125))

                if compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png")
                    screen.blit(image, (-50, 125))

        if niv == 'levels/map2.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

            else:
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png").convert()
                    screen.blit(image, (-50, 125))

                if compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png").convert()
                    screen.blit(image, (-50, 125))

        if niv == 'levels/map3.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))
            else:
                self.coups = len(self.chemin[0])
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png")
                    screen.blit(image, (-50, 125))

                if compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png")
                    screen.blit(image, (-50, 125))

        if niv == 'levels/map4.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))
            else:
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png")
                    screen.blit(image, (-50, 125))

                elif compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png")
                    screen.blit(image, (-50, 125))

        if niv == 'levels/map5.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))
            else:
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png")
                    screen.blit(image, (-50, 125))

                if compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png")
                    screen.blit(image, (-50, 125))

        if niv == 'levels/map6.txt':
            self.coups = len(self.chemin[0])
            if self.chemin == [] or self.coups == 0:
                print("barvo vous avez battu le robot")
                if monde == 2:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 3:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

                elif monde == 4:
                    image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                    screen.blit(image, (0, 0))

                else:
                    image = pygame.image.load("etoiles/etoile3.png")
                    screen.blit(image, (-50, 125))

            else:
                print("Nope, maybe next time")
                if compteur <= self.coups:
                    if monde == 2:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 3:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                    elif monde == 4:
                        image = pygame.image.load("etoiles/monde_hero/etoile3.png")
                        screen.blit(image, (0, 0))

                    else:
                        image = pygame.image.load("etoiles/etoile3.png")
                        screen.blit(image, (-50, 125))

                elif self.coups < compteur < self.coups + 8:
                    image = pygame.image.load("etoiles/etoile2.png")
                    screen.blit(image, (-50, 125))

                if compteur > self.coups + 8:
                    image = pygame.image.load("etoiles/etoile1.png")
                    screen.blit(image, (-50, 125))

        for i in range(1, 6):
            if niv == 'sauvegarde/sauvegarde' + str(i) + '/partie' + str(i) + '.txt':
                with open('sauvegarde/sauvegarde' + str(i) + '/scores.txt', 'r') as fichier:
                    lire = [l for l in fichier]

                cpt = int(lire[0])

                if cpt + compteur < 25:
                    image = pygame.image.load("etoiles/etoile3.png").convert()
                    screen.blit(image, (-50, 125))
                elif 25 < cpt + compteur < 30:
                    image = pygame.image.load("etoiles/etoile2.png").convert()
                    screen.blit(image, (-50, 125))
                if cpt + compteur > 30:
                    image = pygame.image.load("etoiles/etoile1.png").convert()
                    screen.blit(image, (-50, 125))

        screen.blit(image7, image7_rect)  # dessin des images a lécran
        screen.blit(next_button, next_button_rect)

        # ajout du texte
        draw_text('CliQuez sur la fleche pour revenir au menu ', font, color, screen, 470, 215)
        pygame.display.flip()
