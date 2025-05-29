import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación del Universo")
clock = pygame.time.Clock()

G = 2

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class CelestialBody:
    def __init__(self, x, y, mass, radius, color, name):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.name = name
        self.vx = 0
        self.vy = 0
        self.trail = []

    def draw(self, screen, show_names):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        if show_names:
            font = pygame.font.Font(None, 16)
            text = font.render(self.name, True, WHITE)
            screen.blit(text, (self.x + self.radius + 5, self.y + self.radius + 5))
        for point in self.trail:
          pygame.draw.circle(screen, self.color, point, 1)


    def update(self, bodies):
        fx, fy = 0, 0
        for body in bodies:
            if body != self:
                dx = body.x - self.x
                dy = body.y - self.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance > self.radius + body.radius:
                    force = G * self.mass * body.mass / distance**2
                    fx += force * dx / distance
                    fy += force * dy / distance

        self.vx += fx / self.mass
        self.vy += fy / self.mass
        self.x += self.vx
        self.y += self.vy
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 100:
            self.trail.pop(0)


sun = CelestialBody(WIDTH // 2, HEIGHT // 2, 1000, 50, YELLOW, "Sol")
planet1 = CelestialBody(WIDTH // 2 + 200, HEIGHT // 2, 10, 20, BLUE, "Planeta 1")
planet1.vy = 1.5
planet2 = CelestialBody(WIDTH // 2 + 300, HEIGHT // 2, 15, 25, RED, "Planeta 2")
planet2.vy = 1
planet3 = CelestialBody(WIDTH // 2 + 100, HEIGHT // 2, 5, 15, GREEN, "Planeta 3")
planet3.vy = 2
moon = CelestialBody(planet1.x + 50, planet1.y, 1, 5, WHITE, "Luna")
moon.vy = 2.5

bodies = [sun, planet1, planet2, planet3, moon]
show_names = True
show_trails = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                show_names = not show_names
            if event.key == pygame.K_t:
                show_trails = not show_trails
            if event.key == pygame.K_SPACE:
                bodies.append(CelestialBody(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 2, WHITE, "Asteroide"))


    screen.fill((0, 0, 0))

    for body in bodies:
        body.update(bodies)
        body.draw(screen, show_names)

    fps = clock.get_fps()
    font = pygame.font.Font(None, 36)
    text = font.render(f"Cuerpos: {len(bodies)}, FPS: {fps:.2f}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()