import cv2
import numpy

img = cv2.imread("Resources/me.jpg")
kernel = numpy.ones((5, 5), numpy.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      # Converting img colors
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 200, 150)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


cv2.imshow("Gray Image", imgGray) 
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Erosion Image", imgEroded)