#17-3
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# print("列出物件型態", type(rushMore))
# width, height = rushMore.size
# print("寬度 =", width)
# print("高度 =", height)

#17-6
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# rushMore.save("/Users/chang/PycharmProjects/SCEopenCV/0710/out17_06_01.png")
# rushMore.show()

#17-7
# from PIL import Image
# # pictObj = Image.new("RGB", (300, 180), "aqua")
# pictObj = Image.new("RGB", (300, 180), (255, 0, 0))
# pictObj.save("0710/out17_8.jpg")
# pictObj.show()

#17-9
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# width, height = rushMore.size
# newPict = rushMore.resize((width * 2, height))
# newPict.save("./0710/out17_9_1.jpg")
# newPict.show()

#17-10
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# newPict = rushMore.rotate(90)
# newPict.save("./0710/out17_9_2.jpg")
# newPict.show()

#17-11
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# newPict = rushMore.rotate(45)
# newPict.save("./0710/out17_9_3.jpg")
# newPict.show()
# newPict = rushMore.rotate(45, expand = True)
# newPict.save("./0710/out17_9_4.jpg")
# newPict.show()

#17-12 翻轉  重要!!
# from PIL import Image
# rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# newPict = rushMore.transpose(Image.FLIP_LEFT_RIGHT)
# newPict.save("./0710/out17_9_5.jpg")
# newPict.show()
# newPict2 = rushMore.transpose(Image.FLIP_TOP_BOTTOM)
# newPict2.save("./0710/out17_9_6.jpg")
# newPict2.show()

#17-13 getpixel
# from PIL import Image
# newImage = Image.new("RGBA", (300, 100), "Yellow")
# print(newImage.getpixel((150, 50)))
# newImage.save("out_17_13.png")

#17-14 putpixel
# from PIL import Image
# from PIL import ImageColor

# newImage = Image.new("RGBA", (300, 300), "Yellow")
# for x in range(50, 251):
#     for y in range(50, 151):
#         newImage.putpixel((x, y), (0, 255, 255, 255))
# newImage.save("./0710/out17_14_1.png")
# for x in range(50, 251):
#     for y in range(151, 251):
#         newImage.putpixel((x, y), (ImageColor.getcolor("Blue", "RGBA")))
# newImage.save("./0710/out17_14_2.png")

#17-15 crop
# from PIL import Image
# pict = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# cropPict = pict.crop((80, 170, 500, 550))
# cropPict.save("./0710/out17_15.jpg")
# cropPict.show()

#17-17 copy paste
# from PIL import Image
# pict = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# pictCopy = pict.copy()
# pictCrop = pictCopy.crop((80, 170, 500, 550))
# pictCopy.paste((pictCrop), (80, 370))
# pictCopy.paste((pictCrop), (80, 770))
# pictCopy.save("./0710/out17_17.jpg")
# pictCopy.show()

#17-19 filter
from PIL import Image
from PIL import ImageFilter

rushMore = Image.open("/Users/chang/PycharmProjects/SCEopenCV/0710/rushmore.jpg")
# filterPict = rushMore.filter(ImageFilter.BLUR) #模糊
# filterPict = rushMore.filter(ImageFilter.CONTOUR) #邊緣  最常用
# filterPict = rushMore.filter(ImageFilter.EMBOSS) #效果
filterPict = rushMore.filter(ImageFilter.FIND_EDGES) #邊緣黑白化
filterPict.show()

