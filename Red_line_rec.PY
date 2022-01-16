import cv2
import numpy as np



  






cap = cv2.VideoCapture(0)
cap.set(3,160)
cap.set(4,120)
c = None
while True:
    ret,frame = cap.read()
    #low_b = np.uint8([0,0,5])# 5,5,5
    #high_b = np.uint8([0,5,5])# 0,0,0
   # mask = cv2.inRange(frame,high_b,low_b)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    

    contours,hierarchy = cv2.findContours(red_mask,1,cv2.CHAIN_APPROX_NONE)
    
    if len(contours) > 0:
        c = max(contours,key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX: " + str(cx) +  "CY: " + str(cy))
            if cx>= 120:
                print("Turn Right")
            if cx < 120 and cx >40:
                print("ON TRACK")
            if cx <= 40:
                print("Turn Left")
            cv2.circle(frame,(cx,cy),5,(255,255,255),-1)
    cv2.drawContours(frame,c,-1,(0,255,0),1)
    cv2.imshow("Mask",red_mask)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.realise(0)
cv2.destroyAllWindows()


