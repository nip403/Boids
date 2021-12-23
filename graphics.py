import pygame
import numpy as np
import sys

pygame.init()

BG_COLOUR = (0, 0, 0)
BOID_COLOUR = (255, 255, 255)

BOID_LENGTH = 20

def plot_boid(boid):
    x = boid.x
    y = boid.y
    a = boid.theta
    
    # initialise boid shape
    points = [
        [0, BOID_LENGTH/2], 
        [-BOID_LENGTH/4, -BOID_LENGTH/2], 
        [BOID_LENGTH/4, -BOID_LENGTH/2],
    ]
    
    # rotate and translate
    for p in points:
        p[:] = [
            (p[0] * np.cos(a)) - (p[1] * np.sin(a)) + x,
            (p[0] * np.sin(a)) + (p[1] * np.cos(a)) + y,
        ]

    return points

class Window:
    def __init__(self, width, height):
        self.dimensions = [width, height]
        self.scr = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Boids demo")
        
    def update(self, boids=[]):
        self.scr.fill(BG_COLOUR)
        
        for b in boids:
            pygame.draw.polygon(
                self.scr,
                BOID_COLOUR,
                plot_boid(b),
                1,
           )
            
        pygame.display.flip()
    