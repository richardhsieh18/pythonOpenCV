#17-20 draw line
# from PIL import Image, ImageDraw
# newImage = Image.new("RGBA", (300, 300), "Yellow")
# drawObj = ImageDraw.Draw(newImage)

# # 繪製點
# for x in range(100, 200, 3):
#     for y in range(100, 200, 3):
#         drawObj.point([(x,y)], fill="Green")

# # 繪製線條, 繪外框線
# drawObj.line([(50, 50), (250, 50), (250, 250), (50, 250), (50, 50)], fill="Black")
# # 繪製右上角美工線
# for x in range(150, 300, 10):
#     drawObj.line([(x, 0), (300, x - 150)], fill="Blue")
#     #print("x = %d, y = %d" % (x, x - 150))

# # 繪製左下角美工線
# for y in range(150, 300, 10):
#     drawObj.line([(0, y), (y - 150, 300)], fill="Blue")
# newImage.save("./0712/out17_20.png")
# newImage.show()

#17-21 drawFace
# from PIL import Image, ImageDraw
# newImage = Image.new('RGBA', (300, 300), 'Yellow') # 建立 300*300 黃色底的影像
# drawObj = ImageDraw.Draw(newImage)

# drawObj.rectangle((0, 0, 299, 299), outline='Black') # 影像外框線
# drawObj.ellipse((30,60,130,100),outline='Black') # 左眼外框
# drawObj.ellipse((65,65,95,95),fill='Blue') # 左眼
# drawObj.ellipse((170,60,270,100),outline='Black') # 右眼外框
# drawObj.ellipse((205,65,235,95),fill='Blue') # 右眼
# drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
# drawObj.rectangle((100,210,200,240), fill='Red') # 嘴
# newImage.save("./0712/out17_21.png")
# newImage.show()

#17-23 qrcode
# import qrcode
# codeText = "https://www.google.com.tw"
# img = qrcode.make(codeText)
# print("檔案格式", type(img))
# img.save("./0712/out17_23.png")
# img.show()

#18-1
# import tkinter as tk

# window = tk.Tk()
# window.mainloop()

#18-2
# from tkinter import *
# window = Tk()
# window.title("MyWindow") # 視窗標題
# window.geometry("300x160") # 視窗大小
# window.mainloop()

# 18_03
# from tkinter import *
# window = Tk()
# window.title("ch18_3") # 視窗標題
# label = Label(window,text="I like tkinter")
# label.pack() # 包裝與定位元件
# window.mainloop()

# 18_03_1
# from tkinter import *
# window = Tk()
# window.title("ch18_3_1") # 視窗標題
# label = Label(window,text="I like tkinter").pack()
# window.mainloop()

# 18_04
# from tkinter import *
# window = Tk()
# window.title("ch18_4") # 視窗標題
# label = Label(window,text="I like tkinter",
# bg="lightyellow", # 標籤背景是淺黃色

# width=15) # 標籤寬度是 15
# label.pack() # 包裝與定位元件
# window.mainloop()

# 18_04_01
# from tkinter import *
# window = Tk()
# window.title("ch18_4_1") # 視窗標題
# label = Label(window,text="I like tkinter",
# bg="lightyellow", # 標籤背景是淺黃色
# width=15, # 標籤寬度是 15
# font="Helvetica 16 bold italic")
# label.pack() # 包裝與定位元件
# window.mainloop()

# 18_05
# from tkinter import *
# window = Tk()
# window.title("ch18_5") # 視窗標題
# lab1 = Label(window,text="Hello",
# bg="lightyellow", # 標籤背景是淺黃色
# width=15) # 標籤寬度是 15
# lab2 = Label(window,text="Hi",
# bg="lightgreen", # 標籤背景是淺綠色
# width=15) # 標籤寬度是 15
# lab3 = Label(window,text="Good",
# bg="lightblue", # 標籤背景是淺藍色
# width=15) # 標籤寬度是 15
# lab1.pack() # 包裝與定位元件
# lab2.pack() # 包裝與定位元件
# lab3.pack() # 包裝與定位元件
# window.mainloop()

# 19_01
# from tkinter import *
# import math
# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# x_center, y_center, r = 320, 240, 100
# x, y = [], []
# for i in range(12): # 建立圓外圍 12 個點
#     x.append(x_center + r * math.cos(30*i*math.pi/180))
#     y.append(y_center + r * math.sin(30*i*math.pi/180))
# for i in range(12): # 執行 12 個點彼此連線
#     for j in range(12):
#         canvas.create_line(x[i],y[i],x[j],y[j])
# tk.mainloop()

# 19_02
# from tkinter import *
# import math
# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# canvas.create_line(100,100,500,100)
# canvas.create_line(100,125,500,125,width=5)
# canvas.create_line(100,150,500,150,width=10,fill='blue')
# canvas.create_line(100,175,500,175,dash=(10,2,2,2))
# tk.mainloop()

