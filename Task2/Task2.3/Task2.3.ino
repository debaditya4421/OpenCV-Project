#include <AFMotor.h>


AF_DCMotor M1(1);
AF_DCMotor M2(2);
int speed1, speed2;
int x;



void setup()
{  
  M1.setSpeed(55);
  M2.setSpeed(55);
  Serial.begin(9600);
}

void loop() 
{ 
 x = Serial.readString().toInt();
 Serial.println(x);
 if(x==1)           //Red light
 {
  halt();
 }
 
 else if(x==2)      //Green light
 {
 speed1=60;
 speed2=60;
 forward();
 }
 else if(x==3)      //Right turn
 {
 turnright();
 }
 else if(x==4)      //Left turn
 {
  turnleft();
 }

 else if(x==5)      //U turn
 {
 speed1=70;
 speed2=70;
 Uturn();
 }
 else if(x==6)      //hospital zone
 {
 speed1=45;
 speed2=45;
 forward();
 }
 else if(x==7)      //hump
 {
 speed1=40;
 speed2=40;
 forward();
 }
 else if(x==8)      //30 limit
 {
 speed1=50;
 speed2=50;
 forward();
 }
 else if(x==9)      //20 limit
 {
 speed1=45;
 speed2=45;
 forward();
 }
 else if(x==10)     //school zone
 {
 speed1=50;
 speed2=50;
 forward();
 }
 else if(x==11)     //stop
 {
  halt();
 }
 
 else if(x==12)     //don't stop
 {
 speed1=60;
 speed2=60;
 forward();
 }
 else if(x==13)     //reverse
 {
 speed1=55;
 speed2=55;
 backward();
 }
 else if(x==14)     //rightcurve
 {
 speed1=60;
 speed2=50;
 forward();
 }
 else if(x==15)    //leftcurve
 {
 speed1=50;
 speed2=60;
 forward();
 }
 else
 {
 halt();
 } 
  
}

void backward()
{
  M1.run(BACKWARD);
  M2.run(BACKWARD);
  delay(1000);
}

void forward()
{
  setspeed();
  M1.run(FORWARD);
  M2.run(FORWARD);
  delay(1000);
}

void halt()
{
  M1.run(RELEASE);
  M2.run(RELEASE);
  delay(1000);
}

void turnleft()
{
  M2.setSpeed(70);
  M2.run(FORWARD);
  delay(1000);   
}

void turnright()
{
  M1.setSpeed(70);
  M1.run(FORWARD);
  delay(1000); 
}

void Uturn()
{
  setspeed();
  M1.run(FORWARD);
  M2.run(BACKWARD);
}

void setspeed()
{
  M1.setSpeed(speed1);
  M2.setSpeed(speed2);
}
