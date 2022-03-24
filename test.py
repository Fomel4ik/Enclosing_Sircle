import cv2
import numpy as np
import math

def find_contours(img, color):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(img_hsv, color[0], color[1])
    contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

image = cv2.imread('Images/pool_two_bins.jpg')
drawing = image.copy()

color = (
            (30, 8, 0),
            (70, 200, 255)
        )

contours =  find_contours(image, color)

for contour in contours:
    contour_area = cv2.contourArea(contour)
    if contour_area >= 100:
        print('Площадь контура:', contour_area)
        cv2.drawContours(drawing, [contour], 0, (255, 255, 255), 3)
        (circle_x, circle_y), circle_radius = cv2.minEnclosingCircle(contour)
        circle_area = math.pi * circle_radius ** 2
        print('Полощадь круга:', circle_area)
        cv2.circle(drawing, (int(circle_x), int(circle_y)), int(circle_radius), (255, 255, 0), 3)


cv2.imshow('output', drawing)
cv2.waitKey(0)