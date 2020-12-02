import os
import cv2 as cv
import numpy as np
from PIL import Image
import pickle

# Geeting the location file faces.train.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Geeting the location of all the faces
image_dir = os.path.join(BASE_DIR, "Faces")

haar_cascade = cv.CascadeClassifier('Code/haar_face_detection.xml')

# Training the model
recognizer = cv.face.LBPHFaceRecognizer_create()

# For new label
current_id = 0
# Dictionary
lable_ides = {}
y_label = []
x_train = []
# Accessing the location of each and every image
for root, dir, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            # Label of each image
            label = os.path.basename(root).replace(' ', '-').lower()
            # print(label, path)
            # creating a label for each person
            if label not in lable_ides:
                lable_ides[label] = current_id
                current_id += 1
            id_ = lable_ides[label]
            # print(lable_ides)

            # y_label.append(label)  # Some Number
            # x_train.append(path)  # verify this image, turn into numpy array, gray
            # Opening the image
            pil_image = Image.open(path).convert('L')  # Grayscale
            # resizing the image -- sometime it doesn't work properly so we have to resize the image
            # size = (550, 550)
            # final_image = pil_image.resize(size, Image.ANTIALIAS)
            img_array = np.array(pil_image)
            # print(img_array)
            faces = haar_cascade.detectMultiScale(img_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = img_array[y:y+w, x:x+h]
                x_train.append(roi)
                y_label.append(id_)

# print(y_label)
# print(x_train)

# Saving the labels
with open('labels.pickle', 'wb') as f:
    pickle.dump(lable_ides, f)

recognizer.train(x_train, np.array(y_label))
recognizer.save('trainer.yml')