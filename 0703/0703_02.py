#串列 List
#6-1
# james = [23, 22, 18, 31, 98]
# print("james 串列", james)
# James = ['Lebron James', 23, 22, 18, 31, 98]
# print("james 串列", James)
# print(type(james))
# print(type(James))

#6-2
# james = [23, 19, 22, 31, 18]
# print("第1場得分", james[0])
# print("第2場得分", james[1])
# print("第3場得分", james[2])
# print("第4場得分", james[3])
# print("第5場得分", james[4])

#6-4
# james = [23, 19, 22, 31, 18]
# print("列印james第1-3場得分", james[0:3])
# print("列印james第1-3場得分", james[0:2+1])
# print("列印james第2-4場得分", james[1:4])
# print("列印james第1,3,5場得分", james[0:6:2])
# print("列印james第1,3,5場得分", james[0:5+1:2])
# print("列印james第1,3,5場得分", james[0::2])
# print("列印james第2,4場得分", james[1::2])
# print("列印james第5場得分", james[-1])

#6-8
# james = [23, 19, 22, 31, 18]
# print("List元素共有", len(james))
# print("最高分", max(james))
# print("最低分", min(james))
# print("分數加總", sum(james))

# #6-11
# james = [23, 19, 22, 31, 18]
# print(james)
# james[4] = 28
# print(james)

#6-14  相加
# num1 = [1, 3, 5]
# num2 = [2, 4, 6]
# num3 = num1 + num2
# print(num3)

#6-15  相乘
# cars = ["toyota", "nissan", "honda"]
# nums = [1, 3, 5]
# carslist = cars * 3
# print(carslist)
# numslist = nums * 3
# print(numslist)

#6-17
warriors = ["Curry", "Durant", "Iquodala", "Bell", "Thompson"]
print(warriors)
del warriors[3]
print(warriors)

#6-18
nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前   =", nums1)
del nums1[1]
print("刪除nums1串列索引1元素後   =", nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]前   =", nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]後   =", nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("判除nums3串列索引[0:6:2]前 =", nums3)
del nums3[0:6:2]
print("判除nums3串列索引[0:6:2]後 =", nums3)