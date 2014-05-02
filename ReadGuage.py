__author__ = 'paul'
import numpy as np
import cv2

#Set Colour Codes
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

# Load up image and convert it to greyscale - This needs to be taken from web cam
im = cv2.imread("guage.jpg")
gray_im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

# create version to draw on and blurredversion - blurred version makes it easier to
# distinguish the lines on the image
draw_im = cv2.cvtColor(gray_im, cv2.COLOR_GRAY2RGB)
blur = cv2.GaussianBlur(gray_im, (0,0), 5)

m, n = gray_im.shape

# Hough transform for circles use this to find all circles
# Maybe should update this to look for the strongest circle but working for the time being
circles = cv2.HoughCircles(gray_im, cv2.cv.CV_HOUGH_GRADIENT, 2, 10,
                           np.array([]), 20, 60, m/10)[0]

# Hough transform  to find the lines - Will restrict this to one
edges = cv2.Canny(blur, 20, 60)
lines = cv2.HoughLines(edges, 2, np.pi/90, 40)[0]
plines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, np.array([]), 10)[0]

# draw
for c in circles[:1]:
 # green for circles (only draw the strongest) - This May Need Messed about with
    ##Draw The Circle Outline
    cv2.circle(draw_im, (c[0], c[1]), c[2], green, 2)
    ##Put Red Dot In Centre Of Circle
    cv2.circle(draw_im, (c[0], c[1]), 2, red, 3)
    centreOfCircle = (c[0], c[1])

for (rho, theta) in lines[:1]:
 # blue for infinite lines (only draw the 5 strongest)
    x0 = np.cos(theta)*rho
    y0 = np.sin(theta)*rho
    pt1 = (int(x0 + (m+n)*(-np.sin(theta))), int(y0 + (m+n)*np.cos(theta)) )
    pt2 = (int(x0 - (m+n)*(-np.sin(theta))), int(y0 - (m+n)*np.cos(theta)) )
    cv2.line(draw_im, centreOfCircle, pt2, blue, 2)
    print pt1
    print pt2



"""
for l in plines:
 # red for line segments
    cv2.line(draw_im, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 2)
"""
cv2.imshow("circles", draw_im)
cv2.waitKey()

# save the resulting image
cv2.imwrite("res.jpg", draw_im)