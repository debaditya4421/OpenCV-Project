import cv2
import numpy as np
import serial
import time

arduino = serial.Serial(port='COM4' , baudrate = 9600 , timeout = .1)
#Arduino and Python is connected by Serial Communication

f = open('directionOutputsBonus.txt', 'W+') #a new text file is created and opened to store the outputs in tne text file

def write_read(x):
    arduino.write(bytes(x, 'utf-8')) #x is passed to the arduino after converting to bytes(of utf-8 encoding)
    time.sleep(0.05)

#the matchimage function matches the template(i.e. each of the 15 images) with the image and returns the image number with which it matches
def matchimage(frame1):
    for i in range(1, 16):
        img = cv2.imread((str(i) + '.jpeg'), 0)
        imgnew = cv2.resize(src=img, dsize=(40, 40), interpolation=cv2.INTER_AREA)
        # the image is resized to (40, 40) from (600,600)
        if cv2.matchTemplate(frame1, imgnew, cv2.TM_CCOEFF_NORMED) >= 0.9: #template matching
            return i

#the disp function stores the output(for this part, we have just stored the image number) in the text file
def disp(j):
    print(j, file=f)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video2.mp4', fourcc, 1, (600, 600))
for j in range(90):
    i = np.random.randint(1, 16)
    imgwrite = cv2.imread(str(i) + '.jpeg', 1)
    video.write(imgwrite)
    img1 = cv2.resize(src=imgwrite, dsize=(40, 40), interpolation=cv2.INTER_AREA)
    # the image is resized to (40, 40) from (600,600)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #the BGR image is converted to a Grayscale image
    i1 = matchimage(img1)
    disp(i1)
    write_read(f.readline())  #reads the file line by line
    time.sleep(1.01)
    # also , once a red signal comes up, immediately after that the green signal should be shown
    if i == 1:
        imgwrite = cv2.imread('2.jpeg', 1) #storing the green light signal
        video.write(imgwrite)
        disp(2)
        j += 1

f.close()
video.release() #the created video is released
