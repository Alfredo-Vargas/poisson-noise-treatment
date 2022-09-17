import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img_location: str = '../images/img_2048x2494x15.jpg'
img = cv.imread(img_location)
cv.imshow('lungs', img)
cv.waitKey(0)
