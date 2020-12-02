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

cap = cv.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+h]

        # recognizer
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45 and conf <= 85:
            print(id_)
            print(labels[id_])
            cv.putText(frame, labels[id_], (x-15, y-10), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, 
                       cv.LINE_AA)
        img_item = "my_img.png"
        cv.imwrite(img_item, roi_gray)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
