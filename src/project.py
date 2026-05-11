import pygame
import random
import os

# TO-DO:
# proper menu screen? 
# item counter / multiple items spied in one instance? 
# selecting designated coordinates then would change the counter and edit the image selected, rather than leading immediately for an end game

pygame.init()
pygame.display.set_caption("I Spy")
resolution = (1920, 1080) 
screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont("Comic Sans MS", 32)

def placement():
    x_coord = random.randrange(400, 1400)
    y_coord = random.randrange(200, 700)
    return (x_coord, y_coord)

def item_placement(level): 
    screen.fill(pygame.Color(0,0,15))
    folder = "items"
    level_folder = level 
    img_path = os.path.join(folder, level_folder)
    items = [ ]
    for filename in os.listdir(img_path):
        image = os.path.join(folder, level_folder, filename)
        img = pygame.image.load(image).convert_alpha()
        if img.width > img.height:
            divider = img.width // 150
        else:
            divider = img.height // 150
        new_width = img.width // divider
        new_height = img.height // divider
        img_final = pygame.transform.scale(img, (new_width, new_height))
        
        i = 0
        while i < 1000: 
            x_coord, y_coord = placement()
            img_rect = pygame.Rect(x_coord, y_coord, new_width, new_height)
            rects = []
            for (rect, mask, name) in items:
                item_rect = pygame.Rect((rect))
                rects.append(item_rect)
            if pygame.Rect.collidelistall(img_rect, rects) == []:
                break
            i += 1
        screen.blit(img_final, (x_coord, y_coord))
        
        rect = img_final.get_rect(topleft=(x_coord, y_coord))
        mask = pygame.mask.from_surface(img_final)
        name, ext = os.path.splitext(filename)
    
        items.append((rect, mask, name))
    
    selected_item = random.randrange(0, len(items))
    (rect, mask, name) = items[selected_item]
    return True, (rect, mask, name)

def game(items_placed, level, win_counter):
    
    #gamestate = "play"
    #if(gamestate == "play"):
        if not items_placed:
            items_placed, (return_rect, return_mask, return_filename) = item_placement(level)
            selected_rect = return_rect
            selected_mask = return_mask
            selected_filename = return_filename 
            instruction = font.render(("I spy with my little eye ... a " + selected_filename + "!"), True, (255, 255, 255))
            instruction_rect = instruction.get_rect(center=(960, 900))
            screen.blit(instruction, instruction_rect)

        return (selected_rect, selected_mask)

def win(win_counter): 
    screen.fill(pygame.Color(0,50,15))
    text = font.render((f"YOU FOUND IT!\n\nitems found: {win_counter}"), True, (255, 255, 255))
    text_rect = text.get_rect(center=(960,540))
    screen.blit(text, text_rect)
    return True

def main(): 
    running = True
    items_placed = False
    #gamestate = "start"
    win_counter = 0
    #if (gamestate == "start"): 
        # start_message = font.render("I SPY ...\n\nPRESS SPACE TO START\npress esc to quit", True, (255, 255, 255))
    start_message = font.render("I SPY ...\n\npress esc to quit", True, (255, 255, 255))
    start_rect = start_message.get_rect(center=(960,540))
    screen.blit(start_message, start_rect)

    one_button = pygame.Rect(300, 300, 200, 50)
    two_button = pygame.Rect(300, 380, 200, 50)

    pygame.draw.rect(screen, (0,50,15), one_button)
    pygame.draw.rect(screen, (0,50,15), two_button)

    one_text = font.render("Theme 1", True, (255, 255, 255))
    two_text = font.render("Theme 2", True, (255, 255, 255))

    screen.blit(one_text, (335, 305))
    screen.blit(two_text, (335, 385))
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    running = False 
                # if event.key == pygame.K_BACKSPACE:
                    #return to menu
                if (wins == True): 
                    if event.key == pygame.K_SPACE: 
                        selected_rect, selected_mask = game(items_placed, "one", win_counter)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if(gamestate != "play"):
                        
                    if one_button.collidepoint(pygame.mouse.get_pos()) == True:
                        #gamestate = "play"
                        selected_rect, selected_mask = game(items_placed, "one", win_counter)
                        
                    if two_button.collidepoint(pygame.mouse.get_pos()) == True:
                        #gamestate = "play"
                        selected_rect, selected_mask = game(items_placed, "two", win_counter)

                    mx, my = pygame.mouse.get_pos()
                    distance_x = mx - selected_rect.x
                    distance_y = my - selected_rect.y 
                    if 0 <= distance_x < selected_rect.width and 0 <= distance_y < selected_rect.height: 
                        if selected_mask.get_at((distance_x, distance_y)):
                           win_counter += 1
                           wins = win(win_counter)
        # play game :) 
        #if(gamestate == "play"):
            #if not items_placed:
                #items_placed, (return_rect, return_mask, return_filename) = item_placement()
                #selected_rect = return_rect
                #selected_mask = return_mask
                #selected_filename = return_filename 
                #instruction = font.render(("I spy with my little eye ... a " + selected_filename + "!"), True, (255, 255, 255))
                #instruction_rect = instruction.get_rect(center=(960, 900))
                #screen.blit(instruction, instruction_rect)
        #if(gamestate == "win"): 
            #screen.fill(pygame.Color(0,50,15))
            #text = font.render((f"YOU FOUND IT!\n\nitems found: {win_counter}"), True, (255, 255, 255))
            #text_rect = text.get_rect(center=(960,540))
            #screen.blit(text, text_rect)
            ## game reset
            #items_placed = False
            #selected_rect = None
            #selected_mask = None
            #selected_filename = ""
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__": 
    main()