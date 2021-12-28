import numpy as np
import random

# general
MAXSPEED = 20
MINSPEED = 5
EYESIGHT = 75

# separation
SEPARATION_FACTOR = 0.05
MIN_DIST = 20

# alignment
ALIGNMENT_FACTOR = 0.05

# cohesion
COHESION_FACTOR = 0.005

# bounds
MARGIN = 50
TURNFACTOR = 1

def dist(a: float, b: float) -> float:
    return ((a ** 2) + (b ** 2)) ** 0.5

def init_boids(num: int, dimensions: list) -> list:
    boids = []
    
    for _ in range(num):
        boids.append(
            Boid(
                random.random() * dimensions[0],
                random.random() * dimensions[1],
                random.random() * MAXSPEED - 0.5 * MAXSPEED,
                random.random() * MAXSPEED - 0.5 * MAXSPEED,
            )
        )
        
    return boids

class Boid:
    def __init__(self, x: float, y: float, dx: float, dy: float):
        self.x = x
        self.y = y
        
        self.dx = dx
        self.dy = dy
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.x += self.dx
        self.y += self.dy
        
        return self
    
    def separation(self, boids: list):
        move_x = 0
        move_y = 0
        
        for b in boids:
            if not self == b:
                if dist(self.x - b.x, self.y - b.y) < MIN_DIST:
                    move_x += self.x - b.x
                    move_y += self.y - b.y
                    
        self.dx += move_x * SEPARATION_FACTOR
        self.dy += move_y * SEPARATION_FACTOR
    
    def alignment(self, boids: list):
        mean_dx = 0
        mean_dy = 0
        
        num = 0
        
        for b in boids:
            if dist(self.x - b.x, self.y - b.y) < EYESIGHT:
                mean_dx += b.dx
                mean_dy += b.dy

                num += 1
                
        if num:
            self.dx += ((mean_dx / num) - self.dx) * ALIGNMENT_FACTOR
            self.dy += ((mean_dy / num) - self.dy) * ALIGNMENT_FACTOR
    
    def cohesion(self, boids: list):
        centre_x = 0
        centre_y = 0
        
        num = 0
        
        for b in boids:
            if dist(self.x - b.x, self.y - b.y) < EYESIGHT:
                centre_x += b.x
                centre_y += b.y
                
                num += 1
        
        if num:
            self.dx += ((centre_x / num) - self.x) * COHESION_FACTOR
            self.dy += ((centre_y / num) - self.y) * COHESION_FACTOR
    
    def limspeed(self):
        speed = dist(self.dx, self.dy)
        
        if speed > MAXSPEED:
            self.dx *= MAXSPEED / speed
            self.dy *= MAXSPEED / speed
            
        elif speed < MINSPEED:
            self.dx *= MINSPEED / speed
            self.dy *= MINSPEED / speed
    
    def enforce_bounds(self, dimensions: list, crossover: bool):
        #######crossover
        assert all(i > 2 * MARGIN for i in dimensions)
        
        if self.x < MARGIN:
            self.dx += TURNFACTOR
        elif self.x > dimensions[0] - MARGIN:
            self.dx -= TURNFACTOR
            
        if self.y < MARGIN:
            self.dy += TURNFACTOR
        elif self.y > dimensions[1] - MARGIN:
            self.dy -= TURNFACTOR
    
