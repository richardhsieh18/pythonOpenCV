#2-5
# import numpy as np

# img = np.zeros((2, 4, 3), dtype=np.uint8)
# print("img = \n", img)
# print("img[0, 3]=", img[0, 3])
# print("img[1, 2, 2]=", img[1, 2, 2])
# img[0, 3] = 255
# img[0, 0] = [66, 77, 88]

# img[1, 1, 1] = 3
# img[1, 2, 2] = 4
# img[0, 2, 0] = 5

# print("before: img\n", img)
# print("before: img[1, 2, 2]=", img[1, 2, 2])

#2-6
# import cv2
# # img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png")
# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0719/IMG_0253.PNG")
# cv2.imshow("before", img)
# print("img[0, 0]=", img[0, 0])
# print("img[0, 0, 0]=", img[0, 0, 0])
# print("img[0, 0, 1]=", img[0, 0, 1])
# print("img[0, 0, 2]=", img[0, 0, 2])
# print("img[50, 0]=", img[50, 0])
# print("img[100, 0]=", img[100, 0])

# #zone 1
# for i in range(0, 50):
#     for j in range(0, 100):
#         for k in range(0, 3):
#             img[i, j, k] = 255

# #zone 2
# for i in range(50, 100):
#     for j in range(0, 100):
#         img[i, j] = [128, 128, 128]

# #zone 3
# for i in range(100, 150):
#     for j in range(0, 100):
#         img[i, j] = 0

# cv2.imshow("after", img)
# print("after")
# print("img[0, 0]=", img[0, 0])
# print("img[0, 0, 0]=", img[0, 0, 0])
# print("img[0, 0, 1]=", img[0, 0, 1])
# print("img[0, 0, 2]=", img[0, 0, 2])
# print("img[50, 0]=", img[50, 0])
# print("img[100, 0]=", img[100, 0])


# key = cv2.waitKey()
# cv2.destroyAllWindows()

#2-7 使用 numpy.array 存取像素 item(), itemset()
# import numpy as np
# img = np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)
# print("before img=\n", img)
# print("img.item(3, 2)=", img.item(3, 2))
# img.itemset((3, 2), 255)
# print("after img=\n", img)
# print("after img.item(3, 2)=", img.item(3, 2))

#2-8
# import numpy as np
# import cv2

# img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
# cv2.imshow("demo", img)
# key = cv2.waitKey()
# cv2.destroyAllWindows()

#2-9
# import cv2
# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)
# print("img.item(3, 2)", img.item(3, 2))
# img.itemset((3, 2), 255)
# print("after img.item(3, 2)", img.item(3, 2))

# cv2.imshow("before", img)

# for i in range(10, 100):
#     for j in range(10, 100):
#         img.itemset((i, j), 255)

# cv2.imshow("after", img)
# key = cv2.waitKey()
# cv2.destroyAllWindows()

#2-10
# import numpy as np
# img = np.random.randint(10, 99, size=[2, 4, 3], dtype=np.uint8)
# print("img=\n", img)
# print("img[1, 2, 0]", img.item(1, 2, 0))
# print("img[0, 2, 1]", img.item(0, 2, 1))
# print("img[1, 0, 2]", img.item(1, 0, 2))

# img.itemset((1, 2, 0), 255)
# img.itemset((0, 2, 1), 255)
# img.itemset((1, 0, 2), 255)

# print("after img=\n", img)

#2-12
# import cv2
# import numpy as np
# img = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png")
# cv2.imshow("before:", img)
# print("img.item(0, 0, 0) =", img.item(0, 0, 0))
# print("img.item(0, 0, 1) =", img.item(0, 0, 1))
# print("img.item(0, 0, 2) =", img.item(0, 0, 2))
# for i in range(0, 50):
#     for j in range(0, 100):
#         for k in range(0, 3):
#             img.itemset((i, j, k), 255)

# cv2.imshow("after", img)
# print("img.item(0, 0, 0) = ", img.item(0, 0, 0))
# print("img.item(0, 0, 1) = ", img.item(0, 0, 1))
# print("img.item(0, 0, 2) = ", img.item(0, 0, 2))

# key = cv2.waitKey()
# cv2.destroyAllWindows()


#2-13 ROI (Region of Interest)
# import cv2
# import numpy as np
# a = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# print(a[220:400, 250:350])
# face = a[220:400, 250:350]
# cv2.imshow("original", a)
# cv2.imshow("face", face)
# cv2.waitKey()
# cv2.destroyAllWindows()

#2-14
# import cv2
# import numpy as np

# a = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png", cv2.IMREAD_UNCHANGED)
# cv2.imshow("original", a)

# face = np.random.randint(0, 256, (180, 100, 3))
# print(face.shape)
# a[220:400, 250:350] = face
# cv2.imshow("result", a)

# cv2.waitKey()
# cv2.destroyAllWindows()

#2-15
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", cv2.IMREAD_UNCHANGED)
# dollar = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/dollar.bmp", cv2.IMREAD_UNCHANGED)
# cv2.imshow("lena", lena)
# cv2.imshow("dollar", dollar)

# face = lena[220:400, 250:350]
# dollar[160:340, 200:300] = face

# cv2.imshow("result", dollar)
# cv2.waitKey()
# cv2.destroyAllWindows()

#2-16 bgr split
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png", cv2.IMREAD_UNCHANGED)
# cv2.imshow("lena1", lena)
# b = lena[:, :, 0]
# g = lena[:, :, 1]
# r = lena[:, :, 2]
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)
# lena[:, :, 0] = 0
# cv2.imshow("lenab0", lena)
# lena[:, :, 1] = 0
# cv2.imshow("lenab0g0", lena)

# cv2.waitKey()
# cv2.destroyAllWindows()

