#Face tracker using OpenCV and Arduino
#by Shubham Santosh
import cv2
import time
from time import time
from datetime import datetime


import copy
servo = 12
servo2 = 13

face_cascade= cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')
cap=cv2.VideoCapture(0)
width = 1280
height = 720
xpos = 1000
ypos = 1000
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))

angle = 15
x_mid = 100
y_mid = 100

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,100)
fontScale = 1
thickness = 2
date= datetime.utcnow() - datetime(1970, 1, 1)
seconds =(date.total_seconds())
int_milliseconds = round(seconds*1000)
date3= datetime.utcnow() - datetime(1970, 1, 1)
seconds =(date3.total_seconds())
int_milliseconds2 = round(seconds*1000)

cap.set(3, 1280)
cap.set(4, 720)
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("CAP_PROP_FPS : '{}'".format(cap.get(cv2.CAP_PROP_FPS)))
print("CAP_PROP_POS_MSEC : '{}'".format(cap.get(cv2.CAP_PROP_POS_MSEC)))
print("CAP_PROP_FRAME_COUNT  : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print("CAP_PROP_BRIGHTNESS : '{}'".format(cap.get(cv2.CAP_PROP_BRIGHTNESS)))
print("CAP_PROP_CONTRAST : '{}'".format(cap.get(cv2.CAP_PROP_CONTRAST)))
print("CAP_PROP_SATURATION : '{}'".format(cap.get(cv2.CAP_PROP_SATURATION)))
print("CAP_PROP_HUE : '{}'".format(cap.get(cv2.CAP_PROP_HUE)))
print("CAP_PROP_GAIN  : '{}'".format(cap.get(cv2.CAP_PROP_GAIN)))
print("CAP_PROP_CONVERT_RGB : '{}'".format(cap.get(cv2.CAP_PROP_CONVERT_RGB)))
xa = [0,0,0,0,0,0,0,0,0]
ya = [0,0,0,0,0,0,0,0,0]
wa = [0,0,0,0,0,0,0,0,0]
ha = [0,0,0,0,0,0,0,0,0]
while cap.isOpened():

    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image
    #frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #print(frame.shape)
    faces_num = 0
    bodies_num = 0	
    date2= datetime.utcnow() - datetime(1970, 1, 1)
    
    seconds =(date2.total_seconds())
    milliseconds = round(seconds*1000)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(milliseconds - int_milliseconds)
    if(milliseconds - int_milliseconds  > 300):
        #print("face")
        int_milliseconds = milliseconds
        faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face
    #bodies= body_cascade.detectMultiScale(gray,1.1,6)  #detect the face
    faceflag = 0
    for x,y,w,h in faces:
        if(faces_num < len(xa)):
            xa[faces_num] = x
            ya[faces_num] = y
            wa[faces_num] = w
            ha[faces_num] = h
        faces_num = faces_num + 1
        # Import class time from time module

 
        milliseconds  = int(time() * 1000)
 
        
        #sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        
        
        x_mid = x+w//2
        y_mid = (y+h//2)
        #plot the center of the face

        #cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        if (x_mid < (width / 2 + 30)):
            xpos = xpos +angle
        if (x_mid > width / 2 - 30):
            xpos = xpos - angle
        if (y_mid > height / 2 + 30):
            ypos = ypos-angle
        if (y_mid < height / 2 - 30):
            ypos =ypos+ angle
        #f the servo degree is outside its range
        
        if (xpos >= 2500):
            xpos = 2500
        elif (xpos <= 500):
            xpos = 500
        if (ypos >= 2500):
            ypos = 2500
        elif (ypos <= 500):
            ypos = 500
        #print(f"xpos: {xpos} ypos: {ypos}")
        #print(milliseconds - int_milliseconds )
       # if(milliseconds - int_milliseconds  > 1):
        #    int_milliseconds = milliseconds
        faceflag = 1
            
    lar = 0
    ind = 0
    for i in range(faces_num):
        if(faces_num < len(xa)):
            area = wa[i]*ha[i]
            if(area > lar):
                lar = area 
                ind = i
                cv2.circle(frame,(xa[i]+wa[i]//2,ya[i]+ha[i]//2),2,(0,255,0),2)
                #plot the roi
                cv2.rectangle(frame,(xa[i],ya[i]),(xa[i]+wa[i],ya[i]+ha[i]),(0,0,255),1)
 
    #print(f"x {xa}, y {ya}, h {ha}, w {wa}")
    #plot the squared region in the center of the screen
   
    fa = str(faces_num) + " people"
    frame = cv2.putText(frame,fa,org,font,fontScale,(255,255,255),thickness,cv2.LINE_AA)
    
   
    cv2.circle(frame,(width//2,height//2),7,(255,255,255),3)
    if( faceflag ):
        cv2.circle(frame,(xa[ind]+wa[ind]//2,ya[ind]+ha[ind]//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(xa[ind],ya[ind]),(xa[ind]+wa[ind],ya[ind]+ha[ind]),(0,255,255),1)
        if (x_mid < (width / 2 + 30)):
            xpos = xpos +angle
        if (x_mid > width / 2 - 30):
            xpos = xpos - angle
        if (y_mid > height / 2 + 30):
            ypos = ypos-angle
        if (y_mid < height / 2 - 30):
            ypos =ypos+ angle
        #f the servo degree is outside its range
        
        if (xpos >= 2500):
            xpos = 2500
        elif (xpos <= 500):
            xpos = 500
        if (ypos >= 2500):
            ypos = 2500
        elif (ypos <= 500):
            ypos = 500
        #print(f"xpos: {xpos} ypos: {ypos}")
        #print(milliseconds - int_milliseconds )
        if(milliseconds - int_milliseconds  > 1):
            int_milliseconds = milliseconds
            
            pwm.set_servo_pulsewidth( servo, ypos ) ;
            pwm.set_servo_pulsewidth( servo2, xpos ) ;
        faceflag = 0
        pass
    #out.write(frame)
    if(milliseconds - int_milliseconds2  > 34):
        int_milliseconds2 = milliseconds
        cv2.imshow('img',frame)
            
   



    #cv2.imwrite('output_img.jpg',frame)
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''
    # press q to Quit
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
