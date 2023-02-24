import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define UI elements
button = pygame.Rect(50, 50, 100, 50)
textbox = pygame.Rect(50, 150, 400, 50)
label = pygame.font.SysFont(None, 30).render('Gmail', True, (255, 255, 255))

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # Handle button click
                pass
    # Draw elements
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), button)
    pygame.draw.rect(screen, (255, 255, 255), textbox)
    screen.blit(label, (50, 10))
    # Update display
    pygame.display.flip()