#2-17 cv2.split()
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lenacolor.png", cv2.IMREAD_UNCHANGED)
# b, g, r = cv2.split(lena)

# cv2.imshow("B", b)
# cv2.imshow("G", g)
# cv2.imshow("R", r)

# bgr = cv2.merge([b, g, r])
# rgb = cv2.merge([r, g, b])

# cv2.imshow("original", lena)
# cv2.imshow("bgr", bgr)
# cv2.imshow("rgb", rgb)

# cv2.waitKey()
# cv2.destroyAllWindows()

#運算子
#3-1 +
# import numpy as np

# img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
# img2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)

# print("img1 = \n", img1)
# print("img2 = \n", img2)
# print("img1+img2 =\n", img1 + img2)

#3-2 cv2.add()
# import numpy as np
# import cv2
# img1 = np.random.randint(0, 256, size=[3,3], dtype=np.uint8)
# img2 = np.random.randint(0, 256, size=[3,3], dtype=np.uint8)
# print("img1=\n", img1)
# print("img2=\n", img2)
# img3 = cv2.add(img1, img2)
# print("cv2.add(img1, img2)=\n", img3)

#3-3
# import cv2

# a = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)
# b = a

# result1 = a + b
# result2 = cv2.add(a, b)

# cv2.imshow("original", a)
# cv2.imshow("result1", result1)
# cv2.imshow("result2", result2)

# cv2.waitKey()
# cv2.destroyAllWindows()

#3-04
# 影響加權和: 
# dst = saturate(src1 × α + src2 × β + γ) 
# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma) 

# import cv2 
# import numpy as np

# img1 = np.ones((3, 4), dtype = np.uint8)*100 
# img2 = np.ones((3, 4), dtype = np.uint8)*10
# gamma = 3 
# img3 = cv2.addWeighted(img1, 0.6, img2, 5, gamma)
# print(img3)

#3-5
# import cv2

# a = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0719/boat.bmp")
# b = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")

# result = cv2.addWeighted(a, 0.6, b, 0.4, 0)

# cv2.imshow("boat", a)
# cv2.imshow("lena", b)
# cv2.imshow("result", result)

# cv2.waitKey()
# cv2.destroyAllWindows()

#3-6
# import cv2
# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp")
# dollar = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/dollar.bmp")

# cv2.imshow("lena", lena)
# cv2.imshow("dollar", dollar)

# face1 = lena[220:400, 250:350]
# face2 = dollar[160:340, 200:300]

# add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
# dollar[160:340, 200:300] = add

# cv2.imshow("result", dollar)

# cv2.waitKey()
# cv2.destroyAllWindows()

#3-7 逐位元
# import cv2
# import numpy as np

# a = np.random.randint(0, 255, (5, 5), dtype = np.uint8)
# b = np.zeros((5, 5), dtype = np.uint8)

# b[0:3, 0:3] = 255
# b[4, 4] = 255

# c = cv2.bitwise_and(a, b)

# print("a=\n", a)
# print("b=\n", b)
# print("c=\n", c)

#3-8
# import cv2
# import numpy as np

# a = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)
# b = np.zeros(a.shape, dtype=np.uint8)

# b[100:400, 200:400] = 255
# b[100:500, 100:200] = 255

# c = cv2.bitwise_and(a, b)

# cv2.imshow("a", a)
# cv2.imshow("b", b)
# cv2.imshow("c", c)

# cv2.waitKey()
# cv2.destroyAllWindows()

#3-10
# import cv2
# import numpy as np

# img1 = np.ones((4, 4), dtype=np.uint8) * 3
# img2 = np.ones((4, 4), dtype=np.uint8) * 5
# mask = np.zeros((4, 4), dtype=np.uint8)

# mask[2:4, 2:4] = 1
# img3 = np.ones((4, 4), dtype=np.uint8) * 66

# print("img1=\n", img1)
# print("img2=\n", img2)
# print("mask=\n", mask)
# print("before img3=\n", img3)
# img3 = cv2.add(img1, img2, mask = mask) #mask
# print("after img3=\n", img3)

#3-13 位元分解 bit
# import cv2
# import numpy as np

# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)
# cv2.imshow("lena", lena)

# r, c = lena.shape
# x = np.zeros((r, c, 8), dtype=np.uint8)

# for i in range(8):
#     x[:, :, i] = 2 ** i
# # print(x)

# r = np.zeros((r, c, 8), dtype=np.uint8)
# for i in range(8):
#     r[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
#     mask = r[:, :, i] > 0
#     r[mask] = 255
#     cv2.imshow(str(i), r[:, :, i])

# cv2.waitKey()
# cv2.destroyAllWindows()

# 3-14 xor加解密
# import cv2
# import numpy as np

# lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)
# r, c = lena.shape
# key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)

# encryption = cv2.bitwise_xor(lena, key)         #加密後
# decryption = cv2.bitwise_xor(encryption, key)   #解密後

# # cv2.imshow("lena", lena)
# # cv2.imshow("key", key)
# cv2.imshow("encryption", encryption)
# cv2.imshow("decryption", decryption)

# cv2.waitKey()
# cv2.destroyAllWindows()

# 3-15 add watermark
import cv2
import numpy as np

lena = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0717/lena.bmp", 0)

watermark = np.ones((lena.shape), dtype=np.uint8)
watermark = watermark * 255
watermark[100:200, 100:200] = 0
watermark[120:180, 120:180] = 255
cv2.imwrite("watermark01.bmp", watermark)

watermark1 = cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0719/watermark01.bmp", 0)
w = watermark1[:, :] > 0
watermark1[w] = 1

r, c = lena.shape
t254 = np.ones((r, c), dtype=np.uint8) * 254

cv2.waitKey()
cv2.destroyAllWindows()