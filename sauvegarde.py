from grille import Grille
from player import Joueur
import pygame
import os


def sauvegarde(n, niveau, compteur, file, monde):
    """ Cette fonction permet de sauvegarder la partie en cours """
    g = Grille(file, monde)
    j = Joueur(file, monde)

    if not os.path.exists('sauvegarde/sauvegarde' + str(n)):
        os.mkdir('sauvegarde/sauvegarde' + str(n))

    # création du nouveau fichier:
    save = open('sauvegarde/sauvegarde' + str(n) + '/partie' + str(n) + '.txt', 'w')
    for lin in range(len(niveau)):
        for col in range(len(niveau[lin])):
            save.write(str(niveau[lin][col]))
        save.write('\n')
    save.close()

    # création du fichier qui va contenir nos scores
    save2 = open('sauvegarde/sauvegarde' + str(n) + '/scores.txt', 'w')

    # sauvegadre nombre de pas
    save2.write(str(compteur))
    save2.write('\n')

    # position personnage
    for lin in range(len(niveau)):
        for col in range(len(niveau[lin])):
            if niveau[lin][col] == 3:
                save2.write(str(j.position_joueur(niveau)))
    save2.write('\n')

    # position caisses
    save2.write(str(g.caisses_pos(niveau)))
    save2.write('\n')

    # pour sauvegarder une donnée créer à chaque fois un nouveau fichier texte
    save2.close()

    # création d'un fichier .txt qui va sauvegarder les coordonnées des objectifs
    save3 = open('sauvegarde/sauvegarde' + str(n) + '/coordonnees_objectifs.txt', 'w')
    if file == 'sauvegarde/sauvegarde' + str(n) + '/partie' + str(n) + '.txt':
        with open(file, 'r') as fichier:
            niveau = [[int(l) for l in ligne.strip()] for ligne in fichier]
        for lin in range(len(niveau)):
            for col in range(len(niveau[lin])):
                if niveau[lin][col] == 2 or niveau[lin][col] == 6:
                    save3.write(str(lin))
                    save3.write(str(col))
                save3.write('\n')

        # ouvre le fichier contenant l'historique des objectifs
        with open('sauvegarde/sauvegarde' + str(n) + '/coordonnees_objectifs.txt', 'r') as fichier:
            lire = [l for l in fichier]
        for i in range(0, len(lire)):
            x = int(lire[i][0])
            y = int(lire[i][1])
            if (j.position_joueur(niveau)[0], j.position_joueur(niveau)[1]) == (x, y):
                save3.write(str(j.position_joueur(niveau)[0]))
                save3.write(str(j.position_joueur(niveau)[1]))
                save3.write('\n')
    else:
        for (x, y) in g.objectifs():
            save3.write(str(x))
            save3.write(str(y))
            if (j.position_joueur(niveau)[0], j.position_joueur(niveau)[1]) in g.objectifs():
                save3.write(str(x))
                save3.write(str(y))
            save3.write('\n')
    save3.close()

    # création d'un fichier qui va retenir coordonnées des caisses
    save4 = open('sauvegarde/sauvegarde' + str(n) + '/coordonnees_caisses.txt', 'w')
    for (x, y) in g.caisses_pos(niveau):
        save4.write(str(x))
        save4.write(str(y))
        save4.write('\n')
    save4.close()


def chemin_sauvegarde(niveau, file, screen, monde):
    g = Grille(file, monde)
    j = Joueur(file, monde)
    if file == 'levels/map1.txt' or file == 'sauvegarde/sauvegarde1/partie1.txt':
        g.n = 1
        sauvegarde(1, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)

    if file == 'levels/map2.txt' or file == 'sauvegarde/sauvegarde2/partie2.txt':
        sauvegarde(2, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)

    if file == 'levels/map3.txt' or file == 'sauvegarde/sauvegarde3/partie3.txt':

        sauvegarde(3, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)

    if file == 'levels/map4.txt' or file == 'sauvegarde/sauvegarde4/partie4.txt':
        sauvegarde(4, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)

    if file == 'levels/map5.txt' or file == 'sauvegarde/sauvegarde5/partie5.txt':
        sauvegarde(5, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)

    if file == 'levels/map6.txt' or file == 'sauvegarde/sauvegarde6/partie6.txt':
        sauvegarde(6, niveau, j.compteur, file, monde)
        font = pygame.font.Font('8-BIT WONDER.TTF', 15)
        screen.blit(font.render('sauvegarde en cours ...', True, (0, 0, 0)), (775, 10))
        pygame.display.flip()
        pygame.time.delay(2000)
