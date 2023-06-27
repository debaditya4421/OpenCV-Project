# CV-Project
Making a project using computer vision library opencv using python based on what we have learnt in the Winter Workshop

TASK 1.1 :
 
1. The randmatrix.py file contains the program to generate a random matrix in case we only want to generate a random matrix.
2. We have upsized our random matrix from 20*20 to 60*60, 40*40 and 100*100 because most are facing stack overflow with higher order matrices.
3. For the Dijkstra and Astar program, we have considered the weights for horizontal/vertical moves as 2 and for diagonals 1. 
4. The Dijkstra program takes about 10 to 15 seconds to compile.
5. We have also used another path finding algorithm - RRT algorithm - Rapidly Exploring Random Tree. 

TASK 1.2 :
1. We have added the BFS, DFS and Astar solution. Dijkstra and RRT methods are facing stack overflow and tend to not work even on adding more stacks and setting a higher recursion depth. 
2. The image being used in this program is named “map1.2.png”. Kindly download the image before running the program.

TASK 1.3 :
1. The image being used in this program is named “homemap.jpeg”. Kindly download the image before running the program. 
2. All the 5 algorithms that we have used, have been implemented successfully. 

TASK 2.1:
1. We have used 15 different images showing different traffic signals.
Please download these 15 images before running the program.
2. A video of about 1.5 minutes is generated using the 15 different images at random ensuring that a red traffic light is always followed by a green traffic light.

TASK 2.2:
1. The video generated in part 2.1 is read and depending on the different road signals, the program will generate different outputs and store them in a text file, ‘directionOutputs2.txt’ .


Bonus Part - TASK 2.3:

TASK 2.3a :
1. Using the 15 different images at random, a video  of about 1.5 minutes is generated and simultaneously based on different road signals, different outputs are stored in a text file, ‘directionOutputsBonus.txt’ .
2. For the bonus part, we have stored the image number as the output in the text file, since we need to pass it to Arduino by Serial Communication for hardware implementation in parts 2.3b and 2.3c. 

TASK 2.3 ino : 
1. Arduino Motor Driver library should be installed.
2. The port should be set to COM4. 
3. Make sure to upload this program to Arduino IDE before running parts 2.3b and 2.3c. 

TASK 2.3b :
1. The output produced in the text file is read and sent to the Arduino by Serial Communication.
2. According to the value received by Arduino, it directs the motors to perform different operations. 

TASK 2.3c :
1. In this part, we have implemented everything in sync i.e. in parallel. The video is generated using the 15 different images and simultaneously the output is stored in a text file, ‘directionOutputsBonus.txt’  and also the output is read and sent to the Arduino for hardware implementation

HARDWARE REQUIREMENTS :
1. Arduino UNO
2. Motor Driver
3. Two motors and wheels
4. Four Jumper Wires

