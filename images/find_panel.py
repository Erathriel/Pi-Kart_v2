# import the necessary packages
import numpy as np
import cv2
 
# load the image
image = cv2.imread("feu-vert.jpg")
 
# find the red color in the image
# upper = np.array([65, 65, 255])
# lower = np.array([0, 0, 200])

#find the green color
upper = np.array([30, 255, 0])
lower = np.array([0, 40, 0])
mask = cv2.inRange(image, lower, upper)
 
# find contours in the masked image and keep the largest one
(_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv2.contourArea)
 
# approximate the contour
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.005 * peri, True)
 
# draw a green bounding box surrounding the red or green
cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)
