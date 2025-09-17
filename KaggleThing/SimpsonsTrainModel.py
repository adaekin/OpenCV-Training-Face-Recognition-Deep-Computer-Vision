import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt

IMG_SIZE = (80,80)
channels = 1
char_path = r'C:\Users\adaek\Desktop\OPENCVcourse\simpsons_dataset'

char_dict = {}

for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path,char)))

# Sort in descending

char_dict = caer.sort_dict(char_dict, descending=True)
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break

print(characters)


# Create the training data

train = caer.preprocess_from_dir(char_path, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True)
np.save('train.npy', train)

