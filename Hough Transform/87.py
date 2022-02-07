
# Probabilistic_hough_transform -- using mathematical formular to complete a shape

# step 1: edge dtection
# step 2: mappign of edges to hough space and store it
# step 3: interpret storage edges to give line
# step 4: convert infinite lines to finite lines

import cv2
import numpy as np

img = cv2.imread('road.png')
#img = cv2.imread('road1.jpg')
#img = cv2.imread('road2.jpg')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)   # 200 represents the threshold parameter

cv2.imshow("edges", edges)

for line in lines:

    x1, y1, x2, y2 = line[0]

    cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2)



cv2.imshow("lines", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
