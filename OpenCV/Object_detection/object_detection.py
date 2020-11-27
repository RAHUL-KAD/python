import cv2 as cv

img = cv.imread('Images/c.jpg')
# Storing the names of different objects in classnames list
# we can directly give names also but it will be lenghty
classnames = []
# Reading the file from the directory
classFile = 'Code/Object_detection/coco.names'
with open(classFile, 'rt') as f:
    classnames = f.read().rstrip('\n').split('\n')    
# print(classnames)

# Configuring the pathes of the files
confiPath = 'Code/Object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'Code/Object_detection/frozen_inference_graph.pb'

# This function already provides us all the information about object detection
net = cv.dnn_DetectionModel(weightPath, confiPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Now we need to send our image to model
classIds, confs, boundryBox = net.detect(img, confThreshold=0.5)
print(classIds, boundryBox)

# Now we will store value of each image into single variable
if len(classIds) != 0:
    for classId, configure, box in zip(classIds.flatten(), confs.flatten(), boundryBox):
        cv.rectangle(img, box, color=(0, 255, 0), thickness=3)
        cv.putText(img, classnames[classId-1].upper(), (box[0]+10, box[1]+30), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

cv.imshow('Output', img)
cv.waitKey(0)