# Bonus Part - TASK 2.3:

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
