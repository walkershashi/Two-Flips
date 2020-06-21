import pygame
import game_config as gc
from animal import Animal
from time import sleep

from pygame import display, event, image

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption("Matchers")
name = input("Player's Name: ")
cnt = 0

# Return a screen which is a surface object of the desired size
screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')

"""
# Blit method displays an image on another surface 
screen.blit(matched, (0, 0))
# Displayes an updated screen after the match
display.flip() 
"""
running = True

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

current_images = []

"""
event module let us get a list of all the keyboard 
and mouse events with the help of get function and all the events 
fetched from the events queue from this function will be removed
from the queue and returned as a list
"""

while running:
    current_events = event.get()

    for e in current_events:
        # When we close the window QUIT variable is generated 
        # which is defined in the pygame module
        if e.type == pygame.QUIT:
            running = False
        
        # If the escape character is pressed then quit
        # keydown = keyboard character
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        
        # handling mouse character events
        if e.type == pygame.MOUSEBUTTONDOWN:
            cnt += 1

            # get the position of the mouse cursor 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            index = find_index(mouse_x, mouse_y)
            
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]
            
    
    screen.fill((255, 255, 255))

    total_skipped = 0

    for _, tile in enumerate(tiles):
        image_i = tile.image if tile.index in current_images else tile.box
        
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1
    
    display.flip()

    if len(current_images) == 2:
        index1, index2 = current_images
        if tiles[index1].name == tiles[index2].name:
            tiles[index2].skip = True
            tiles[index1].skip = True
            sleep(0.4)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.4)
            current_images = []

    if total_skipped == len(tiles):
        running = False

score_file = open('score_file.txt', 'a')
score_file.write("{}: {}".format(name, cnt)) 
score_file.write("\n")
score_file.close()
print("{} your total moves are {}".format(name, cnt))
print("Goodbye")