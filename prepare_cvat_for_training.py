import os
import argparse
import re
import random

parser = argparse.ArgumentParser(description="")
parser.add_argument("--folderpath", default=0,
                    help="Folderpath of the cvat files")
args = parser.parse_args()

x_resolution = 1280
y_resolution = 720

def get_jpg_path(textfile):
    return textfile.replace('.txt', '.jpg')

train_fn = os.path.join(args.folderpath, 'train.txt')
eval_fn = os.path.join(args.folderpath, 'eval.txt')
with open(train_fn, 'w') as trainfile, open(eval_fn, 'w') as evalfile:
    framenames = []
    for root, dirs, files in os.walk(args.folderpath):
        for filename in files:
            if re.match(r"frame\d{5}.txt", filename):
                framenames.append(os.path.join(root, filename))
    for index, filename in enumerate(framenames):
        filepath = os.path.join(args.folderpath, filename)
        jpg_path = get_jpg_path(filename)
        outputstring = f"{index} {jpg_path} {x_resolution} {y_resolution}"
        with open(filepath) as readfile:
            for line in readfile:
                category, x, y, width, height = line.split(' ')
                width = width[:-1] # remove new line
                x = float(x)
                y = float(y)
                height = float(height)
                width = float(width)
                x1 = x - (width/2)
                y1 = y - (height/2)
                x2 = x + (width/2)
                y2 = y + (height/2)
                outputstring += f" {category} {int(x1*x_resolution)} {int(y1*y_resolution)} {int(x2*x_resolution)} {int(y2*y_resolution)}"
        if random.randint(0, 9) != 0:
            trainfile.write(outputstring + '\n')
        else:
            evalfile.write(outputstring + '\n')
