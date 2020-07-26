#顏色
#4-14 plot + cv.calcHist() + BGR

# import cv2
# import matplotlib.pyplot as plt

# o = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png")

# histb = cv2.calcHist([o], [0], None, [256], [0, 255]) #cv2.calcHist(影像, 通道, 遮罩, 區間數量, 數值範圍)
# histg = cv2.calcHist([o], [1], None, [256], [0, 255])
# histr = cv2.calcHist([o], [2], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
# plt.plot(histr, color='r')
# plt.show()

#4-15 mask + cv2.calcHist()
# import cv2
# import numpy as np

# import matplotlib.pyplot as plt
# image = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image', image)
# mask = np.zeros(image.shape, np.uint8)
# mask[200:400, 200:400] = 255
# cv2.imshow('mask', mask)
# histImage = cv2.calcHist([image], [0], None, [256], [0, 255])
# histMI = cv2.calcHist([image], [0], mask, [256], [0, 255])
# plt.plot(histImage)
# plt.plot(histMI)
# plt.show()

#4-16 直方圖等化
# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("original", img)

# equ = cv2.equalizeHist(img)
# cv2.imshow("equ", equ)

# plt.figure("原始影像長條圖")
# plt.hist(img.ravel(), 256)
# plt.figure("均質化後長條圖")
# plt.hist(equ.ravel(), 256)
# plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-17 RGB 直方圖等化
# import numpy as np
# import cv2

# def RGB_histogram_equalization(f):
#     g = f.copy()
#     for k in range(3):
#         g[:,:,k] = cv2.equalizeHist(f[:, :, k])
#     return g

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/Rose.bmp", -1)
# img2 = RGB_histogram_equalization(img1)
# cv2.imshow("Original", img1)
# cv2.imshow("Histogram Equaliztaion(RGB)", img2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-18 HSV_histogram_equaliztaion
# import numpy as np
# import cv2

# def HSV_histogram_equaliztaion(f):
#     hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
#     hsv[:,:,2] = cv2.equalizeHist( hsv[:, :, 2])
#     g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#     return g

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0724/Rose.bmp", 1)
# img2 = HSV_histogram_equaliztaion(img1)
# cv2.imshow("Original", img1)
# cv2.imshow("Histogram Equaliztaion(HSV)", img2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-20 影像濾波 高斯模糊
# import numpy as np
# import cv2

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0726/Baboon.bmp", -1)
# img2 = cv2.GaussianBlur(img1, (5,5), 0) #(圖像, 遮罩大小)

# cv2.imshow("Original Image", img1)
# cv2.imshow( "Gaussian Filtering", img2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#4-22 HSV + 色彩分割
# import numpy as np
# import cv2

# def HSV_color_segmentation(f, H1, H2, S1, S2, V1, V2):
#     g = f.copy()
#     nr, nc = f.shape[:2]
#     hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
#     for x in range(nr):
#         for y in range(nc):
#             H = hsv[x, y, 0] * 2  #For HSV, Hue range is [0,179]
#             S = hsv[x, y, 1] / 255 * 100
#             V = hsv[x, y, 2] / 255 * 100
#             if not ( H >= H1 and H <= H2 and S >= S1 and S <= S2 and V >= V1 and V <= V2 ):
#                 g[x,y,0] = g[x,y,1] = g[x,y,2] = 0

#     return g

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0726/Flower.bmp", -1 )
# img2 = HSV_color_segmentation( img1, 30, 70, 30, 100, 30, 100 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "HSV Color Segmentation", img2 )
# cv2.waitKey()
# cv2.destroyAllWindows()

#4-23 cv2.inRange()
# import cv2
# import numpy as np

# img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)

# min_ = 100
# max_ = 200
# mask = cv2.inRange(img, min_, max_)
# print("img=\n", img)
# print("mask=\n", mask)

#4-24 cv2.inRange() ROI
# import cv2
# import numpy as np

# img = np.ones([5, 5], dtype=np.uint8)* 9
# mask = np.zeros([5, 5], dtype=np.uint8)
# mask[0:3, 0] = 1
# mask[2:5, 2:4] = 1
# roi = cv2.bitwise_and(img, img, mask=mask)
# print("img=\n", img)
# print("mask=\n", mask)
# print("roi=\n", roi)

#4-25 opencv Logo
# import cv2
# import numpy as np
# opencv = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0726/opencv.jpg")
# hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)
# cv2.imshow("opencv", opencv)

# minBlue = np.array([110, 50, 50])
# maxBlue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, minBlue, maxBlue)
# blue = cv2.bitwise_and(opencv, opencv, mask = mask)
# cv2.imshow("blue", blue)

# minGreen = np.array([50, 50, 50])
# maxGreen = np.array([70, 255, 255])
# maskGreen = cv2.inRange(hsv, minGreen, maxGreen)
# green = cv2.bitwise_and(opencv, opencv, mask = maskGreen)
# cv2.imshow("Green", green)

