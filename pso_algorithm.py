# Import necessarry library
import random
import numpy as np

class Particle:
    """
    A class to represent the particles
    """
    def __init__(self, position: list, velocity: list):
        self.position = position # Position value
        self.velocity = velocity # Velocity value
        self.particle_best = self.position # Particle best value

class PSO:
    """
    A class to apply the PSO algorithm to the objective function
    """
    def __init__(self, objective_function, W: float, C1: float, C2: float, num_particles: int):
        self.objective_function = objective_function # Objective Function
        self.W = W # Inertia Weight
        self.C1 = C1 # Cognitive Coefficient
        self.C2 = C2 # Social Coefficient
        self.num_particles = num_particles # Number of particles
        self.global_best = [None, None] # Global best value (current best solution to the objective function)

    def initialize_particles(self) -> list[Particle]:
        """
        A function to initialize the particles.
        """
        particles = []
        for _ in range(self.num_particles):
            position = [random.uniform(-100, 100) for i in range(2)]
            velocitiy = [random.uniform(-100, 100) for i in range(2)]
            particles.append(Particle(position, velocitiy))

        return particles

    def calculate_fitness_values(self, particles: list[Particle]) -> list:
        """
        A function to calculate the fitness values for each particle.
        """
        fitness_values = []
        for particle in particles:
            position = particle.position
            fitness_value = self.objective_function(position[0], position[1])
            fitness_values.append(fitness_value)
        
        return fitness_values

    def set_p_bests(self, particles: list[Particle], fitness_values: list) -> None:
        """
        A function to set particle best values for each particle.
        """
        for i in range(len(particles)):
            particle = particles[i]
            new_fitness_value = fitness_values[i]
            old_fitness_value = self.objective_function(particle.particle_best[0],particle.particle_best[1])
            particle.particle_best = particle.position if new_fitness_value < old_fitness_value else particle.particle_best

    def set_global_best(self, particles: list[Particle], fitness_values: list) -> None:
        """
        A function to set global best value.
        """
        for i in range(len(particles)):
            particle = particles[i]
            if None in self.global_best:
                self.global_best = particle.particle_best
            particle_fitness_value = fitness_values[i]
            global_best_fitness_value = self.objective_function(self.global_best[0], self.global_best[1])
            self.global_best = particle.particle_best if particle_fitness_value < global_best_fitness_value else self.global_best

    def update_velocities(self, particles: list[Particle]) -> None:
        """
        A function to update the velocity values for each particle.
        """
        random_number_1 = random.random()
        random_number_2 = random.random()
        for particle in particles:
            for dim in range(len(particle.velocity)):
                particle.velocity[dim] = self.W * particle.velocity[dim] + self.C1 * random_number_1 * (particle.particle_best[dim] - particle.position[dim]) + self.C2 * random_number_2 * (self.global_best[dim] - particle.position[dim])

    def update_positions(self, particles: list[Particle]):
        """
        A function to update position values for each particle. 
        """
        for particle in particles:
            for dim in range(len(particle.position)):
                particle.position[dim] = particle.position[dim] + particle.velocity[dim]

def objective_function(x1: float, x2: float) -> float:
    """
    Objective Function.
    """
    return x1 ** 2 + x2 ** 2

# Create global variables
W = 0.5
C1 = 1.5
C2 = 1.5
NUM_PARTICLES = 10
NUM_LOOPS = 10000

""" Initially """
# Create an instance of PSO class to apply PSO algorithm
pso = PSO(objective_function = objective_function, W = W, C1 = C1, C2 = C2, num_particles = NUM_PARTICLES)
# Initialize the particles
particles = pso.initialize_particles()

""" Repeat the operation """
for epoch in range(NUM_LOOPS):
    # Calculate the fitness values
    fitness_values = pso.calculate_fitness_values(particles)

    # Update particle best values
    pso.set_p_bests(particles, fitness_values)

    # Update global best values
    pso.set_global_best(particles, fitness_values)
    
    # Update particle velocity values
    pso.update_velocities(particles)

    # Update particle position values
    pso.update_positions(particles)

""" Finally """
# Get the best solution index
best_solution_index = np.argmin(fitness_values)

# Get the best solution
best_solution = pso.global_best

# Print the best solution and the final value
print(f"The best solution found after {NUM_LOOPS} iteration is : \nx: {best_solution[0]:.6f}\ny: {best_solution[1]:.6f}\n")
print(f"The best value found after {NUM_LOOPS} iteration is : \n{objective_function(best_solution[0], best_solution[1]):.10f}")