import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as rd
import random as rd

pg.init()

VINDU_BREDDE = 500
VINDU_HØYDE = 500

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HØYDE])

class Mario:
    """Klasse for å representere en Mario-figur"""
    def __init__(self, x, y, fart, radius, farge, vinduobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.farge = farge
        self.vinduobjekt = vindusobjekt

    def tegn(self):
        """En metode for å tegne Mario-figuren"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

    def flytt(self, taster)
        """Metode for å flytte Mario-figuren"""
        if taster[K_UP]:
            self.y 