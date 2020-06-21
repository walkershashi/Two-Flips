import os

IMAGE_SIZE = 128 # size of one image
SCREEN_SIZE = 512 # size of screen
NUM_TILES_SIDE = 4 # number of image on one side
NUM_TILES_TOTAL  = 16 # Total number of images
MARGIN = 4 # gap between images  

ASSET_DIR = "assets"
ASSET_FILES = [i for i in os.listdir(ASSET_DIR) if i[-3:].lower() == 'png']

assert len(ASSET_FILES) == 8
