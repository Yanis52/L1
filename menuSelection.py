import pygame
import sys
import launcher
from changeWorld import World

# Setup pygame/window ---------------------------------------- #

from pygame.locals import *

pygame.init()


class Texture:
    def __init__(self):
        pass

    def choix(self, monde):
        if monde == 1:
            Vide = pygame.image.load('PNG/Defaultsize/Ground/ground_06.png').convert_alpha()
            obstacle = pygame.image.load('PNG/Defaultsize/Blocks/block_01.png').convert_alpha()
            objectif = pygame.image.load('PNG/Defaultsize/Ground/ground_04.png').convert_alpha()
            caisse = pygame.image.load('PNG/Defaultsize/Crates/crate_02.png').convert_alpha()
            point = pygame.image.load('PNG/Defaultsize/Crates/crate_06.png').convert_alpha()

            decor8 = pygame.image.load('PNG/Defaultsize/Crates/crate_23.png').convert_alpha()

            left = pygame.image.load("PNG/Defaultsize/Player/player_02.png").convert_alpha()
            right = pygame.image.load("PNG/Defaultsize/Player/player_01.png").convert_alpha()
            down = pygame.image.load("PNG/Defaultsize/Player/player_11.png").convert_alpha()
            up = pygame.image.load("PNG/Defaultsize/Player/player_14.png").convert_alpha()
            return Vide, obstacle, objectif, caisse, point, decor8, left, right, down, up

        # monde mario
        if monde == 2:
            Vide = pygame.image.load('PNG/monde_mario/ground_01.png').convert_alpha()
            obstacle = pygame.image.load('PNG/monde_mario/testtt.PNG').convert_alpha()
            objectif = pygame.image.load('PNG/monde_mario/marioObjF.png').convert_alpha()
            caisse = pygame.image.load('PNG/monde_mario/mario_caisses.jpg').convert_alpha()
            point = pygame.image.load('PNG/monde_mario/Mario_OjectifFINALE.png').convert_alpha()

            decor8 = pygame.image.load('PNG/monde_mario/mario_murfinal2.png').convert_alpha()

            left = pygame.image.load('PNG/monde_mario/mario_haut.gif').convert_alpha()
            right = pygame.image.load('PNG/monde_mario/mario_bas.gif').convert_alpha()
            down = pygame.image.load('PNG/monde_mario/mario_droite.gif').convert_alpha()
            up = pygame.image.load('PNG/monde_mario/mario_gauche.gif').convert_alpha()
            return Vide, obstacle, objectif, caisse, point, decor8, left, right, down, up

        # monde pacman
        if monde == 3:
            Vide = pygame.image.load('PNG/monde_packman/bg.png').convert_alpha()
            obstacle = pygame.image.load('PNG/monde_packman/pacmanmurbleu.png').convert_alpha()

            objectif = pygame.image.load('PNG/monde_packman/objectifPMNoir.png').convert_alpha()
            caisse = pygame.image.load('PNG/monde_packman/fantome.png').convert_alpha()
            point = pygame.image.load('PNG/monde_packman/atteint.png').convert_alpha()

            decor8 = pygame.image.load('PNG/monde_packman/pacmanmur2.PNG').convert_alpha()

            left = pygame.image.load('PNG/monde_packman/persoPacmanhaut.png').convert_alpha()
            right = pygame.image.load('PNG/monde_packman/persoPacmanbas.png').convert_alpha()
            down = pygame.image.load('PNG/monde_packman/persoPacmandroite.png').convert_alpha()
            up = pygame.image.load('PNG/monde_packman/persoPacmangauche.png').convert_alpha()
            return Vide, obstacle, objectif, caisse, point, decor8, left, right, down, up

        # monde HERO
        if monde == 4:
            Vide = pygame.image.load('PNG/monde_hero/backpropre.png').convert_alpha()
            obstacle = pygame.image.load('PNG/Defaultsize/Blocks/block_01.png').convert_alpha()

            objectif = pygame.image.load('PNG/monde_hero/objectif.png').convert_alpha()
            caisse = pygame.image.load('PNG/monde_hero/HEROcaisset.png').convert_alpha()
            point = pygame.image.load('PNG/monde_hero/caisse_ok.jpg').convert_alpha()

            decor8 = pygame.image.load('PNG/monde_hero/caisse_ok.jpg').convert_alpha()

            left = pygame.image.load('PNG/monde_hero/hautt.png').convert_alpha()
            right = pygame.image.load('PNG/monde_hero/bast.png').convert_alpha()
            down = pygame.image.load('PNG/monde_hero/droitet.png').convert_alpha()
            up = pygame.image.load('PNG/monde_hero/gauchet.png').convert_alpha()

            return Vide, obstacle, objectif, caisse, point, decor8, left, right, down, up


def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


click = False


