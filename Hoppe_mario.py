import pygame
import sys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random
import math
pygame.init()
pygame.mixer.init()

#Lydeffekter
lydeffekt_start = pygame.mixer.Sound("mariosnakk.mp3")
lydeffekt_hopping = pygame.mixer.Sound("hopping.mp3")
lydeffekt_løping = pygame.mixer.Sound("fotsteg.mp3")
lydeffekt_sang = pygame.mixer.Sound("Super-Mario-Bros_SANG.mp3")
lydeffekt_gameover = pygame.mixer.Sound("gameover.wav")

gameover_Kanal = pygame.mixer.Channel(1)

# Får den klassiske mario-lyden til å spille og en kontinuerlig loop med
# pygame.mixer.music.load og play. La til -1 for at det skal funke.
lydeffekt_start.play()
pygame.mixer.music.load("Super-Mario-Bros_SANG.mp3")
pygame.mixer.music.play(-1)

KLOKKE = pygame.time.Clock()
SKJERM = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Super-Mario KOPI")

X_POSISJON, Y_POSISJON = 400, 645
hopping = False

# Variabelen holder kontroll på om spillet er gameover
gameover = False

Y_GRAVITASJON = 1
HOPPE_HØYDE = 20
Y_VELOCITY = HOPPE_HØYDE
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("mario_standing.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("mario_jumping.png"), (48, 64))
BACKGROUND = pygame.transform.scale(pygame.image.load("WHu9Z.png"), (800, 800))

#mario_rect = STANDING_SURFACE.get_rect(center=(X_POSISJON, Y_POSISJON))


class Mario:
    """Klasse for å representere en Mario figur"""
    def __init__(self, x, y, fart, vindusobjekt):
        self.x = x
        self.y = y
        self.fart = fart
        self.vindusobjekt = vindusobjekt
    
    def flytt(self, taster):
        if taster[K_LEFT]:
            self.x -= self.fart
            lydeffekt_løping.play()
        if taster[K_RIGHT]:
            self.x += self.fart
            lydeffekt_løping.play()
            

class Goomba:
    def __init__(self, x, y, fart, vindusobjekt):
        self.x = x
        self.y = y
        self.fart = fart
        self.vindusobjekt = vindusobjekt
        self.bilde = pygame.transform.scale(pygame.image.load("goomba.png"), (85, 80))
        self.rect = self.bilde.get_rect(center=(self.x, self.y))
        self.retning = 1
        
    def flytt(self):
        self.x += self.fart * self.retning
        if self.rect.right >= self.vindusobjekt.get_width() and self.rect.left > 0:
           # Her skal Goombaen endre retning når den treffer kanten av skjermen.
           self.x = self.vindusobjekt.get_width() - self.rect.width
           self.retning *= -1
        elif self.rect.left <= 0 and self.retning < 0:
            self.x = 0
            self.retning = 1
        self.rect.center = (self.x, self.y)

           
           
mario = Mario(X_POSISJON, Y_POSISJON, 5, SKJERM)  # Opprett et Mario-objekt
goomba = Goomba(500, 660, 2, SKJERM)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_SPACE]:
        hopping = True
        lydeffekt_hopping.play()


    # Kall flytt-metoden for Mario-objektet basert på tastetrykkene
    mario.flytt(keys_pressed)
    
    if not (keys_pressed[K_LEFT], keys_pressed[K_RIGHT]):
        lydeffekt_løping.stop()
    
    SKJERM.blit(BACKGROUND, (0, 0))
    
    if hopping:
        Y_POSISJON -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITASJON
        if Y_VELOCITY < -HOPPE_HØYDE:
            hopping = False
            Y_VELOCITY = HOPPE_HØYDE
        mario_rect = JUMPING_SURFACE.get_rect(center=(mario.x, Y_POSISJON))
        SKJERM.blit(JUMPING_SURFACE, mario_rect)
    
    else:
        mario_rect = STANDING_SURFACE.get_rect(center=(mario.x, Y_POSISJON))
        SKJERM.blit(STANDING_SURFACE, mario_rect)
    #Goombaens plassering oppdateres
    goomba.flytt()
    #Gombaen tenges
    SKJERM.blit(goomba.bilde, goomba.rect)
    
    if mario_rect.colliderect(goomba.rect):
        if mario_rect.bottom <= goomba.rect.top + 10:
            goomba.rect.x = -100
            #lydeffekt_død = pygame.mixer.Sound("død_lyd.mp4")
            #lydeffekt_død.play()
            
        
        else:
            
            # Stopper alle lydeffekter og spiller en gameover-lyd
            pygame.mixer.music.stop()
            lydeffekt_gameover = pygame.mixer.Sound("gameover.wav")
            gameover_Kanal.play(lydeffekt_gameover)
       
            # Vis en gameover-melding
            gameover_font = pygame.font.Font(None, 74)
            gameover_text = gameover_font.render('Game Over', True, (255, 0, 0))
            SKJERM.blit(gameover_text, (250, 350))
            pygame.display.update()
            # Venter i noen sekunder før jeg avslutter eller restarter spillet
            pygame.time.wait(3000)
        
            break  # Avslutter spill-løkken
    

    
    pygame.display.update()
    KLOKKE.tick(60)
 