#1-1 imread
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# print(lena)
# print(lena.shape)

#1-2
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# cv2.namedWindow("lesson")
# cv2.imshow("lesson", lena)

#waitKey
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# cv2.imshow("demo", lena)
# key = cv2.waitKey(5000) #5000ms  有回傳值
# print(key)

#1-3
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# cv2.imshow("demo", lena)
# key = cv2.waitKey() #沒給秒數
# print(key)

# if (key == ord("a")):
#     cv2.imshow("press a", lena)
#     cv2.waitKey()
# elif (key == ord("b")):
#     cv2.imshow("press b", lena)
#     cv2.waitKey()
# else:
#     print("Not include")

#1-4
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# cv2.imshow("demo", lena)
# key = cv2.waitKey()
# cv2.destroyWindow("demo")

# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# cv2.imshow("demo1", lena)
# cv2.imshow("demo2", lena)
# key = cv2.waitKey()
# cv2.destroyAllWindows()

#1-7 cv2.imwrite()
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# retval = cv2.imwrite("result.bmp", lena)
# print(retval)

#2-1
# import cv2
# import numpy as np
# img = np.zeros((512,512), dtype=np.uint8)
# print("img=\n", img)
# cv2.imshow("one", img)
# print("img[0, 3]=", img[0, 3])
# img[0, 3] = 255
# cv2.imshow("two", img)
# key = cv2.waitKey()
# cv2.destroyAllWindows()

#2-2
# import cv2
# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0) #0 for graysale
# cv2.imshow("before", img)

# for i in range(10, 100):
#     for j in range(80, 100):
#         img[i, j] = 255

# cv2.imshow("after", img)
# key = cv2.waitKey()
# cv2.destroyAllWindows()

#2-3 opencv BGR
import cv2
import numpy as np
blue = np.zeros((300, 300, 3), dtype=np.uint8)
blue[:, :, 0] = 255 #BGR 將B層值給255
print("blue=\n", blue)
cv2.imshow("blue", blue)

green = np.zeros((300, 300, 3), dtype=np.uint8)
green[:, :, 1] = 255 #BGR 將G層值給255
print("green=\n", green)
cv2.imshow("green", green)

red = np.zeros((300, 300, 3), dtype=np.uint8)
red[:, :, 2] = 255 #BGR 將R層值給255
print("red=\n", red)
cv2.imshow("red", red)



#2-4
import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:, 0:100, 0] = 255
img[:, 100:200, 1] = 255
img[:, 200:300, 2] = 255
print("img = \n", img)

cv2.imshow("img", img)

key = cv2.waitKey()
cv2.destroyAllWindows()

#2-5
# import numpy as np
# img = np.zeros((2, 4, 3), dtype=np.uint8)
# print("img = \n", img)
# print("img[0, 3]=", img[0, 3])
# print("img[1, 2, 3]=", img[1, 2, 2])

# img[0, 3] = 255
# img[0, 0] = [66, 77, 88]