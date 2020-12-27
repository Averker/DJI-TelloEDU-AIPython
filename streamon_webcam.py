import cv2
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 從視訊鏡頭擷取影片
cap = cv2.VideoCapture(0)
i = 1
while True:
    # Read the frame
    _, frame = cap.read()

    H, W, _ = frame.shape
    centerX = W // 2
    centerY = H // 2

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 轉成灰階圖片

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #gray,scaleFactor=1.08,minNeighbors=15,minSize=(32, 32) 可縮寫
# 繪製人臉部份的方框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #圖片數據、兩個對角座標、線的顏色、線的粗細

    # 顯示成果

    frame_center = (centerX, centerY)
    cv2.putText(frame, f"DCT",frame_center, cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2, cv2.LINE_AA)
    
    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
    cv2.imshow('img', frame)                     #秀出圖片

    if cv2.waitKey(30)== ord('q'):
        break

           
cap.release()
cv2.destroyAllWindows()