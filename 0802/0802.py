#7-3 Hough_line_detection 霍夫域
# import numpy as np
# import cv2
# import math

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/Traffic_Lanes.bmp", -1 )
# img2 = img1.copy( )

# gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY ) #轉灰階
# edges = cv2.Canny( gray, 50, 200 ) #使用Canny找邊緣
# lines = cv2.HoughLines( edges, 1, math.pi/180.0, 120 ) #找霍夫線
# if lines is not None:
#     a,b,c = lines.shape
#     for i in range( a ):
#         rho = lines[i][0][0]
#         theta = lines[i][0][1]
#         a = math.cos( theta )
#         b = math.sin( theta )
#         x0, y0 = a*rho, b*rho
#         pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
#         pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
#         cv2.line( img2, pt1, pt2, ( 255, 0, 0 ), 1, cv2.LINE_AA )

# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Canny Edge Detection", edges )
# cv2.imshow( "Hough Line Detection", img2 )
# cv2.waitKey( 0 )


#7-4 Hough_circle_detection 霍夫圓
# import numpy as np
# import cv2
# import math

# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/Cans.bmp", -1 )
# img2 = img1.copy( )
# gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY )
# circles = cv2.HoughCircles( gray, cv2.HOUGH_GRADIENT, 1, 150, 200, 50,
# minRadius = 120, maxRadius = 200 )
# circles = np.uint16( np.around( circles ) )
# for i in circles[0,:]:
#     cv2.circle( img2, ( i[0], i[1] ), i[2], ( 0, 255, 0 ), 2 )
#     cv2.circle( img2, ( i[0], i[1] ), 2, ( 0, 0, 255 ), 3 )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Circle Detection", img2 )
# cv2.waitKey( 0 )

#7-5 thresholding 絕對閥值
# import numpy as np
# import cv2
# img1 = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/Bug.bmp", 0 )
# thresh, img2 = cv2.threshold( img1, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )
# print( "Threshold =", thresh )
# cv2.imshow( "Original Image", img1 )
# cv2.imshow( "Thresholding", img2 )
# cv2.waitKey( 0 )

#7-6 adaptive_thresholding 適應性閥值
# import numpy as np
# import cv2

# img = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/Script.bmp", 0 )
# thresh, img1 = cv2.threshold( img, 128, 255, cv2.THRESH_BINARY )
# img2 = cv2.adaptiveThreshold( img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0 )
# img3 = cv2.adaptiveThreshold( img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0 )

# cv2.imshow( "Original Image", img )
# cv2.imshow( "Global Thresholding", img1 )
# cv2.imshow( "Adaptive Thresholding(Mean)", img2 )
# cv2.imshow( "Adaptive Thresholding(Gaussian)", img3 )
# cv2.waitKey( 0 )

#8-1 erosion
# import numpy as np
# import cv2

# img = np.zeros((5, 5), np.uint8)
# img[1:4, 1:4] = 1

# kernel = np.ones((3, 1), np.uint8)
# erosion = cv2.erode(img, kernel) #侵蝕

# print("img=\n",img)
# print("kernel=\n",kernel)
# print("erosion=\n",erosion)

#8-2 cv2.erode()
# import cv2
# import numpy as np

# o=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/erode.bmp",cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(o,kernel)
# cv2.imshow("orriginal",o)
# cv2.imshow("erosion",erosion)
# cv2.waitKey()
# cv2.destroyAllWindows()

#8-3 cv2.erode() size
# import cv2
# import numpy as np

# o=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/erode.bmp",cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(o,kernel,iterations =5) #疊代次數5
# cv2.imshow("orriginal",o)

# cv2.imshow("erosion",erosion)
# cv2.waitKey()
# cv2.destroyAllWindows()

#8-4 dilation 膨脹
# import cv2
# import numpy as np

# img=np.zeros((5,5),np.uint8)
# img[2:3,1:4]=1
# kernel = np.ones((3,1),np.uint8)
# dilation = cv2.dilate(img,kernel)

# print("img=\n",img)
# print("kernel=\n",kernel)
# print("dilation\n",dilation)

#8-5 cv2.dilate() 
# import cv2
# import numpy as np

# o=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/dilation.bmp",cv2.IMREAD_UNCHANGED)
# kernel = np.ones((9,9),np.uint8)
# dilation = cv2.dilate(o,kernel)
# cv2.imshow("original",o)
# cv2.imshow("dilation",dilation)
# cv2.waitKey()
# cv2.destroyAllWindows()

#8-7 open 開運算
# import cv2
# import numpy as np

# img1=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/opening.bmp")
# img2=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/opening2.bmp")

# k=np.ones((10,10),np.uint8)
# r1=cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)
# r2=cv2.morphologyEx(img2,cv2.MORPH_OPEN,k)

# cv2.imshow("img1",img1)
# cv2.imshow("result1",r1)
# cv2.imshow("img2",img2)
# cv2.imshow("result2",r2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#8-8 close 閉運算
# import cv2
# import numpy as np

# img1=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/closing.bmp")
# img2=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/closing2.bmp")

# k=np.ones((10,10),np.uint8)
# r1=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,k,iterations=3)
# r2=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,iterations=3)