# minRed = np.array([0, 50, 50])
# maxRed = np.array([10, 255, 255])
# maskRed = cv2.inRange(hsv, minRed, maxRed)
# red = cv2.bitwise_and(opencv, opencv, mask = maskRed)
# cv2.imshow("Red", red)

# cv2.waitKey()

#4-26 標記人臉膚色
# import cv2

# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0726/face.jpg")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
# minHue = 5
# maxHue = 170
# hueMask = cv2.inRange(h, minHue, maxHue)
# minSat = 25
# maxSat = 166
# satMask = cv2.inRange(s, minSat, maxSat)
# mask = hueMask & satMask
# roi = cv2.bitwise_and(img, img, mask = mask)
# cv2.imshow("img", img)
# cv2.imshow("ROI", roi)
# cv2.waitKey()
# cv2.destroyAllWindows()

#幾何轉換 AffineTransform Perspective
#5-1 Scaling cv2.INTER_NEAREST cv2.INTER_LINEAR cv2.INTER_CUBIC
# import numpy as np
# import cv2

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", -1)
# nr, nc = img1.shape[:2]
# scale = eval(input("Please enter scale:"))
# nr2 = int(nr * scale)
# nc2 = int(nc * scale)
# img2 = cv2.resize(img1, (nr2, nc2), interpolation=cv2.INTER_NEAREST)
# img3 = cv2.resize(img1, (nr2, nc2), interpolation=cv2.INTER_LINEAR)
# img4 = cv2.resize(img1, (nr2, nc2), interpolation=cv2.INTER_CUBIC)
# cv2.imshow("Original", img1)
# cv2.imshow("Resize Nearest", img2)
# cv2.imshow("Resize Linear", img3)
# cv2.imshow("Resize Cubic", img4)
# cv2.waitKey()

#cv2.imread Flag Description
#https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80

#5-2
# import numpy as np
# import cv2
# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0726/Baboon.bmp", 0 )
# nr1, nc1 = img.shape[:2]
# nr2, nc2 = nr1 // 4, nc1 // 4
# img1 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_NEAREST )
# img1 = cv2.resize( img1, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
# img2 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_LINEAR )
# img2 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
# img3 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_CUBIC )
# img3 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_CUBIC )
# cv2.imshow( "Original Image", img )
# cv2.imshow( "Nearest Neighbor", img1 )
# cv2.imshow( "Bilinear", img2 )
# cv2.imshow( "Bicubic", img3 )
# cv2.waitKey( 0 )

#5-3 rotation
# import numpy as np
# import cv2

# img1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", -1)
# nr2, nc2 = img1.shape[:2]
# rotation_matrix = cv2.getRotationMatrix2D( ( nr2 / 2, nc2 / 2 ), 30, 1 )
# print(nr2, nc2)
# print(rotation_matrix)
# img2 = cv2.warpAffine( img1, rotation_matrix, ( nr2, nc2 ) )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Image Rotation", img2 )
# cv2.waitKey( 0 )

#5-5 AffineTransform 仿射變換
# import numpy as np
# import cv2

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0726/Poker.bmp", -1 )
# nr, nc = img1.shape[:2]
# pts1 = np.float32( [ [ 160, 165 ], [ 240, 390 ], [ 270, 125 ] ] )
# pts2 = np.float32( [ [ 190, 140 ], [ 190, 375 ], [ 310, 140 ] ] )

# T = cv2.getAffineTransform( pts1, pts2 )
# img2 = cv2.warpAffine( img1, T, ( nc, nr ) )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Affine Transform", img2 )
# cv2.waitKey( 0 )

#5-6 perspective 透視投影
# import numpy as np
# import cv2
# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0726/Gallery.bmp", -1 )
# nr, nc = img1.shape[:2]

# pts1 = np.float32( [ [ 795, 350 ], [ 795, 690 ], [ 1090, 720 ], [ 1090, 250 ] ] )
# pts2 = np.float32( [ [ 0, 0 ], [ 0, 500 ], [ 650, 500 ], [ 650, 0 ] ] )

# T = cv2.getPerspectiveTransform( pts1, pts2 ) #透視轉換矩陣
# print(T)
# img2 = cv2.warpPerspective( img1, T, ( 650, 500 ) )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Perspective Transform", img2 )

# cv2.waitKey( 0 )

# 6-4 convolution 卷積
# import numpy as np

# x = np.array( [ 1, 2, 4, 3, 2, 1, 1 ] )
# h = np.array( [ 1, 2, 3, 1, 1 ] )
# y = np.convolve( x, h, 'full' ) #取全部
# y1 = np.convolve( x, h, 'same' ) #取與位數相同的數量
# print( "x =", x )
# print( "h =", h )
# print( "Full Convolution y =", y ) 
# print( "Convolution y =", y1 )

#6-5 convolution 2D
import numpy as np
from scipy.signal import convolve2d

x = np.array( [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ] )
h = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
y = convolve2d( x, h, 'same' )
print( "x =" )
print( x )
print( "h =" )
print( h )
print( "Convolution y =" )
print( y )