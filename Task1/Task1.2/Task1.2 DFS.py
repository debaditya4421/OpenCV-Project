import cv2
import numpy as np
from collections import deque
import time
import sys

sys.setrecursionlimit(1700)

img=cv2.imread('map1.2.png',0)      #Reading it as greyscale to reduce computations
b=880
a=145
d=359
c=563
x,y=img.shape
img[a][b] = 128             #setting the end pixel to grey
img[c][d] = 200             #Setting the starting pixel to value 200 initially to avoid it being mistaken for final pixel
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)

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
        l1=len(stack1)                           #The length of our stack will be equal to the number of pixels in the solution path
        print("distance=", l1)
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
