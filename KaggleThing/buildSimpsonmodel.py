import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical


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

trained = np.load('train.npy', allow_pickle= True)

plt.figure(figsize=(30,30))
plt.imshow(trained[0][0], cmap='gray')
plt.show()

featuresSet, labels = caer.sep_train(trained, IMG_SIZE=IMG_SIZE)


# Normalize the FeatureSet ==> (0,1)

featuresSet = caer.normalize(featuresSet)
labels = to_categorical(labels, len(characters))

x_train, x_val, y_train, y_val = caer.train_val_split(featuresSet, labels, val_ratio= .2)

del trained 
del featuresSet
del labels
gc.collect()

BATCH_SIZE=32
EPOCHS = 10


datagen = canaro.generators.imageDataGenerator()
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)

model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dim=len(characters), loss='binary_crossentropy', decay=1e-6, learning_rate=0.001, momentum=0.9, nesterov=True)
model.summary()

model.save('simpsons_model.h5')