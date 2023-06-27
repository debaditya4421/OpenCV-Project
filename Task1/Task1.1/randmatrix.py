import numpy as np
import cv2

#finding a probability between 20 and 30 to have an obstacle
prob=np.random.randint(20,31)  #as range is [Low,High)
print(4*prob)

#We will generate a matrix of size 20*20 and then resize it to 400*400
#Since the number of pixels in a 20*20 matrix is 400, The total number of obstacle pixels will be 4*prob

#generating a 20*20 matrix
img=np.full((20,20),255).astype(np.uint8)
count=0
while(count<4*prob):
    i=np.random.randint(0,20)
    j=np.random.randint(0,20)
    if(img[i,j]!=0):    #checking for repitition
        count+=1
        img[i,j]=0

cv2.namedWindow('smolimg', cv2.WINDOW_NORMAL)
cv2.imshow('smolimg', img)

#resizing it to a 400*400 matrix
img=cv2.resize(src=img,dsize=(400,400),interpolation=cv2.INTER_AREA)

#adding 2 random grey pixels to the maze
n=0
while(n<2):
    i=np.random.randint(0,400)
    j=np.random.randint(0,400)
    if(img[i,j]==255):    #checking for a white pixel
        n+=1
        img[i,j]=127
        start=(j,i)         #taking the second grey pixel formed to be the starting point
print(start)
cv2.namedWindow('bigimg', cv2.WINDOW_NORMAL)
cv2.imshow('bigimg', img.astype(np.uint8))


cv2.waitKey(0)
cv2.destroyAllWindows