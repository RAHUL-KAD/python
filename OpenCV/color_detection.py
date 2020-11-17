import cv2 as cv
import numpy as np
# we will be detecting the color in the image


# Creating a trackbars to get the correct value of the color which we want to show
# maximum value of trackbars is 360 but in opencv maximum value of trackbars is 179

def empty(a):
    pass

cv.namedWindow('Trackbars')
cv.resizeWindow('Trackbars', 640, 240)
cv.createTrackbar('Hue min', 'Trackbars', 0, 179, empty)
cv.createTrackbar('Hue max', 'Trackbars', 179, 179, empty)
cv.createTrackbar('Sat min', 'Trackbars', 0, 255, empty)
cv.createTrackbar('Sat max', 'Trackbars', 255, 255, empty)
cv.createTrackbar('Val min', 'Trackbars', 0, 255, empty)
cv.createTrackbar('Val max', 'Trackbars', 255, 255, empty)

# Now we will read trackbar values so we can apply them on our image
while True:
    # Reading a image
    img = cv.imread('Images/doctor.png')
    # Converting image into HSV
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos('Hue min', 'Trackbars')
    h_max = cv.getTrackbarPos('Hue max', 'Trackbars')
    s_min = cv.getTrackbarPos('Sat min', 'Trackbars')
    s_max = cv.getTrackbarPos('Sat max', 'Trackbars')
    v_min = cv.getTrackbarPos('Val min', 'Trackbars')
    v_max = cv.getTrackbarPos('Val max', 'Trackbars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # To get the perticular color of the image we will create mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    # insted of black and white image we will get colored image using this method
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # showing an image
    cv.imshow('Colored image', img)
    cv.imshow('HSV image', imgHSV)
    cv.imshow('Masked image', mask)
    cv.imshow('Filtered colored image', imgResult)
    cv.waitKey(1)
