#6-6 平均濾波
# import numpy as np
# import cv2

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", -1)
# img3 = cv2.blur(img1, (3, 3)) #模糊化
# img5 = cv2.blur(img1, (5, 5)) #模糊化
# img7 = cv2.blur(img1, (7, 7)) #模糊化

# cv2.imshow("Orginal", img1)
# cv2.imshow("Average Filtering3", img3)
# cv2.imshow("Average Filtering5", img5)
# cv2.imshow("Average Filtering7", img7)
# cv2.waitKey( 0 )

#6-7 Gaussian 高斯模糊
# import numpy as np
# import cv2

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", -1)
# imgB5 = cv2.blur(img1, (5, 5)) #模糊化
# imgGB5 = cv2.GaussianBlur(img1, (5, 5), 0) #高斯模糊

# cv2.imshow("Orginal", img1)
# cv2.imshow("Average Filtering5", imgB5)
# cv2.imshow("Gaussian Blur5", imgGB5)

# cv2.waitKey( 0 )

#6-8 Graident 梯度
# import numpy as np
# import cv2

# def Sobel_gradient( f, direction = 1 ):
#     sobel_x = np.array( [ [-1,-2,-1], [ 0, 0, 0], [ 1, 2, 1] ] )
#     sobel_y = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
#     if direction == 1:
#         grad_x = cv2.filter2D( f, cv2.CV_32F, sobel_x )
#         gx = abs( grad_x )
#         g = np.uint8( np.clip( gx, 0, 255 ) )
#     elif direction == 2:
#         grad_y = cv2.filter2D( f, cv2.CV_32F, sobel_y )
#         gy = abs( grad_y )
#         g = np.uint8( np.clip( gy, 0, 255 ) )
#     else:
#         grad_x = cv2.filter2D( f, cv2.CV_32F, sobel_x )
#         grad_y = cv2.filter2D( f, cv2.CV_32F, sobel_y )
#         magnitude = abs( grad_x ) + abs( grad_y )
#         g = np.uint8( np.clip( magnitude, 0, 255 ) )
#     return g

# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1)
# gx = Sobel_gradient( img, 1 )
# gy = Sobel_gradient( img, 2 )
# g = Sobel_gradient( img, 3 )
# cv2.imshow( "Original Image", img )
# cv2.imshow( "Gradient in x", gx )
# cv2.imshow( "Gradient in y", gy )
# cv2.imshow( "Gradient", g )
# cv2.waitKey( 0 )

#6-9 laplacian 拉普拉斯運算子 銳利化
# import numpy as np
# import cv2
# def laplacian( f ):
#     temp = cv2.Laplacian( f, cv2.CV_32F ) + 128
#     g = np.uint8( np.clip( temp, 0, 255 ) )
#     return g

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1 )
# img2 = laplacian( img1 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Laplacian", img2 )
# cv2.waitKey( 0 )

#6-10 Composite Laplacian 混合拉普拉斯運算子
# import numpy as np
# import cv2

# def composite_laplacian( f ):
#     kernel = np.array( [ [0, -1, 0], [-1, 5, -1], [0, -1, 0] ] )
#     temp = cv2.filter2D( f, cv2.CV_32F, kernel )
#     g = np.uint8( np.clip( temp, 0, 255 ) )
#     return g

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1 )
# img2 = composite_laplacian( img1 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Composite Laplacian", img2 )
# cv2.waitKey( 0 )

#6-11 Unsharp Masking 非銳化遮罩 書上有錯 第二行g(x, y) 應為gmax(x, y)
# import numpy as np
# import cv2

# def unsharp_masking( f, k = 1.0 ):
#     g = f.copy( )
#     nr, nc = f.shape[:2]
#     f_avg = cv2.GaussianBlur( f, ( 15, 15 ), 0 )
#     for x in range( nr ):
#         for y in range( nc ):
#             g_mask = int( f[x,y] ) - int( f_avg[x,y] )
#             g[x,y] = np.uint8( np.clip( f[x,y] + k * g_mask, 0, 255 ) )
#     return g

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1 )
# img2 = unsharp_masking( img1, 10.0 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Unsharp Masking", img2 )
# cv2.waitKey( 0 )

#6-12 bilateral filter 雙邊濾波 美肌
# import numpy as np
# import cv2

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Jenny.bmp", -1 )
# img2 = cv2.bilateralFilter( img1, 11, 50, 50 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Bilateral Filtering", img2 )
# cv2.waitKey( 0 )




# 影像偵測 影像分割
# 7-1 Sobel_edge_detection
# import numpy as np
# import cv2

# def Sobel_edge_detection( f ):
#     grad_x = cv2.Sobel( f, cv2.CV_32F, 1, 0, ksize = 3 )
#     grad_y = cv2.Sobel( f, cv2.CV_32F, 0, 1, ksize = 3 )
#     magnitude = abs( grad_x ) + abs( grad_y )
#     g = np.uint8( np.clip( magnitude, 0, 255 ) )
#     ret,g = cv2.threshold( g, 127, 255,
#     cv2.THRESH_BINARY + cv2.THRESH_OTSU )
#     return g


# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1 )
# img2 = Sobel_edge_detection( img1 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Sobel Edge Detection", img2 )
# cv2.waitKey( 0 )

#7-2 Canny_edge_detection 二階導數
import numpy as np
import cv2

img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0731/Osaka.bmp", -1 )
img2 = cv2.Canny( img1, 50, 200 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Canny Edge Detection", img2 )
cv2.waitKey( 0 )

