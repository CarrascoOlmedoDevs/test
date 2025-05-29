import pygame
import sys
import math
import random

# Constants
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARKGREY = (80, 78, 81)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

G = 2  # Gravitational constant (adjusted for simulation)
AU = 50  # Astronomical Unit (scaling factor)
TIMESTEP = 0.1  # Simulation time step

class CelestialBody:
    def __init__(self, x, y, radius, color, mass, name, is_static=False, is_moon=False, parent_body=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name
        self.is_static = is_static
        self.is_moon = is_moon
        self.parent_body = parent_body # Used for initial positioning/velocity calc only
        self.vel_x = 0
        self.vel_y = 0
        self.trail = []
        self.trail_length = 100 # Number of points in the trail

    def draw(self, win, font, show_names):
        # Draw trail
        if self.trail and show_trails:
            points = []
            for i in range(len(self.trail) - 1):
                points.append((int(self.trail[i][0]), int(self.trail[i][1])))
            if len(points) > 1:
                 pygame.draw.lines(win, self.color, False, points, 1)

        # Draw body
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), int(self.radius))

        # Draw name
        if show_names:
            text = font.render(self.name, 1, WHITE)
            win.blit(text, (self.x - text.get_width()/2, self.y - self.radius - 15))

    def update_position(self):
        if not self.is_static:
            self.x += self.vel_x * TIMESTEP
            self.y += self.vel_y * TIMESTEP

            # Update trail
            self.trail.append((self.x, self.y))
            if len(self.trail) > self.trail_length:
                self.trail.pop(0)

    def apply_force(self, force_x, force_y):
        if not self.is_static:
            acc_x = force_x / self.mass
            acc_y = force_y / self.mass
            self.vel_x += acc_x * TIMESTEP
            self.vel_y += acc_y * TIMESTEP

    def calculate_attraction(self, other):
        if self is other:
            return 0, 0

        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        # Avoid division by zero if bodies overlap perfectly
        if distance < self.radius + other.radius: # Simple collision check / avoid extreme forces
             # Can add collision logic here if needed, for now just prevent extreme force
             distance = self.radius + other.radius # Set minimum distance
             if distance == 0: distance = 1 # Should not happen with radius > 0

        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(dy, dx)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)

        return force_x, force_y

def create_initial_solar_system():
    sun = CelestialBody(WIDTH // 2, HEIGHT // 2, 25, YELLOW, 5000, "Sol", is_static=True)

    # Planets (distance in AU, scaled by AU constant)
    mercury = CelestialBody(WIDTH // 2 + 0.4 * AU, HEIGHT // 2, 5, DARKGREY, 0.1, "Mercurio")
    venus = CelestialBody(WIDTH // 2 + 0.7 * AU, HEIGHT // 2, 8, ORANGE, 0.8, "Venus")
    earth = CelestialBody(WIDTH // 2 + 1.0 * AU, HEIGHT // 2, 10, BLUE, 1.0, "Tierra")
    mars = CelestialBody(WIDTH // 2 + 1.5 * AU, HEIGHT // 2, 7, RED, 0.5, "Marte")


    # Calculate initial orbital velocities for planets
    bodies = [sun, mercury, venus, earth, mars] # Add planets to list before calculating velocities

    for body in [mercury, venus, earth, mars]:
        # Assume orbiting the Sun
        primary = sun
        dx = primary.x - body.x
        dy = primary.y - body.y
        distance = math.sqrt(dx**2 + dy**2)
        # Speed for circular orbit: sqrt(G * M / r)
        orbital_speed = math.sqrt(G * primary.mass / distance)

        # Set initial velocity perpendicular to the position vector relative to primary
        # If body is at (dx, dy) relative to primary, velocity is proportional to (-dy, dx) or (dy, -dx)
        # Let's make planets orbit counter-clockwise
        body.vel_x = -dy/distance * orbital_speed
        body.vel_y = dx/distance * orbital_speed

    # Add a moon orbiting Earth
    moon = CelestialBody(earth.x + 20, earth.y, 3, WHITE, 0.01, "Luna", is_moon=True, parent_body=earth)
    # Calculate initial velocity for the moon relative to Earth AND inherit Earth's velocity
    primary_moon = earth
    dx_moon = primary_moon.x - moon.x
    dy_moon = primary_moon.y - moon.y
    distance_moon = math.sqrt(dx_moon**2 + dy_moon**2)
    orbital_speed_moon = math.sqrt(G * primary_moon.mass / distance_moon)

    # Set moon's velocity relative to its parent (Earth)
    moon_vel_x_rel = -dy_moon/distance_moon * orbital_speed_moon
    moon_vel_y_rel = dx_moon/distance_moon * orbital_speed_moon

    # Add parent's velocity to get absolute velocity
    moon.vel_x = moon_vel_x_rel + primary_moon.vel_x
    moon.vel_y = moon_vel_y_rel + primary_moon.vel_y

    bodies.append(moon)

    return bodies

def create_asteroid(bodies):
    # Create asteroid far from the center with random properties
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(2 * AU, 4 * AU) # Appear far out
    x = WIDTH // 2 + distance * math.cos(angle)
    y = HEIGHT // 2 + distance * math.sin(angle)

    radius = random.uniform(2, 6)
    mass = random.uniform(0.001, 0.05)
    color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)) # Greyish/rocky color

    asteroid = CelestialBody(x, y, radius, color, mass, f"Asteroide {len([b for b in bodies if 'Asteroide' in b.name]) + 1}")

    # Give it a small random initial velocity, maybe pointing slightly towards the center
    asteroid.vel_x = random.uniform(-0.5, 0.5)
    asteroid.vel_y = random.uniform(-0.5, 0.5)

    bodies.append(asteroid)


# Pygame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Universo")
font = pygame.font.SysFont("monospace", 15)
info_font = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initial system setup
celestial_bodies = create_initial_solar_system()
show_names = True
show_trails = True

# Main simulation loop
running = True
while running:
    clock.tick(60) # Limit FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                show_names = not show_names
            if event.key == pygame.K_t:
                show_trails = not show_trails
            if event.key == pygame.K_SPACE:
                create_asteroid(celestial_bodies)


    # Calculate forces
    forces = {}
    for body in celestial_bodies:
        forces[body] = (0, 0) # Initialize total force for each body

    for i, body1 in enumerate(celestial_bodies):
        for j, body2 in enumerate(celestial_bodies):
            if i != j:
                # Calculate force body2 exerts on body1
                force_x, force_y = body1.calculate_attraction(body2)
                forces[body1] = (forces[body1][0] + force_x, forces[body1][1] + force_y)


    # Apply forces and update positions
    for body in celestial_bodies:
        if not body.is_static: # Only apply force and update position for non-static bodies
            body.apply_force(forces[body][0], forces[body][1])
            body.update_position()


    # Drawing
    WIN.fill(BLACK) # Background

    for body in celestial_bodies:
        body.draw(WIN, font, show_names)

    # Display info
    body_count_text = info_font.render(f"Cuerpos: {len(celestial_bodies)}", 1, WHITE)
    fps_text = info_font.render(f"FPS: {int(clock.get_fps())}", 1, WHITE)
    key_info_text = info_font.render("N: Nombres | T: Estelas | Espacio: Asteroide", 1, WHITE)

    WIN.blit(body_count_text, (10, 10))
    WIN.blit(fps_text, (10, 30))
    WIN.blit(key_info_text, (10, HEIGHT - 20))

    pygame.display.flip()

pygame.quit()
sys.exit()