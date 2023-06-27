import cv2
import numpy as np
import math
import time

#HOMEMAP TRAVERSAL USING RRT ALGORITHM
#RRT - Rapidly exploring Random Trees

begin = time.time() #start time
img = cv2.imread('homemap.jpeg', 0) #the map is stored in Grayscale format
n, m = img.shape
for i in range(n):
    for j in range(m):
        if img[i, j] < 243:
            img[i, j] = 0
        else:
            img[i, j] = 255

kernel = np.ones((2, 2), np.uint8)
#a kernel matrix is created
img = cv2.dilate(img, kernel, iterations=1) #dilation applied on the image with the kernel

a, b = (8, 23)
c, d = (51, 26)
img[a, b] = 127
img[c, d] = 127
cv2.namedWindow('dilated', cv2.WINDOW_NORMAL)
cv2.imshow('dilated', img.astype(np.uint8))
#Processed homemap displayed
print(a,b)
print(c,d)
# start : a,b
# end : c,d
img[a][b] = 255
img[c][d] = 255

c1=c
d1=d
tr = np.full((n,m),0)
img1=np.full((n,m,3),0)
#the tr matrix keeps a track of all the positions which are a part of the Randomly Generated Tree
#if a pixel is a part of the tree, then tr value at that pixel is stored as 200, else tr value at that pixel is stored as 0
#initially only the starting point is a part of the tree
for i in range(n):
    for j in range(m):
        if img[i,j]==255:
            img1[i][j][0]=255
            img1[i][j][1] = 255
            img1[i][j][2] = 255
#img1 is a matrix, which stores a copy of the original image initially, and then stores the tree as BLUE pixels and,
#the final path over the tree is stored as RED pixels in img1 matrix
tr[a][b] = 200 #initial point, a part of the tree

def dist(p,q,r,s): #calculates distance between 2 points
    k1 = (p-r)*(p-r)
    k2 = (q - s) * (q - s)
    u = math.sqrt(k1+k2)
    return u

def track1(l1,l2): #stores the tree pixels as BLUE
    tr[l1][l2] = 200
    img1[l1][l2][0] = 255
    img1[l1][l2][1] = 25
    img1[l1][l2][2] = 25
    cv2.imshow('tree', img1.astype(np.uint8))
    # displaying the tree continuously
    cv2.waitKey(10)
cv2.namedWindow('tree', cv2.WINDOW_NORMAL) #window for displaying the tree and the final path over it
while True :
    i1 = np.random.randint(0, n)
    j1 = np.random.randint(0, m)
    # random point (i1,j1) is stored
    i2=a
    j2=b
    min = dist(i1,j1,a,b)
    if (img[i1][j1] == 255) and (tr[i1][j1] == 0):
        for i in range(n):
            for j in range(m):
                if (tr[i][j] == 200) and (dist(i1, j1, i, j) < min):
                    min = dist(i1, j1, i, j)
                    i2=i
                    j2=j
        #i2,j2 stores the row and column of that pixel whose distance from the random point is minimum
        if (i2 == i1) and (j1>j2) :
            if (j2+1<m) and (img[i2][j2+1]==255) and (tr[i2][j2+1]==0):
                track1(i2,j2+1)
                if (i2==c) and (j2+1==d):
                    break
        elif (i2 == i1) and (j1<j2) :
            if (j2>0) and (img[i2][j2-1]==255) and (tr[i2][j2-1]==0):
                track1(i2,j2-1)
                if (i2 == c) and (j2 - 1 == d):
                    break
        elif (j2 == j1) and (i1>i2) :
            if (i2 + 1 < n) and (img[i2+1][j2] == 255) and (tr[i2+1][j2] == 0):
                track1(i2+1, j2)
                if (i2+1 == c) and (j2== d):
                    break
        elif (j2 == j1) and (i1<i2) :
            if (i2>0) and (img[i2-1][j2]==255) and (tr[i2-1][j2]==0):
                track1(i2-1, j2)
                if (i2 - 1 == c) and (j2 == d):
                    break
        elif (i2 < i1) and (j1>j2) :
            if (j2+1<m) and (i2 + 1 < n) and (img[i2+1][j2+1]==255) and (tr[i2+1][j2+1]==0):
                tr[i2+1][j2+1] = 200
                track1(i2+1, j2 + 1)
                if (i2 + 1 == c) and (j2+1 == d):
                    break
        elif (i2 > i1) and (j1>j2) :
            if (j2+1<m) and (i2>0) and (img[i2-1][j2+1]==255) and (tr[i2-1][j2+1]==0):
                track1(i2-1, j2 + 1)
                if (i2 - 1 == c) and (j2 + 1 == d):
                    break
        elif (i2 < i1) and (j1<j2) :
            if (j2>0) and (i2 + 1 < n) and (img[i2+1][j2-1]==255) and (tr[i2+1][j2-1]==0):
                track1(i2+1, j2 - 1)
                if (i2 + 1 == c) and (j2 - 1 == d):
                    break
        elif (i2 > i1) and (j1<j2) :
            if (j2>0) and (i2>0) and (img[i2-1][j2-1]==255) and (tr[i2-1][j2-1]==0):
                track1(i2-1, j2 - 1)
                if (i2 - 1 == c) and (j2 - 1 == d):
                    break
        # once the end point (c,d) becomes a part of the tree, loop is terminated

