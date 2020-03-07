#!/usr/bin/env python

import rospy
try:
    import RPi.GPIO as IO
except ImportError as err:
    print(err)

tx_pin = 23
rx_pin = 24
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(tx_pin,GPIO.OUT) # TX Setup
    GPIO.setup(rx_pin,GPIO.IN)  # RX Setup
except NameError as err:
    print(err)

rospy.init_node("motor_control")

while not rospy.is_shutdown():
    usr_input = raw_input("WASD to move and SPACE to stop -> ")
    print(+ "----> User pressed " + usr_input)
    if(usr_input==' '):
        rospy.loginfo("Stopped")
    elif(usr_input=='w'):
        rospy.loginfo("Moving Forward")
    elif(usr_input=='s'):
        rospy.loginfo("Moving Backwards")
    elif(usr_input=='a'):
        rospy.loginfo("Turning Left")
    elif(usr_input=='d'):
        rospy.loginfo("Turning Right")
    else:
        rospy.logwarn("Incorrect Input, Try Again!")
