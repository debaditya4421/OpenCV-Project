import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video1new.mp4', fourcc, 1, (600, 600))
#A video(mp4 format) is to be generated using 15 images at random for 90 times

for j in range(90):
    i = np.random.randint(1, 16)
    img = cv2.imread(str(i) + '.jpeg', 1)
    video.write(img)
    #once a red signal comes up, immediately after that the green signal should be shown
    if i == 1:
        img = cv2.imread('2.jpeg', 1) #storing the green light signal
        video.write(img)
        j += 1
cv2.destroyAllWindows()
video.release() #the created video is released 
