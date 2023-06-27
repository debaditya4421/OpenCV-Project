import numpy as np
from collections import deque
import cv2
import time
import sys

sys.setrecursionlimit(1900)

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


#resizing it to a 400*400 matrix
img=cv2.resize(src=img,dsize=(60,60),interpolation=cv2.INTER_AREA)

#adding 2 random grey pixels to the maze
n=0
while(n<2):
    i=np.random.randint(0,60)
    j=np.random.randint(0,60)
    if(img[i,j]==255):    #checking for a white pixel
        n+=1
        img[i,j]=128
        print(j,i)
m=i         #taking the second grey pixel formed to be the starting point
n=j

img[m,n]=200        #setting the starting pixel to value 200 initially to avoid it being mistaken for final pixel
x,y=img.shape
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
stack1=deque()              #Stack1 is used to store the x component of the pixels
stack2=deque()              #Stack2 is used to store the y component of the pixels

def dfs(i,j):
    if img[i,j]!=128:
            img[i,j]=127            #setting all traversed pixels to value 127 to avoid revisiting
            stack1.append(i)        #adding the x and y components of the traversed pixels to the stack
            stack2.append(j)
            cv2.imshow('Image', img)        
            cv2.waitKey(5)
            if(j-1)>=0:                     #making sure the pixel we are going to check is not out of bounds
                if(img[i,j-1]==128):        #checking if it is the final pixel
                    print("complete")
                    dfs(i,j-1)              #If it is the final pixel, we perform dfs on it again since it will move to the else condition then
                elif(img[i,j-1]==255):      #If it is an untraversed pixel of the path, we perform dfs on it
                    dfs(i,j-1)
            if(j+1<y):                      #checking other surrounding pixels
                if(img[i,j+1]==128):
                    print("complete")
                    dfs(i,j+1)
                elif(img[i,j+1]==255):
                    dfs(i,j+1)
            if(i+1<x):
                if(img[i+1,j]==128):
                    print("complete")
                    dfs(i+1,j)
                elif(img[i+1,j]==255):
                    dfs(i+1,j)
            if(i-1)>=0:
                if(img[i-1,j]==128):
                    print("complete")
                    dfs(i-1,j)
                elif(img[i-1,j]==255):
                    dfs(i-1,j)
            
            stack1.pop()                        #If we reach a dead end i.e. a pixel surrounded by no white pixel, we consider out path taken to be wrong
            stack2.pop()                        #We backtrack to the pixel which has untraversed pixels by popping the pixels that belong the wrong path until one of the if conditions is satisfied
            
    else:
        print("complete")                       #The final pixel is reached
        l=len(stack1)                           #The length of our stack will be equal to the number of pixels in the solution path
        print("distance=", l)
        end=time.time()                         
        print("time=",end-begin)     
        for k in range(l):                      #Backtracking to generate the solution path
            img[stack1.pop(),stack2.pop()]=200
            cv2.imshow('Image', img)
            cv2.waitKey(50)
        cv2.waitKey(0)
        exit()
            
begin=time.time()                               #time shown includes the time delay we have used to show the traversal of pixels
dfs(m,n)

cv2.destroyAllWindows()
