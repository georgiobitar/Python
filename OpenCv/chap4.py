import cv2
import numpy
import math

# 0 is black
width=512
w=3
nbofSquares=9
delta=int((((width*math.sqrt(2))/2)-nbofSquares*(2*w*math.sqrt(2)))/nbofSquares)

img = numpy.zeros((width, width, 3), numpy.uint8)
img1 = numpy.zeros((width, width, 3), numpy.uint8)
img2 = numpy.zeros((width, width, 3), numpy.uint8)
img3 = numpy.zeros((width, width, 3), numpy.uint8)

# print(img)
# img[200:300, 0:100] = 255, 0, 0


# Strong to Bright
for i in range(int(((width*math.sqrt(2))/2.8))):
    cv2.line(img, (i, i), (512-i, i), (i, 255, i), 3)
    cv2.line(img, (i, i), (i, 512-i), (i, 255, i), 3)
    cv2.line(img, (512-i, i), (512-i, 512-i), (i, 255, i), 3)
    cv2.line(img, (i, 512-i), (512-i, 512-i), (i, 255, i), 3)

cv2.imshow("Strong to Bright", img)

# Bright to Strong
for i in range(int(((width*math.sqrt(2))/2.8))):
    cv2.line(img1, (i, i), (512-i, i), (255-i, 255, 255-i), 3)
    cv2.line(img1, (i, i), (i, 512-i), (255-i, 255, 255-i), 3)
    cv2.line(img1, (512-i, i), (512-i, 512-i), (255-i, 255, 255-i), 3)
    cv2.line(img1, (i, 512-i), (512-i, 512-i), (255-i, 255, 255-i), 3)

cv2.imshow("Bright to Strong", img1)

# Patterns
for i in range(0, int(((width*math.sqrt(2))/2)), delta):
    cv2.line(img2, (i, i), (512-i, i), (i, 255-i, i+100), w)
    cv2.line(img2, (i, i), (i, 512-i), (i+20, 255-i-50, i+125), w)
    cv2.line(img2, (512-i, i), (512-i, 512-i), (i+40, 255-i-100, i+150), w)
    cv2.line(img2, (i, 512-i), (512-i, 512-i), (i+60, 255-i-150, i+175), w)

cv2.imshow("patterns", img2)

cv2.line(img3, (0, 0), (img3.shape[1], img3.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img3, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(img3, (400, 50), 30, (255, 0, 0), 5)
cv2.putText(img3, " OPENCV ", (300, 100), cv2.QT_FONT_NORMAL, 1, (0, 150, 0), 1)
cv2.imshow("a", img3)


cv2.waitKey(0)