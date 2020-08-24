# coding: utf-8

# Imports
import pygame

# Additional code


# Pygame init
pygame.init()

# Set screen size variables
width = 500
height = 500
# Create the screen
screen = pygame.display.set_mode((width, height))
# Change the window name
pygame.display.set_caption("SavalFer")


# Main loop
def main():
    """
        Main game loop
    """
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


if __name__ == "__main__":
    main()
