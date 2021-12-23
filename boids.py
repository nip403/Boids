from graphics import Window
from ai import Boid, init_boids, manage_overlap
import pygame

def main():
    s = [1200, 800]
    boids = init_boids(10, s)
    win = Window(*s)
    
    while True:
        win.clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        for b in boids:
            b.apply_rules(boids, s)
            b.init_next(s)
            
        for b in boids:
            next(b)
                
        win.update(boids)
    

if __name__ == "__main__":
    main()