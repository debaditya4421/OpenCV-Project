import cv2
import numpy as np
import time

img=cv2.imread('homemap.jpeg', 0)
n,m=img.shape
for i in range (n):             #Thresholding
    for j in range(m):
        if img[i,j]<243:
            img[i,j]=0
        else:
            img[i,j]=255



kernel = np.ones((2,2), np.uint8)       #kernel for dilating the map to avoid unnecessary isolated white pixels
 

img = cv2.dilate(img, kernel, iterations=1)         #dilation

a,b=(15,3)              #a,b is the start
c,d=(46,49)             #c,d is the end

print(b,a)
print(d,c)

path1=[]                    #path1 stores the x coordinates of all the elements of the path
path2=[]                    #path2 stores the y coordinates of all the elements of the path
z=n*n                       #max possible distance between two nodes
value=[z,z,z,z,z,z,z,z]     #stack that is used to find the pixel which is closest to end pixel
end=0                       #A variable declared to end the function when the final pixel is reached
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
def astar(i,j):
    global end
    if end==0:              #checking if current pixel is the final pixel
        while(i,j!=c,d):
            img[i,j]=127    #making the traversed pixels grey to avoid repitition
            value=[z,z,z,z,z,z,z,z]         #redefining the stack back to its original value to check min value for the next pixel
            path1.append(i)                 #adding the coordinates of the traversed pixel to the path
            path2.append(j)
            cv2.imshow('Image', img)
            cv2.waitKey(20)
            if(i-1>=0):                     #checking boundary conditions
                if((i-1,j)==(c,d)):         #checking if it is the final pixel
                    print("complete")
                    end=1                   #ensures to end the function and bactrace in the next step
                    astar(c,d)
                elif(img[i-1,j]==255):      #checks if it is an untraversed pixel
                    g=2                     #The four adjacent pixels have a value of 2 as we will prefer diagonals over adjacent pixels if they have the same distance from the goal
                    h=(c-i+1)**2+(d-j)**2   #checking the minimum distance to the final pixel
                    f=g+h                   #the f value indicates the value of each surrounding pixel
                    value[0]=f              #the f value of each surrounding pixel is added to the stack

            if(j-1>=0):
                if((i,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i,j-1]==255):
                    g=2
                    h=(c-i)**2+(d-j+1)**2
                    f=g+h
                    value[1]=f
                    
            if(i+1<n):
                if((i+1,j)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j]==255):
                    g=2
                    h=(c-i-1)**2+(d-j)**2
                    f=g+h
                    value[2]=f
                    
            if(j+1<m):
                if((i,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i,j+1]==255):
                    g=2
                    h=(c-i)**2+(d-j-1)**2
                    f=g+h
                    value[3]=f
                    

            if(j+1<m and i+1<n):
                if((i+1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j+1]==255):
                    g=1                         #diagonals have a value 1 since they will be preferred over adjacent pixels to avoid extra traversals 
                    h=(c-i-1)**2+(d-j-1)**2
                    f=g+h
                    value[4]=f

            if(j+1<m and i-1>=0):
                if((i-1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i-1,j+1]==255):
                    g=1
                    h=(c-i+1)**2+(d-j-1)**2
                    f=g+h
                    value[5]=f

            if(i+1<n and j-1>=0):
                if((i+1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i+1,j-1]==255):
                    g=1
                    h=(c-i-1)**2+(d-j+1)**2
                    f=g+h
                    value[6]=f

            if(j-1>=0 and i-1>=0):
                if((i-1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d)
                elif(img[i-1,j-1]==255):
                    g=1
                    h=(c-i+1)**2+(d-j+1)**2
                    f=g+h
                    value[7]=f  
            
            if min(value)==z:               #checks if no neighbouring pixel is a traversible path. i.e. all are black or grey
                path1.pop()                 #in that case, it will remove that pixel from the stack
                path2.pop()

            

            minpos=value.index(min(value))          #based on the minimum f value, the next pixel in the path will be decided
            if minpos==0:
                astar(i-1,j)
            elif minpos==1:
                astar(i,j-1)
            elif minpos==2:
                astar(i+1,j)
            elif minpos==3:
                astar(i,j+1)
            elif minpos==4:
                img[i+1,j+1]=127
                astar(i+1,j+1)
            elif minpos==5:
                img[i-1,j+1]=127
                astar(i-1,j+1)
            elif minpos==6:
                img[i+1,j-1]=127
                astar(i+1,j-1)
            elif minpos==7:
                img[i-1,j-1]=127
                astar(i-1,j-1)
            break
    
    else:
        print("final complete")
begin=time.time()               #start time
astar(a,b)
end=time.time()                 #endtime which includes waitKeys
l=len(path1)                    #length of the stack=distance of path
print("distance=", l)
print("time=",end-begin)
for k in range(l):
    img[path1.pop(),path2.pop()]=200        #backtracking
    cv2.imshow('Image', img)
    cv2.waitKey(20)

cv2.waitKey(0)
cv2.destroyAllWindows()
                        
