# -*- coding: utf-8 -*-
import pygame
import sys
import math

from player import Joueur   # import de la classe Joueur
from grille import Grille   # import de la classe Grille
from grille import Texture
from game import Game
from solv import IA         # import de l'IA
from felicitation import Felicitation
import sauvegarde as sv
import menuSelection as ms
import menuSelectionSaves as mss

pygame.init()
#background1 = pygame.image.load('PNG/fond.png')
ga = Game()

screen = pygame.display.set_mode((1080, 720))


    #\------------------------------------ Début -----------------------------------------------/#


def main(screen, file, monde):
    """ cette fonction permet de lancer le niveau sélectionné """
    slv = IA(file, monde)
    g = Grille(file, monde)
    t = Texture()
    t.monde = monde
    boucle = True
    while boucle:
        if g.endgame(g.niveau):
            boucle = False
            partie(screen, file, False, monde)
        else:
            partie(screen, file, boucle, monde)
            slv.astar()


def partie(screen, file, affiche, monde):
    """ cette fonction permet de charger la partie """
    slv = IA(file, monde)
    g = Grille(file, monde)
    j = Joueur(file, monde)  # appel à la classe Joueur

    if monde == 3:
        background2 = pygame.image.load("PNG/monde_packman/bg.png")
        background1 = pygame.image.load("PNG/blackFont.png")

    elif monde == 4:
        background2 = pygame.image.load("PNG/monde_hero/backgroungpropre.png")
        background1 = pygame.image.load("PNG/avnture back gorund 4.gif")
    elif monde == 2:
        background2 = pygame.image.load("PNG/monde_mario/BACKGROUNDMARIO.png")
        background1 = pygame.image.load("PNG/marioBackGround.jpg")
    else:
        background2 = pygame.image.load("PNG/background2.png")
        background1 = pygame.image.load("PNG/fond.png")


    restartMusic = pygame.image.load("PNG/relancerMusic.png")
    couperMisuc = pygame.image.load("PNG/CouperMusic.png")
    passMusic = pygame.image.load("PNG/passSound.png")
    searchMusic = pygame.image.load("PNG/searchMusic.png")
    creditJeu = pygame.image.load("PNG/credits.png")

    autoButton = pygame.image.load("PNG/bouttonAuto.png")
    autoButton = pygame.transform.scale(autoButton, (200, 80))
    quiterButton = pygame.image.load("PNG/bouttonExit.png")
    quiterButton = pygame.transform.scale(quiterButton, (200, 80))
    levelsButton = pygame.image.load("PNG/BouttonLevels.png")
    levelsButton = pygame.transform.scale(levelsButton, (200, 80))
    restartPartie = pygame.image.load("PNG/bouttonRestart.png")
    restartPartie = pygame.transform.scale(restartPartie, (200, 80))
    saveButton = pygame.image.load("PNG/bouttonSave.png")
    saveButton = pygame.transform.scale(saveButton, (200, 80))

    menuPrincipaleButton = pygame.image.load("PNG/menuPrincipaleButton.png")
    menuPrincipaleButton = pygame.transform.scale(menuPrincipaleButton, (200, 70))

    # rcup des rect
    restartMusic_rect = restartMusic.get_rect()
    couperMisuc_rect = couperMisuc.get_rect()
    passMusic_rect = passMusic.get_rect()
    searchMusic_rect = searchMusic.get_rect()
    creditJeu_rect = creditJeu.get_rect()
    autoButton_rect = autoButton.get_rect()
    quiterButton_rect = quiterButton.get_rect()
    levelsButton_rect = levelsButton.get_rect()
    restartPartie_rect = restartPartie.get_rect()
    saveButton_rect = saveButton.get_rect()
    menuPrincipaleButton_rect = menuPrincipaleButton.get_rect()

    # on les places avec le math.ceil
    restartMusic_rect.x = math.ceil(screen.get_width() / 2.14)
    restartMusic_rect.y = math.ceil(screen.get_height() / 1.36)

    couperMisuc_rect.x = math.ceil(screen.get_width() / 1.75)
    couperMisuc_rect.y = math.ceil(screen.get_height() / 1.36)

    passMusic_rect.x = math.ceil(screen.get_width() / 1.5)
    passMusic_rect.y = math.ceil(screen.get_height() / 1.36)

    searchMusic_rect.x = math.ceil(screen.get_width() / 1.3)
    searchMusic_rect.y = math.ceil(screen.get_height() / 1.36)

    creditJeu_rect.x = math.ceil(screen.get_width() / 1.166)
    creditJeu_rect.y = math.ceil(screen.get_height() / 1.36)
    #######
    autoButton_rect.x = math.ceil(screen.get_width() / 2.166)
    autoButton_rect.y = math.ceil(screen.get_height() / 2.36)

    quiterButton_rect.x = math.ceil(screen.get_width() / 1.36)
    quiterButton_rect.y = math.ceil(screen.get_height() / 1.76)

    levelsButton_rect.x = math.ceil(screen.get_width() / 2.166)
    levelsButton_rect.y = math.ceil(screen.get_height() / 1.80)

    restartPartie_rect.x = math.ceil(screen.get_width() / 1.36)
    restartPartie_rect.y = math.ceil(screen.get_height() / 2.36)

    saveButton_rect.x = math.ceil(screen.get_width() / 1.35)
    saveButton_rect.y = math.ceil(screen.get_height() / 3.3)

    menuPrincipaleButton_rect.x = math.ceil(screen.get_width() / 2.14)
    menuPrincipaleButton_rect.y = math.ceil(screen.get_height() / 3.2)

    niveau = g.niveau

    start_time = pygame.time.get_ticks()
    while affiche:
        # capte le signal si le joueur a joué un coup ou pas
        if j.go == False:
            slv.astar()

        # pour détecter la touche
        for event in pygame.event.get():

            # pour quitter le jeu
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                screen.blit(background1, (0, 0))
                screen.blit(background2, (0, 0))
                g.affichage(niveau, screen)
                j.move(niveau, screen, 0)

            # le mini-menu lorsque on lance le niveau
            if event.type == pygame.MOUSEBUTTONDOWN:
                # boutton pour revenir au levels
                if levelsButton_rect.collidepoint(pygame.mouse.get_pos()):
                    for i in range(1, 6):
                        if file == 'sauvegarde/sauvegarde' + str(i) + 'partie' + str(i) + '.txt':
                            mss.savespartie(screen, monde)
                        if file == 'levels/map' + str(i) + '.txt':
                            ms.levels(screen, monde)

                # boutton pour replay la musique
                elif restartMusic_rect.collidepoint(event.pos):
                    pygame.mixer.music.rewind()

                # boutton pour unpause la musique
                elif passMusic_rect.collidepoint(event.pos):
                    pygame.mixer.music.unpause()

                # boutton pour les informations complémentaires
                elif searchMusic_rect.collidepoint(event.pos):
                    print("réseaux sociaux")

                # boutton pour les crédits
                elif creditJeu_rect.collidepoint(event.pos):
                    print("on affiche les credits les regles...")

                # boutton pour couper la musique
                elif couperMisuc_rect.collidepoint(event.pos):
                    pygame.mixer.music.pause()

                # boutton pour quitter
                elif quiterButton_rect.collidepoint(event.pos):
                    sys.exit()

                # boutton pour restart
                elif restartPartie_rect.collidepoint(event.pos):
                    j.recommencer(niveau)
                    start_time = pygame.time.get_ticks()

                # boutton pour lancer l'IA manuellement si jamais (à revoir vu que l'ia s'enclenche lui-même
                elif autoButton_rect.collidepoint(event.pos):
                    pass
                # boutton pour sauvegarder la partie
                elif saveButton_rect.collidepoint(event.pos):
                    sv.chemin_sauvegarde(niveau, file, screen, monde)

                # boutton pour revenir au menu principal
                elif menuPrincipaleButton_rect.collidepoint(event.pos):
                    lancement()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOLLAR]:
                for i in range(1, 6):
                    if file == 'sauvegarde/sauvegarde' + str(i) + 'partie' + str(i) + '.txt':
                        mss.savespartie(screen, monde)
                    if file == 'levels/map' + str(i) + '.txt':
                        ms.levels(screen, monde)

            # activer le robot manuellement
            if keys[pygame.K_a]:
                print(slv.astar())
                print('nombre de coups maximums : ', len(slv.astar()))

            # restart le niveau
            if keys[pygame.K_r]:
                j.recommencer(niveau)
                start_time = pygame.time.get_ticks()
                j.compteur = 0

            # quitter le jeu
            if keys[pygame.K_TAB]:
                sys.exit()

            # sauvegarder la partie
            if keys[pygame.K_w]:
                sv.chemin_sauvegarde(niveau, file, screen, monde)

        # affichage du mini-menu à droite
        if g.endgame(niveau) == False:
            if monde == 2:
                pygame.draw.rect(screen, (15, 157, 232), pygame.Rect(500, 100, 500, 500))
            elif monde == 3:
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(490, 100, 515, 515))

                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(495, 105, 505, 505))
            elif monde == 4:
                pygame.draw.rect(screen, (144,238,144), pygame.Rect(500, 100, 500, 500))
            else:
                pygame.draw.rect(screen, (251, 164, 86), pygame.Rect(500, 100, 500, 500))
        font = pygame.font.Font('8-BIT WONDER.TTF', 20)
        clock = pygame.time.Clock()

        # check si le niveau est réussi
        if g.endgame(niveau):
            restartMusic_rect.x = -99999
            restartMusic_rect.y = -99999

            couperMisuc_rect.x = -99999
            couperMisuc_rect.y = -99999

            passMusic_rect.x = -99999
            passMusic_rect.y = -99999

            searchMusic_rect.x = -99999
            searchMusic_rect.y = -99999

            creditJeu_rect.x = -99999
            creditJeu_rect.y = -99999
            #######
            autoButton_rect.x = -99999
            autoButton_rect.y = -99999

            quiterButton_rect.x = -99999
            quiterButton_rect.y = -99999

            levelsButton_rect.x = -99999
            levelsButton_rect.y = -99999

            restartPartie_rect.x = -99999
            restartPartie_rect.y = -99999

            saveButton_rect.x = -99999
            saveButton_rect.y = -99999

            menuPrincipaleButton_rect.x = -99999
            menuPrincipaleButton_rect.y = -99999
            start_time = None
            if slv.solutionIA == []:
                print("Bravo vous avez battu le robot")
                f = Felicitation(file, slv.solutionIA, j.compteur, monde)
                f.lvlcompleted(screen, monde)
                j.go = True
            else:
                f = Felicitation(file, slv.solutionIA[-1], j.compteur, monde)
                f.lvlcompleted(screen, monde)
                j.go = True

        if start_time and g.endgame(niveau) == False:
            time_since_enter = pygame.time.get_ticks() - start_time
            message = 'time : ' + str(time_since_enter // 1000) + ' seconds '
            message2 = 'Nombre de coups ' + str(j.compteur)
            if monde == 3 :
                screen.blit(font.render(message, True, (255, 255, 0)), (600, 150))
                screen.blit(font.render(message2, True, (255, 255, 0)), (600, 200))
            else:
                screen.blit(font.render(message, True, (0, 0, 0)), (600, 150))
                screen.blit(font.render(message2, True, (0, 0, 0)), (600, 200))

            screen.blit(restartMusic, restartMusic_rect)
            screen.blit(couperMisuc, couperMisuc_rect)
            screen.blit(passMusic, passMusic_rect)
            screen.blit(searchMusic, searchMusic_rect)
            screen.blit(creditJeu, creditJeu_rect)
            screen.blit(autoButton, autoButton_rect)
            screen.blit(restartPartie, restartPartie_rect)
            screen.blit(quiterButton, quiterButton_rect)
            screen.blit(saveButton, saveButton_rect)
            screen.blit(levelsButton, levelsButton_rect)
            screen.blit(menuPrincipaleButton, menuPrincipaleButton_rect)
            clock.tick(60)

        pygame.display.flip()


def lancement():
    while ga.running:
        ga.curr_menu.display_menu()
        ga.game_loop()
