import cv2 as cv
import pytesseract

# Passign the location of tesseract.exe file
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Reading the image
img = cv.imread('Images/8.png')
# Converting into RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Printing the text from the image
print(pytesseract.image_to_string(rgb))

## Detecting the charactes:

# Defining the locaion of the character
hImg, wImg, _ = rgb.shape
boxes = pytesseract.image_to_boxes(rgb)

# Drawing a red boxes around character and showing a character
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv.rectangle(rgb, (x, hImg-y), (w, hImg-h), (0, 0, 255), 3)
    cv.putText(rgb, b[0], (x, hImg-y+30), cv.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)


## Detecting the Words:

# Defining the locaion of the character
hImg, wImg, _ = rgb.shape
boxes = pytesseract.image_to_data(rgb)

# Drawing a red boxes around character and showing a character
# for x, b in enumerate(boxes.splitlines()):
    # if x != 0:
        # b = b.split()
        # if len(b) == 12:  
            # x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            # cv.rectangle(rgb, (x, y), (w+x, y+h), (0, 0, 255), 3)
            # cv.putText(rgb, b[11], (x-10, y), cv.FONT_HERSHEY_COMPLEX_SMALL, 5, (0, 255, 0), 2)

cv.imshow('RGB image', rgb)
cv.waitKey(0)
