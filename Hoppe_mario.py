import pygame
import sys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

pygame.init()

KLOKKE = pygame.time.Clock()
SKJERM = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Hoppe i Pygame")

X_POSISJON, Y_POSISJON = 400, 650
hopping = False

Y_GRAVITASJON = 1
HOPPE_HØYDE = 20
Y_VELOCITY = HOPPE_HØYDE
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("stående_mario.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("hoppende_mario.png"), (48, 64))
BACKGROUND = pygame.transform.scale(pygame.image.load("WHu9Z.png"), (800, 800))

mario_rect = STANDING_SURFACE.get_rect(center=(X_POSISJON, Y_POSISJON))

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
        if taster[K_RIGHT]:
            self.x += self.fart

mario = Mario(X_POSISJON, Y_POSISJON, 5, SKJERM)  # Opprett et Mario-objekt

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_SPACE]:
        hopping = True

    # Kall flytt-metoden for Mario-objektet basert på tastetrykkene
    mario.flytt(keys_pressed)
    
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
    
    pygame.display.update()
    KLOKKE.tick(60)
 