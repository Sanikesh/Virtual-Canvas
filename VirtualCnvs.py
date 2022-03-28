import cv2
import numpy as np


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,130)

myColors=[[36,255,62,80,255,255]]
myColorVal=[[51,102,0]]
myPoints=[] #[x,y,colorID]
def findColor(img,myColors,myColorVal):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:
        lower=np.array(myColors[0][0:3])
        upper=np.array(myColors[0][3:6])
        mask=cv2.inRange(imgHSV,lower,upper)
        cv2.imshow("img",mask)
        x   ,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorVal[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints


def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCnvs(myPoints,myColorVal):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10, myColorVal[point[2]], cv2.FILLED)
while True:
    success,img=cap.read()
    imgResult=img.copy()
    newPoints=findColor(img,myColors,myColorVal)
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCnvs(myPoints,myColorVal)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break