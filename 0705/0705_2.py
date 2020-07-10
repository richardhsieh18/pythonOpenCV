#7-3
# players = ["Curry", "Jordan", "James", "Durant", "Obama"]
# for i in players:
#     print(i)

# #7-5 title會把第一個字改成大寫
# players = ["Curry", "Jordan", "James", "Durant", "Obama"]
# for i in players:
#     print(i.title() + ". it was a great game.")

#7-6 列印區間
# players = ["Curry", "Jordan", "James", "Durant", "Obama"]
# for i in players[:3]:
#     print(i)

# for i in players[-3:]:
#     print(i)

#7-7 字尾
# files = ["da1.c", "da2.py", "da3.py", "da4.java"]
# py = []

# for i in files:
#     if i.endswith(".py"):
#         py.append(i)

# print(py)

# #7-8 字首
# files = ["da1.c", "da2.py", "da3.py", "da4.java"]
# py = []

# for i in files:
#     if i.startswith("da1"):
#         py.append(i)

# print(py)

#7-10 range()
# n = int(input("請輸入星星數量:"))
# for i in range(n):
#     print("*", end="")

# #7-19 range(a, b) 九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d*%d=%-3d" % (i, j, i*j), end=" ")
#     print("")

#7-20
# for i in range(1, 10):
#     for j in range(1, 10):
#         if (i >= j):
#             print("aa", end="")
#     print("")

#7-23 continue
# scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
# games = 0
# for i in scores:
#     if(i < 30):
#         continue
#     games += 1

# print(games)

#7-24 break
# num = int(input("請輸入整數，判斷是否為質數:"))
# if (num == 2):
#     print("%d 是質數" % num)
# else:
#     for i in range(2, num):
#         if (num % i == 0):
#             print("%d 不是質數" % num)
#             break
#     else:
#         print("%d 是質數" % num)

#7-29
# answer = 30
# guess = 0
# while(guess != answer):
#     guess = int(input("請猜1-100間數字:"))
#     if (guess > answer):
#         print("請猜小一點")
#     elif (guess < answer):
#         print("請猜大一點")
#     else:
#         print("答案為%d" % answer)

#7-30
# index = 1
# while(index <= 5):
#     print("第%d次的while迴圈" % index)
#     index += 1

#7-31
# i = 1
# while(i <= 9):
#     j = 1
#     while(j <= 9):
#         print("%d*%d=%-3d" % (i, j, i*j), end=" ")
#         j += 1
#     print("")
#     i += 1

#8-1 Tuple
# numbers = (1, 2, 3, 4, 5)
# print(numbers)
# print(type(numbers))

#8-10 Tuple
# keys = ("magic", "xaab", 9099)
# listKeys = list(keys)
# listKeys.append("secret")
# keysTuple = tuple(listKeys)
# print("列印Tuple", keys)
# print("列印List", listKeys)
# print("列印Tuple", keysTuple)

# #9-1 Dict
# frutis = {"西瓜":15, "香蕉":20, "水蜜桃": 25}
# noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
# frutis["橘子"] = 18
# print(frutis)
# print(noodles)

#9-10 clear()
# frutis = {"西瓜":15, "香蕉":20, "水蜜桃": 25}
# print(frutis)
# frutis.clear()
# print(frutis)

#11-1
# def greeting():
#     """我的第一個Python函數設計"""
#     print("Python歡迎你")
#     print("祝福學習順利")
#     print("謝謝")

# greeting()
# greeting()
# greeting()

#11-3 傳遞參數
# def greeting(name):
#     print("Python歡迎" + name + ",您好")
#     print("祝福學習順利")
#     print("謝謝")

# greeting("Tom")

#11-5 減法
# def subtract(x1, x2):
#     result = x1 - x2
#     return result

# print("減法運算")
# a = int(input("請輸入數字1:"))
# b = int(input("請輸入數字2:"))
# returnResult = subtract(a, b)
# print("結果為", returnResult)

# def multifunction(x1, x2):
#     addresult = x1 + x2
#     subresult = x1 - x2
#     mulresult = x1 * x2
#     divresult = x1 / x2
#     return addresult, subresult, mulresult, divresult

# x1 = x2 = 10
# add, sub, mul, div = multifunction(x1, x2)
# print(type(multifunction(x1, x2)))
# print("x1 + x2 =", add)
# print("x1 - x2 =", sub)
# print("x1 * x2 =", mul)
# print("x1 / x2 =", div)

#11-8
# def interest(interest_type, subject="敦煌"):
#     print("我的興趣是:" + interest_type)
#     print("在 " + interest_type + "最喜歡的是" + subject)
#     print("")

# interest("旅遊")
# interest(interest_type = "旅遊")
# interest("旅遊", "張家界")
# interest(interest_type = "旅遊", subject="張家界")
# interest(subject="張家界", interest_type = "旅遊")
# interest("閱讀", "旅遊類")

#13-14 random
# import random
# n = 3
# for i in range(n):
#     print("1-100     :", random.randint(1, 100))
# for i in range(n):
#     print("500-1000  :", random.randint(500, 1000))
# for i in range(n):
#     print("1000-5000 :", random.randint(1000, 5000))

#13-15
# import random
# min, max = 1, 10
# ans = random.randint(min, max)

# while (True):
#     yourNum = eval(input("猜數字 1-10: "))
#     if (yourNum == ans):
#         print("答對了")
#         break
#     elif (yourNum < ans):
#         print("猜大一點")
#     else:
#         print("猜小一點")

#13-20
# import random
# import time

# min, max = 1, 10
# ans = random.randint(min, max)
# yourNum = eval(input("猜數字 1-10: "))
# startTime = int(time.time())
# while (True):
#     if (yourNum == ans):
#         print("答對了")
#         endTime = int(time.time())
#         print("所花的時間", endTime - startTime, "秒")
#         break
#     elif (yourNum < ans):
#         print("猜大一點")
#     else:
#         print("猜小一點")
#     yourNum = eval(input("猜數字 1-10: "))

#13-21
# import time

# frutis = ["蘋果", "香蕉", "西瓜"]
# for i in frutis:
#     print(i)
#     time.sleep(1)

#
from PIL import Image
img1 = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0705/well.jpg")
print(type(img1))
width, height = img1.size
print("寬度", width)
print("高度", height)
