
import sys
import pygame
import random
pygame.init()

class game:
    def __init__(self):
        self.ecran= pygame.display.set_mode((800,600)) # taille fenetre
        pygame.display.set_caption('Snake')  # nom de la fenetre
        self.game_on = True

        self.position_snake_x = 300
        self.position_snake_y = 300
        self.direction_snake_x = 0
        self.direction_snake_y = 0
        self.serpent = 16

        self.position_pomme_x = random.randrange(110,690,10)
        self.position_pomme_y = random.randrange(110,590,10)
        self.pomme = 10
        
        self.clock = pygame.time.Clock()

        self.positions_snake = []

        self.taille_serpent = 1

        self.acceuil = True

        # images 
        self.image = pygame.image.load('snake-game.jpg')
        self.image_t= pygame.transform.scale(self.image,(400,200))

        self.img_tete = pygame.image.load('tete_serpent.png')
        self.img_pomme = pygame.image.load('pomme.png')
        
        self.score = 0 



    def f(self):

        def reload(self):
                self.position_snake_x = 300
                self.position_snake_y = 300
                self.direction_snake_x = 0
                self.direction_snake_y = 0
                self.serpent = 16

                self.position_pomme_x = random.randrange(110,690,10)
                self.position_pomme_y = random.randrange(110,590,10)
                self.pomme = 15
            
                self.clock = pygame.time.Clock()

                self.positions_snake = []

                self.taille_serpent = 1

                self.score = 0 
                

        while self.acceuil:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: #ferme la fenetre
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        self.game_on= True
                        self.acceuil = False
                        reload(self)
                        
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                
                # couleur de fond acceuil
                self.ecran.fill((0,0,0))

                #image jeu snake
                self.ecran.blit(self.image_t,(200,20,100,50))
                
                #messages sur ecran d'acceuil
                self.ecriture("grande","Bienvenue sur mon jeu Snake",(0,255,0),(170,300,200,5))
                self.ecriture("petite","Déplacer vous à l'aide des flèches pour manger les pommes et faire grandir votre serpent !",(240,240,240), (130,350,200,5))
                self.ecriture("grande","Appuyer sur Entrée pour commencer" ,(255,255,255),(130,450,200,5) )
                
                pygame.display.flip()

        while self.game_on: #tant que le jeu est en cours

           
            for e in pygame.event.get():
                if e.type == pygame.QUIT: #ferme la fenetre
                    sys.exit()
                

                # control du serpent
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT: #fleche droite
                        self.direction_snake_x = 10
                        self.direction_snake_y = 0
                    
                    if e.key == pygame.K_LEFT: #fleche gauche
                        self.direction_snake_x = -10
                        self.direction_snake_y = 0

                    if e.key == pygame.K_DOWN: #fleche du bas
                        self.direction_snake_x = 0
                        self.direction_snake_y = 10
                    
                    if e.key == pygame.K_UP: #fleche du haut
                        self.direction_snake_x = 0
                        self.direction_snake_y = -10

                    if e.key == pygame.K_ESCAPE: # touche echap
                        self.acceuil = True
                        self.f()
                   
                        

            

            tete_serpent = []
            tete_serpent.append(self.position_snake_x)
            tete_serpent.append(self.position_snake_y)

            self.positions_snake.append(tete_serpent)

            if len(self.positions_snake) > self.taille_serpent:
                self.positions_snake.pop(0)

            # quitte le jeu si serpent est hors limites
            if self.position_snake_x <= 90 or self.position_snake_x >= 690 or self.position_snake_y <= 80 or self.position_snake_y >= 580:
                self.acceuil = True
                self.f()
                
                
            self.position_snake_x += self.direction_snake_x
            self.position_snake_y += self.direction_snake_y

            
            # si serpent mange pomme
            if self.position_pomme_y == self.position_snake_y and self.position_pomme_x == self.position_snake_x:
               
                #pomme change de place
                self.position_pomme_x = random.randrange(100,580,10)
                self.position_pomme_y = random.randrange(90,570,10)
                
                self.taille_serpent += 1
                self.score += 1

             # si le serpent se touche lui meme
            for p in self.positions_snake[:-1]:
                if tete_serpent == p:
                    self.acceuil = True
                    self.f() 
            
    
            # change couleur fond
            self.ecran.fill((0,0,0)) 
            
            
            # affiche images
            self.ecran.blit(self.img_pomme,(self.position_pomme_x,self.position_pomme_y,self.pomme,self.pomme))
            self.ecran.blit(self.img_tete,(self.position_snake_x,self.position_snake_y,self.serpent,self.serpent))

            for p in self.positions_snake:
                pygame.draw.rect(self.ecran, (0,255,0),(p[0],p[1],self.serpent,self.serpent))

           
           
            # affiche score 
            self.ecriture("grande","Score : ",(255,255,255),(320,10,10,50))
            self.ecriture("grande", '{}'.format(str(self.score)),(255,255,255),(450,10,50,50))
            
            self.clock.tick(15)
            self.limites()
            pygame.display.flip()


    # limites du jeu
    def limites(self):
        pygame.draw.rect(self.ecran,(0,255,255),(90,80,600,500),2)


    # types écritures
    def ecriture(self,font,message,couleur,message_rect):
        if font == "petite":
            font = pygame.font.SysFont('Lato',20,False)
        elif font == "grande":
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)
        self.ecran.blit(message,message_rect)
    

if __name__== '__main__':

    pygame.init()
    game().f()
    pygame.quit()



