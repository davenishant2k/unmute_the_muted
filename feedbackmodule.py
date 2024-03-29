# Python program to save a 
# video using OpenCV
  
   
import cv2
import os
import sys  
import time

# Create an object to read 
# from camera
def feedback_code(current_user,corrected_text):
    video = cv2.VideoCapture(0)
    # video.set(cv2.CAP_PROP_FPS, 25)
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    ds_factor = 0.5
    # We need to check if camera
    # is opened previously or not
    if (video.isOpened() == False): 
        print("Error reading video file")
    
    # video.set(3, 160)
    # video.set(4, 160)
    # We need to set resolutions.
    # so, convert them from float to integer.
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    
    size = (frame_width, frame_height)
    
    # Below VideoWriter object will create
    # a frame of above defined The output 
    # is stored in 'filename.avi' file.
    result = cv2.VideoWriter('user feedbacks/'+str(current_user)+'_feedback_video.mp4', 
                            cv2.VideoWriter_fourcc(*'XVID'),
                            25, (160, 160))
    record = False
    count = 0
    while(True):
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k = cv2.waitKey(1)
        if ret == True: 
    
            # Write the frame into the
            # file 'filename.avi'
            # mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
            # for (x,y,w,h) in mouth_rects:
            #     y = int(y - 0.15*h)
            #     cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
            #     break
            if k%256 == 32:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time)
                print("Recording started")
                record = True
                
            if record:
                count+=1
                print(count)
                result.write(cv2.resize(frame,(160,160),fx=0,fy=0, interpolation = cv2.INTER_CUBIC))
    
            # Display the frame
            # saved in the file
            cv2.imshow('Frame', frame)
            # print(frame.shape)
            # Press S on keyboard 
            # to stop the process
            # if cv2.waitKey(1) & 0xFF == ord('s'):
            #     break
            if count == 75 or (cv2.waitKey(1) & 0xFF == ord('s')):
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time)
                print("recording ended")
                break
    
        # Break the loop
        else:
            break
    
    # When everything done, release 
    # the video capture and video 
    # write objects
    video.release()
    result.release()
        
    # Closes all the frames
    cv2.destroyAllWindows()
    
    print("The video was successfully saved")
    file = open('user feedbacks/'+str(current_user)+'_feedback_video.txt',"w")
    file.write(corrected_text)
    file.close()