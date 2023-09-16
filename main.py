import numpy as np
import pygame

class Simulation:
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, simulation_speed):
        pygame.init()

        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH = WINDOW_WIDTH

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.simulation_speed = simulation_speed

        self.running = True

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

        self.screen.fill("black")

        pygame.display.flip()

        self.clock.tick(self.simulation_speed)

    pygame.quit()

class Agent:
    def __init__(self):
        pass

if __name__ == "__main__":
    print("running")
    sim = Simulation(100, 100, 60)
    sim.run()