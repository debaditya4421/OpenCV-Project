import cv2
import numpy as np
import time

#MAZE TRAVERSAL USING BFS ALGORITHM

#firstly, we generate a random maze
begin = time.time() #start time
prob=np.random.randint(20,31)
img=np.full((20,20),255).astype(np.uint8)
count=0
while(count<4*prob):
    i=np.random.randint(0,20)
    j=np.random.randint(0,20)
    if(img[i,j]!=0):    #checking for repitition
        count+=1
        img[i,j]=0

img=cv2.resize(src=img,dsize=(60,60),interpolation=cv2.INTER_AREA)
n=0
pos1 = [] #stores row number for starting and ending point
pos2 = [] #stores column number for starting and ending point
while ( n < 2 ): #for generating random starting and ending point
    i=np.random.randint(0,60)
    j=np.random.randint(0,60)
    if (img[i,j]==255):    #checking for a white pixel
        pos1.append(i)
        pos2.append(j)
        n+=1
        img[i,j]=127
n, m = img.shape
a = pos1[0]
b = pos2[0]
c = pos1[1]
d = pos2[1]
c1=c
d1=d

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
img[a][b] = 255
img[c][d] = 255

img1 = np.full((n, m), 0) #stores step values for the required path as 1,2,3 .. so on
img1[a][b] = 1
# start : a,b
# end : c,d
stack1=[]
stack2=[]
stack1.append(a)
stack2.append(b)
stack3=[]
stack4=[]
#stack1 stores the row for that particular step with step number k
#stack2 stores the column for that particular step with step number k
#stack3 stores the rows for all the next step values i.e. k+1
#stack4 stores the columns for all the next step values i.e. k+1
def step(i,j,k):
    if (i > 0) and (img1[i - 1][j] == 0) and (img[i - 1][j] == 255):
        img1[i - 1][j] = k + 1
        stack3.append(i - 1)
        stack4.append(j)
    if (j > 0) and (img1[i][j - 1] == 0) and (img[i][j - 1] == 255):
        img1[i][j - 1] = k + 1
        stack3.append(i)
        stack4.append(j - 1)
    if (i + 1 < n) and (img1[i + 1][j] == 0) and (img[i + 1][j] == 255):
        img1[i + 1][j] = k + 1
        stack3.append(i + 1)
        stack4.append(j)
    if (j + 1 < m) and (img1[i][j + 1] == 0) and (img[i][j + 1] == 255):
        img1[i][j + 1] = k + 1
        stack3.append(i)
        stack4.append(j + 1)
    if (i + 1 < n) and (j + 1 < m) and (img1[i + 1][j + 1] == 0) and (img[i + 1][j + 1] == 255):
        img1[i + 1][j + 1] = k + 1
        stack3.append(i + 1)
        stack4.append(j + 1)
    if (i + 1 < n) and (j > 0) and (img1[i + 1][j - 1] == 0) and (img[i + 1][j - 1] == 255):
        img1[i + 1][j - 1] = k + 1
        stack3.append(i + 1)
        stack4.append(j - 1)
    if (j + 1 < m) and (i > 0) and (img1[i - 1][j + 1] == 0) and (img[i - 1][j + 1] == 255):
        img1[i - 1][j + 1] = k + 1
        stack3.append(i - 1)
        stack4.append(j + 1)
    if (i > 0) and (j > 0) and (img1[i - 1][j - 1] == 0) and (img[i - 1][j - 1] == 255):
        img1[i - 1][j - 1] = k + 1
        stack3.append(i - 1)
        stack4.append(j - 1)
#checking all the 8 neighbours/children and if path(untraversed white pixel) is available , then step number
#increases by 1

cp=0
k = 0
while (img1[c][d]==0):
    cp = 0
    k = k + 1
    while cp < len(stack1):
        step(stack1[cp], stack2[cp], k)  # traversing step by step
        cp = cp + 1
    s = 0
    stack1.clear()
    stack2.clear()
    #copying all the rows and column numbers for next iteration from stack3 and stack4 to stack1 and stack2
    while s < len(stack3):
        stack1.append(stack3[s])
        stack2.append(stack4[s])
        s = s + 1
    stack3.clear()
    stack4.clear()
    #stack3[] and stack4[] cleared once a particular iteration is done


cv2.namedWindow('NewImage', cv2.WINDOW_NORMAL) ##window for display of path

p = img1[c][d]
#path1 function retraces the shortest path
def path1(r,s,p):
    global c
    global d
    if (r > 0) and (img1[r - 1][s] == p - 1):
        img[r - 1][s] = 127
        c = r-1
        d = s
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)

    elif (s > 0) and (img1[r][s - 1] == p - 1):
        img[r][s - 1] = 127
        c = r
        d = s - 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (r + 1 < n) and (img1[r + 1][s] == p - 1):
        img[r + 1][s] = 127
        c = r + 1
        d = s
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (s + 1 < m) and (img1[r][s + 1] == p - 1):
        img[r][s + 1] = 127
        c = r
        d = s+1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (r + 1 < n) and (s + 1 < m) and (img1[r + 1][s + 1] == p - 1):
        img[r + 1][s + 1] = 127
        c = r + 1
        d = s + 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (r + 1 < n) and (s > 0) and (img1[r + 1][s - 1] == p - 1):
        img[r + 1][s - 1] = 127
        c = r + 1
        d = s - 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (r > 0) and (s + 1 < m) and (img1[r - 1][s + 1] == p - 1):
        img[r - 1][s + 1] = 127
        c = r - 1
        d = s + 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
    elif (r > 0) and (s > 0) and (img1[r - 1][s - 1] == p - 1):
        img[r - 1][s - 1] = 127
        c = r - 1
        d = s - 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(10)
#for each step , if any neighbour is available with previous step value, then we get the path
while p>1:
    path1(c,d,p)
    p = p-1 #when step number 1 is reached, we get the entire shortest path
end = time.time() #end time
print("Distance" , img1[c1][d1]-1) #distance of the shortest path
print(end - begin) #total time taken
cv2.waitKey(0)
cv2.destroyAllWindows()
