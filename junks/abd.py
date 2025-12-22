import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Message Display")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font settings
font = pygame.font.Font(None, 100)  # Default font, size 100
text = font.render("KYS BRO", True, RED)  # Render text in red
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

# Main loop
running = True
while running:
    screen.fill(BLACK)  # Fill screen with black
    screen.blit(text, text_rect)  # Draw text

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update screen

pygame.quit()
import pandas as pd
