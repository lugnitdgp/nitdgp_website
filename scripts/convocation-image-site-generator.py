#!/usr/bin/env python3

from PIL import Image
from os import listdir, mkdir
from pathlib import Path

BASE_DIR = "/var/www/html/convocation-images/"

if not Path(BASE_DIR).exists():
    print(BASE_DIR, "is not accessible")
    exit(-1)

def check_image_type(x):
    return x.endswith('JPG') or x.endswith('jpg') or x.endswith('jpeg')

def change_file_destination(x):
    x = x.split('/')
    x[0] += "-small"
    return "/".join(x)

n = int(input("Enter number of sets of images: "))
image_dirs = list(map(lambda x: "SET" + str(x), range(1, n + 1)))
image_files = []

for i in image_dirs:
    image = listdir(BASE_DIR + i)   # List files in each set
    image_files += map(lambda x: i + "/" + x, filter(check_image_type , image))
print("Got", len(image_files), "images to generate")

confirm = input("Resize all the images? [y/n]")
if confirm != 'y':
    print("Action cancelled")
    exit(0)

destination_files = list(map(change_file_destination, image_files))

# Make the destination location
for i in image_dirs:
    path = BASE_DIR + i + "-small"
    if not Path(path).exists():
        print("Creating directory", path)
        mkdir(path)

# Resize the images
try:
    for i in range(len(image_files)):
        source = BASE_DIR + image_files[i]
        destination = BASE_DIR + destination_files[i]
        if not Path(destination).exists():
            print("[" + str(i + 1) + "] Resizing", source, end=" ")
            foo = Image.open(source)
            foo = foo.resize((int(foo.size[0] / 15), int(foo.size[1] / 15)), Image.ANTIALIAS)
            foo.save(destination, optimize=True)
            print("Done")
except KeyError:
    print("Invalid image type")
except IOError:
    print("Unable to write to file")
