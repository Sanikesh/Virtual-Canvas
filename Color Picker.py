import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 1000)
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",6,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",53,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",165,255,empty)
cv2.createTrackbar("Val Min","TrackBars",126,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
while True:
    success, img = cap.read()
    #cv2.imshow("Webcam", img)
    #if cv2.waitKey(1) & 0xFF == ord("q"):
        #break
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    Result=cv2.bitwise_and(img,img,mask=mask)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,Result])
    cv2.imshow("Horizontal Stacking",hstack)
    if cv2.waitKey(1)&0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()