#!/usr/bin/env python

import rospy
import serial

try:
    import RPi.GPIO as IO
    rospy.loginfo("Imported RPi.GPIO")
except ImportError as err:
    rospy.loginwarn("Could not import RPi.GPIO")

ser = serial.Serial(port='/dev/ttyAMA0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

mode = 255
device_num = 13
speed_stop = 127
speed_run = 200
tx_pin = 14
rx_pin = 15
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(tx_pin,GPIO.OUT) # TX Setup
    GPIO.setup(rx_pin,GPIO.IN)  # RX Setup
    rospy.loginfo("GPIO Setup Completed")
except NameError as err:
    rospy.logwarn("GPIO Setup Failed")
rospy.init_node("motor_control")

while not rospy.is_shutdown():
    usr_input = raw_input("WASD to move and SPACE to stop -> ")
    print( "----> User pressed " + usr_input)
    if(usr_input==' '):
        rospy.loginfo("Stopped")
        ser.write([mode,13,speed_stop])
        ser.write([mode,14,speed_stop])
    elif(usr_input=='w'):
        rospy.loginfo("Moving Forward")
        ser.write([mode,13,speed_run])
        ser.write([mode,14,speed_run])
    elif(usr_input=='s'):
        rospy.loginfo("Moving Backwards")
    elif(usr_input=='a'):
        rospy.loginfo("Turning Left")
    elif(usr_input=='d'):
        rospy.loginfo("Turning Right")
    else:
        rospy.logwarn("Incorrect Input, Try Again!")
