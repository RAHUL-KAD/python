import cv2 as cv
import pickle

# Haar cascade is a trined data.
haar_cascade = cv.CascadeClassifier('Code/haar_face_detection.xml')
# We first build this recognizer in faces_train.py file
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Loading the lebles for image
labels = {}
with open('labels.pickle', 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

# Reading the image
img = cv.imread('Code/Face_recognation/1.jpg')
# Converting into gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Detecting face in the image
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

for (x, y, w, h) in faces:
    # print(x, y, w, h)
    roi_gray = gray[y:y+h, x:x+h]
    # Recognizer
    id_, conf = recognizer.predict(roi_gray)
    print(id_)
    print(labels[id_])
    # putting text of each person on image
    cv.putText(img, labels[id_], (x, y-20), cv.FONT_HERSHEY_SIMPLEX, 1, (0,215,255), 2, cv.LINE_AA)
    # Drawing a rectangle
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Showing the image
    cv.imshow('Friends Cast', img)
    # Holding the image on screen
    cv.waitKey(0)
