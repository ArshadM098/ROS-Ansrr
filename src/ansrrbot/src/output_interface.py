#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Bool

rospy.init_node("output_interface")

def display_message(input,args):
    #print(input.data)
    str = input.data
    pub = args
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
        if(str == "5"):
            print("\t> "+"Mode: Autonomous")
        if(str == "6"):
            print("\t> "+"Initializing the robot")
            pub.publish(True)
print("Reading Commands: ")
pub_init = rospy.Publisher("init_flag", Bool, queue_size=1)
rospy.Subscriber("user_command", String, display_message,pub_init)
rospy.spin()
