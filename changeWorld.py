import pygame
import sys
import launcher
import menuSelection as ms


class World:
    def __init__(self):
        self.decision = 0

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def world(self):
        screen = pygame.display.set_mode((1080, 720))
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                running = False

            if running:
                mx, my = pygame.mouse.get_pos()

                # placer et afficher les boutons
                button_1 = pygame.Rect(200, 100, 200, 200)
                button_2 = pygame.Rect(200, 455, 200, 200)
                button_3 = pygame.Rect(700, 100, 200, 200)
                button_4 = pygame.Rect(700, 455, 200, 200)

                button_7 = pygame.Rect(460, 65, 150, 80)  # 905
                boutton_8 = pygame.Rect(950, 40, 150, 80)

                image1 = pygame.image.load('PNG/HHHHH.png')
                image2 = pygame.image.load('PNG/WolrdMario.png')
                image3 = pygame.image.load('PNG/pacmanBk.png')
                image4 = pygame.image.load('PNG/heroworld.gif')

                # yanis ajout boutton retour
                image7 = pygame.image.load('PNG/bouttonRetour.png')
                image7 = pygame.transform.scale(image7, (170, 55))
                # ajout pour mute la musique
                couperSonSelect = pygame.image.load("PNG/couperSonSelect.png")
                couperSonSelect = pygame.transform.scale(couperSonSelect, (50, 50))

                fond = pygame.image.load("PNG/menufond.jpg")

                screen.blit(fond, (0, 0))
                screen.blit(image1, button_1)
                screen.blit(image2, button_2)
                screen.blit(image3, button_3)
                screen.blit(image4, button_4)

                screen.blit(image7, button_7)
                screen.blit(couperSonSelect, boutton_8)

                # afficher le nom des niveaux :

                font = pygame.font.Font('8-BIT WONDER.TTF', 15)
                color = (255, 255, 255)
                self.draw_text('Choisissez votre monde', font, color, screen, 407, 5)
                self.draw_text('monde 1', font, color, screen, 230, 320)
                self.draw_text('monde 2', font, color, screen, 230, 430)
                self.draw_text('monde 3', font, color, screen, 730, 320)
                self.draw_text('monde 4', font, color, screen, 730, 430)

                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                # Lance le niveau 1
                if button_1.collidepoint((mx, my)):
                    if click:
                        ms.levels(screen, monde1())

                # Lance le niveau 2
                if button_2.collidepoint((mx, my)):
                    if click:
                        ms.levels(screen, monde2())

                # Lance le niveau 3
                if button_3.collidepoint((mx, my)):
                    if click:
                        ms.levels(screen, monde3())

                # Lance le niveau 4
                if button_4.collidepoint((mx, my)):
                    if click:
                        ms.levels(screen, monde4())

                # retour au menu principal
                if button_7.collidepoint((mx, my)):
                    if click:
                        launcher.lancement()
                if boutton_8.collidepoint((mx, my)):
                    if click:
                        pygame.mixer.music.pause()

            pygame.display.update()

def monde1():
    world = 1
    return world


def monde2():
    world = 2
    return world


def monde3():
    world = 3
    return world


def monde4():
    world = 4
    return world
