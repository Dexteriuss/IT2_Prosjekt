import pygame
import sys

pygame.init()

KLOKKE = pygame.time.Clock()
SKJERM = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Hoppe i Pygame")

X_POSISJON, Y_POSISJON = 400, 660

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/stående_mario.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets(hoppende_mario.png)"), (48, 64))
BACKGROUND = pygame.image.load("assets/WHu9Z.png")

mario_rect = STANDING_SURFACE.get_rect(center=(X_POSISJON, Y_POSISJON))

while True:
    