# cv2.imshow("img1",img1)
# cv2.imshow("result1",r1)
# cv2.imshow("img2",img2)
# cv2.imshow("result2",r2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#8-9 形態學梯度運算 取輪廓
# import cv2
# import numpy as np

# o=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/gradient.bmp",cv2.IMREAD_UNCHANGED)
# k=np.ones((5,5),np.uint8)
# r=cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)

# cv2.imshow("original",o)
# cv2.imshow("result",r)

# cv2.waitKey()
# cv2.destroyAllWindows()

#8-10 禮帽運算 取雜訊
# import cv2
# import numpy as np

# o1=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/tophat.bmp",cv2.IMREAD_UNCHANGED)
# o2=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/lena.bmp",cv2.IMREAD_UNCHANGED)

# k=np.ones((5,5),np.uint8)
# r1=cv2.morphologyEx(o1,cv2.MORPH_TOPHAT,k)
# r2=cv2.morphologyEx(o2,cv2.MORPH_TOPHAT,k)

# cv2.imshow("original1",o1)
# cv2.imshow("original2",o2)
# cv2.imshow("result1",r1)
# cv2.imshow("result2",r2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#8-11 黑帽運算 取圖片中的小孔
# import cv2
# import numpy as np

# o1=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/blackhat.bmp",cv2.IMREAD_UNCHANGED)
# o2=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0802/lena.bmp",cv2.IMREAD_UNCHANGED)

# k=np.ones((5,5),np.uint8)
# r1=cv2.morphologyEx(o1,cv2.MORPH_BLACKHAT,k)
# r2=cv2.morphologyEx(o2,cv2.MORPH_BLACKHAT,k)

# cv2.imshow("original1",o1)
# cv2.imshow("original2",o2)
# cv2.imshow("result1",r1)
# cv2.imshow("result2",r2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#9-1 cv2.line()
# import numpy as np
# import cv2

# n = 300
# img = np.zeros((n+1,n+1,3), np.uint8)
# img = cv2.line(img,(0,0),(n,n),(255,0,0),3)
# img = cv2.line(img,(0,100),(n,100),(0,255,0),1)
# img = cv2.line(img,(100,0),(100,n),(0,0,255),6)
# winname = 'Demo19.1'
# cv2.namedWindow(winname)
# cv2.imshow(winname, img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#9-2 cv2.rectangle()
# import numpy as np
# import cv2

# n = 300
# img = np.ones((n,n,3), np.uint8)*255
# img = cv2.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
# winname = 'Demo19.1'
# cv2.namedWindow(winname)
# cv2.imshow(winname, img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#9-3 cv2.circle()
# import numpy as np
# import cv2

# d = 400
# img = np.ones((d,d,3),dtype="uint8")*255
# (centerX,centerY) = (round(img.shape[1] / 2),round(img.shape[0] / 2))
# red = (0,0,255)
# for r in range(5,round(d/2),12):
#     cv2.circle(img,(centerX,centerY),r,red,3)

# cv2.imshow("Demo19.3",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#9-5 cv2.ellipse()
# import numpy as np
# import cv2
# d = 400
# img = np.ones((d,d,3),dtype="uint8")*255
# center=(round(d/2),round(d/2))
# size=(100,200)
# for i in range(0,10):
#     angle = np.random.randint(0,361)
#     color = np.random.randint(0,high = 256,size = (3,)).tolist()
#     thickness = np.random.randint(1,9)
#     cv2.ellipse(img, center, size, angle, 0, 360, color,thickness)

# cv2.imshow("demo19.5",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#下午
#攝影機搭配濾波器
# import numpy as np
# import cv2
# import time

# cap = cv2.VideoCapture(0)
# #Delay才不會掛
# time.sleep(2)

# while(cap.isOpened()):
#   # 從攝影機擷取一張影像
#   ret, frame = cap.read()
#   # print(ret)
#   # print(frame)
#   # 顯示圖片
#   cv2.imshow('frame', frame)

#   # 加濾波器
#   frame2 = cv2.Canny(frame, 100, 200) #CannyEdge
#   frame3 = cv2.bilateralFilter( frame, 11, 50, 50 ) #雙邊濾波
#   cv2.imshow('frame2', frame2)
#   cv2.imshow('frame3', frame3)

#   # 若按下 q 鍵則離開迴圈
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# # 釋放攝影機
# cap.release()
# cv2.destroyAllWindows()

#haar cascade
import numpy as np
import cv2
import time
from PIL import Image

pictPath = r'/Users/chang/PycharmProjects/SCEopenCV/0802/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath) #分類器

# img = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/IMG_6889.JPG")
# img = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/baseballAudience.jpeg")
img = cv2.imread( "/Users/chang/PycharmProjects/SCEopenCV/0802/protest.jpg")

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))
cv2.putText(img, "Finding " + str(len(faces)) + " face", (img.shape[1]-350  , img.shape[0]-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
# print(faces)

num = 1
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 5)
  #save Faces
  filename = "/Users/chang/PycharmProjects/SCEopenCV/0802/Faces/face" + str(num) + ".jpg"
  image = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0802/protest.jpg")
  imageCrop = image.crop((x, y, x+w, y+h))
  imageResize = imageCrop.resize((150, 150), Image.ANTIALIAS)
  imageResize.save(filename)
  num = num + 1

cv2.namedWindow("Face", cv2.WINDOW_NORMAL)
cv2.imshow('Face', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

