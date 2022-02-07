# hough_transform -- using mathematical formular to complete a shape

# step 1: edge dtection
# step 2: mappign of edges to hough space and store it
# step 3: interpret storage edges to give line
# step 4: convert infinite lines to finite lines

import cv2
import numpy as np

img = cv2.imread('sudoku.png')
cv2.imshow("Image", img)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey, 50, 100, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)   # 200 represents the threshold parameter


for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    # x1 stores rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores rounded off value of (r * cos(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)



cv2.imshow("lines", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
