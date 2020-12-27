import cv2
from djitellopy import Tello
import imutils
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

tello = Tello()
tello.connect()

tello.streamon()

time.sleep(1 / 60)

frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    frame = frame_read.frame
    frame = imutils.resize(frame, width=400)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 轉成灰階圖片

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #gray,scaleFactor=1.08,minNeighbors=15,minSize=(32, 32) 可縮寫
    # 繪製人臉部份的方框    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #圖片數據、兩個對角座標、線的顏色、線的粗細

    # 顯示成果
    cv2.imshow('img', frame)

    if cv2.waitKey(30)== ord('q'):
        tello.land()
        break
 
# tello.land()
frame.release()
cv2.destroyAllWindows()



