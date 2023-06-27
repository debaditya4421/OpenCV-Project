import cv2

vi = cv2.VideoCapture('video1new.mp4') #stores the video generated
cv2.namedWindow('Frame' , cv2.WINDOW_NORMAL)
ct =0
f=open('directionOutputs2.txt', 'w') #a new text file is created and opened to store the outputs in tne text file
#the matchimage function matches the template(i.e. each of the 15 images) with the frame image extracted from the
#video at that instant and returns the image number with which it matches
def matchimage(frame1):
    for i in range(1,16):
        img = cv2.imread((str(i) + '.jpeg'), 0)
        imgnew = cv2.resize(src=img, dsize=(40, 40), interpolation=cv2.INTER_AREA)
        #the image is resized to (40, 40) from (600,600)
        if cv2.matchTemplate(frame1, imgnew, cv2.TM_CCOEFF_NORMED) >= 0.9: #template matching
            return i
            break
#the disp function prints and stores the outputs in the text file f
def disp(j):
    if j==1:
        print("stop motors", file=f)
    elif j==2:
        print("move forward. Speed=40", file=f)
    elif j==3:
        print("right turn", file=f)
    elif j==4:
        print("left turn", file=f)
    elif j==5:
        print("U turn", file=f)
    elif j==6 :
        print("Hospital zone. Speed=25", file=f)
    elif j==7 :
        print("Hump ahead. Decelerate", file=f)
    elif j == 8 :
        print("Speed=30", file=f)
    elif j==9:
        print("Speed=20", file=f)
    elif j==10:
        print("School ahead. Speed=20", file=f)
    elif j==11:
        print("Stop motors", file=f)
    elif j==12:
        print("keep moving", file=f)
    elif j==13:
        print("Wrong way ahead. Move in reverse direction", file=f)
    elif j==14 :
        print("Right curve. RightSpeed=30 Leftspeed=20", file=f)
    elif j==15 :
        print("Left curve. LeftSpeed=30 Rightspeed=20", file=f)

while(True) :
    ret,frame = vi.read()
    #vi.read() reads the video and returns 2 objects - ret stores the boolean object, true if any frame is found, else false
    #frame stores the image at that instant
    if ret :
        ct+=1
        frame11 = cv2.resize(src=frame, dsize=(40,40), interpolation=cv2.INTER_AREA)
        #frame resized to (40, 40) from (600,600)
        frame1=cv2.cvtColor(frame11 , cv2.COLOR_BGR2GRAY) #it is converted to Grayscale image
        i1 = matchimage(frame1)
        disp(i1)
        cv2.imshow('Frame' , frame) #the frames from video is displayed continuously
        cv2.waitKey(100)
    else :
        break
print(ct) #displays the total number of frames
f.close()
cv2.destroyAllWindows()
