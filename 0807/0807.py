#10-2 LBPHFace
# import cv2
# import numpy as np

# images = []
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/a1.png",cv2.IMREAD_GRAYSCALE))
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/a2.png",cv2.IMREAD_GRAYSCALE))
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/b1.png",cv2.IMREAD_GRAYSCALE))
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/b2.png",cv2.IMREAD_GRAYSCALE))
# labels=[0,0,1,1] #兩張臉
# print(labels)

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.train(images, np.array(labels))
# predict_image=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/a3.png",cv2.IMREAD_GRAYSCALE)
# label,confidence= recognizer.predict(predict_image)
# print("label=",label)
# print("confidence=",confidence)

#10-3 EigenFace 特徵向量 PCA 主成份分析
# import cv2
# import numpy as np
# images=[] 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/e01.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/e02.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/e11.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/e12.png",cv2.IMREAD_GRAYSCALE)) 
# labels=[0,0,1,1]
# print(labels)
# recognizer = cv2.face.EigenFaceRecognizer_create() 
# recognizer.train(images, np.array(labels)) 
# predict_image=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/eTest.png",cv2.IMREAD_GRAYSCALE) 
# label,confidence= recognizer.predict(predict_image) 
# print("label=",label)
# print("confidence=",confidence)

#10-4 FisherFace 投影 線性判別
# import cv2
# import numpy as np
# images=[] 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/f01.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/f02.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/f11.png",cv2.IMREAD_GRAYSCALE)) 
# images.append(cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/f12.png",cv2.IMREAD_GRAYSCALE)) 
# labels=[0,0,1,1]
# #print(labels)
# recognizer = cv2.face.FisherFaceRecognizer_create() 
# recognizer.train(images, np.array(labels)) 
# predict_image=cv2.imread("/Users/chang/PycharmProjects/SCEopenCV/0807/fTest.png",cv2.IMREAD_GRAYSCALE) 
# label,confidence= recognizer.predict(predict_image) 
# print("label=",label)
# print("confidence=",confidence)

#10-13 移動偵側
# import cv2
# import numpy as np

# # 開啟網路攝影機
# cap = cv2.VideoCapture(0)
# # 設定影像尺寸 
# width = 1280
# height = 960
# # 設定擷取影像的尺寸大小 
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# # 計算畫面面積 
# area = width * height
# # 初始化平均影像 
# ret, frame = cap.read()
# avg = cv2.blur(frame, (4, 4))
# avg_float = np.float32(avg)

# while(cap.isOpened()):
#     # 讀取一幅影格
#     ret, frame = cap.read()
#     # 若讀取至影片結尾，則跳出
#     if ret == False: 
#         break
#     # 模糊處理
#     blur = cv2.blur(frame, (4, 4))
#     # 計算目前影格與平均影像的差異值
#     diff = cv2.absdiff(avg, blur)
#     # 將圖片轉為灰階
#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#     # 篩選出變動程度大於門檻值的區域
#     ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
#     # 使用型態轉換函數去除雜訊
#     kernel = np.ones((5, 5), np.uint8)
#     thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) 
#     thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
#     # 產生等高線
#     contours_all, hierachy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for c in contours_all:
#         # 忽略太小的區域
#         if cv2.contourArea(c) < 2500:
#             continue
#         # 偵測到物體，可以自己加上處理的程式碼在這裡...
#         # 計算等高線的外框範圍
#         (x, y, w, h) = cv2.boundingRect(c)
#         # 畫出外框
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         # 畫出等高線(除錯用)
#         cv2.drawContours(frame, contours_all, -1, (0, 255, 255), 2)

        
#     # 顯示偵測結果影像 
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break
#     # 更新平均影像 
#     cv2.accumulateWeighted(blur, avg_float, 0.01) 
#     avg = cv2.convertScaleAbs(avg_float)

# cap.release()
# cv2.destroyAllWindows()

# 10-14 移動偵側錄影  失敗
import cv2
import numpy as np

# 開啟網路攝影機
cap = cv2.VideoCapture(0)
# 設定影像尺寸 
width = 1280
height = 960
# 設定擷取影像的尺寸大小 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
out = cv2.VideoWriter('/Users/chang/PycharmProjects/SCEopenCV/0807/output.avi', fourcc, 16, (width, height))

# 計算畫面面積 
area = width * height
# 初始化平均影像 
ret, frame = cap.read()
avg = cv2.blur(frame, (4, 4))
avg_float = np.float32(avg)

while(cap.isOpened()):
    # 讀取一幅影格
    ret, frame = cap.read()
    # 若讀取至影片結尾，則跳出
    if ret == False: 
        break
    # 模糊處理
    blur = cv2.blur(frame, (4, 4))
    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(avg, blur)
    # 將圖片轉為灰階
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # 篩選出變動程度大於門檻值的區域
    ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
    # 使用型態轉換函數去除雜訊
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) 
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    # 產生等高線
    contours_all, hierachy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours_all:
        # 忽略太小的區域
        if cv2.contourArea(c) < 2500:
            continue
        # 偵測到物體，可以自己加上處理的程式碼在這裡...
        # 加上錄影
        out.write(frame)
        # 計算等高線的外框範圍
        (x, y, w, h) = cv2.boundingRect(c)
        # 畫出外框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 畫出等高線(除錯用)
        cv2.drawContours(frame, contours_all, -1, (0, 255, 255), 2)

        
    # 顯示偵測結果影像 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    # 更新平均影像 
    cv2.accumulateWeighted(blur, avg_float, 0.01) 
    avg = cv2.convertScaleAbs(avg_float)

out.release()
cap.release()
cv2.destroyAllWindows()