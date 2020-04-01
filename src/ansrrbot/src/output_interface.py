#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("output_interface")

def display_message(input):
    #print(input.data)
    str = input.data
    if(str == "Error"):
        print("Incorrect Command. Check Input and Retry")
    else:
        print("Incoming Command: " + str)
        if(str == "1"):
            print("\t> "+"Initiating Going Home")
        if(str == "2"):
            print("\t> "+"Task has been Paused")
        if(str == "3"):
            print("\t> "+"Task has been Stopped, Going home now!")
        if(str == "4"):
            print("\t> "+"Initiating Cleaning Procedure")
        if(str == "4"):
            print("\t> "+"Mode: Manual")
        if(str == "5"):
            print("\t> "+"Mode: Autonomous")

print("Reading Commands: ")
sub = rospy.Subscriber("user_command", String, display_message)
rospy.spin()
