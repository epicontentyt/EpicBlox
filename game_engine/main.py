import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('EpicBlox Game Engine')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    window.fill((0, 0, 0))
    
    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
