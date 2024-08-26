from adafruit_servokit import ServoKit # type: ignore
import time

kit = ServoKit(channels=8)
#

def FrontLeftForward():
    kit.servo[1].angle = 110
    time.sleep(0.3)
    kit.servo[0].angle = 0
    time.sleep(0.3)
    kit.servo[1].angle = 45

def Stretch():
    kit.servo[0].angle = 0
    kit.servo[1].angle = 170
    kit.servo[2].angle = 180
    kit.servo[3].angle = 20
    kit.servo[4].angle = 0
    kit.servo[5].angle = 150
    kit.servo[6].angle = 180
    kit.servo[7].angle = 20

#START: Set to neutral
#Left side: 0 forward, 90 perpendicular, 180 behind
kit.servo[0].angle = 90
kit.servo[2].angle = 90
#Right Side: 180 forward, 90 perpendicular, 0 behind
kit.servo[4].angle = 90
kit.servo[6].angle = 90
#Fronts - 0 down, 180 up
#Rears - 180 down, 0 up 
kit.servo[1].angle = 0
kit.servo[3].angle = 170
kit.servo[5].angle = 0
kit.servo[7].angle = 170

time.sleep(1.5)

#Stretch



#FrontLeftForward()