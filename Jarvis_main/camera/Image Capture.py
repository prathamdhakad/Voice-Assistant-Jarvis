import cv2
img = cv2.imread(filename="c:/path/to/image.png")
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread(filename="c:/path/to/image.png")
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
cv2.imshow('image', img)
cv2.waitKey(0)

import cv2
import numpy as np
from PIL import ImageGrab
while (True):
    screen = np.array(ImageGrab.grab())
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)
    cv2.imshow('my_screen', screen)
    
    # press escape to exit
    if (cv2.waitKey(30) == 27):
       break
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
    cv2.imshow('webcam', frame)
# press escape to exit
    if (cv2.waitKey(30) == 27):
       break
cap.release()
cv2.destroyAllWindows()


cap = vc2.VideoCapture('c:/path/to/my/file.mp4
