#2-10
import numpy as np

#print(np.zeros(10))
# print(np.zeros(10, dtype=int))
# a = np.zeros((3, 4))
# print(a)

# b = np.zeros((a.shape))
# print(b)
# b = np.zeros_like(a)

# a = np.array([[1, 2, 3], [2, 3, 4]])
# c = np.ones_like(a)
# print(a)
# print(c)

#2-12
# import numpy as np
# # a = np.empty(10)  #速度比ones快
# # print(a)

# # print(np.eye(3)) #對角
# # print(np.eye(10))
# print(np.eye(2, 3))
# print(np.eye(5, k=1)) #移動
# print(np.eye(5, k=-1))

#2-15
# import numpy as np
# print(np.identity(5))

#2-24
# import numpy as np
# print(np.random.randint(10))
# print(np.random.rand(2, 3))
# print(np.random.randint(5, 10, size=10))

#2-24-2 seed 基數
# import numpy as np
# np.random.seed(seed=21)
# print(np.random.rand())
# np.random.seed(21)
# print(np.random.rand())