import serial
import time
f=open('directionOutputsBonus.txt', 'r') #the already generated text file is opened in read-only mode

arduino = serial.Serial(port='COM4' , baudrate = 9600 , timeout = .1)
#Arduino and Python is connected by Serial Communication

def write_read(x):
    arduino.write(bytes(x, 'utf-8')) #x is passed to the arduino after converting to bytes(of utf-8 encoding)
    time.sleep(0.05)
for i in range(93):
    str = f.readline() #reads the file line by line
    print(str)
    write_read(str)
    time.sleep(1.01)
f.close()
