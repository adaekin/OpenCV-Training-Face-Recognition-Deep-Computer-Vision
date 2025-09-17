import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model


test_path = r'C:\Users\adaek\Desktop\OPENCVcourse\simpsons_dataset\bart_simpson\pic_0003.jpg'
img = cv.imread(test_path)

char_path = r'C:\Users\adaek\Desktop\OPENCVcourse\simpsons_dataset'

char_dict = {}

for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path,char)))

char_dict = caer.sort_dict(char_dict, descending=True)
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break

print(characters)
plt.imshow(img, cmap='gray')
IMG_SIZE = (80,80)
def prepare(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)
    img = caer. reshape(img,IMG_SIZE, 1)
    return img
model = load_model('simpsons_model.h5')
predictions = model.predict(prepare(img))

print(characters[np.argmax(predictions[0])])
plt.show()