path1 = np.full((n,m),0) #stores step values for the required path as 1,2,3 .. so on
path1[a][b] = 1
k=1

def trac(k1):
    for i in range(n):
        for j in range(m):
            if path1[i][j]==k1 : #checks for step number k
                if (i > 0) and (img[i - 1][j] == 255) and (tr[i - 1][j] == 200) and (path1[i-1][j]==0):
                    path1[i - 1][j] = k1+1
                if (j > 0) and (img[i][j-1] == 255) and (tr[i][j-1] == 200) and (path1[i][j-1]==0):
                    path1[i][j-1] = k1+1
                if (i + 1 < n) and (img[i + 1][j] == 255) and (tr[i + 1][j] == 200) and (path1[i+1][j]==0):
                    path1[i+1][j] = k1 + 1
                if (j + 1 < m) and (img[i][j + 1] == 255) and (tr[i][j + 1] == 200) and (path1[i][j+1]==0):
                    path1[i][j+1] = k1 + 1
                if (i + 1 < n) and (j + 1 < m) and (img[i + 1][j+1] == 255) and (tr[i + 1][j + 1] == 200) and (path1[i+1][j+1]==0):
                    path1[i + 1][j + 1] = k1+1
                if (i + 1 < n) and (j > 0) and (img[i + 1][j-1] == 255) and (tr[i + 1][j - 1] == 200) and (path1[i+1][j-1]==0):
                    path1[i + 1][j - 1] = k1+1
                if (j + 1 < m) and (i > 0) and (img[i - 1][j+1] == 255) and (tr[i - 1][j + 1] == 200) and (path1[i-1][j+1]==0):
                    path1[i - 1][j + 1] = k1+1
                if (i > 0) and (j > 0) and (img[i - 1][j-1] == 255) and (tr[i - 1][j - 1] == 200) and (path1[i-1][j-1]==0):
                    path1[i - 1][j - 1] = k1+1
                # checking all the 8 neighbours/children and if path is available , then step number increases by 1

while True:
    trac(k)
    k+=1
    if path1[c][d] > 1:
        break
p=path1[c][d]
img1[c][d][0] = 10
img1[c][d][1] = 10
img1[c][d][2] = 255
#starting point made red
def track(c3,d3): #makes the path over the tree as RED
    tr[c3][d3] = 255
    img1[c3][d3][0] = 10
    img1[c3][d3][1] = 10
    img1[c3][d3][2] = 255
    cv2.imshow('tree', img1.astype(np.uint8)) #displays the path continuously
    cv2.waitKey(10)
#retrac function retraces the shortest path
def retrac(c2,d2,p2):
    global c
    global d
    if (c2 > 0) and (path1[c2 - 1][d2] == p2 - 1):
        c = c2 - 1
        d = d2
        track(c,d)
    elif (d2 > 0) and (path1[c2][d2 - 1] == p2 - 1):
        c = c2
        d = d2 - 1
        track(c,d)
    elif (d2 + 1 < m) and (path1[c2][d2 + 1] == p2 - 1):
        c = c2
        d = d2 + 1
        track(c,d)
    elif (c2 + 1 < n) and (path1[c2 + 1][d2] == p2 - 1):
        c = c2 + 1
        d = d2
        track(c,d)
    elif (c2 + 1 < n) and (d2 + 1 < m) and (path1[c2 + 1][d2 + 1] == p2 - 1):
        c = c2 + 1
        d = d2 + 1
        track(c, d)
    elif (c2 > 0) and (d2 + 1 < m) and (path1[c2 - 1][d2 + 1] == p2 - 1):
        c = c2 - 1
        d = d2 + 1
        track(c, d)
    elif (d2 > 0) and (c2 + 1 < n) and (path1[c2 + 1][d2 - 1] == p2 - 1):
        c = c2 + 1
        d = d2 - 1
        track(c,d)
    elif (d2 > 0) and (c2 > 0) and (path1[c2 - 1][d2 - 1] == p2 - 1):
        c = c2 - 1
        d = d2 - 1
        track(c,d)

while p>1:
    retrac(c,d,p)
    p=p-1 #when step number 1 is reached, we get the entire shortest path
print("Distance = " , path1[c1][d1]) #distance of the shortest path
end = time.time() #end time
print(end-begin) #total time taken
cv2.waitKey(0)
cv2.destroyAllWindows()
