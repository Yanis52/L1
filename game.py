from menu import *
import menuSelectionSaves as Mss
from changeWorld import World


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False      #déclaration des self.running toujours vrai , et le .playing qui se met en True lors du click sur le boutton Start.
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False   #declaration des touches de navigations dont on aura besoin pour le menu initiallement en False
        self.DISPLAY_W, self.DISPLAY_H = 1080, 720   #taille d"ecran
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))  #fenetre
        self.font_name = '8-BIT WONDER.TTF'   #import de la police style "minecraft :)"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)   #definir les différentes couleurs noir et blanc
        self.main_menu = MainMenu(self)  #on ramene le mainMenu
        self.Commandes = CommandesMenu(self)   # ''''''''' les commandes et les credits
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        # ajout Yenni
        self.fond = pygame.image.load('PNG/fond.png')

    def game_loop(self):  #boucle du jeu

        while self.playing:  #tant que le jeu est ouvert
            keys = pygame.key.get_pressed()

            if keys[pygame.K_BACKSPACE]: #si on appuie sur backspace
                self.playing = False
            else:
                self.check_events()
                if self.START_KEY:
                    self.playing = False
                else:
                    self.display.blit(self.fond, (0, 0))  #charger le font
                    self.window.blit(self.display, (0, 0))  #appeler le fond
                    if self.main_menu.state == 'Charger une partie':  #appeler la sauvegarde
                        Mss.savespartie(self.window, 1)
                    if self.main_menu.state == 'Start':
                        World().world()
                    if self.main_menu.state == 'Commandes':
                        self.background = pygame.image.load('PNG/commandesbackground.png')
                        self.display.blit(self.background, (0, 0))
                        self.window.blit(self.display,(0,0))
                    if self.main_menu.state == 'Credits':
                        self.background = pygame.image.load('PNG/creditsBackgroundm.png')
                        self.display.blit(self.background, (0, 0))
                        self.window.blit(self.display, (0, 0))

                self.reset_keys()  #renitialiser nos clefs a false

    win = pygame.display.set_mode((1080, 720))
    win.fill((255, 255, 255))
    pygame.mixer.init()  #import musique du jeu
    pygame.mixer.music.load('sound/musique_jeu.ogg')
    pygame.mixer.music.play(-1)  #pour la jouer en boucle

    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("sokoban")

    def check_events(self):   #Fonction qui verifie les entrés et les bouttons sur lesquels on appuie
        for event in pygame.event.get(): #recup des evenements
            if event.type == pygame.QUIT:   #si on ferme la fenetre
                self.running, self.playing = False, False  #mettre en false les fonctions initialements misent en True plus haut
                self.curr_menu.run_display = False   #on arette le menu
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  #si ont apuie sur entrer
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:  #si on appuie sur back space
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:  #si on appuie sur fleche du bas
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:   #si on appuie sur fleche du haut
                    self.UP_KEY = True

    def reset_keys(self):  #on renitialise les variables on appel cette fonction a la fin de la boucle plus haut
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):     #fonction qui permet d'afficher le texte a l'écran
        font = pygame.font.Font(self.font_name, size)  #le font du texte

        # modifier par Yenni:
        text_surface = font.render(text, True, self.BLACK) #couleur noire
        text_rect = text_surface.get_rect()   #recuperer le rectangle du texte
        text_rect.center = (x, y)    #le positonner
        self.display.blit(text_surface, text_rect)  #l'afficher "dessinner
