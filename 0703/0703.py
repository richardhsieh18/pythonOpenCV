#5-4
# num = int(input("請輸入數字:"))
# rem = num % 2
# if (rem == 0):
#     print("%d 是偶數" % num)
# else:
#     print("%d 是奇數" % num)8

# #5-5
# print("計算最終成績")
# score = input("請輸入分數:")
# sc = int(score)
# if (sc >= 90):
#     print("A")
# elif (sc >= 80):
#     print("B")
# elif (sc >= 70):
#     print("C")
# elif (sc >= 60):
#     print("D")
# else:
#     print("E")

#5-6
# print("計算票價")
# age = input("請輸入年齡:")
# age = int(age)
# ticket = 100
# if (age >= 80 or age <= 6):
#     ticket = ticket * 0.2
#     print("票價是: %d" % ticket)
# elif (age >= 60 or age <= 12):
#     ticket = ticket * 0.5
#     print("票價是: %d" % ticket)
# else:
#     print("票價是: %d" % ticket)

#5-7
# print("判斷輸入字元類別")
# ch = input("請輸入字元:")
# chAscii = ord(ch)
# if (chAscii > ord("A") and chAscii < ord("Z")):
#     print("這是大寫字元")
# elif (chAscii > ord("a") and chAscii < ord("z")):
#     print("這是小寫字元")
# elif (chAscii > ord("0") and chAscii < ord("9")):
#     print("這是數字")
# else:
#     print("這是特殊字元")

#5-8
# print("判斷閏年")
# year = int(input("請輸入年份(西元):"))

# rem4 = year % 4
# rem100 = year % 100
# rem400 = year % 400

# if (rem4 == 0):
#     if (rem100 != 0 or rem400 == 0):
#         print("%d 是閏年" % year)
#     else:
#         print("%d 不是閏年" % year)
# else:
#     print("%d 不是閏年" % year)

#5-13
a = 3
b = 5
c = 1
r1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
r2 = (-b - (b**2-4*a*c)**0.5) / (2*a)
print("r1= %6.4f, r2 = %6.4f" % (r1, r2))