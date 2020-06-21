# For Custom Class

import os 
import random
import game_config as gc

from pygame import image, transform

# Initialy all the animals count will be zero
animals_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_animals():
    # All animals whose count is less than two
    return [a for a, c in animals_count.items() if c < 2]

class Animal:
    def __init__(self, index):
        self.index = index
        # The tiles are arranged as 
        # 0 1 2 3 
        # 4 5 6 7
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        
        # Select random animal
        self.name = random.choice(available_animals())
        
        # update the count in the dictionary 
        animals_count[self.name] += 1 
        
        # path of the ramdom image 
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        
        # load the image
        self.image = image.load(self.image_path)

        # Resize the image to display as desired size
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN))
        
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))
        
        # if the copy of the image is matched then skip
        self.skip = False