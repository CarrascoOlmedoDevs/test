import pygame
import math
import random

# --- Constants ---
WIDTH, HEIGHT = 1000, 800
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Universe Simulator")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
GREEN = (0, 255, 0) # For moon
ORANGE = (255, 165, 0) # For another planet
PURPLE = (128, 0, 128) # For another planet

# Simulation Constants
G = 2 # Adjusted gravitational constant
AU = 100 # Astronomical Unit, a scaling factor for distance in pixels
TIMESTEP = 0.1 # Time step for simulation

# --- CelestialBody Class ---
class CelestialBody:
    def __init__(self, x, y, radius, color, mass, name=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name

        self.is_sun = False

        self.x_vel = 0
        self.y_vel = 0

        self.trail = []
        self.max_trail_length = 150 # Max points in trail

    def draw(self, win, show_names, show_trails, font):
        # Adjust position relative to screen center
        draw_x = self.x + WIDTH / 2
        draw_y = self.y + HEIGHT / 2

        # Draw trail
        if show_trails and len(self.trail) > 1:
            points = []
            for pos in self.trail:
                # Adjust trail points relative to screen center
                points.append((pos[0] + WIDTH / 2, pos[1] + HEIGHT / 2))

            # Draw lines between points
            pygame.draw.lines(win, self.color, False, points, 1)

        # Draw body
        pygame.draw.circle(win, self.color, (int(draw_x), int(draw_y)), self.radius)

        # Draw name
        if show_names and self.name:
            text = font.render(self.name, 1, WHITE)
            win.blit(text, (draw_x - text.get_width() / 2, draw_y - self.radius - 15)) # Position name above body

    def attraction(self, other):
        # Calculate the force vector exerted by 'other' on 'self'
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # Avoid division by zero or extreme forces at very small distances
        if distance < self.radius + other.radius: # Simple collision check / minimum distance
             distance = self.radius + other.radius

        # Gravitational force magnitude: F = G * m1 * m2 / r^2
        force = G * self.mass * other.mass / distance**2

        # Calculate force components (vector)
        # The force is directed along the line connecting the two bodies.
        # Direction vector from self to other: (distance_x, distance_y)
        # Normalized direction vector: (distance_x / distance, distance_y / distance)
        # Force vector: force * normalized_direction_vector
        force_angle = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(force_angle)
        force_y = force * math.sin(force_angle)

        return force_x, force_y

# --- Helper function to calculate initial orbital velocity ---
def calculate_orbital_velocity(body_pos_x, body_pos_y, central_mass_pos_x, central_mass_pos_y, central_mass):
    """Calculates the initial velocity for a circular orbit."""
    dx = body_pos_x - central_mass_pos_x
    dy = body_pos_y - central_mass_pos_y
    distance = math.sqrt(dx**2 + dy**2)

    if distance == 0:
        return 0, 0 # Should not happen for orbiting bodies

    # Speed for circular orbit: v = sqrt(G * M / r)
    speed = math.sqrt(G * central_mass.mass / distance)

    # Velocity vector is perpendicular to the position vector (dx, dy)
    # Perpendicular vector: (-dy, dx) or (dy, -dx)
    # We want counter-clockwise orbit here, so velocity is roughly in the direction (-dy, dx).
    # Normalize the perpendicular vector and scale by speed.
    # The vector from central mass to body is (dx, dy).
    # A vector perpendicular to (dx, dy) is (-dy, dx).
    # Normalize this perpendicular vector: (-dy/distance, dx/distance)
    # Scale by speed: (speed * -dy/distance, speed * dx/distance)

    vel_x = speed * (-dy / distance)
    vel_y = speed * (dx / distance)

    return vel_x, vel_y

# --- Main Game Loop ---
def main():
    run = True
    clock = pygame.time.Clock()

    # --- Create Celestial Bodies ---
    # Sun is at the center (0,0) in simulation coordinates
    sun = CelestialBody(0, 0, 30, YELLOW, 1.989e30 * 500) # Sun's mass is large, scaled up
    sun.is_sun = True

    # Planets orbiting the Sun
    # Position is relative to the Sun (0,0)
    # Masses are scaled up for G=2
    earth = CelestialBody(-1.5 * AU, 0, 16, BLUE, 5.972e24 * 50)
    earth.name = "Earth"
    earth.x_vel, earth.y_vel = calculate_orbital_velocity(earth.x, earth.y, sun.x, sun.y, sun)

    mars = CelestialBody(-2 * AU, 0, 12, RED, 6.417e23 * 50)
    mars.name = "Mars"
    mars.x_vel, mars.y_vel = calculate_orbital_velocity(mars.x, mars.y, sun.x, sun.y, sun)

    jupiter = CelestialBody(3 * AU, 0, 25, DARK_GREY, 1.898e27 * 50)
    jupiter.name = "Jupiter"
    jupiter.x_vel, jupiter.y_vel = calculate_orbital_velocity(jupiter.x, jupiter.y, sun.x, sun.y, sun)

    # Add another planet
    venus = CelestialBody(1 * AU, 0, 15, ORANGE, 4.867e24 * 50)
    venus.name = "Venus"
    venus.x_vel, venus.y_vel = calculate_orbital_velocity(venus.x, venus.y, sun.x, sun.y, sun)


    # Moon orbiting Earth
    # Position is relative to Earth's initial position
    # Initial velocity relative to Earth's initial velocity
    moon_dist_from_earth = 0.2 * AU # Distance from Earth
    moon = CelestialBody(earth.x - moon_dist_from_earth, earth.y, 8, GREEN, 7.342e22 * 5) # Moon mass scaled up
    moon.name = "Moon"
    # Calculate moon's velocity relative to Earth for a circular orbit around Earth
    moon_vel_x_rel, moon_vel_y_rel = calculate_orbital_velocity(moon.x, moon.y, earth.x, earth.y, earth)
    # Moon's initial velocity is its orbital velocity around Earth PLUS Earth's velocity around the Sun
    moon.x_vel = earth.x_vel + moon_vel_x_rel
    moon.y_vel = earth.y_vel + moon_vel_y_rel


    bodies = [sun, earth, mars, jupiter, venus, moon] # List of all bodies in the simulation

    # --- Game State Flags ---
    show_names = True
    show_trails = True

    # --- Font for text ---
    font = pygame.font.SysFont("monospace", 16)
    hud_font = pygame.font.SysFont("monospace", 20)

    # --- Game Loop ---
    while run:
        clock.tick(60) # Limit frame