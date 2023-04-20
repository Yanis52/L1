import pygame
import sys

class Menu:              #creation de la class menu
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 #stocker la hauteur /2 et la largeur /2

        self.run_affichage = True
        self.cursseur_rect = pygame.Rect(0, 0, 20, 20)  #creation du rectangle du cursseur
        self.offset = -200    #decalage entre le curseur et le texte (<0 pour gauche)


    def cursseurEtoile(self):  #Affectation du curseur , ici une "*"

        self.game.draw_text("*", 15, self.cursseur_rect.x, self.cursseur_rect.y)




    def afficherLecran(self):  #pour ne pas tomber dans la redoncance de code on stock tout dans cette fonction
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):  #creation de la class du menu principal
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"   # quand le menu demare le curseur apparait a cette endroit
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.commandesx, self.commandesy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90    #Gestion des positions
        self.partiex, self.partiey = self.mid_w, self.mid_h + 120
        self.quitterx, self.quittery = self.mid_w, self.mid_h + 150
        self.cursseur_rect.midtop = (self.startx + self.offset, self.starty) #assigner une position de depart au curseur notamenet celle du start

        # ajouter par Yenni
        self.background = pygame.image.load('PNG/interieur.jpg')

    def display_menu(self):  #pour afficher a l'écran le menu
        self.run_affichage = True
        while self.run_affichage:     #Tant que sa fonctionne
            self.game.check_events() #pour le deplacement du curseur on appel la fonction qui verifie les events
            self.check_input()  #fonction plus  bas

            # Yenni ajout
            #on affiche ce qu'on souhaite avec des draw text
            self.game.display.blit(self.background, (0, 0))
            self.game.draw_text('Menu sokoban', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text(" Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Commandes", 20, self.commandesx, self.commandesy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Charger une partie", 20, self.partiex, self.partiey)
            self.game.draw_text("Quitter vers le bureau", 20, self.quitterx, self.quittery)
            self.cursseurEtoile()  #afficher le curseur
            self.afficherLecran() #aficher le tout


    def deplacementCurseur(self):   #deplacmeent du curseur
        if self.game.DOWN_KEY:   # si on clique sut flèche du bas
            if self.state == 'Start':     #on verifie l'etat (l'emplacement du curseur au moment du clik)
                self.cursseur_rect.midtop = (self.commandesx + self.offset, self.commandesy)   #ajuster le curseur plus bas de 1
                self.state = 'Commandes' #réajustement
            elif self.state == 'Commandes':
                self.cursseur_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursseur_rect.midtop = (self.partiex + self.offset, self.partiey)
                self.state = 'Charger une partie'
            elif self.state == 'Charger une partie':
                self.cursseur_rect.midtop = (self.quitterx + self.offset, self.quittery)
                self.state = 'Quitter vers le bureau'
            elif self.state == 'Quitter vers le bureau':
                self.cursseur_rect.midtop = (self.startx + self.offset, self.starty) #on repositionne le curseur au début ainsi de suite
                self.state = 'Start'

        elif self.game.UP_KEY:  # si on clique sut flèche du Haut
            if self.state == 'Start':    #meme principe qu en haut
                self.cursseur_rect.midtop = (self.quitterx + self.offset, self.quittery)
                self.state = 'Quitter vers le bureau'
            elif self.state == 'Commandes':
                self.cursseur_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursseur_rect.midtop = (self.commandesx + self.offset, self.commandesy)
                self.state = 'Commandes'
            elif self.state == 'Charger une partie':
                self.cursseur_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Quitter vers le bureau':
                self.cursseur_rect.midtop = (self.partiex + self.offset, self.partiey)
                self.state = 'Charger une partie'

    def check_input(self):
        self.deplacementCurseur()   #on verifie sur le joueur déplace le cursseur et si il sélectionne l'un des menus
        if self.game.START_KEY:
            if self.state == 'Start':   #si on appuie sur lancer une partie
                self.game.playing = True

            elif self.state == 'Commandes':    #si on rentre dans les commandes
                self.game.curr_menu = self.game.Commandes

            elif self.state == 'Credits': # '' '' ''  ' '''  ''  les crédits
                self.game.curr_menu = self.game.credits

            elif self.state == 'Charger une partie':   #si on charge la partie
                self.game.playing = True

            elif self.state == 'Quitter vers le bureau':   #si on veut quitter
                sys.exit()
            self.run_affichage = False


class CommandesMenu(Menu): #interface commandes
    def __init__(self, game):
        Menu.__init__(self, game)  #héritage du menu


    def display_menu(self):
        self.run_affichage = True
        while self.run_affichage:
            self.background = pygame.image.load('PNG/commandesbackground.png')
            self.game.check_events()     #meme fonctionement
            self.check_input()
            self.game.display.blit(self.background, (0, 0))
            self.afficherLecran()
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_affichage = False      #retour au menu principal quand on clique sur backspace
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            #if self.state == 'Volume':
            self.state = 'Controls'





            


class CreditsMenu(Menu): #pour les crédits
    def __init__(self, game):
        Menu.__init__(self, game)

        # on afifche directement cette image
        self.background = pygame.image.load('PNG/creditsBackgroundm.png')

    def display_menu(self):
        self.run_affichage = True
        while self.run_affichage:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY: #meme principe pour revenir en arriere
                self.game.curr_menu = self.game.main_menu
                self.run_affichage = False

            
            self.game.display.blit(self.background, (0, 0))



            self.afficherLecran()
