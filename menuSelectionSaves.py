import pygame, sys, os
import launcher


# Setup pygame/window ---------------------------------------- #

from pygame.locals import *

pygame.init()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def savespartie(screen, monde):
    running = True
    while running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            running = False

        if running == True:
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

            image1 = pygame.image.load('PNG/niveau1.png')
            image2 = pygame.image.load('PNG/niveau2.png')
            image3 = pygame.image.load('PNG/niveau3.png')
            image4 = pygame.image.load('PNG/niveau4.png')
            image5 = pygame.image.load('PNG/niveau5.png')
            image6 = pygame.image.load('PNG/niveau1.png')
            image7 = pygame.image.load('PNG/bouttonRetour.png')
            image7 = pygame.transform.scale(image7, (170, 55))
            fond = pygame.image.load("PNG/menufond.jpg")
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
            draw_text('Vos Sauvegardes', font, color, screen, 407, 5)
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
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)

            # Lance le niveau 2
            if button_2.collidepoint((mx, my)):
                if click:
                    file = niveau2()
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)

            # Lance le niveau 3
            if button_3.collidepoint((mx, my)):
                if click:
                    file = niveau3()
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)

            # Lance le niveau 4
            if button_4.collidepoint((mx, my)):
                if click:
                    file = niveau4()
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)

            # Lance le niveau 5
            if button_5.collidepoint((mx, my)):
                if click:
                    file = niveau5()
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)

            # Lance le niveau 6
            if button_6.collidepoint((mx, my)):
                if click:
                    file = niveau6()
                    if not os.path.exists(file):
                        draw_text("Vous n avez pas de sauvegarde de ce niveau", font, color, screen, 240, 360)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    else:
                        launcher.main(screen, file, monde)
            # retour au menu principal
            if button_7.collidepoint((mx, my)):
                if click:
                    launcher.lancement()
            if boutton_8.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.pause()
                   


        pygame.display.flip()

def niveau1():
    file = 'sauvegarde/sauvegarde1/partie1.txt'
    return file

def niveau2():
    file = 'sauvegarde/sauvegarde2/partie2.txt'
    return file

def niveau3():
    file = 'sauvegarde/sauvegarde3/partie3.txt'
    return file

def niveau4():
    file = 'sauvegarde/sauvegarde4/partie4.txt'
    return file

def niveau5():
    file = 'sauvegarde/sauvegarde5/partie5.txt'
    return file

def niveau6():
    file = 'sauvegarde/sauvegarde6/partie6.txt'
    return file
