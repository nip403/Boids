import numpy as np
import random

SPEED_LIM = 20
EYESIGHT = 50

# separation rule vars
AVOID_DIST = 20
SEPARATION_STRENGTH = 0.05

# alignment rule vars
ALIGN_STRENGTH = 0.05

# cohesion rule vars
COHESION_STRENGTH = 0.01

class Boid:
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        
        self.newx = x
        self.newy = y
        
        self.dx = dx
        self.dy = dy
        
    @property
    def theta(self):
        return np.arctan(self.dx/self.dy)
    
    def __iter__(self):
        return self
        
    def __next__(self):     
        # move boid
        self.x = self.newx
        self.y = self.newy
        
        return self
    
    def init_next(self, dimensions=[500, 500]):
        self.newx = self.x + self.dx
        self.newy = self.y + self.dy
        
        manage_overlap(self, dimensions)
    
    def apply_rules(self, boids=[], dimensions=[500, 500]):
        self.separation()
        self.alignment()
        self.cohesion()        
        self.limit_speed()
        
    def separation(self, boids=[]):
        changex = 0
        changey = 0

        for b in boids:
            if not b == self:
                if dist(self, b) <= AVOID_DIST:
                    changex += self.x - b.x
                    changey += self.y - b.y
        
        self.dx += changex * SEPARATION_STRENGTH
        self.dy += changey * SEPARATION_STRENGTH
    
    def alignment(self, boids=[]):
        averagex = 0
        averagey = 0
        num = 0
        
        for b in boids:
            if not b == self:
                if dist(self, b) <= EYESIGHT:
                    num += 1
                    
                    averagex += b.dx
                    averagey += b.dy
        
        if not num:
            return
        
        self.dx += averagex/num * ALIGN_STRENGTH
        self.dy += averagey/num * ALIGN_STRENGTH
    
    def cohesion(self, boids=[]):
        centrex = 0
        centrey = 0
        num = 0

        for b in boids:
            if not self == b:
                if dist(self, b) <= EYESIGHT:
                    num += 1
                    
                    centrex += b.x
                    centrey += b.y
                    
        if not num:
            return
        
        self.dx += centrex/num * COHESION_STRENGTH
        self.dy += centrey/num * COHESION_STRENGTH
    
    def limit_speed(self):
        speed = ((self.dx ** 2) + (self.dy ** 2)) ** 0.5
        
        if speed >= SPEED_LIM:
            self.dx = self.dx/speed * SPEED_LIM
            self.dy = self.dy/speed * SPEED_LIM
        
def init_boids(amount=10, dimensions=[500, 500]):
    boids = []
    
    for _ in range(amount):
        boids.append(
            Boid(
                random.random() * dimensions[0],
                random.random() * dimensions[1],
                random.random() * 10,
                random.random() * 10
                )
        )
        
    return boids

def manage_overlap(boid, dimensions=[500, 500]):
    if boid.newx <= 0:
        boid.newx = dimensions[0]
        
    if boid.newx >= dimensions[0]:
        boid.newx = 0
        
    if boid.newy <= 0:
        boid.newy = dimensions[1]
        
    if boid.newy >= dimensions[1]:
        boid.newy = 0
        
def dist(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2) ** 0.5