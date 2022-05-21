import os
import pygame


#ecran = pygame.display.set_mode((300, 200))

class gameclass():

    def __init__(self):
        pygame.init()
        self.directory_pics = "./charas"
        self.number_of_pics = len([item for item in os.listdir(self.directory_pics) if os.path.isfile(os.path.join(self.directory_pics, item))])

        #self.ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ecran = pygame.display.set_mode((600, 200), pygame.RESIZABLE)
        self.surface = pygame.display.get_surface() #get the surface of the current active display


        #--- Nombre d'images par rangée
        self.pics_per_row = 6

        #--- Décalage par rapport au bords de l'écran
        self.vertical_border_padding_percentage = 10
        self.horizontal_border_padding_percentage = 10

        self.vertical_border_padding = int(self.surface.get_height()/100 * self.vertical_border_padding_percentage)
        self.horizontal_border_padding = int(self.surface.get_width()/100 * self.horizontal_border_padding_percentage)

        #---- Espacement des cartes
        self.vertical_padding_percentage = 5
        self.horizontal_padding_percentage = 3

        self.vertical_padding = int(self.surface.get_height()/100 * self.vertical_padding_percentage)
        self.horizontal_padding = int(self.surface.get_width()/100 * self.horizontal_padding_percentage)

        print(self.surface.get_width(), self.surface.get_height()) #create an array of surface.width and surface.height
        

    def playing(self, playername):


        while True:
            mouseX, mouseY = pygame.mouse.get_pos()
            print(mouseX, mouseY)

            #--- Display the background
            background = pygame.image.load("./res/background.png").convert_alpha()
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height())) 
            self.ecran.blit(background, (0,0))          

            #--- Display the characters
            counter = 0
            x = self.horizontal_border_padding + int((self.surface.get_width() - self.horizontal_border_padding)/self.pics_per_row)
            y = self.vertical_border_padding
            
            for filename in os.listdir(self.directory_pics):
                character = pygame.image.load(self.directory_pics + "/" + filename).convert_alpha()
                character = pygame.transform.scale(character, (int(95 * self.surface.get_width()/1920), int(175 * self.surface.get_height()/1080) ))
                self.ecran.blit(character, (x,y))
                x += character.get_width() + self.horizontal_padding
                counter += 1

                if x > (self.surface.get_width() - self.horizontal_border_padding) - character.get_width() or counter == self.pics_per_row:
                    y += character.get_height() + self.vertical_padding
                    x = self.horizontal_border_padding + int((self.surface.get_width() - self.horizontal_border_padding)/self.pics_per_row)
                    counter = 0


            #--- Refresh the display
            for event in pygame.event.get():
                pygame.display.flip()
        pygame.quit()

my_game = gameclass()
my_game.playing("Mash")


