import pygame
import numpy as np
import sys

FPS = 60
BG_COLOUR = (0, 0, 0)
BOID_COLOUR = (255, 255, 255)

pygame.init()

class Demo:
    def __init__(self, dimensions: list):
        self.dim = dimensions
        self.boids = []
        self.window = pygame.display.set_mode(self.dim, 0, 32)
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Boids Demo")
        
    def update_boids(self, boids: list):
        self.boids = boids
        
    def sim(self):
        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.window.fill(BG_COLOUR)
            
            for b in self.boids:
                pygame.draw.circle(self.window, BOID_COLOUR, (b.x, b.y), 5, 0)
                
                b.cohesion(self.boids)
                b.separation(self.boids)
                b.alignment(self.boids)
                b.limspeed()
                b.enforce_bounds(self.dim, False)
                
            for b in self.boids:
                next(b)
                
            pygame.display.flip()
