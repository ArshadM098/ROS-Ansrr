#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('input_interface')

#Command Publisher
pub = rospy.Publisher('user_command',String,queue_size=1)
valid_input = ("1","2","3","4","5","6")
while(not rospy.is_shutdown()):
    usrInput = raw_input("> ")
    is_valid = False
    for i in range(len(valid_input)):
        if(usrInput == valid_input[i]):
            is_valid=True
            break
    if(not is_valid):
        usrInput = "Error"
    pub.publish(usrInput)
print("Ending Program")
