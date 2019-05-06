import numpy as np
import cv2
from matplotlib import pyplot as plt
# cap = cv2.imread("dataset/co/00000007_co.png")

#simple thresholding
# k = 1
# t = 200
# blur = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(blur, (k, k), 0)
# (t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)
# mask = cv2.merge([maskLayer, maskLayer, maskLayer])
# sel = cv2.bitwise_and(cap, mask)
# cv2.imshow("orig", cap)
# cv2.imshow("mask", mask)
# cv2.imshow("selected", sel)
# cv2.waitKey()
# cv2.destroyAllWindows()

#adaptive thresholding
# k = 1
# t = 180
# blur = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(blur, (k, k), 0)
# (t, maskLayer) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY +
# 	cv2.THRESH_OTSU)
# mask = cv2.merge([maskLayer, maskLayer, maskLayer])
# sel = cv2.bitwise_and(cap, mask)
# cv2.imshow("orig", cap)
# cv2.imshow("mask", mask)
# cv2.imshow("selected", sel)
# cv2.waitKey()
# cv2.destroyAllWindows()
