#Numpy
#1-1 np.array()
# import numpy as np
# a = np.array([1, 2, 3]) #np.array()
# b = [1, 2, 3]
# print(type(a))
# print(type(b))

# print(a * 3)
# print(a + 2)
# print(b * 3)
# print(b + 2)

# b = np.array([2, 2, 0])

# print(a + b)
# # print(a / b)
# print(a * b)

# print(np.arange(10)) #[0 1 2 3 4 5 6 7 8 9]
# print(np.arange(0, 10, 2)) #[0 2 4 6 8]

# print(np.linspace(0, 10, 15)) # 0-10 divideCout 15 [ 0.          0.71428571  1.4285714  ... 10]

# c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)
# print(c.shape) #tuple (2, 3) Dimenstion

# d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
# [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
# print(d)
# print(d.shape)

# c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)
# print(c.reshape(3, 2))
# print(c.reshape(6, 1))

#1-2 ndarray
# import numpy as np
# a = np.array([1, 2, 3])
# print(a.data)
# print(a.dtype)

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print(b.shape)
# print(b.T) #Transpose 轉置
# print((b.T).shape)
# print((b.T).ndim)

#1-3 axis
import numpy as np
# a = np.array([[0, 1], [2, 3], [4, 5]])
# print(a)
# # print(a.shape)
# # print(a.ndim)

# b = np.array([a, a])
# print(b)
# # print(b.shape)
# # print(b.ndim)
# # b_sum = b.sum(axis=0) #[[0  2] [4  6] [8 10]]
# # b_sum = b.sum(axis=1) #[[6 9] [6 9]]
# b_sum = b.sum(axis=2)   #[[1 5 9] [1 5 9]]
# print(b_sum)

# print(b.shape)
# print(b.ndim)
# print(b_sum.shape)
# print(b_sum.ndim)

# c = np.array([0, 1, 2], dtype="float")
# print(c)

# f = np.array([0, 3, 0, -1], dtype="bool")
# print(f)

#1-5 Slice
# b = np.arange(20).reshape(4, 5)
# print(b)
# print(b[1:3, 2:4])
# print(b[:2, 1:])
# print(b[::2, :])
# print(b[::, ::2])
# print(b[:, ::-1])
# print(b[::-1, ::-1])

#1-6 Broadcasting
import numpy as np
# a = np.array([[1, 2]])
# print(a.shape)
# b = np.array([3, 4])
# print(b.shape)
# print(a + b)

a = np.array([1, 2])
b = np.array([[3, 4], [2, 3]])
print(a + b)