# 19_03
# from tkinter import *
# from random import *
# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# for i in range(50): # 隨機繪 50 個不同位置與大小的矩形
#     x1, y1 = randint(1, 640), randint(1, 480)
#     x2, y2 = randint(1, 640), randint(1, 480)
# if x1 > x2: x1,x2 = x2,x1 # 確保左上角 x 座標小於右下角 x 座標
# if y1 > y2: y1,y2 = y2,y1 # 確保左上角 y 座標小於右下角 y 座標
# canvas.create_rectangle(x1, y1, x2, y2)
# mainloop()

# 19_04
# from tkinter import *
# from random import *
# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# canvas.create_rectangle(10, 10, 120, 60, fill='red')
# canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
# canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')
# mainloop()

# 19_05
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# # 以下以圓形為基礎
# canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
# canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
# canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
# canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
# canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# # 以下以橢圓形為基礎
# canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
# canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
# canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
# canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)
# mainloop()

# 19_10 changeBg
# from tkinter import *
# def bgUpdate(source):
#     ''' 更改畫布背景顏色 '''
#     red = rSlider.get() # 讀取 red 值
#     green = gSlider.get() # 讀取 green 值
#     blue = bSlider.get( ) # 讀取 blue 值
#     print("R=%d, G=%d, B=%d" % (red, green, blue)) # 列印色彩數值
#     myColor = "#%02x%02x%02x" % (red, green, blue) # 將顏色轉成 16 進位字串
#     print(myColor) # 列印色彩數值
#     canvas.config(bg=myColor) # 設定畫布背景顏色

# tk = Tk()
# canvas = Canvas(tk, width=640, height=240) # 初始化背景
# rSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
# gSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
# bSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
# gSlider.set(125) # 設定 green 是 125

# rSlider.grid(row=0, column=0) #排列UI
# gSlider.grid(row=0, column=1)
# bSlider.grid(row=0, column=2)
# canvas.grid(row=1, column=0, columnspan=3)
# mainloop()

#19-11 move
# from tkinter import *
# import time

# tk = Tk()
# canvas = Canvas(tk, width=500, height=150)
# canvas.pack()

# canvas.create_oval(10, 50, 60, 100, fill="Yellow", outline="Lightgray")

# while(1):
#     for x in range(80):
#         canvas.move(1, 5, 0)
#         tk.update() #視窗重繪
#         time.sleep(0.05)

#19-13
# from tkinter import *
# import time

# tk = Tk()
# canvas = Canvas(tk , width=500, height=250)
# canvas.pack()

# id1 = canvas.create_oval(10, 50, 60, 100, fill="Yellow")
# id2 = canvas.create_oval(10, 150, 60, 200, fill="Blue")

# for x in range(0, 80):
#     canvas.move(id1, 5, 0) # id1 x 軸移動 5 像素, y 軸移動 0 像素
#     canvas.move(id2, 5, 0) # id2 x 軸移動 5 像素, y 軸移動 0 像素
#     tk.update() # 強制 tkinter 重繪
#     time.sleep(0.05)

#19-14
# from tkinter import *
# import time
# from random import *

# tk = Tk()
# canvas = Canvas(tk , width=500, height=250)
# canvas.pack()

# id1 = canvas.create_oval(10, 50, 60, 100, fill="Yellow")
# id2 = canvas.create_oval(10, 150, 60, 200, fill="Blue")

# for x in range(0, 100):
#     if randint(1, 100) > 50:
#         canvas.move(id2, 5, 0) # id2 x 軸移動 5 像素, y 軸移動 0 像素
#     else:
#         canvas.move(id1, 5, 0) # id1 x 軸移動 5 像素, y 軸移動 0 像素

#     tk.update() # 強制 tkinter 重繪
#     time.sleep(0.05)

#19-15 keyEvent
from tkinter import *
import time

def ballMove(event):
    if event.keysym == 'Left': # 左移
        canvas.move(1, -5, 0)
    if event.keysym == 'Right': # 右移
        canvas.move(1, 5, 0)
    if event.keysym == 'Up': # 上移
        canvas.move(1, 0, -5)
    if event.keysym == 'Down': # 下移
        canvas.move(1, 0, 5)

tk = Tk()
canvas = Canvas(tk, width=500, height=300)
canvas.pack()

canvas.create_oval(225, 125, 275, 175, fill="Red")
canvas.bind_all("<KeyPress-Left>", ballMove)
canvas.bind_all("<KeyPress-Right>", ballMove)
canvas.bind_all("<KeyPress-Up>", ballMove)
canvas.bind_all("<KeyPress-Down>", ballMove)
mainloop()
