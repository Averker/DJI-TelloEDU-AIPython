import ffmpeg
import cv2
from djitellopy import Tello
import imutils
import time

i=0

tello = Tello()
tello.connect()

tello.streamon()

time.sleep(1 / 60)

frame_read = tello.get_frame_read()

# tello.takeoff()

while True:
    frame = frame_read.frame

    frame = imutils.resize(frame, width=400)
    H, W, _ = frame.shape

    #cv2.imwrite("picture.png", frame)
    
    # display the frame to the screen
    cv2.imshow("Tello Stream", frame)    

    

    key = cv2.waitKey(30) & 0xff

    if key == ord('s'):   #按下s，儲存照片
        cv2.imwrite(str(i)+".png", frame) #儲存路徑
        i = i + 1

    
    # 當按下ESC鍵，則關閉串流
    if key == 27: # ESC
        # tello.streamoff()
        break
    
tello.land()
 
frame.release()
cv2.destroyAllWindows()



