import pygame
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Hexagon with Gravity Ball")

# Colors
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
RED = (255, 0, 0)

# Hexagon properties
hex_radius = 100
hex_center = (WIDTH // 2, HEIGHT // 2)
angle = 0  # Rotation angle

# Ball properties
ball_radius = 10
ball_pos = list(hex_center)
ball_velocity = [0, 0]  # x and y velocity
gravity = 0.2  # Simulated gravity

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)  # Clear screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate hexagon
    angle += 2  # Increase angle to rotate clockwise
    angle_rad = math.radians(angle)

    # Calculate hexagon vertices
    hex_points = []
    for i in range(6):
        theta = angle_rad + math.pi / 3 * i
        x = hex_center[0] + hex_radius * math.cos(theta)
        y = hex_center[1] + hex_radius * math.sin(theta)
        hex_points.append((x, y))

    # Simulate ball movement (gravity effect)
    ball_velocity[1] += gravity  # Apply gravity
    ball_pos[1] += ball_velocity[1]  # Move ball down
    
    # Check if ball touches bottom of hexagon
    for i in range(6):
        x1, y1 = hex_points[i]
        x2, y2 = hex_points[(i + 1) % 6]
        
        # Line to point distance calculation
        dx1 = ball_pos[0] - x1
        dy1 = ball_pos[1] - y1
        dx2 = ball_pos[0] - x2
        dy2 = ball_pos[1] - y2
        cross_product = dx1 * dy2 - dy1 * dx2
        distance = abs(cross_product) / math.hypot(x2 - x1, y2 - y1)
        
        if distance < ball_radius:
            ball_pos[1] = y1 - ball_radius  # Set ball on top of the line
            ball_velocity[1] = -ball_velocity[1] * 0.8  # Bounce effect
            break  # Exit the loop once the ball collides

    # Draw hexagon
    pygame.draw.polygon(screen, LIME, hex_points, 3)

    # Draw ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()