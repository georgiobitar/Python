import cv2
import numpy

img = cv2.imread("Resources/me.jpg")
imgResize = cv2.resize(img, (200, 100))

print(img.shape)
print(imgResize.shape)

imgCropped=img[0:206, 206:512]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)