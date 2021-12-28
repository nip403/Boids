from ai import Boid, init_boids
from graphics import Demo

# add option (sliders/keypresses) to modify sim constants

def main():
    dimensions = [1400, 1000]
    boids = init_boids(100, dimensions)
    
    demo = Demo(dimensions)
    demo.update_boids(boids)
    demo.sim()

if __name__ == '__main__':
    main()
