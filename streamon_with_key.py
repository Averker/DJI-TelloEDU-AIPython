import ffmpeg
import cv2
from djitellopy import Tello 
import imutils
import time


tello = Tello()
tello.connect()

tello.streamon()

time.sleep(1 / 60)

frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    frame = frame_read.frame

    frame = imutils.resize(frame, width=400)
    H, W, _ = frame.shape

    #cv2.imwrite("picture.png", frame)
    
    # display the frame to the screen
    cv2.imshow("Face Tracking", frame)    

    key = cv2.waitKey(5) & 0xff
    # 當按下ESC鍵，則關閉串流
    if key == 27: # ESC
        tello.streamoff()
        tello.land()
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)


 
frame.release()
cv2.destroyAllWindows()





