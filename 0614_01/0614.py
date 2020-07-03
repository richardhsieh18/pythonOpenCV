# x = 10
# y = x + 5.5
# print(x)
# print(type(x))
# print(y)
# print(type(y))

# x = 0b1110
# print(x)
# y = 13
# print(bin(y))

# x = 0x5D
# print(x)
# y = 93
# print(hex(y))

# x = 10
# print(type(x))
#
# y = float(x) + 10
# print(y)
# print(type(y))

# x = -10
# print(abs(x))
#
# print(pow(x, 4))

# x = True
# print(type(x))
# print(int(x))

# STRING
# x = "I can't sleep"
# print(type(x))

# num1 = 222
# num2 = 333
# num3 = num1 + num2
# print("數值相加", num3)
#
# strnumb1 = "222"
# strnumb2 = "333"
# strnumb3 = (strnumb1 + strnumb2)
# print("字串相加", strnumb3)


# str1 = "I \tcan't stop \nloving you."
# print(str1)

# strnumb1 = "222"
# strnumb2 = "333"
# strnumb3 = (int(strnumb1) + int(strnumb2))
# print("字串ToInt相加", strnumb3)

# x1 = "A"
# x2 = x1 * 10
# print(x2)
# xx1 = 65
# print(chr(xx1))
# print(ord(x1))
# print(bin(ord(x1)))
# x3 = "ABC"
# x4 = x3 * 5
# print(x4)

# x5 = "測"
# print(hex(ord(x5)))

# dist = 384400
# speed = 1225
#
# total_hours = dist // speed
# # days = total_hours // 24
# # hours = total_hours % 24
# days, hours = divmod(total_hours, 24)
#
# print("總共需要天數:")
# print(days)
# print("小時數:")
# print(hours)

# x1 = 1
# y1 = 8
# x2 = 3
# y2 = 10
# distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# print("兩點的距離是：")
# print(distance)

# 輸入與輸出
# num1 = 222
# num2 = 333
# num3 = num1 + num2
# print("這是數值相加", num3, end = "\t")
# str1 = str(num1) + str(num2)
# print("這是字串相加", str1, sep = " $$$ ")

# name = "XXX"
# count = 1
# score = 90
# print("%s你的第%d次物理考試成續是%d分" % (name, count, score))

# x = 100
# print("100 to Hex is %x, oct is %o" % (x, x))

# 4-6
# x = 10
# print("整數%d \n浮點數 %f \n字串 %s" % (x, x, x))
# y = 9.9
# print("整數%d \n浮點數 %f \n字串 %s" % (y, y, y))

# # 4-7
# x = 100
# print("x=|%6d|" % x)
# y = 10.5
# print("y=|%6.2f|" % y)
# s = "Deep"
# print("s=|%6s|" % s)
# print("以下是保留格數空間不足的實例")
# print("x=|%2d|" % x)
# print("y=|%3.2f|" % y)
# print("s=|%2s|" % s)

# 4-8
# x = 100
# print("x=|%-6d|" % x)
# y = 10.5
# print("y=|%-6.2f|" % y)
# s = "Deep"
# print("s=|%-6s|" % s)

# 4-11
# score = 90
# name = "TTT"
# count = 1
# string = "{} 你的第 {} 次物理考試成績是 {}"
# print(string.format(name, count, score))

# 4-14 輸入
# name = input("請輸入姓名：")
# score = input("請輸入成續：")
# print("name資料型態是 ", type(name))
# print("score資料型態是 ", type(score))
# print("{}的成績是{}".format(name, score))

# 4-15 成續輸入系統
# print("歡迎輸入成續查詢系統")
# name = input("請輸入姓名：")
# scoreCht = eval(input("請輸入國文成續："))
# scoreEng = eval(input("請輸入英文成續："))
# totalScore = scoreCht + scoreEng
# print("%s你的總成續是%.2f" % (name, totalScore))

# 4-16
# numberStr = input("請輸入一個算式: ")
# number = eval(numberStr)
# print("計算結果 : %5.2f" % number)

# 4-19
# n1, n2, n3 = eval(input("請輸入三個數字:"))
# average = (n1 + n2 + n3) / 3
# print("3 個數字平均是 %6.2f" % average)

# 4-20
# f = input("請輸入華氏溫度:")
# c = (eval(f) - 32) * 5 / 9
# print("華氏 %s 等於攝氏 %4.1f" % (f, c))

# 4-22
# import math
# s = eval(input("請輸入五角形邊長:"))
# area = (5 * 2 ** 2) / (4 * math.tan(math.pi / 5))
# print("area = %f" % area)

# 4-23
# import math
# r = 6371
# x1, y1 = 22.2838, 114.1731
# x2, y2 = 25.0452, 121.5168
# d = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2))
#                          + math.cos(math.radians(x1)) * math.cos(math.radians(x2))
#                   * math.cos(math.radians(y1 - y2)))
# print("distance %f" % d)

# 5-1
# age = input("請輸入年齡:")
# if (int(age) < 20):
#     print("你年齡太小")
#     print("需年滿20歲才可以購買菸酒")
# else:
#     print("你可以購買")

# 5-4
# print("奇數偶數判斷")
# num = input("請輸入數字: ")
# rem = eval(num) % 2
# if (rem == 0):
#     print("%s是偶數。" % num)
# else:
#     print("%s是奇數。" % num)

# 5-5
print("計算最終成績")
score = input("請輸入分數:")
sc = int(score)
if (sc >= 90):
    print("A")
elif (sc >= 80):
    print("B")
elif (sc >= 70):
    print("C")
elif (sc >= 60):
    print("D")
else:
    print("E")