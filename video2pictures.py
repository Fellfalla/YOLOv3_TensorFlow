# coding: utf-8

from __future__ import division, print_function

import argparse
import cv2
import os


parser = argparse.ArgumentParser(description="YOLO-V3 test single image test procedure.")
parser.add_argument("--filepath", default=0,
                    help="Filepath of the video file")
args = parser.parse_args()


vidcap = cv2.VideoCapture(args.filepath)
folderpath, _ = os.path.splitext(args.filepath)
os.mkdir(folderpath)
success,image = vidcap.read()
count = 0
while success:
  # save every tenth frame
  if (count % 10) == 0:
    cv2.imwrite(os.path.join(folderpath, "frame%05i.jpg" % count), image)     # save frame as JPEG file
    print('Saved a new frame: ', success)
  success,image = vidcap.read()
  count += 1