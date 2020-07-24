#4-1 RGB 色彩模型
# import numpy as np
# import cv2

# def RGB_model(f, channel):
#     if channel == 1:    #Red
#         return f[:, :, 2]
#     elif channel == 2:  #Green
#         return f[:, :, 1]
#     else:               #Blue
#         return f[:, :, 0]


# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/Rose.bmp", -1)
# R = RGB_model(img, 1)
# G = RGB_model(img, 2)
# B = RGB_model(img, 3)

# cv2.imshow("Original", img)
# cv2.imshow("Red", R)
# cv2.imshow("Green", G)
# cv2.imshow("Blue", B)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-2 CMY 色彩模型
# import numpy as np
# import cv2

# def CMY_model(f, channel):
#     if (channel == 1):
#         return 255 - f[:, :, 2]
#     elif (channel == 2):
#         return 255 - f[:, :, 1]
#     else:
#         return 255 - f[:, :, 0]

# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/Rose.bmp", -1)
# C = CMY_model(img, 1)
# M = CMY_model(img, 2)
# Y = CMY_model(img, 3)

# cv2.imshow("Original", img)
# cv2.imshow("Cyan", C)
# cv2.imshow("Magenta", M)
# cv2.imshow("Yellow", Y)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-4 HSV 色彩模型
# import numpy as np
# import cv2

# def HSV_model(f, channel):
#     hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
#     if channel == 1:    #Hue
#         return hsv[:, :, 0]
#     elif channel == 2:   #Saturation
#         return hsv[:, :, 1]
#     else:               #Value
#         return hsv[:, :, 2]

# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/Rose.bmp", -1)
# H = HSV_model(img, 1)
# S = HSV_model(img, 2)
# V = HSV_model(img, 3)

# cv2.imshow("Original", img)
# cv2.imshow("Hue", H)
# cv2.imshow("Saturation", S)
# cv2.imshow("Value", V)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-7
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0719/boat.bmp")
# o = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/graydog.jpg")
cv2.imshow("original", o)

plt.hist(o.ravel(), 256) #hist Histogram 直方圖 二維轉一維灰階圖
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()