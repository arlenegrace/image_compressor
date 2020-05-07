import os
from PIL import Image, ImageFile
import numpy

ImageFile.LOAD_TRUNCATED_IMAGES = True
MAX_SIZE = 1000000 #max file size in bytes
MAX_RES = 1080 #maximum width or height, whichever is larger
SOURCE = "/DIR/HERE/"
DESTINATION = "/DIR/HERE/"
FILES = os.listdir(SOURCE)
FINISHED_IMAGES = []

#checks destination folder for already compressed images
for filename in os.listdir(DESTINATION):
    FINISHED_IMAGES.append(filename)

for filename in FILES:
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")): 
        continue

    if filename in FINISHED_IMAGES:
        continue

    img = Image.open(SOURCE + filename)
    size = img.size
    min_length = min(size)

    if min_length < MAX_RES:
        continue

    width, height = (MAX_SIZE, MAX_RES) if size[0] > size[1] else (MAX_RES, MAX_SIZE)

    img.thumbnail((width, height), Image.LANCZOS)
    img.save(DESTINATION + filename, quality=90)