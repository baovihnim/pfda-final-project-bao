import pygame
from PIL import Image
import random
import os

# grab images from image folder 
# randomize image coordinates while also preventing overlap
# random select an image to be the "object to find" 
# make the coordinates of selected image clickable/the area being clicked makes pygame running = false
# message to player of "I spy with my little eye... something [image/object name]!" pull file name and strip .png

# item counter / multiple items spied in one instance? 
# selecting designated coordinates then would change the counter and edit the image selected, rather than leading immediately for an end game

# def image_resize():
    # for filename in os.listdir(folder):

def item_placement(screen): 
    screen.fill(pygame.Color(0,0,0))
    folder = "items"
    for filename in os.listdir(folder):
        image = os.path.join(folder, filename)
        img = pygame.image.load(image).convert_alpha()
        img_final = pygame.transform.scale(img, (100, 100))
        x_coord = random.randrange(50, 1800)
        y_coord = random.randrange(50, 1000)
        screen.blit(img_final, (x_coord, y_coord))
    pygame.display.flip()

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
           # else event.type == pygame.MOUSEBUTTONDOWN: 
                # if [point and click on the proper image] 
                    #running = False
        # play game :) 
        gamestate = "play"
        if(gamestate == "play"):
            item_placement(screen)
        
    pygame.quit()

if __name__ == "__main__": 
    main()