import numpy as np
import cv2
import time

#MAZE TRAVERSAL USING DIJKSTRA’S SHORTEST PATH ALGORITHM

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
# start : a,b
# end : c,d
print("start",b,a)
print("end",d,c)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
#displaying original image

img[a][b] = 255
img[c][d] = 255

temp = np.full((n, m), 0)
#temp matrix stores the Temporary cost required to move to a particular position from the starting position
per = np.full((n, m), 0)
#per matrix stores the Permanent cost required to travel to that particular position from the starting position
vis = np.full((n, m), 0)
#keeps a track of the visited and the unvisited nodes
#if it is unvisited, then value is 0
#if it is visited, the value is 127

for i in range(n):
    for j in range(m):
        temp[i][j]=1000 #initially storing all temporary costs as a very high value
temp[a][b] = 0 #temporary cost for the starting position = 0

#the cost between Diagonals is taken as 1
#the cost for horizontal/vertical steps is taken as 2
a1=a
b1 = b
c1=c
d1=d
for i in range(n):
    for j in range(m):
        if img[i][j] == 0:
            vis[i][j] = 127 #all the black pixels are not to be visited , so their value in vis stored as 127 

#algo function takes the position of a pixel, then goes to each neighbour and checks if the the cost of moving to
#that particular neighbour along that point is less than the temporary cost or not,
#if less, updates the temporary cost
#after exploring each neighbour, this position is visited >> thus vis ; 127
#Then , permanent cost = temporary cost
def algo(p,q):
    if (p>0) and (img[p-1][q]==255):
        if 2+temp[p][q] < temp[p-1][q] :
            temp[p-1][q] = 2+temp[p][q]
    if (q>0) and (img[p][q-1]==255):
        if 2+temp[p][q] < temp[p][q-1] :
            temp[p][q-1] = 2+temp[p][q]
    if (p+1<n) and (img[p+1][q]==255):
        if 2+temp[p][q] < temp[p+1][q] :
            temp[p+1][q] = 2+temp[p][q]
    if (q+1<m) and (img[p][q+1]==255):
        if 2+temp[p][q] < temp[p][q+1] :
            temp[p][q+1] = 2+temp[p][q]
    if (p + 1 < n) and (q+1<m) and (img[p + 1][q+1] == 255):
        if 1 + temp[p][q] < temp[p+1][q + 1]:
            temp[p+1][q + 1] = 1 + temp[p][q]
    if (p + 1 < n) and (q>0) and (img[p + 1][q-1] == 255):
        if 1 + temp[p][q] < temp[p+1][q - 1]:
            temp[p+1][q - 1] = 1 + temp[p][q]
    if (q+1<m) and (p>0) and (img[p - 1][q+1] == 255):
        if 1 + temp[p][q] < temp[p-1][q + 1]:
            temp[p-1][q + 1] = 1 + temp[p][q]
    if (p > 0) and (q>0) and (img[p - 1][q-1] == 255):
        if 1+ temp[p][q] < temp[p-1][q - 1]:
            temp[p-1][q - 1] = 1 + temp[p][q]
    vis[p][q] = 127 #visited
    per[p][q] = temp[p][q]
    
g = 5
ct = 0
min = temp[0][0]
while g==5 :
    ct=0
    #the unvisited node with minimum temporary cost is to be explored
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0:
                ct = ct+1
    
    min = 10000
    i1=-1
    j1=-1
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 :
                if temp[i][j]<min :
                    min = temp[i][j]
                    i1=i
                    j1=j
    if ct>0 : #checks if there is any unvisited node
        algo(i1, j1)


    if ct==0: #if there is unvisited node left, then loop terminates
        g=10
        
z=30
img[c1][d1]=127
cv2.namedWindow('NewImage', cv2.WINDOW_NORMAL)

count =0
#path function retraces the path
#checks surrounding pixels
#if cost between surrounding pixels and itself + permanent cost of surrounding pixel equals the permanent cost of itself
#then path is found
def path(x,y):
    global z
    global c
    global d
    global count
    if (x > 0) and (img[x - 1][y] == 255) and (2+ per[x - 1][y] == per[x][y]):
        img[x - 1][y] = 127
        c=x-1
        d=y
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (y > 0) and (img[x][y - 1] == 255) and (2+ per[x][y - 1] == per[x][y]):
        img[x][y - 1] = 127
        c=x
        d=y-1
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (x + 1 < n) and (img[x + 1][y] == 255) and (2 + per[x + 1][y] == per[x][y]):
        img[x + 1][y] = 127
        c = x + 1
        d = y
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (y + 1 < m) and (img[x][y + 1] == 255) and (2 + per[x][y + 1] == per[x][y]):
        img[x][y + 1] = 127
        c = x
        d = y+1
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (y + 1 < m) and (x+1<n) and (img[x+1][y + 1] == 255) and (1 + per[x+1][y + 1]==per[x][y]):
        img[x+1][y + 1] = 127
        c = x+1
        d = y+1
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (y + 1 < m) and (x>0) and (img[x-1][y + 1] == 255) and (1 + per[x-1][y + 1]==per[x][y]):
        img[x-1][y + 1] = 127
        c = x-1
        d = y+1
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (y > 0) and (x>0) and (img[x-1][y - 1] == 255) and (1 + per[x-1][y - 1]==per[x][y]):
        img[x-1][y - 1] = 127
        c = x-1
        d = y-1
        count = count + 1
        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15
    elif (x + 1 < n) and (y>0) and (img[x+1][y - 1] == 255) and (1 + per[x+1][y - 1]==per[x][y]):
        img[x+1][y - 1] = 127
        c = x+1
        d = y-1
        count = count + 1

        cv2.imshow('NewImage', img)
        cv2.waitKey(20)
        if (c == a1) and (d == b1): #whenever start point is reached, loop terminates
            z=15

while z==30 :
    path(c, d)

end = time.time() #end time
print("Distance=",count) #total distance traversed
print("time=",end - begin) #time displayed
cv2.waitKey(0)
cv2.destroyAllWindows()