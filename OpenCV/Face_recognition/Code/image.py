import cv2 as cv
import pickle

haar_cascade = cv.CascadeClassifier('Code/haar_face_detection.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Loading the lebles for image
labels = {}
with open('labels.pickle', 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

img = cv.imread('Code/Face_recognation/8.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

for (x, y, w, h) in faces:
    # print(x, y, w, h)
    roi_gray = gray[y:y+h, x:x+h]
    # Recognizer
    id_, conf = recognizer.predict(roi_gray)
    print(id_)
    print(labels[id_])
    cv.putText(img, labels[id_], (x-20, y-20), cv.FONT_HERSHEY_SIMPLEX, 1, (0,215,255), 2, cv.LINE_AA)
    img_item = "my_img.png"
    cv.imwrite(img_item, roi_gray)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Friends Cast', img)
    cv.waitKey(0)
