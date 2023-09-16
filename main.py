import pygame


class Simulation:
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, simulation_speed, grid_size):
        self.agents = []

        pygame.init()

        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH = WINDOW_WIDTH

        self.grid_size = grid_size

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.simulation_speed = simulation_speed

        self.running = True

    def get_gird_size(self):
        return self.grid_size

    def get_screen(self):
        return self.screen

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            for agent in self.agents:
                agent.draw()

            pygame.display.flip()

            self.clock.tick(self.simulation_speed)

    pygame.quit()


class Agent:
    def __init__(self, simulation, heading_direction, location, sensors, sensor_distance,
                 sensor_angle):
        self.simulation = simulation
        self.heading_direction = heading_direction
        self.location = location
        self.sensors = sensors
        self.sensor_distance = sensor_distance
        self.sensor_angle = sensor_angle

        self.simulation.add_agent(self)
        self.screen = simulation.get_screen()
        self.grid_size = simulation.get_gird_size()

    def up(self):
        return 1, 0

    def down(self):
        return -1, 0

    def left(self):
        return 0, -1

    def right(self):
        return 0, 1

    def rotate(self):
        pass

    def move(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (
            self.location[0] * self.grid_size + self.grid_size, self.location[1] * self.grid_size + self.grid_size,
            self.grid_size,
            self.grid_size))


class Particle(Agent):
    def __init__(
            self,
            simulation,
            heading_angle,
            location,
            sensors,
            sensor_distance,
            sensor_angle
    ):
        super(Particle, self).__init__(simulation, heading_angle, location, sensors, sensor_distance,
                                       sensor_angle)


if __name__ == "__main__":
    print("running")
    sim = Simulation(1000, 1000, 60, 10)
    particle_alpha = Particle(
        simulation=sim,
        heading_angle=None,
        sensor_angle=None,
        sensor_distance=None,
        sensors=None,
        location=(50, 50)
    )

    sim.run()
