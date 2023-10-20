import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NucleusRadius = 20
ElectronRadius = 10
Orbit1Radius = 100
Orbit2Radius = 150
OrbitSpeed = 0.005  # Reduced speed for slower electron movement

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORBIT_COLOR = (100, 100, 100)
ELECTRON_LABEL_COLOR = (0, 255, 0)  # Electron label color
YELLOW = (255, 255, 0)  # Yellow color for the title

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lithium (Li) - Bohr Model")

# Font
font = pygame.font.Font(None, 36)

# Main loop
running = True
angle1 = 0
angle2 = math.pi  # Second electron is in the K shell
angle3 = math.pi  # Third electron is in the L shell

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate electron positions
    electron1_x = WIDTH // 2 + Orbit1Radius * math.cos(angle1)
    electron1_y = HEIGHT // 2 + Orbit1Radius * math.sin(angle1)
    electron2_x = WIDTH // 2 + Orbit1Radius * math.cos(angle2)  # Both electrons are on the first orbit
    electron2_y = HEIGHT // 2 + Orbit1Radius * math.sin(angle2)
    electron3_x = WIDTH // 2 + Orbit2Radius * math.cos(angle3)  # Third electron is in the L shell
    electron3_y = HEIGHT // 2 + Orbit2Radius * math.sin(angle3)

    # Draw the orbit paths
    pygame.draw.circle(screen, ORBIT_COLOR, (WIDTH // 2, HEIGHT // 2), Orbit1Radius, 1)
    pygame.draw.circle(screen, ORBIT_COLOR, (WIDTH // 2, HEIGHT // 2), Orbit2Radius, 1)

    # Draw the nucleus with label in red
    pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), NucleusRadius)
    nucleus_label = font.render("Nucleus", True, RED)
    screen.blit(nucleus_label, (WIDTH - 150, HEIGHT - 130))

    # Draw the electrons with labels at the bottom right corner
    electron_label1 = font.render("Electron 1", True, ELECTRON_LABEL_COLOR)
    electron_label2 = font.render("Electron 2", True, ELECTRON_LABEL_COLOR)
    electron_label3 = font.render("Electron 3", True, ELECTRON_LABEL_COLOR)
    
    screen.blit(electron_label1, (WIDTH - 150, HEIGHT - 100))
    screen.blit(electron_label2, (WIDTH - 150, HEIGHT - 70))
    screen.blit(electron_label3, (WIDTH - 150, HEIGHT - 40))

    pygame.draw.circle(screen, ELECTRON_LABEL_COLOR, (int(electron1_x), int(electron1_y)), ElectronRadius)
    pygame.draw.circle(screen, ELECTRON_LABEL_COLOR, (int(electron2_x), int(electron2_y)), ElectronRadius)
    pygame.draw.circle(screen, ELECTRON_LABEL_COLOR, (int(electron3_x), int(electron3_y)), ElectronRadius)

    # Title in yellow
    title = font.render("Lithium (Li) - Bohr Model", True, YELLOW)
    screen.blit(title, (WIDTH // 2 - 180, 20))

    pygame.display.flip()

    angle1 += OrbitSpeed
    angle2 += OrbitSpeed
    angle3 += OrbitSpeed  # L shell electron moves in the outer orbit

    # Introduce a delay for slower electron movement
    time.sleep(0.02)  # Adjust this value for the desired speed

pygame.quit()
