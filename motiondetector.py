import cv2
import winsound
from track import main
def motion():
    cam = cv2.VideoCapture(0)
    cam.set(3,1280)
    cam.set(4,720)
    cam.set(10,70)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1,frame2)
        gray= cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur= cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c)<10000:
                continue
                #record(cam)
    
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
                
            winsound.Beep(500, 200)
            main(cam)
            #record(cam)
               
        c = cv2.waitKey(1)
        if c == ord('e'):
            break
        cv2.imshow('Smart Camera',frame1)
    cam.release()
    cv2.destroyAllWindows()
