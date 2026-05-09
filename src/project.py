import pygame
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
    screen.fill(pygame.Color(0,0,15))
    folder = "items"
    items = [ ]
    for filename in os.listdir(folder):
        image = os.path.join(folder, filename)
        img = pygame.image.load(image).convert_alpha()
        img_final = pygame.transform.scale(img, (100, 100))
        x_coord = random.randrange(300, 1500)
        y_coord = random.randrange(200, 800)
        screen.blit(img_final, (x_coord, y_coord))
        # bounding box for item for point and click potentially
        rect = img_final.get_rect(topleft=(x_coord, y_coord))
        mask = pygame.mask.from_surface(img_final)
        name, ext = os.path.splitext(filename)
        print(name)

        items.append((rect, mask, name))
    
    selected_item = random.randrange(0, len(items))
    (rect, mask, name) = items[selected_item]
    # print("I spy with my little eye ... a " + filename + "!")
    return True, (rect, mask, name)

def main(): 
    pygame.init()
    pygame.display.set_caption("I Spy")
    resolution = (1920, 1080) 
    screen = pygame.display.set_mode(resolution)
    running = True
    items_placed = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gamestate == "play":
                    mx, my = pygame.mouse.get_pos()
                    distance_x = mx - selected_rect.x
                    distance_y = my - selected_rect.y 
                    if 0 <= distance_x < selected_rect.width and 0 <= distance_y < selected_rect.height: 
                        if selected_mask.get_at((distance_x, distance_y)):
                            gamestate = "win"
                # if [point and click on the proper image] 
        # play game :) 
        gamestate = "play"
        font = pygame.font.SysFont("Arial", 32)
        if(gamestate == "play"):
            if not items_placed:
                items_placed, (return_rect, return_mask, return_filename) = item_placement(screen)
                selected_rect = return_rect
                selected_mask = return_mask
                selected_filename = return_filename 
                instruction = font.render(("I spy with my little eye ... a " + selected_filename + "!"), True, (255, 255, 255))
                instruction_rect = instruction.get_rect(center=(960, 900))
                screen.blit(instruction, instruction_rect)
        if(gamestate == "win"): 
            screen.fill(pygame.Color(0,100,0))
            text = font.render("You found it!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(960,540))
            screen.blit(text, text_rect)
            #game reset
            items_placed = False
            selected_rect = None
            selected_mask = None
            selected_filename = ""
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__": 
    main()