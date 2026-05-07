import pygame
import random

def main(): 
    pygame.init()
    pygame.display.set_caption("I Spy")
    resolution = (1920, 1080) 
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    running = False
        black = pygame.Color(0,0,0)
        screen.fill(black)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__": 
    main()