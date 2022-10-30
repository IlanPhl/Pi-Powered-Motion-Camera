#import modules
import freenect
import cv2
import numpy as np

#functiuon to get RGB image
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    while 1:
        #get a frame from the kinect
        frame = freenect.get_video()
        #display the frame
        cv2.imshow('RGB image',frame)

        # quit when 'esc' key is pressed
        K = cv2.waitKey(5) & 0xFF
        if K ==27:
            break
    cv2.destroyAllWindows()
