#Face tracker using OpenCV and Arduino
#by Shubham Santosh
import RPi.GPIO as GPIO
import pigpio
import cv2
import time
from time import time
servo = 12
servo2 = 13

face_cascade= cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')
cap=cv2.VideoCapture(0)
width = 480
height = 640
xpos = 1000
ypos = 1000
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))

angle = 15
x_mid = 100
y_mid = 100
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 50 )
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,100)
fontScale = 1
thickness = 2
int_milliseconds = int(time() * 1000)
pwm.set_servo_pulsewidth( servo, xpos ) ;
pwm.set_servo_pulsewidth( servo2, ypos ) ;
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
while cap.isOpened():

    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #print(frame.shape)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face
   # bodies= body_cascade.detectMultiScale(gray,1.1,6)  #detect the face
    faces_num = 0
    bodies_num = 0	
    for x,y,w,h in faces:
		
      
        faces_num = faces_num + 1
        # Import class time from time module

 
        milliseconds  = int(time() * 1000)
 
        
        #sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        
        
        x_mid = x+w//2
        y_mid = (y+h//2)
        #plot the center of the face

        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
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

    #plot the squared region in the center of the screen
            
    fa = str(faces_num) + " people"
    frame = cv2.putText(frame,fa,org,font,fontScale,(255,255,255),thickness,cv2.LINE_AA)
    
   
    cv2.circle(frame,(width//2,height//2),7,(255,255,255),3)
    #out.write(frame)
    #cv2.imshow('img',frame)



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