def levels(screen, monde):
    running = True
    while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                running = False

            if running:
                mx, my = pygame.mouse.get_pos()

            # placer et afficher les boutons
                button_1 = pygame.Rect(200, 25, 200, 200)
                button_2 = pygame.Rect(200, 255, 200, 200)
                button_3 = pygame.Rect(200, 495, 200, 200)
                button_4 = pygame.Rect(700, 25, 200, 200)
                button_5 = pygame.Rect(700, 255, 200, 200)
                button_6 = pygame.Rect(700, 495, 200, 200)
                button_7 = pygame.Rect(460, 65, 150, 80)
                boutton_8 = pygame.Rect(950, 40, 150, 80)

                # monde pour mario
                if monde == 2:
                    image1 = pygame.image.load('PNG/monde_mario/niveau_1.PNG')
                    image2 = pygame.image.load('PNG/monde_mario/niveau_2.PNG')
                    image3 = pygame.image.load('PNG/monde_mario/niveau_3c.png')
                    image4 = pygame.image.load('PNG/monde_mario/niveau_4.PNG')
                    image5 = pygame.image.load('PNG/monde_mario/niveau_5.PNG')
                    image6 = pygame.image.load('PNG/monde_mario/niveau_6c.png')
                    fond = pygame.image.load("PNG/marioBackGroundChoise.jpg")


                # monde pour pacman
                elif monde == 3:
                    image1 = pygame.image.load('PNG/monde_packman/niveau_1.PNG')
                    image2 = pygame.image.load('PNG/monde_packman/niveau_2.PNG')
                    image3 = pygame.image.load('PNG/monde_packman/niveau_3.PNG')
                    image4 = pygame.image.load('PNG/monde_packman/niveau_4.PNG')
                    image5 = pygame.image.load('PNG/monde_packman/niveau_5.PNG')
                    image6 = pygame.image.load('PNG/monde_packman/niveau_6.PNG')
                    fond = pygame.image.load("PNG/blackFont.png")


                # monde aventurier
                elif monde == 4:
                    image1 = pygame.image.load('PNG/monde_hero/niveau_1.PNG')
                    image2 = pygame.image.load('PNG/monde_hero/niveau_2.PNG')
                    image3 = pygame.image.load('PNG/monde_hero/niveau_3.PNG')
                    image4 = pygame.image.load('PNG/monde_hero/niveau_4C.png')
                    image5 = pygame.image.load('PNG/monde_hero/niveau_5.PNG')
                    image6 = pygame.image.load('PNG/monde_hero/niveau_6.PNG')
                    fond = pygame.image.load("PNG/avnture back gorund 4choise.png")

                else:
                    # monde par défaut (celui de l'entrepot)
                    image1 = pygame.image.load('PNG/niveau_1.PNG')
                    image2 = pygame.image.load('PNG/niveau_2.PNG')
                    image3 = pygame.image.load('PNG/niveau_3.PNG')
                    image4 = pygame.image.load('PNG/niveau_4.PNG')
                    image5 = pygame.image.load('PNG/niveau_5.PNG')
                    image6 = pygame.image.load('PNG/niveau_6.PNG')

                    fond = pygame.image.load("PNG/menufond.jpg")

                # yanis ajout boutton retour
                image7 = pygame.image.load('PNG/bouttonRetour.png')
                image7 = pygame.transform.scale(image7, (170, 55))

                # ajout pour mute la musique
                couperSonSelect = pygame.image.load("PNG/couperSonSelect.png")
                couperSonSelect = pygame.transform.scale(couperSonSelect, (50, 50))

                screen.blit(fond, (0, 0))
                screen.blit(image1, button_1)
                screen.blit(image2, button_2)
                screen.blit(image3, button_3)
                screen.blit(image4, button_4)
                screen.blit(image5, button_5)
                screen.blit(image6, button_6)
                screen.blit(image7, button_7)
                screen.blit(couperSonSelect, boutton_8)

            # afficher le nom des niveaux :

                font = pygame.font.Font('8-BIT WONDER.TTF', 15)
                color = (255, 255, 255)
                draw_text('Selection des niveaux', font, color, screen, 407, 5)
                draw_text('niveau 1', font, color, screen, 230, 230)
                draw_text('niveau 2', font, color, screen, 230, 465)
                draw_text('niveau 3', font, color, screen, 230, 695)
                draw_text('niveau 4', font, color, screen, 730, 230)
                draw_text('niveau 5', font, color, screen, 730, 465)
                draw_text('niveau 6', font, color, screen, 730, 695)

                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                # Lance le niveau 1
                if button_1.collidepoint((mx, my)):
                    if click:
                        file = niveau1()
                        launcher.main(screen, file, monde)

                # Lance le niveau 2
                if button_2.collidepoint((mx, my)):
                    if click:
                        file = niveau2()
                        launcher.main(screen, file, monde)

                # Lance le niveau 3
                if button_3.collidepoint((mx, my)):
                    if click:
                        file = niveau3()
                        launcher.main(screen, file, monde)

                # Lance le niveau 4
                if button_4.collidepoint((mx, my)):
                    if click:
                        file = niveau4()
                        launcher.main(screen, file, monde)

                # Lance le niveau 5
                if button_5.collidepoint((mx, my)):
                    if click:
                        file = niveau5()
                        launcher.main(screen, file, monde)

                # Lance le niveau 6
                if button_6.collidepoint((mx, my)):
                    if click:
                        file = niveau6()
                        launcher.main(screen, file, monde)

                # retour au menu principal
                if button_7.collidepoint((mx, my)):
                    if click:
                        World().world()
                if boutton_8.collidepoint((mx, my)):
                    if click:
                        pygame.mixer.music.pause()

            pygame.display.update()


def niveau1():
    file = 'levels/map1.txt'
    return file


def niveau2():
    file = 'levels/map2.txt'
    return file


def niveau3():
    file = 'levels/map3.txt'
    return file


def niveau4():
    file = 'levels/map4.txt'
    return file


def niveau5():
    file = 'levels/map5.txt'
    return file


def niveau6():
    file = 'levels/map6.txt'
    return file
